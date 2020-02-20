#
#   PIN_assembly.py
#   A test implementation of creating a secure PIN.
#   By - Robert Maloy
#   19 February 2020
#

## Import libraries so we can extract data and write data
import uuid
import csv

## Extract MAC Address using UUID
var_MAC_addr = hex(uuid.getnode())
# print("MAC address: "+var_MAC_addr) -- debug statement

## Set up the four-digit hex string we're going to convert into a PIN
var_ext_Digits = str(var_MAC_addr[2:4] + var_MAC_addr[-2:])
# print("pulled digits: "+var_ext_Digits) -- debug statement

##Create hexadecimal pin
pin_hex = var_ext_Digits[1]+var_ext_Digits[0]+var_ext_Digits[3]+var_ext_Digits[2]
# print("assembled hex phrase: "+pin_hex) -- debug statement

## Create integer pin
pin_int = int(pin_hex, 16)
if(len(str(pin_int)) <= 4):
    pin_int = pin_int + '0'
# print("assembled integer pin: "+str(pin_int)) -- debug statement

# Write user data to database.csv.
try:
    f = open('database.csv') #attempt to open CSV file as variable f
except IOError: #if you cannot find this file
    print("Database file not found! Creating...")
    with open('database.csv', 'w', newline='') as csvfile: #open to write file immediately
        dbWrite = csv.writer(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL) #set parameters
        dbWrite.writerow(['Index']+['User']+['Pin']) # write data
        print("Success!") #confirm that this worked

with open('database.csv', 'rt') as a: #open it again, this time to read it
    reader=csv.reader(a, delimiter=',', quotechar="'") #set parameters
    for row in reader: #for all rows in the reader
        for field in row: #for specific fields in that row
            if field == str(pin_int): #if the field is equivalent to our PIN, that means we've already stuck it in there.
                print("PIN already in database.") #indicate we're not creating a duplicate value.
                exit() #kill this script

#If the script has not been killed by the previous check, then proceed here.
with open('database.csv', 'a', newline='') as csvfile: #Open file for appending
        dbWrite = csv.writer(csvfile, delimiter=',', quotechar="'", quoting=csv.QUOTE_ALL) #set parameters
        dbWrite.writerow(['1']+['service'] + [pin_int]) #write the row for our pin and user
        print("Administrative user added.") #indicate we've successfully written the new user.
        exit() #terminate