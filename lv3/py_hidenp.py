def hidenp(small: str, big: str) -> bool:
    i: int = 0
    j: int = 0
    while i < len(small) and j < len(big):
        if small[i] == big[j]:
            i += 1
        j += 1

    return i == len(small)

def main() -> None:
    print(hidenp("abc", "a1b2c3"))
    print(hidenp("", "a1b2c3"))
    print(hidenp("abc", "ab"))
    print(hidenp("ab", "abc"))
    print(hidenp("abc", "a1b2c3"))
    print(hidenp("aaaa", "aaa"))
    print(hidenp("sing","subsequence testing"))


if __name__ == "__main__":
    main()

