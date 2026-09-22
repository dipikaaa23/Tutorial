text = input("Enter a string with at least 8 characters: ")

if len(text) < 8:
    print("Please enter a string with at least 8 characters.")
else:
    # Display ASCII value of each character
    print("ASCII values:")

    for character in text:
        print(character, "=", ord(character))

    # Capitalize characters at positions 2, 4, 6, 8, ...
    modified_text = ""

    for i in range(len(text)):
        character = text[i]

        if (i + 1) % 2 == 0:
            ascii_value = ord(character)

            if ascii_value >= 97 and ascii_value <= 122:
                ascii_value = ascii_value - 32
                character = chr(ascii_value)

        modified_text = modified_text + character

    print("Final modified string:", modified_text)