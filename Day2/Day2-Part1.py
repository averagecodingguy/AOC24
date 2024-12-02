x = open('/workspaces/AOC24/Day2/Input.txt', 'r')
Lines = x.readlines()
FinalLines = []
x.close()
sum = 0
SecondArray = []
for i in Lines:
    Line, Line2 = [], []
    Line = i.split(' ')
    for i in Line:
        Line2.append(int(i))
    FinalLines.append(Line2)
for i in FinalLines:
    if i[0] > i[1]:
        for q in range(len(i)-1):
            if i[q]< i[q+1] or abs(i[q+1]-i[q]) < 1 or abs(i[q+1]-i[q]) >3:
                break
            else:
                if q == len(i)-2:
                    sum+=1
    if i[0] < i[1]:
        for q in range(len(i)-1):
            if i[q]> i[q+1] or abs(i[q+1]-i[q]) < 1 or abs(i[q+1]-i[q]) >3:
                break
            else:
                if q == len(i)-2:
                    sum+=1
print(sum)
