x = int(input('請輸入分子'))
y = int(input('請輸入分母'))

def zero(func):
    def wrap(n, d):
        if d == 0 :
            return 0
        else:
            return n  / d
    return wrap

@zero
def divide(n,  d):
       return int(n  / d)

print(divide(x,y))