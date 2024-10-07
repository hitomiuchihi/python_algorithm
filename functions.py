def num(value):
    return value

value1 = num(0) and num(1) and num(2)
value2 = num(0) or num(1) or num(2)

print(f"value1:{value1}, value2:{value2}")
# value1:0, value2:1

def judge_value(value):
    if value is None:
        return (f"value: None.")
    else:
        return (f"value: {type(value)}")

print(judge_value(None))
print(judge_value("dog"))

def try_range(num):
    if num <= 10:
        for i in range(num):
            print(f"num:{num}, i = {i}")
    elif num > 10 and num <= 20:
        for i in range(num, num+5):
            print(f"num:{num}, i={i}")
    else:
        for i in range(num, num+10, 3):
            print(f"num:{num}, i={i}")

try_range(9)
try_range(15)
try_range(25)

family = {
    'papa': 'yuuichi',
    'mama': 'hitomi',
    'daughter': 'peco',
    'son': 'bitaro'
}

print(family.items())

for k,v in family.items():
    print(k, v)

numbers = [1,9,4,5,6,3,2]
characters = ['あ', 'ん', 'う', 'お', 'か', 'え']
print(sorted(numbers))
print(sorted(characters))
print(reversed(sorted(numbers)))
print(reversed(sorted(characters)))
print(list(reversed(sorted(numbers))))
print(list(reversed(sorted(characters))))

list_a = [2, 4, 6]
list_b = ['a', 'b', 'c']

for a, b in zip(list_a, list_b):
    print(f"a:{a}, b:{b}, a*b:{a*b}")

def function(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)

function(1, 'one', kwargs1='kw1', kwargs='kw2')

function = lambda x, y: (y + 2, x * 4)
a, b = 2, 5
a, b = function(a, b)
print(a, b)

def function(a, b):
    """
    1行目には、クラスや関数の説明コメントを書く

    3行目には詳細な説明（呼び出しや引数についてなど）
    """
    return a + b

print(function.__doc__)

