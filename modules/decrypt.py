# def decrypt(cipher_text, shift):
#   plain_text = ""
#   for char in cipher_text:
#     curr_position = alphabets.index(char)
#     shift_position = curr_position - shift 
#     if shift_position < 0:
#       shift_position = shift_position + 26 
#     # print(shift_position)
#     plain_text += alphabets[shift_position]
#   print(f"The decoded text is {plain_text}")

# decrypt(message, shift)