# ここに回答を作成
# 問題1:整数が与えられたとき、その数が素数かどうかを判定する関数 is_prime(n)
def is_prime(n):
    print(f"n:{n}")
    if n < 2:
        return False
    elif n >= 2:
        for i in range(2, int(n/2) +1):
            print(f"i:{i}")
            print(f"n%i:{n%i}")
            if n % i == 0:
                return False
    return True
    
#print(is_prime(11))  # True
#print(is_prime(4))   # False

# 問題2:N 番目のフィボナッチ数を返す関数 fibonacci(n)
def fibonacci(n):
    return "fib"


print(fibonacci(10))  # 55