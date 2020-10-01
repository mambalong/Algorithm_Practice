
def toBaseN(num, base):
    table = '0123456789ABCDEF'
    res = ''
    negative = 0
    if num < 0:
        num = -num
        negative = 1
    
    while num:
        res = table[num % base] + res
        num //= base
    return '-' + res if negative else res

print(toBaseN(16, 2))