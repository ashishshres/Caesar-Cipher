from modules.caesar import caesar
from modules.logo import logo

logo()

choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

if choice != "encode" and choice != "decode":
  print("Invalid choice!")
else:
  message = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text = message, method = choice, shift = shift)

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