# Ask Paragraf, change what to what

def main():
    paragraph = input("Enter your paragraph:\n")

    words_to_change = []
    replacement_words = []

    try:
        number_of_words = int(
            input("How many words do you want to change (n):\n")
        )
    except ValueError:
        print("You typed wrong, changing the number of words to 1")
        number_of_words = 1

    # Ask which words to change
    for i in range(number_of_words):
        word = input(f"({i + 1}) Word you want to change: ")
        words_to_change.append(word)

    # Ask what they should become
    for i in range(number_of_words):
        word = input(f"({i + 1}) Word to change it to: ")
        replacement_words.append(word)

    remove_caps = input(
        "Would you want to remove capitalization? (Y/n): "
    ).upper()

    if remove_caps == "Y":
        paragraph = paragraph.lower()
        words_to_change = [word.lower() for word in words_to_change]
        replacement_words = [word.lower() for word in replacement_words]

    paragraph = changer(
        paragraph,
        words_to_change,
        replacement_words
    )

    print("\nResult:")
    print(paragraph)


def changer(paragraph, words, replacements):
    for i in range(len(words)):
        paragraph = paragraph.replace(
            words[i],
            replacements[i]
        )

    return paragraph


if __name__ == "__main__":
    main()
