import sys
import method as md

#question user enter encode or decode
type_crypt = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n" ).lower()

#check whether if user enter (encode, decode)
if type_crypt in ("encode","decode"):
    #user enter message which want to move character
    message = input("Type your message:\n")
    #enter number of shift for entered String
    number = int(input("Type the shift number:\n"))
    if type_crypt == "encode":
        md.encrypt(message, number)
    else:
        md.decrypt(message, number)
else:
    print("enter encode or decode")
    sys.exit()