import sys

for line in sys.stdin.readlines():
     if line == '0\n': break
     inputs = iter(sys.stdin.readlines)
     events = int(next(inputs))
     for event in range(events):
          emoogle = list(map(int, inputs().split))
          happy = emoogle.count(0)
          sad = len(list) - happy
          print('Case {}: {}'.format(event, sad-happy))
