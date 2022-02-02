x=10
y='luis'

z=x
x=y
y=z
print(f'x={x} e y={y}')

#outro método
x,y=y,x
print(f'x={x} e y={y}')