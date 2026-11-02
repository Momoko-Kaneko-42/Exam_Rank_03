def count_letters(s: str) -> dict[str, int]:
    count: dict[str, int] = {}

    for c in s.lower():
        if c != " ":
            if c in count:
                count[c] += 1
            else:
                count[c] = 1

    return count


def anagram(s1: str, s2: str) -> bool:
    res1: dict[str, int] = count_letters(s1)
    res2: dict[str, int] = count_letters(s2)

    return res1 == res2

# def anagram(s1: str, s2: str) -> bool:
#     # スペースを削除し、小文字に変換
#     s1_nospace = s1.lower().replace(" ", "")
#     s2_nospace = s2.lower().replace(" ", "")
#     # 文字数が違ったら、False
#     if len(s1_nospace) != len(s2_nospace):
#         return False
#     # 比べるほうs2をリストにする
#     s2_nospace_list = list(s2_nospace)
#     # s1の文字がs2にあったら、s2のその文字を削除する
#     for c in s1_nospace:
#         if c in s2_nospace_list:
#             s2_nospace_list.remove(c)
#         else:
#             return False

#     return not s2_nospace_list


def main() -> None:
    print(anagram("listen", "silent"))
    print(anagram("Triangle", "Integral"))
    print(anagram("Dormitory", "Dirty Room"))
    print(anagram("hello", "world"))
    print(anagram("", ""))
    print(anagram("abc", "abcc"))


if __name__ == "__main__":
    main()
