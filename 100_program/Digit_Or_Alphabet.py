# Check digit or alphabet

ch = input("Enter a character: ")

if ch.startswith('-') and len(ch) > 1:
    print("Character invalid !")

elif len(ch) != 1:
    print("Character invalid !")

elif ch.isdigit():
    print("Digit")

elif ch.isalpha():
    print("Alphabet")

else:
    print("Special Character")


# Output:
# Enter a character: 7
# Digit
