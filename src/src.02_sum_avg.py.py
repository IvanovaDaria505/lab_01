a=input('a: ')
b=input('b: ')
a=a.replace(',','.',1)
b=b.replace(',','.',1)
a=float(a)
b=float(b)
c=a+b
print(f'sum={c:.2f}; avg={(c/2):.2f}')
