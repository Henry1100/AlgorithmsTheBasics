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

        if n % 2 != 0: # n should divisible by 2
            n += 1

        return (10 ** n) * ac + (10 ** (n // 2)) * adcb + bd 


if __name__ == "__main__":
    result = karatsuba_multiplication(12345678998765432112345678987654321, 1212121212121234343434343434343434444444444)
    print(result == 14964459392443222363386654166355210140914770544956011896745221548821561042524)
    result_2 = karatsuba_multiplication(99999, 9999)
    print(f"{result_2: ,}")
    result_3 = karatsuba_multiplication(54912929456625402256174854408349005059747367418045281224869677103460587001371838509047325775339825409089700424382586661886548455, 46159761840763928340146255755371712831239294454920928659343103820160462080093196044837908676121279113445132081834876936121057294)
    print(result_3 == 2534767745696498721291598226410808420875926624404989594109011804054230420328163716811636469827804550673802278410568911221048870743264706668346786117132264407551450821426489441139772838020127634525234251586349419324977858145598895358201970734412370962180770)