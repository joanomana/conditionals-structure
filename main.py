print("Exercise 4")

word1 = str(input("Enter a word: "))
word2 = str(input("Enter another word: "))

if len(word1) > len(word2):
    sword=len(word1)-len(word2)
    print(f"The {word1} have {sword} more letters than {word2}")
elif len(word2) > len(word1):
        sword=len(word2)-len(word1)
        print(f"The {word2} have {sword} more letters than {word1}")
else:
        print(f"{word1} and {word2} are the same length")

