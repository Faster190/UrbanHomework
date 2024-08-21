def is_prime(funk):
    def wrapper(*num):
        res = funk(*num)
        ctr = 0
        tmp = 0
        while ctr < 3 and tmp <= res:
            tmp += 1
            if res % tmp == 0:
                ctr += 1
        if ctr == 2:
            print("Простое")
        else:
            print("Составное")
        return res
    return wrapper


@is_prime
def sum_three(*num):
    sum_ = 0
    for i in num:
        sum_ += i
    return sum_


result = sum_three(2, 3, 6)
print(result)
