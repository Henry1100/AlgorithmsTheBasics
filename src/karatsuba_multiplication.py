# Implement Karatsuba´s multiplication algorithm in your
# favorite programming language. Your program should invoke
# the language´s multiplication operator only on pairs of single-digit 
# numbers

def karatsuba_multiplication(x : int, y : int) -> int:
    x_str = str(x)
    y_str = str(y)

    if len(x_str) < len(y_str):
        x_str = '0' * (len(y_str) - len(x_str)) + x_str
    elif len(x_str) > len(y_str):
        y_str = '0' * (len(x_str) - len(y_str)) + y_str

    if len(x_str) == 1: # Can be either len(x) or len(y) as we are assumming n digit number for both
        return x * y
    else:
        n = len(x_str)
        # First and Second halves of x
        a = int(x_str[:len(x_str) // 2])
        b = int(x_str[len(x_str) // 2:])
        # First and Second halves of y
        c = int(y_str[:len(y_str) // 2])
        d = int(y_str[len(y_str) // 2:])
        # Compute a + b and c + d
        p = a + b
        q = c + d
        # Compute ac, bd, pq recursively
        ac = karatsuba_multiplication(a, c)
        bd = karatsuba_multiplication(b, d)
        pq = karatsuba_multiplication(p, q)

        adcb = pq - ac - bd

        if n % 2 != 0:
            n += 1

        return (10 ** n) * ac + (10 ** (n // 2)) * adcb + bd 


if __name__ == "__main__":
    print(karatsuba_multiplication(5678, 1234))