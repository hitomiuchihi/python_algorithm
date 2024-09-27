### 問題 1: 素数判定

整数が与えられたとき、その数が素数かどうかを判定する関数 `is_prime(n)` を作成せよ。

**サンプル入力**:

```python
print(is_prime(11))  # True
print(is_prime(4))   # False
```

---

### 問題 2: フィボナッチ数列

N 番目のフィボナッチ数を返す関数 `fibonacci(n)` を作成せよ。

**サンプル入力**:

```python
print(fibonacci(10))  # 55
```

---

### 問題 3: 回文判定

文字列が与えられたとき、その文字列が回文かどうかを判定する関数 `is_palindrome(s)` を作成せよ。

**サンプル入力**:

```python
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
```

---

### 問題 4: 階乗計算

整数 `n` に対してその階乗を返す関数 `factorial(n)` を作成せよ。

**サンプル入力**:

```python
print(factorial(5))  # 120
```

---

### 問題 5: 配列の最大値

与えられた整数の配列から最大値を返す関数 `find_max(arr)` を作成せよ。

**サンプル入力**:

```python
print(find_max([1, 5, 9, 3, 7]))  # 9
```

---

### 問題 6: 文字列の逆順

文字列を逆順にする関数 `reverse_string(s)` を作成せよ。

**サンプル入力**:

```python
print(reverse_string("python"))  # "nohtyp"
```

---

### 問題 7: 重複要素の削除

与えられたリストから重複要素を削除する関数 `remove_duplicates(lst)` を作成せよ。

**サンプル入力**:

```python
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]
```

---

### 問題 8: リストの積

与えられたリスト内の全ての要素の積を計算する関数 `list_product(lst)` を作成せよ。

**サンプル入力**:

```python
print(list_product([1, 2, 3, 4]))  # 24
```

---

### 問題 9: 二分探索

ソートされたリスト `lst` とターゲット `x` が与えられたとき、`x` のインデックスを返す関数 `binary_search(lst, x)` を作成せよ。見つからない場合は `-1` を返す。

**サンプル入力**:

```python
print(binary_search([1, 2, 3, 4, 5], 3))  # 2
print(binary_search([1, 2, 3, 4, 5], 6))  # -1
```

---

### 問題 10: 最長の単語

与えられた文字列から最も長い単語を返す関数 `longest_word(s)` を作成せよ。

**サンプル入力**:

```python
print(longest_word("The quick brown fox jumps over the lazy dog"))  # "jumps"
```

---

### 問題 11: 素数のリスト

N 以下の全ての素数をリストで返す関数 `prime_numbers(n)` を作成せよ。

**サンプル入力**:

```python
print(prime_numbers(10))  # [2, 3, 5, 7]
```

---

### 問題 12: アナグラム判定

2つの文字列が与えられたとき、それらがアナグラムかどうかを判定する関数 `is_anagram(s1, s2)` を作成せよ。

**サンプル入力**:

```python
print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False
```

---

### 問題 13: 文字数カウント

与えられた文字列内の文字の出現回数をカウントして辞書で返す関数 `char_count(s)` を作成せよ。

**サンプル入力**:

```python
print(char_count("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

---

### 問題 14: 数字のカウント

与えられた整数のリストから偶数と奇数の数をカウントする関数 `count_even_odd(lst)` を作成せよ。

**サンプル入力**:

```python
print(count_even_odd([1, 2, 3, 4, 5, 6]))  # (3, 3)
```

---

### 問題 15: 文字列の圧縮

与えられた文字列の連続する同じ文字を圧縮して返す関数 `compress_string(s)` を作成せよ。

**サンプル入力**:

```python
print(compress_string("aaabbbcccaaa"))  # "a3b3c3a3"
```

---

### 問題 16: 配列の反転

与えられた配列を反転させる関数 `reverse_list(lst)` を作成せよ。

**サンプル入力**:

```python
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
```

---

### 問題 17: 2つのリストの交差

2つのリストの共通要素を返す関数 `list_intersection(lst1, lst2)` を作成せよ。

**サンプル入力**:

```python
print(list_intersection([1, 2, 3], [3, 4, 5]))  # [3]
```

---

### 問題 18: 完全数の判定

与えられた整数が完全数かどうかを判定する関数 `is_perfect_number(n)` を作成せよ。完全数とは、自分自身を除く約数の和が自分自身に等しい数である。

**サンプル入力**:

```python
print(is_perfect_number(6))   # True
print(is_perfect_number(28))  # True
print(is_perfect_number(12))  # Fals
```

---

### 問題 19: ローマ数字変換

整数をローマ数字に変換する関数 `int_to_roman(num)` を作成せよ。

**サンプル入力**:

```python
print(int_to_roman(58))  # "LVIII"
```

---

### 問題 20: 連続した要素の和

与えられたリストから連続した要素の部分配列のうち最大の和を持つものを返す関数 `max_subarray_sum(lst)` を作成せよ。

**サンプル入力**:
```python
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
```