def main():
    """
    Take in a word and an integer and repeat the word n times
    """
    word = input("Enter word to repeat: ")
    n = int(input("Enter number of times to repeat: "))

    for i in range(0, n):
        print(word)


if __name__ == "__main__":
    main()
