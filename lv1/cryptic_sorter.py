# 複数の条件を、どうやって一つのソートにまとめるか？
def cryptic_sorter(strings: list[str]) -> list[str]:
    tmp: list[str] = strings[:]
    n = len(tmp)

    for i in range(n - 1):
        for j in range(n - 1):
            if not compare_2_strings(tmp[j], tmp[j + 1]):
                tmp[j], tmp[j + 1] = tmp[j + 1], tmp[j]
    return tmp


def return_vowels_count(letters: str) -> int:
    count = 0
    for c in letters:
        if c in "aeiou":
            count += 1
    return count


def compare_2_strings(stra: str, strb: str) -> bool:
    if len(stra) > len(strb):
        return False
    if len(stra) == len(strb):
        if stra.lower() > strb.lower():
            return False
        if stra.lower() < strb.lower():
            return True
        if return_vowels_count(stra) > return_vowels_count(strb):
            return False
        if return_vowels_count(stra) < return_vowels_count(strb):
            return True
        if stra > strb:
            return False
        else:
            return True
    else:
        return True


def main() -> None:
    print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))


if __name__=="__main__":
    main()
