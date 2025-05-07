alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(message, shift):
  # print(message)
  # print(shift)
  cipher_text = ""
  for char in message:
    curr_position = alphabets.index(char)
    shift_position = curr_position + shift 
    if shift_position >= 25:
      shift_position = shift_position % 26 
    print(shift_position)
    cipher_text += alphabets[shift_position]
  print(cipher_text)

encrypt(message, shift)

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