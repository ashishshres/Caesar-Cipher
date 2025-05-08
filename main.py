from modules.caesar import caesar
from modules.logo import logo
import os

os.system("cls")
should_continue = True

while should_continue:
  logo()
  choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

  if choice != "encode" and choice != "decode":
    print("Invalid choice!")
    input("Press any key to continue..")
    os.system("cls")
  else:
    message = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))
    caesar(text = message, method = choice, shift = shift_amount)
    go_again = input("Would you like to go again? Type 'yes' to continue or 'no' to exit:\n").lower()

    if go_again != "no" and go_again != "yes":
      print("Invalid choice!")
      input("Press any key to continue..")
      os.system("cls")
    elif go_again == "no":
      should_continue = False
      print("Goodbye! Thanks for using the Caesar Cipher tool.")
          
    os.system("cls")
  # if choice == "encode":
  #   encrypt(message, shift)
  # else: 
  #   decrypt(message, shift)

# alternative
# def encrypt(message, shift):
#   # print(message)
#   # print(shift)
#   cipher_text = ""
#   for i in range(len(message)):
#     char = message[i]
#     shift_char = alphabets.index(char) + shift
#     cipher_text += alphabets[shift_char]
#   print(cipher_text)