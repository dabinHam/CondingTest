str = input()

converted_str = ''
for char in str:
    if char.isupper():
        converted_str += char.lower()
    elif char.islower():
        converted_str += char.upper()
    else:
        converted_str += char
        
print(converted_str)