import sys


sys.path.append("../shared")


from encryption_helper import EncryptionHelper
from passwords import Passwords


encryption_helper = EncryptionHelper("test")
passwords = Passwords(encryption_helper)

passwords.add_password("Test", "test-user", "test-password")