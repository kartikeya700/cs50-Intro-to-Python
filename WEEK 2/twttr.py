def main():
    text = input("Input: ")
    vowel = ["a", "e", "i", "o", "u"]
    for c in text:
        if c.lower() in vowel:
            print("", end="")
        else:
            print(c, end="")
    print()
main()
