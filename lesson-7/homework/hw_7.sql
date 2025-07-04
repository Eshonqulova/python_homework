def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
is_prime(5)

def digit_sum(k):
    if len(str(k))==2:
        return k%10+k//10
    elif len(str(k))==3:
        hundered = k//100
        ten = (k//10)%10
        one = k%10
        return hundered+ten+one

digit_sum(125)


def ikki_sonning_darajalari(n):
    k = 1
    while 2 ** k <=n:
        print(2**k,end=' ')
        k+=1

ikki_sonning_darajalari(10)

