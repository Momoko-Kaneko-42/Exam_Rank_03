# textの中の隣り合う数字を2文字ずつ順番に比較して、1文字目が2文字目より1だけ小さいペアの数を数えて返す
# 1 2 3 4 なら、1と2で一つ、2と3で一つ、3と4で一つなので戻り値は３
def pattern_tracker(text: str) -> int:
    count: int = 0
    test: int | None = None

    for c in text:
        v: int = "0123456789".find(c)
        if v == -1:
            test = None
        else:
            if test is not None and test == v - 1:
                count += 1
            test = v

    return count


def main() -> None:
    print(pattern_tracker(""))
    print(pattern_tracker("5"))
    print(pattern_tracker("1a2b3c4"))
    print(pattern_tracker("112233"))
    print(pattern_tracker("01234567"))


if __name__ == "__main__":
    main()
