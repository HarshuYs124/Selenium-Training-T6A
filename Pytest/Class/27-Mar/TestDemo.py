from ctypes.macholib.dyld import framework_find


class TestDemo:
    # def __init__(self): # can not use constructors
    #     print("Constructor called ")
    def test_register(self):
      print("registering ......")
    def test_login(self):
      print("logging in .....")
    def test_logout(self):
      print("loggging out .....")


'''pytest is the unit testing framework
the rules are:
1. file name starts with "test-"
2. func and method name starts with "test-"
2. file name ends with ".py"
2. -v stands for verbocity gives detailed description of code
3. s stands for scripting , it will print all ststements

Note: if the function is not written according to rule, pytest doesn't recognize the functions.'''


