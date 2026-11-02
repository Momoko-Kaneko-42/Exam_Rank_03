# 偶数文字目は大文字、奇数文字目は小文字、アルファベット以外はそのまま出力、スペースの後は小文字から始まる
def string_sculptor(text: str) -> str:
    result: str = ""
    count: int = 0

    for c in text:
        if c.isalpha():
            if count % 2 == 0:
                count += 1
                result += c.upper()
            else:
                count += 1
                result += c.lower()
        elif c == " ":
            count = 1
            result += c
        else:
            count += 1
            result += c
    return result


def main() -> None:
    print(string_sculptor("hello"))
    print(string_sculptor("Hello World"))
    print(string_sculptor("abc123def"))
    print(string_sculptor("Python3.9!"))
    print(string_sculptor(""))


if __name__ == "__main__":
    main()
