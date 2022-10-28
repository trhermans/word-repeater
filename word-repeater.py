def main():
    """
    Take in a word and an integer and repeat the word n times
    """
    word = input("Enter word to repeat: ")
    n = int(input("Enter number of times to repeat: "))

    for i in range(1, n+1):
        print(word)

# fix the problem the words repeat n-1 times
if __name__ == "__main__":
    main()
