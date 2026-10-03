#  Text Mystery Analyzer

print("================================")
print("      TEXT MYSTERY ANALYZER")
print("================================")

text = input("Enter your message: ")

while True:

    print("\n--------- MENU ---------")
    print("1. Show Message")
    print("2. Count Characters")
    print("3. Count Words")
    print("4. Find Repeated Word")
    print("5. Find Repeated Character")
    print("6. Show First and Last Character")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    # 1. Show message
    if choice == "1":
        print("\nYour Message:")
        print(text)

    # 2. Count characters
    elif choice == "2":
        print("\nTotal Characters:", len(text))

    # 3. Count words
    elif choice == "3":
        words = text.split()
        print("\nTotal Words:", len(words))

    # 4. Find repeated word
    elif choice == "4":
        word = input("Enter a word: ")

        words = text.lower().split()
        count = words.count(word.lower())

        print("The word", word, "appears", count, "time(s).")

    # 5. Find repeated character
    elif choice == "5":
        character = input("Enter one character: ")

        count = text.lower().count(character.lower())

        print("The character", character, "appears", count, "time(s).")

    # 6. First and last character
    elif choice == "6":
        print("\nFirst character:", text[0])
        print("Last character:", text[-1])

    # 7. Exit
    elif choice == "7":
        print("\nThank you for using Text Mystery Analyzer!")
        break

    else:
        print("\nInvalid choice. Please try again.")

