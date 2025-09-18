# check num palindromes from a to b


def is_palindrome(num):
    # skip units
    if num // 10 == 0:
        return False

    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False


def infinite_palindrome():
    num = 0
    while True:
        if is_palindrome(num):
            i = yield num
            if i is not None:
                num = i
        num += 1


def main():
    pal_gen = infinite_palindrome()
    for i in pal_gen:
        print(i)
        digits = len(str(i))
        if digits == 5:
            # pal_gen.throw(ValueError("Size too big."))
            pal_gen.close()
            break
        pal_gen.send(10 ** (digits))


if __name__ == "__main__":
    main()
