import math
warriors = int(input("Ingresa el número de guerreros Etruscian: "))

row = int((-1+math.sqrt(1+8*warriors))//2)
print (row)