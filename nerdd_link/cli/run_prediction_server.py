import logging
from importlib import import_module
from typing import List

import rich_click as click

from ..actions import Action, PredictCheckpointsAction, RegisterModuleAction
from ..channels import KafkaChannel

__all__ = ["run_prediction_server"]

logger = logging.getLogger(__name__)


@click.command(context_settings={"show_default": True})
@click.argument("model-name")
@click.option(
    "--channel",
    type=click.Choice(["kafka"], case_sensitive=False),
    default="kafka",
    help="Channel to use for communication with the model.",
)
@click.option(
    "--broker-url", default="localhost:9092", help="Kafka broker to connect to."
)
@click.option(
    "--data-dir",
    default="sources",
    help="Directory containing structure files associated with the incoming jobs.",
)
@click.option(
    "--log-level",
    default="info",
    type=click.Choice(
        ["debug", "info", "warning", "error", "critical"], case_sensitive=False
    ),
    help="The logging level.",
)
def run_prediction_server(
    # communication options
    channel: str,
    broker_url: str,
    # options
    model_name: str,
    data_dir: str,
    # log level
    log_level: str,
):
    logging.basicConfig(level=log_level.upper())

    channel_instance = None
    if channel == "kafka":
        channel_instance = KafkaChannel(broker_url)
    else:
        raise ValueError(f"Channel {channel} not supported.")

    # import the model class
    package_name, class_name = model_name.rsplit(".", 1)
    package = import_module(package_name)
    Model = getattr(package, class_name)
    model = Model()

    register_module = RegisterModuleAction(channel=channel_instance, model=model)

    predict_checkpoints = PredictCheckpointsAction(
        channel=channel_instance,
        model=model,
        data_dir=data_dir,
    )

    actions: List[Action] = [register_module, predict_checkpoints]

    try:
        for action in actions:
            logging.info(f"Running action {action}")
            action.start()
        for action in actions:
            action.join()
    except KeyboardInterrupt:
        logger.info("Shutting down server")
        for action in actions:
            action.stop()
        for action in actions:
            action.join()