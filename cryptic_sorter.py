def cryptic_sorter(strings: list[str]) -> list[str]:
    n = len(strings)

    for i in range(n - 1):
        for j in range(n - 1):
            if len(strings[j]) > len(strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
            elif len(strings[j]) == len(strings[j + 1]):
                if strings[j].lower() > strings[j + 1].lower():
                    strings[j], strings[j + 1] = strings[j + 1], strings[j]
