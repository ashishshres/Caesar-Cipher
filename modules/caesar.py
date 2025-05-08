alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, method, shift):
  message = ""
  for char in text:
    if char != " ":
      curr_position = alphabets.index(char)
      if method == "encode":
        shift_position = curr_position + shift 
        if shift_position >= 25:
          shift_position = shift_position % 26 
      else:
        shift_position = curr_position - shift 
        if shift_position < 0:
          shift_position = shift_position + 26 
    
      message += alphabets[shift_position]
    else:
      message += " "
    
  print(f"The {method}d message is '{message}'")
