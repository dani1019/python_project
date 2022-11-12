#print make user enter encode or decode
type_crypt = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n" ).lower()

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
                changed_result.append(chr(changed_char_ord + 25))
            else:
                changed_result.append(chr(changed_char_ord))
        else:
            #a~z
            if changed_char_ord - 97 < 0:
                changed_result.append(chr(changed_char_ord + 25))
            else:
                changed_result.append(chr(changed_char_ord))

print(''.join(changed_result))



        #A 65 Z 90
        #a 97 z 122
        # if ord(message_chr) == 65:
        #     char_ord = ord("Z") + 1
        # #a change z    
        # elif ord(message_chr) == 97:
        #     char_ord = ord("z") + 1
        # char_ord = char_ord - number
        # changed_result.append(chr(char_ord))
print(''.join(changed_result))