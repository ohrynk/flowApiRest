Run pytest:
commands: easy_install -U pytest sobre la carpeta flowApiRest
check version instalada: pytest --version
run unit test: pytest TestCases
run all methods: pytest -v TestCases

Example:
C:\FlowProjects\apiRestProyect\flowApiRest>pytest -v TestCases


============================================================================= test session starts ==============================================================================
platform win32 -- Python 3.8.1, pytest-5.4.1, py-1.8.1, pluggy-0.13.1 -- c:\users\sebastian\appdata\local\programs\python\python38\python.exe
cachedir: .pytest_cache
rootdir: C:\FlowProjects\apiRestProyect\flowApiRest
collected 2 items

TestCases/test_PutToken.py::test_post_token PASSED                                                                                                                        [ 50%]
TestCases/test_PutToken.py::test_post_token_other PASSED

