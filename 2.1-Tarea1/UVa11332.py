import sys
def add (num1):
    num_str = str(num1)
    if len(num_str)==1:
        return num1
    else:
         for value in range(len(num_str)):
             result += map(int, num_str[value])
         return add(result)

for line in sys.stdin.readlines():
     if line == '0\n': break
     number = int(input())
     print(add(number))