# 両方の文字列に出てくる文字を重複なく返す関数だよ。文字は最初の文字列に出てくる順番で追加される.
def inter(s1: str, s2: str) -> str:
    i: int = 0
    result: str = ""

    while i < len(s1):
        if s1[i] in s2 and s1[i] not in result:
            result += s1[i]
        i += 1
    return result


def main() -> None:
    print(inter("hello", "world"))
    print(inter("banana", "band"))
    print(inter("abcabc", "bc"))
    print(inter("abc", "xyz"))
    print(inter("", "abc"))


if __name__ == "__main__":
    main()
