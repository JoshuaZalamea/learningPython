def to_upper(string):
    ## converts a string into uppercase
    upper_case = ""
    for character in string:
        if 'a' <= character <= 'z':
            location = ord(character) - ord('a')
            new_ascii = location + ord('A')
            character = chr(new_ascii)
        upper_case = upper_case + character
    return upper_case

print(to_upper("This is text"))

word = input("Input is: ")
print(to_upper(word))