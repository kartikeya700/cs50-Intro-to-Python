def main():
    Answer=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    match Answer:
        case "42" | "forty-two" | "forty two": print("Yes")
        case _: print("No")
main()
