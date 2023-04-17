import sys
inputs = iter(sys.stdin.readlines())
cases = int(next(inputs))
for case in range(cases):
    lenght, width, height = map(int, next(inputs).split())
    if lenght > 20 or width > 20 or height > 20:
        print('Case {}: bad'.format(case+1))
    else: print('Case {}: good'.format(case+1))
