import sys#
# 
type_crypt = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n" ).lower()

if type_crypt != "encode" or type_crypt != "decode":
    print("enter encode or decode!!!")
    sys.exit()

#user enter message which want to move character
message = input("Type your message:\n")

#enter number of shift for entered String
number = int(input("Type the shift number:\n"))
#ABCD case encrypt ZABC
#ABCD case decrypt BCDF

changed_result = []

#A,a의 경우, Z,z~로 잘 변환되지만, 그외의 글자는 변환이 잘못되는 버그가 일어난다.
if type_crypt == "encode":
    for message_chr in list(message):
        char_ord = ord(message_chr)
        changed_char_ord = char_ord - number
        #A~Z
        if message_chr.isupper():
            if changed_char_ord - 65 < 0:
                changed_result.append(chr(changed_char_ord + 26))
            else:
                changed_result.append(chr(changed_char_ord))
        else:
            #a~z
            if changed_char_ord - 97 < 0:
                changed_result.append(chr(changed_char_ord + 26))
            else:
                changed_result.append(chr(changed_char_ord))
else:
    for message_chr in list(message):
        char_ord = ord(message_chr)
        changed_char_ord = char_ord + number
        if message_chr.isupper():
            if changed_char_ord - 90 > 0:
                changed_result.append(chr(changed_char_ord - 26))
            else:
                changed_result.append(chr(changed_char_ord))                
        else:
            #a~z
            if changed_char_ord - 122 > 0:
                changed_result.append(chr(changed_char_ord + 26))
            else:
                changed_result.append(chr(changed_char_ord))   

print(''.join(changed_result))