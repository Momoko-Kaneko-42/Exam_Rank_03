# 複数の条件を、どうやって一つのソートにまとめるか？
def cryptic_sorter(strings: list[str]) -> list[str]:
    result: list[str] = strings[:]
    n = len(result)

    for _ in range(n):
        for j in range(n - 1):
            if sort_key(result[j]) > sort_key(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


def return_vowels_count(letters: str) -> int:
    count = 0
    for c in letters:
        if c in "aeiou":
            count += 1
    return count

# 優先順位付きの比較項目をタプルにまとめる
def sort_key(s: str) -> tuple[int, str, int, str]:
    return(len(s), s.lower(), return_vowels_count(s), s)


# 比較の内容
# def compare_2_strings(stra: str, strb: str) -> bool:
#     if len(stra) > len(strb):
#         return False
#     if len(stra) == len(strb):
#         if stra.lower() > strb.lower():
#             return False
#         if stra.lower() < strb.lower():
#             return True
#         if return_vowels_count(stra) > return_vowels_count(strb):
#             return False
#         if return_vowels_count(stra) < return_vowels_count(strb):
#             return True
#         if stra > strb:
#             return False
#         else:
#             return True
#     else:
#         return True


def main() -> None:
    print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))


if __name__=="__main__":
    main()
