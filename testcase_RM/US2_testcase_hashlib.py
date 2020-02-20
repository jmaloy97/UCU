##  US2_testcase_hashlib.py
##  Robert Maloy
##  20 February 2020

import hashlib

pin_int = "5494"

pinHashed = hashlib.sha256(pin_int.encode())
pinHashed = pinHashed.hexdigest()
print(pinHashed)
