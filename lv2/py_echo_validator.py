def echo_validator(text: str) -> bool:
    texts: list[str] = []
    for c in text:
        if 'a' <= c.lower() <= 'z':
            texts.append(c.lower())
    if len(texts) == 0:
        return False
    for i in range(len(texts) // 2):
        if texts[i] != texts[len(texts) - 1 - i]:
            return False
    return True

#内包表記を使って短く書くなら
# def echo_validator(text: str) -> bool:
#     s = [c.lower() for c in text if 'a'<= c.lower() <= 'z']
#     return len(s) > 0 and s == s[::-1]


def main() -> None:
    print(echo_validator("A man a plan a canal Panama"))
    print(echo_validator(""))
    print(echo_validator("!!!"))


if __name__ == "__main__":
    main()
