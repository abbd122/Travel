import string
import random


secret_key = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10))

print(secret_key)
