import sys
inputs = iter(sys.stdin.readlines())
gold, silver, copper = map(int, next(inputs).split())
buyingPower = gold * 3 + silver * 2 + copper
if buyingPower < 2:
    print('Copper')
elif buyingPower < 3:
    print('Estate or Copper')
elif buyingPower < 5:
    print('Estate or Silver')
elif buyingPower < 6:
    print('Duchy or Silver')
elif buyingPower < 8:
    print('Duchy or Gold')
else:
    print('Province or Gold')