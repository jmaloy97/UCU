#
#   testcase_StringLength.py
#   A brief little script just to make sure that I know how to check the lengths of strings.
#   By - Robert Maloy
#   19 February 2020
#

pin_int = '98016346'
print(pin_int + " (pre-extend)")

if(len(str(pin_int)) <= 4):
    pin_int = pin_int + '0'
    print(pin_int)