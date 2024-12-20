# CHANGELOG


## v0.2.0 (2024-12-12)

### Features

* feat: Add start and stop method to Channel ([`f4997cf`](https://github.com/molinfo-vienna/nerdd-link/commit/f4997cfac8643307c1c6ed085fe8324a1ec5730c))

### Fixes

* fix: Keep molecule properties when serializing them to pickle (part 2) ([`110103b`](https://github.com/molinfo-vienna/nerdd-link/commit/110103be86e08a847ae62e0129d92292cb20ddbb))

* fix: Keep molecule properties when serializing them to pickle ([`1d9b0b8`](https://github.com/molinfo-vienna/nerdd-link/commit/1d9b0b83dc8c23f953a9a66fb2cdea913cb239c8))

### Unknown

* Merge pull request #19 from shirte/main

Add start and stop method to channels ([`a0f8451`](https://github.com/molinfo-vienna/nerdd-link/commit/a0f845197d4dd3949c3d83eebba82fa5a6f3446b))

* Make sure that all properties are serialized to pickle ([`dd46074`](https://github.com/molinfo-vienna/nerdd-link/commit/dd46074d0e524550c7b03df1a559d8e65a8d7047))

* Implement consumer groups in MemoryChannel ([`aa4f1f6`](https://github.com/molinfo-vienna/nerdd-link/commit/aa4f1f6aaf35d004aa77cd15a940ecc9af7ca2a9))

* Start consumers when restarting in KafkaChannel ([`f4d9e6f`](https://github.com/molinfo-vienna/nerdd-link/commit/f4d9e6f2e0a8fc07c2b127579088b9bcf41e4331))

* Add value serializer in KafkaChannel ([`47da130`](https://github.com/molinfo-vienna/nerdd-link/commit/47da13036c9d1ebae9f428dfd3292b5d26a7c480))

* Let KafkaChannel use consumer group as given ([`e918927`](https://github.com/molinfo-vienna/nerdd-link/commit/e9189276483ba0855645a3bc320cae94264e2735))

* Start kafka producer and consumers in _start method ([`721631e`](https://github.com/molinfo-vienna/nerdd-link/commit/721631eea05edb8e37bbe57bc2faa2e54c6379c1))

* Make channel only usable in running state ([`5ac0f29`](https://github.com/molinfo-vienna/nerdd-link/commit/5ac0f29aa9c4fabddb37d3d96c2c25615d7e7ee0))


## v0.1.0 (2024-12-06)

### Features

* feat: Move ObservableList to utils ([`0c5358d`](https://github.com/molinfo-vienna/nerdd-link/commit/0c5358db561a72ee2ec474d463ed439c44d4af7d))

### Unknown

* Merge pull request #18 from shirte/main

Fix types ([`1331854`](https://github.com/molinfo-vienna/nerdd-link/commit/13318542719128a97f70973620e9abef8b49fe83))

* Add initialize_system command ([`ce229f2`](https://github.com/molinfo-vienna/nerdd-link/commit/ce229f26291b22c6ac03f557171af30990b69c47))

* Add mypy to pre-commit hooks ([`6fe227b`](https://github.com/molinfo-vienna/nerdd-link/commit/6fe227b763693635ec1579890dd5293622426453))

* Ignore aiokafka when checking types ([`95e5d0f`](https://github.com/molinfo-vienna/nerdd-link/commit/95e5d0f6018e03b5767ca4bba9113062cdee9c94))

* Configure semantic release in pyproject.toml ([`500ae8c`](https://github.com/molinfo-vienna/nerdd-link/commit/500ae8c66e28f18239cd71f97a709a9e7bac8cb2))

* Add mypy plugin for pydantic ([`915bbad`](https://github.com/molinfo-vienna/nerdd-link/commit/915bbad81e2a5358ce83a1b7577d1fbbd09717c1))

* Fix types in MemoryChannel ([`339458e`](https://github.com/molinfo-vienna/nerdd-link/commit/339458e407283f6f2a941cb16a62a4b4f0806dc3))

* Merge pull request #17 from shirte/main

Rename DummyChannel and move to main code ([`f1c0235`](https://github.com/molinfo-vienna/nerdd-link/commit/f1c02353741257b3c62bf1278494baad96aa760b))

* Do not return spinalcase in PredictCheckpointsAction ([`5c928c9`](https://github.com/molinfo-vienna/nerdd-link/commit/5c928c9aa53d9d084f96c714139a5da5ec5564ea))

* Rename DummyChannel to MemoryChannel and move to channels submodule ([`78adf26`](https://github.com/molinfo-vienna/nerdd-link/commit/78adf26f568fb0de80644af2304d3184e99899f9))

* Use correct types in WriteOutputAction ([`9647a61`](https://github.com/molinfo-vienna/nerdd-link/commit/9647a61158ee8047738e5d3672946c03985a811c))

* Use logger in DummyChannel ([`9106a16`](https://github.com/molinfo-vienna/nerdd-link/commit/9106a1663c0eb5d208f839d2a8ead2180ef710be))

* Add types to channel classes ([`b62f0fa`](https://github.com/molinfo-vienna/nerdd-link/commit/b62f0fac04c4009b4d12ff727d013f363f140533))

* Add types to cli classes ([`d0c93e2`](https://github.com/molinfo-vienna/nerdd-link/commit/d0c93e23ef7fa3383c372d9e06fd288c3ec2f40a))

* Add types to delegate classes ([`0fbd987`](https://github.com/molinfo-vienna/nerdd-link/commit/0fbd98762c9e86952dc7fe045816b82cee78cf00))


## v0.0.2 (2024-12-05)

### Fixes

* fix: Use spinalcase for specified job_type ([`5c1f5a7`](https://github.com/molinfo-vienna/nerdd-link/commit/5c1f5a787815c0a8d610095a794dda7f87b19949))

### Unknown

* Merge pull request #16 from shirte/main

Add types ([`7e9a229`](https://github.com/molinfo-vienna/nerdd-link/commit/7e9a22935ea65f29a47d45bea86a50e1035f839a))

* Add types to async_to_sync ([`51b92d9`](https://github.com/molinfo-vienna/nerdd-link/commit/51b92d9216f879c4236dccec66dace754baa29ab))

* Add types to StructureJsonReader ([`a294c8a`](https://github.com/molinfo-vienna/nerdd-link/commit/a294c8ae25315e76a8f79e5e69b5e2fd4dc07fb6))

* Always use spinalcase ([`6956dc9`](https://github.com/molinfo-vienna/nerdd-link/commit/6956dc91adc9c82c3e28845a877c4fe845ee7673))

* Check that the given module has a config ([`00b8697`](https://github.com/molinfo-vienna/nerdd-link/commit/00b8697cc97273eb1619dfde721674cc813fe45e))

* Add types to actions ([`f960685`](https://github.com/molinfo-vienna/nerdd-link/commit/f96068534aa9f14a77a28b3104d129deeb6653d4))

* Add pyproject.toml to pre-commit-config ([`c67e8d5`](https://github.com/molinfo-vienna/nerdd-link/commit/c67e8d5590a3316aa658f53aff79b9eb36bcc2f2))

* Use logging in actions ([`4038256`](https://github.com/molinfo-vienna/nerdd-link/commit/4038256832739c41de89e2a6f4c22d056092f56a))


## v0.0.1 (2024-12-03)

### Fixes

* fix: Add update operation to ObservableList ([`d12ba0a`](https://github.com/molinfo-vienna/nerdd-link/commit/d12ba0a8458a60861dc6268193295b6c6b1a7159))

### Unknown

* Merge pull request #15 from shirte/main

Add types ([`965f5b3`](https://github.com/molinfo-vienna/nerdd-link/commit/965f5b3da10a2a8cbe77b1f255b1712c50263ea0))

* Remove kafka-python dependency ([`9949ce9`](https://github.com/molinfo-vienna/nerdd-link/commit/9949ce96750cdbba86b7deb5041063156bb4481b))

* Add types for safetee ([`72a5a67`](https://github.com/molinfo-vienna/nerdd-link/commit/72a5a67455f0afbab21b6d7ad1a9682eb0d29769))

* Add type stubs for stringcase ([`82d7e64`](https://github.com/molinfo-vienna/nerdd-link/commit/82d7e64acb1632e2bdb458e9e436231a7e62ac66))

* Ignore rdkit typing errors ([`e763b33`](https://github.com/molinfo-vienna/nerdd-link/commit/e763b3306da18c42aa73e8005b22a6082fe7fd5c))

* Merge pull request #14 from shirte/main

Let ObservableList track changes ([`6a99d06`](https://github.com/molinfo-vienna/nerdd-link/commit/6a99d0608556306c466ff7c25a0e1a7d7ca468e6))

* Finalize register_module feature test ([`a72d105`](https://github.com/molinfo-vienna/nerdd-link/commit/a72d105e4f8dea39e5a71c3e766659fbd8c8c7ac))

* Let ObservableList track changes ([`eeb4e4f`](https://github.com/molinfo-vienna/nerdd-link/commit/eeb4e4febce98cdebfc59a731946045f4de98e42))

* Merge pull request #13 from shirte/main

Introduce ObservableList ([`6f3a7a4`](https://github.com/molinfo-vienna/nerdd-link/commit/6f3a7a467774b2671505b2a96b6560c32f0e0495))

* Introduce ObservableList ([`d08d896`](https://github.com/molinfo-vienna/nerdd-link/commit/d08d89618ea65125fa02027c5d5b66cc3f556b3c))

* Adapt feature tests ([`72ebace`](https://github.com/molinfo-vienna/nerdd-link/commit/72ebace7f4e9b13d9db02d1f586b3902f63e4381))

* Move data directory step to main code ([`9f04504`](https://github.com/molinfo-vienna/nerdd-link/commit/9f04504ec71a8c2ec293fe4b2814e188ee334206))

* Merge pull request #12 from shirte/main

Add pre-commit hooks ([`0d0b405`](https://github.com/molinfo-vienna/nerdd-link/commit/0d0b405447701cc75f039e762d8439e9c27e0c39))

* Minor changes ([`c78b021`](https://github.com/molinfo-vienna/nerdd-link/commit/c78b021d88fcbb2910878d9adb33707769b6a849))

* Move test code into submodule ([`09dd25d`](https://github.com/molinfo-vienna/nerdd-link/commit/09dd25dec257b19c505e722c40bb0fa85a72f755))

* Run actions in pytest as async with cleanup code ([`ac8639a`](https://github.com/molinfo-vienna/nerdd-link/commit/ac8639aac841c6a6c11de4d19a7d9e6f4c50ce17))

* Reimplement DummyChannel correctly ([`7c0b9bf`](https://github.com/molinfo-vienna/nerdd-link/commit/7c0b9bf73822972ec1649ba7adb70166a06fdb81))

* Avoid mocked communication channel step ([`d2a34ac`](https://github.com/molinfo-vienna/nerdd-link/commit/d2a34ac0898bd121764bd2b8f0f195c98e6cf8b8))

* Use AsyncIterable instead of AsyncIterator ([`77db952`](https://github.com/molinfo-vienna/nerdd-link/commit/77db9527af5b1824b04795daa6c87e6df280d7d4))

* Add waiting step in tests ([`cff0147`](https://github.com/molinfo-vienna/nerdd-link/commit/cff01475480805b1aa87db5b2b7d019fbad518fd))

* Make cli commands async ([`1a48ca9`](https://github.com/molinfo-vienna/nerdd-link/commit/1a48ca9c68c9ba1a3bf450b3e485c30715ea2c64))

* Rename start to run ([`2f79b29`](https://github.com/molinfo-vienna/nerdd-link/commit/2f79b296f8ad5b984c950160cb8b316a6c0f2581))

* Run tests in pull requests ([`f41bc77`](https://github.com/molinfo-vienna/nerdd-link/commit/f41bc77040632b1a45a8c22f9fbefe6dd1372830))

* Increase ruff version ([`5228e8c`](https://github.com/molinfo-vienna/nerdd-link/commit/5228e8c2bfc106a61160aaf5b763a779bed4e3ce))

* Add submodules to main __init__ ([`923fc47`](https://github.com/molinfo-vienna/nerdd-link/commit/923fc47516576d58727a4e1daaf457533951f532))

* Add pre-commit hook ([`1ad6c65`](https://github.com/molinfo-vienna/nerdd-link/commit/1ad6c65054fb473db10aa139bd5ff5b546d638fb))

* Merge pull request #11 from shirte/main

Add async_to_sync helper function ([`d610da8`](https://github.com/molinfo-vienna/nerdd-link/commit/d610da8fe1ae8a09c2b4f8543fb583369dce19a3))

* Add async_to_sync helper function ([`5e61635`](https://github.com/molinfo-vienna/nerdd-link/commit/5e616358326823d28fba9721b48c5a91e2edf893))

* Merge pull request #10 from shirte/main

Downgrade aiokafka dependency ([`0da06ec`](https://github.com/molinfo-vienna/nerdd-link/commit/0da06ec2192b98cc335bca1774129f471d71a643))

* Downgrade aiokafka dependency ([`59677b7`](https://github.com/molinfo-vienna/nerdd-link/commit/59677b72e1ad8eadb1a23cc2b3d51cb29706479b))


## v0.0.0 (2024-11-21)

### Unknown

* Merge pull request #9 from shirte/main

Make code async ([`fddda99`](https://github.com/molinfo-vienna/nerdd-link/commit/fddda9921d75bda2f367fe88d6612dbb7e4ef242))

* Lint code ([`0bd6459`](https://github.com/molinfo-vienna/nerdd-link/commit/0bd6459a5b3933c4de8b88cb4645e6954d187ca7))

* Format code ([`e513022`](https://github.com/molinfo-vienna/nerdd-link/commit/e51302259d99727473ea7e8a0d16a70406d38980))

* Adapt tests to async code ([`090ea42`](https://github.com/molinfo-vienna/nerdd-link/commit/090ea42636284407b18b38f93be40150d602f49e))

* Let cli run async code ([`87ea9e2`](https://github.com/molinfo-vienna/nerdd-link/commit/87ea9e2fd7ce3346347c035e43f31af7e3cde5bc))

* Make actions async ([`a778c03`](https://github.com/molinfo-vienna/nerdd-link/commit/a778c03de6c8af15e85078c304eae74ed71fe7ce))

* Make channels async ([`60aade0`](https://github.com/molinfo-vienna/nerdd-link/commit/60aade046fe482a0b3cb0aec9da82bb31f6d3eca))

* Add aiokafka to pyproject.toml ([`af1bfa0`](https://github.com/molinfo-vienna/nerdd-link/commit/af1bfa0ccf92d869995e2b0dc79480b78863f57f))

* Merge pull request #8 from shirte/main

Simplify StructureJsonReader ([`42ca896`](https://github.com/molinfo-vienna/nerdd-link/commit/42ca896d4b3f564f8815f72340752fa70c21161f))

* Move py.typed file into package ([`daaf6fc`](https://github.com/molinfo-vienna/nerdd-link/commit/daaf6fccf121485000818503c781f9331889320f))

* Simplify StructureJsonReader ([`538a628`](https://github.com/molinfo-vienna/nerdd-link/commit/538a62871949c45f4942de8ebe8cd4b9843db794))

* Always import StructureJsonReader ([`d0ef8cd`](https://github.com/molinfo-vienna/nerdd-link/commit/d0ef8cda59dd9781ef1e3114778534aafa3ec233))

* Merge pull request #7 from shirte/main

Add semantic release ([`d2e2354`](https://github.com/molinfo-vienna/nerdd-link/commit/d2e2354db5df029582cb9a29165c46365540abf3))

* Format code ([`112cf1a`](https://github.com/molinfo-vienna/nerdd-link/commit/112cf1a10abf9a8e3c9cbc210fef11921f33c2b5))

* Convert messaes to pydantic models ([`1a21ee2`](https://github.com/molinfo-vienna/nerdd-link/commit/1a21ee21c39396db782abdd93f545e309cd57203))

* Treat configs as pydantic models ([`6f63315`](https://github.com/molinfo-vienna/nerdd-link/commit/6f63315542e045f2e4efc20b53a8b44a1ab453f7))

* Enable semantic release ([`b8445b6`](https://github.com/molinfo-vienna/nerdd-link/commit/b8445b6e265512e1571c7a5f749b0ecaf3cdf5f4))

* Allow low versions of pydantic ([`0361ec4`](https://github.com/molinfo-vienna/nerdd-link/commit/0361ec44f502fa88ef8e3cc7a2133e0c9019b790))

* Add pypi publishing action ([`a66964d`](https://github.com/molinfo-vienna/nerdd-link/commit/a66964ddb5f67afd2f1825470e6a1be0265df429))

* Add linting to github actions ([`5a75a56`](https://github.com/molinfo-vienna/nerdd-link/commit/5a75a5602e7e465692fff10365afdae759f9ddb5))

* Lint project ([`024898b`](https://github.com/molinfo-vienna/nerdd-link/commit/024898b22d04bbdd470844d5664e55799d5c3e5b))

* Merge pull request #6 from shirte/main

Add format check to github actions ([`392e246`](https://github.com/molinfo-vienna/nerdd-link/commit/392e246fc06d980ccc5dc55d7065819839896aed))

* Add format check to github actions ([`fdf3118`](https://github.com/molinfo-vienna/nerdd-link/commit/fdf311897dccae9b59932e682ba10ebadec55079))

* Format all files ([`9553862`](https://github.com/molinfo-vienna/nerdd-link/commit/9553862b9be6c8e552d0489136ad9b533a4a155c))

* Merge pull request #5 from shirte/main

Use consumer groups ([`45745d2`](https://github.com/molinfo-vienna/nerdd-link/commit/45745d2607cec8694434d0b246ca87110af0aa2d))

* Use consumer groups ([`1648fef`](https://github.com/molinfo-vienna/nerdd-link/commit/1648fef310c9815497bcb0682db58e882bbc9c31))

* Merge pull request #4 from shirte/main

Add files ([`d07a87d`](https://github.com/molinfo-vienna/nerdd-link/commit/d07a87d582c4a721fc1d00aa58253284cceb718c))

* Add structure json reader ([`57c0f97`](https://github.com/molinfo-vienna/nerdd-link/commit/57c0f9756e7be93b2a58a8f553fc34ba377b23ed))

* Add write output action ([`b66a157`](https://github.com/molinfo-vienna/nerdd-link/commit/b66a15713c2ecc7599a8de42d066cab869ab7ea4))

* Merge pull request #3 from shirte/main

Switch to pyproject.toml ([`ae85903`](https://github.com/molinfo-vienna/nerdd-link/commit/ae859039684645d55acfc13ec14a953a86137893))

* Convert setup.py to pyproject.toml ([`09fbab1`](https://github.com/molinfo-vienna/nerdd-link/commit/09fbab188f4df0adf00cc5a638b26486e5b0a6ff))

* Add py.typed file ([`04cd82c`](https://github.com/molinfo-vienna/nerdd-link/commit/04cd82c64969b6495cb9de683eb68e0e8905b777))

* Merge pull request #2 from shirte/main

Rename project to nerdd-link ([`98ca5b7`](https://github.com/molinfo-vienna/nerdd-link/commit/98ca5b705c4fd8556cca321944d8c02148d4f8af))

* Move and rewrite tests ([`b14b0f7`](https://github.com/molinfo-vienna/nerdd-link/commit/b14b0f7f9d436088ed873dfc28b435b31e10a3f5))

* Add message types ([`c644d91`](https://github.com/molinfo-vienna/nerdd-link/commit/c644d9196e44de3a5bb4424b39da99d6799e5604))

* Add utility functions ([`42c4ce1`](https://github.com/molinfo-vienna/nerdd-link/commit/42c4ce138d473d36dabe509f56b1a2b8a85eeaac))

* Add CLI classes ([`126feda`](https://github.com/molinfo-vienna/nerdd-link/commit/126feda08129cecba60e8935b9be5812765626bd))

* Move code to nerdd-link ([`3eecd8a`](https://github.com/molinfo-vienna/nerdd-link/commit/3eecd8aaf492331ad7c722d88ed8441263ce1496))

* Let PredictCheckpointAction write result checkpoints ([`9906cc8`](https://github.com/molinfo-vienna/nerdd-link/commit/9906cc8b00c10165374aa99cc8fa7e3b177d3ee5))

* Add helper classes ([`cc69d65`](https://github.com/molinfo-vienna/nerdd-link/commit/cc69d65e808422d8f8e92d0e5e9a0540d74e02d6))

* Rename project to nerdd-link ([`f122bac`](https://github.com/molinfo-vienna/nerdd-link/commit/f122bac7df0cf26726bfe4769e641ecc08a9e426))

* Merge pull request #1 from shirte/main

Provide basic project structure ([`e8b795c`](https://github.com/molinfo-vienna/nerdd-link/commit/e8b795c50f732b20cbdfb8ae51c55075ade893c2))

* Implement kafka channel ([`fa47d00`](https://github.com/molinfo-vienna/nerdd-link/commit/fa47d00536e008ab88373db815218a1d39cd3643))

* Add channel base class ([`aafc823`](https://github.com/molinfo-vienna/nerdd-link/commit/aafc8237ee2a4801e6ea8b5f09699f7a0a64e298))

* Add empty implementation for write output action ([`a609c32`](https://github.com/molinfo-vienna/nerdd-link/commit/a609c32e0f42e14dfaa25d7d7cbadcd49c3ab3c5))

* Implement register module action ([`0f3448a`](https://github.com/molinfo-vienna/nerdd-link/commit/0f3448a3bceeee44b2060fa2a991925999eddd75))

* Implement process jobs action ([`280bcfb`](https://github.com/molinfo-vienna/nerdd-link/commit/280bcfb9296c005f12835542cf98338b5a35ad35))

* Implement predict checkpoints action ([`ad67c95`](https://github.com/molinfo-vienna/nerdd-link/commit/ad67c95c843be5362e9d16cde4a8d86fef80b586))

* Add action base class ([`fbfb74b`](https://github.com/molinfo-vienna/nerdd-link/commit/fbfb74bf07b1792cc3aef6b6bb7c86906803be80))

* Add environment.yml ([`3c2963a`](https://github.com/molinfo-vienna/nerdd-link/commit/3c2963a467a3abcd74333e4a80fa73c01d8760fa))

* Add ruff_cache to gitignore ([`4549eab`](https://github.com/molinfo-vienna/nerdd-link/commit/4549eab88204dfeb1f36a8002f4565c4d3db9341))

* Fix test cases ([`0de54ed`](https://github.com/molinfo-vienna/nerdd-link/commit/0de54ed5cc8c08136e3944a754cff7e222a367b2))

* Populate repository ([`35aab5d`](https://github.com/molinfo-vienna/nerdd-link/commit/35aab5d50016b23b1524883fa37bd49b6fcc3a01))

* Initial commit ([`561e9f0`](https://github.com/molinfo-vienna/nerdd-link/commit/561e9f000d266e1acc80f207ca8759f0dc8be051))
