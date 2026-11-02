# 2つのリストをマージしてソートされた一つのリストにして返す
# すでに並んでいる2つのリストの性質を使って、1回の走査で合わせる
# 位置を憶えておく変数を2つ用意する。

# result を空で用意
# list1 と list2 のどちらも空でない間:
#     先頭同士を比べて、小さい方を pop(0) して result に追加
# 残っている方を result に足す
# result を返す

def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    result: list[int] = []

    while list1 and list2:
        if list1[0] > list2[0]:
            x: int = list2.pop(0)
        else:
            x = list1.pop(0)
        result.append(x)

    return result + list1 + list2


def main() -> None:
    print(shadow_merge([1, 3, 5], [2, 4, 6]))
    print(shadow_merge([1, 2, 3], [4, 5, 6]))
    print(shadow_merge([1], [2, 3, 4]))
    print(shadow_merge([], [1, 2, 3]))
    print(shadow_merge([1, 1, 2], [1, 3, 3]))


if __name__ == "__main__":
    main()
