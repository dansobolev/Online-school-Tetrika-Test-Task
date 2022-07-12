def first_zero(array: str):
    array = list(map(int, list(array)))
    index = array.index(0)
    return index


print(first_zero("111111111110000000000000000"))  # 11
