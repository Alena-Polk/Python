import re


def validate_name(name):
    return re.findall(r'^[a-z\d@_-]{6,18}$', name, re.IGNORECASE)


print(validate_name('my-p@ssw0rd'))
