# from_base進数で書かれた文字列を、to_base進数の文字列に直します。進数は2から36まで、数字は0-9とA-Z（Aが10、Zが35）です。入力が不正なら、"ERROR"を返します。
# number（from_base進数の文字列）→ 普通の整数
# その整数 → to_base進数の文字列

def to_value(number: str, from_base: int) -> int:
    base: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value: int = 0

    for c in number:
        v: int = base.find(c.upper())
        if 0 <= v < from_base:
            value = value * from_base + v
        else:
            return -1
    return value


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    base: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # 1. from_base / to_base が 2〜36 でなければ "ERROR" を返す
    if 2 > from_base or from_base > 36:
        return "ERROR"
    if 2 > to_base or to_base > 36:
        return "ERROR"
    if number == "":
        return "ERROR"
    # 2. value = to_value(number, from_base)
    value: int = 0
    result: str = ""
    is_negative: bool = False

    # 3.負数かどうか判断
    if len(number) >= 2 and number[0] == '-':
        is_negative = True
        number = number[1:]
    value = to_value(number, from_base)
    # 4. value が -1 なら "ERROR" を返す
    if value == -1:
        return "ERROR"
    # 5. value が 0 なら "0" を返す
    if value == 0:
        return "0" 
    # 6. value を to_base で割った余りを集めて、逆順の文字列にして返す
    while value > 0:
        res: str = base[value % to_base]
        result += res
        value //= to_base

    result = result[::-1]

    if is_negative:
        result = '-' + result
    return result


def main() -> None:
    # print(number_base_converter("1010", 2, 10))
    # print(number_base_converter("FF", 16, 10))
    print(number_base_converter("255", 10, 16))
    print(number_base_converter("123", 10, 2))
    # print(number_base_converter("Z", 36, 10))
    # print(number_base_converter("35", 10, 36))
    # print(number_base_converter("123", 1, 10))
    # print(number_base_converter("G", 16, 10))
    print(number_base_converter("-", 10, 2))
    print(number_base_converter("0", 10, 2))
    print(number_base_converter("-0", 10, 2))
    # print(to_value("1010", 2))
    # print(to_value("FF", 16))
    # print(to_value("G", 16))
    # print(to_value("0", 34))
if __name__ == "__main__":
    main()
