import sys

sys.path.append("../shared")

from encryption_helper import EncryptionHelper
from passwords import passwords_file

encryption_helper = EncryptionHelper("test")
data = encryption_helper.decrypt_file(passwords_file)

print(data)