DATA = [50, 30, 90, 10, 20, 70, 60, 40, 80]
found = False
for i in range(len(DATA)):
    if DATA[i] == 40:
        print(i)
        found = True
        break

if not found:
    print('Not Found')
