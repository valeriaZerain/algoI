import sys
inputs = iter(sys.stdin.readlines())
cases = int(next(inputs))
for case in range(cases):
    speed = list(map(int, next(inputs).split()))
    kids = speed.pop
    maxSpeed = max(speed)
    print('Case {}: {}'.format(case+1, maxSpeed))