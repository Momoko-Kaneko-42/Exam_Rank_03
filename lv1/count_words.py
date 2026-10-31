def count_words(word: str)-> int:
    count: int = 0
    is_word: bool = False

    for c in word:
        if c == " ":
            is_word = False
        elif is_word == False:
            count += 1
            is_word = True

    return count

def main()->None:
    s = "Hello World"
    count = count_words(s)

    print(f"{count}")

if __name__=="__main__":
    main()