import sys
inputs = iter(sys.stdin.readlines)
cases = int(next(inputs))

for case in range(cases):
    points = map(str, next(inputs).split(''))
    sum_points=0
    for i in range(len(points)):
        goodO = 0
        while points[i] == 'O':
            goodO +=1
            i+=1
        sum_points += goodO
    print(sum_points)