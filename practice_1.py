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
    if n < 0:
        return "please input positive integer."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(10))  # 55

# 問題3: 文字列が与えられたとき、その文字列が回文かどうかを判定する関数 is_palindrome(s)
def is_palindrome(str):
    reversed_str = str[::-1]
    if str == reversed_str:
        return True
    else:
        return False

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False

# 問題4: 整数 n に対してその階乗を返す関数 factorial(n)
def factorial(n):
    for i in range(n-1, 0, -1):
        print(F"n:{n}, i:{i}")
        n = n * i
    return n

print(factorial(5))  # 120

# 問題5: 与えられた整数の配列から最大値を返す関数 find_max(arr)
def find_max(arr):
    max_num = max(arr)
    return max_num

print(find_max([1, 5, 9, 3, 7]))  # 9