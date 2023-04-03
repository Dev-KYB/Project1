def add_func(n1, n2):
    res= n1+n2
    return res

def sub_func(n1, n2):
    return n1-n2

def gob_func(n1, n2):
    return n1*n2

def nanu_func(n1, n2):
    return n1/n2

def gob2_func(n3,n4):
    return n3**n4

num1,num2, result=100,200,0
num3,num4, result2=10,2,0


result = add_func(num1, num2)
print(num1, '+', num2, '=', result)

result = add_func(num1, num2)
print(num1, '-', num2, '=', result)

result = gob_func(num1, num2)
print(num1, '*', num2, '=', result)

result = nanu_func(num1, num2)
print(num1, '/', num2, '=', result)

result = gob2_func(num3,num4)
print(num3, '**', num4, '=', result)