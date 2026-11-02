def twist_sequence(arr: list[int], k: int) -> list[int]:
    # 次の行のlen(arr)が0になると、k % 0でZeroDivisionErrorになるので、それを避ける
    if not arr:
        return []
    # kが長さ以上でも、1周分は意味がないので、余りだけに。
    k = k % len(arr)

    # スライスで、「後ろのk個」と「それ以外の前の部分」を取り出して、順番を入れ替えてつなげる。
    # 「arr[-k:]は、k = 0のとき、末尾の0個ではなく、全部を指す」
    return (arr[-k:] + arr[:-k])


def main() -> None:
    print(twist_sequence([1,2,3,4,5], 2))
    print(twist_sequence([1,2,3], 1))
    print(twist_sequence([1,2,3,4], 0))
    print(twist_sequence([1,2,3], 5))
    print(twist_sequence([], 3))


if __name__ == "__main__":
    main()

# Assignment name  : py_twist_sequence
# Expected files   : py_twist_sequence.py
# Allowed functions: 
# --------------------------------------------------------------------------------

# Write a function that rotates an array to the right by k positions.
# Rotating right by k means the last k elements move to the front.

# Function signature:
# def twist_sequence(arr: list[int], k: int) -> list[int]:

# Examples:

# Input:
# twist_sequence([1,2,3,4,5], 2)
# Output:
# [4,5,1,2,3]

# Input:
# twist_sequence([1,2,3], 1)
# Output:
# [3,1,2]

# Input:
# twist_sequence([1,2,3,4], 0)
# Output:
# [1,2,3,4]

# Input:
# twist_sequence([1,2,3], 5)
# Output:
# [2,3,1]

# Input:
# twist_sequence([], 3)
# Output:
# []