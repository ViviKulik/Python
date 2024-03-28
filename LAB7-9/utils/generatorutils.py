import random
import string


def randomString(length):
    letters = string.ascii_lowercase
    resultStr = ''.join(random.choice(letters) for _ in range(length))
    return resultStr
