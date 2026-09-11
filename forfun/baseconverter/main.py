BASE_CHAR_SET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def num_into_base_str(num: int, base: int = 10) -> str:
    output = ""

    while num != 0:
        index = num % base
        num //= base

        output += BASE_CHAR_SET[index]

    return output[::-1]

def base_str_into_num(base_str: str, base: int) -> int:
    output = 0

    for position, char in zip(range(len(base_str) - 1, -1, -1), base_str):
        index = BASE_CHAR_SET.index(char)

        if index >= base:
            raise Exception("out of base range")

        output += index * (base ** position)


    return output
