# 2つの文字列の値が同じだったらTrue

def count_letters(s: str) -> dict[str, int]:
    count: dict[str, int] = {}

    for c in s:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1

    return count


def string_permutation_checker(s1: str, s2: str) -> bool:
    count1: dict[str, int] = count_letters(s1)
    count2: dict[str, int] = count_letters(s2)

    return count1 == count2
    # return sorted(s1) == sorted(s2)

def main() -> None:
    print(string_permutation_checker("abc", "bca")) 
    print(string_permutation_checker("abc", "def"))
    print(string_permutation_checker("listen", "silent"))
    print(string_permutation_checker("hello", "bello"))
    print(string_permutation_checker("", ""))
    print(string_permutation_checker("a", ""))
    print(string_permutation_checker("Abc", "abc"))
    print(string_permutation_checker("a gentleman","elegant man"))


if __name__ == "__main__":
    main()
