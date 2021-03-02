def pow(number, exponent):
    result = 1
    if exponent > 0:
        for exponent in range(exponent, 0, -1):
            result *= number
        return result
    elif exponent < 0:
        for exponent in range(exponent, 0, +1):
            result /= number
        return result

r = pow(10, 6)
print(r)