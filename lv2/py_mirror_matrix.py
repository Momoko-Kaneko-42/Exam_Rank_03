def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    new_matrix = []
    for row in matrix:
        new_matrix.append(row[::-1])
    return new_matrix


def main() -> None:
    print(mirror_matrix([[1,2,3],[4,5,6]]))


if __name__ == "__main__":
    main()
