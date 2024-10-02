# ここに回答を作成
# 問題1
def is_prime(n):
    array = []
    if n < 2:
        return False
    elif n >= 2:
        for i in range(2, n + 1):
            if n % i == 0:
                array.append(i)
        if len(array) == 1:
            return True
        else:
            return False
    
print(is_prime(11))  # True
print(is_prime(4))   # False