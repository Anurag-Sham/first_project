# Encode And Decode
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def caser(plain_text,shift_amount,caser_choice):
    result=""
    for letter in plain_text:
        if letter in alphabet:
             position=alphabet.index(letter)
             if caser_choice =="decode":
                  new_postion=position-shift_amount
             elif caser_choice =="encode":
                  new_postion=position+shift_amount

             result+=alphabet[new_postion]
        else:
             result+=letter
        
    print(f"The {caser_choice}d message is {result}")


should_again=True
while should_again:
     direction =input("Type 'encode' to encrypt , Type 'decode ' to decrypt:\n")
     text=input("Type your message:\n").lower()
     shift=int(input("Tpye the shift number:\n"))
     shift= shift % 25
     
     caser(text,shift,direction)
     again_input=input("Enter if you want to again encode and decode").lower()
     if again_input=="no":
         should_again=False
         print("GoodBye")








     



# def encrypt(plain_text,shift_amount):
#     result=""
#     for letter in plain_text:
#         postion=alphabet.index(letter)
#         new_postion=postion+shift_amount
#         result+=alphabet[new_postion]

#     print(f"Encoded string is ::>> {result}")



# def decrpt(plai_text,shift_amount):
#     result=""
#     for letter in plai_text:
#         postion=alphabet.index(letter)
#         new_postion=postion-shift_amount
#         result+=alphabet[new_postion]

#     print(f"the decoded string is ::>> {result}")


# if direction =="encode":
#     encrypt(text,shift)
# elif direction =="decode":
#     decrpt(text,shift)
# else:
#     print("Enter the valid Choice")







 








