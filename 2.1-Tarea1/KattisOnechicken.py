import sys
for line in sys.stdin.readlines():
    people, chicken = (map(int, line.split()))
totalChicken = chicken-people
if totalChicken > 1:
    print("Dr. Chaz will have {} piece[s] of chicken left over!".format(totalChicken))
elif totalChicken < -1:
    print("Dr. Chaz needs {} more piece[s] of chicken!".format(abs(totalChicken)))
elif totalChicken == 1:
    print("Dr. Chaz will have {} piece of chicken left over!".format(totalChicken))
elif totalChicken == -1:
    print("Dr. Chaz needs {} more piece of chicken!".format(abs(totalChicken)))
