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