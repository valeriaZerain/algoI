import sys
inputs = iter(sys.stdin.readlines())
cases = int(next(inputs))
qualityLife = 0
for _ in range(cases):
    qualityPeriod, years = (map(float, next(inputs).split()))
    qualityLife += (qualityPeriod*years)
print(qualityLife)