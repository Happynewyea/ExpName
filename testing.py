import math

ceil = math.ceil

atkSet = 16
defSet = 8

desmos = []

for i in range(1, 101):
    for j in range(1, 101):
        dam = i * ( 1 - ( 1 + j ) / ( 3 * j ) )
        if dam > 0:
            desmos.append(ceil(dam))

damage = atkSet * ( 1 -  ( 1 + defSet ) / ( 3 * defSet ) )

# print((desmos))
print(len(desmos))
# print(damage)