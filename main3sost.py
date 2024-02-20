import math
import numpy as np
from matplotlib import pyplot as plt
def fun(t):
    xvar = t + 0.1
    return 2.5 * math.cos(2 * xvar) * math.exp(2 * xvar / 3) + 4 * math.sin(3.5 * xvar) * math.exp(
        (-3) * xvar) + 3 * xvar
sh1 = 0
L = 2

sh2 = 0
sh3 = 0
epsilon = 0.000001
answer = 0
bstart = 2.3
aend = 0.1
knots = [0] * 100
moments = [0] * 100
arra = [0] * 40
arrx = [0] * 30
a1g = [[0] * 4 for _ in range(3)]
ag = [[0] * 40 for _ in range(40)]
bg = [0] * 40
xg = [0] * 40
h = 0
ng = 0
ig = 0
jg = 0
kg = 0
dg = 0
sg = 0
k1 = 3
k2 = k1 * L
k3 = k2 * L
h1 = (bstart - aend) / k1
print("h1", h1)
h2 = (bstart - aend) / k2
h3 = (bstart - aend) / k3

for iii in range(1, k1 + 1):#считаем малую квадратурную формулу
    h = (bstart - aend) / k1
    bkstart = aend + (iii) * h
    akend = aend + (iii - 1) * h
    ii = 3
    amount_of_knots = ii
    gap_between_knots = (bkstart - akend) / (amount_of_knots - 1)

    for i in range(amount_of_knots):
        knots[i] = akend + gap_between_knots * i

    for i in range(amount_of_knots):
        moments[i] = pow((bkstart - 0.1), i + 0.8) / (i + 0.8) - pow((akend - 0.1), i + 0.8) / (i + 0.8)

    ng = amount_of_knots

    for i in range(1, ng + 1):
        xg[i] = 0

    bg[0] = 0

    for i in range(1, amount_of_knots + 1):
        for j in range(1, amount_of_knots + 1):
            ag[i][j] = pow(knots[j - 1] - 0.1, i - 1)

    for i in range(1, amount_of_knots + 1):
        bg[i] = moments[i - 1]

    ng = amount_of_knots

    for kg in range(1, ng + 1):
        for jg in range(kg + 1, ng + 1):
            dg = ag[jg][kg] / ag[kg][kg]
            for ig in range(kg, ng + 1):
                ag[jg][ig] = ag[jg][ig] - dg * ag[kg][ig]
            bg[jg] = bg[jg] - dg * bg[kg]

    for kg in range(ng, 0, -1):
        dg = 0
        for jg in range(kg + 1, ng + 1):
            sg = ag[kg][jg] * xg[jg]
            dg = dg + sg
        xg[kg] = (bg[kg] - dg) / ag[kg][kg]

    answerk = 0

    for i in range(1, ng + 1):
        answerk = answerk + xg[i] * (fun(knots[i - 1]))

    answer = answer + answerk
    print("answer", answer)
sh1 = answer
answer = 0

for iii in range(1, k2 + 1):
    h = (bstart - aend) / k2
    bkstart = aend + (iii) * h
    akend = aend + (iii - 1) * h
    ii = 3
    amount_of_knots = ii
    gap_between_knots = (bkstart - akend) / (amount_of_knots - 1)

    for i in range(amount_of_knots):
        knots[i] = akend + gap_between_knots * i

    for i in range(amount_of_knots):
        moments[i] = pow((bkstart - 0.1), i + 0.8) / (i + 0.8) - pow((akend - 0.1), i + 0.8) / (i + 0.8)

    ng = amount_of_knots

    for i in range(1, ng + 1):
        xg[i] = 0

    bg[0] = 0

    for i in range(1, amount_of_knots + 1):
        for j in range(1, amount_of_knots + 1):
            ag[i][j] = pow(knots[j - 1] - 0.1, i - 1)

    for i in range(1, amount_of_knots + 1):
        bg[i] = moments[i - 1]

    ng = amount_of_knots

    for kg in range(1, ng + 1):
        for jg in range(kg + 1, ng + 1):
            dg = ag[jg][kg] / ag[kg][kg]
            for ig in range(kg, ng + 1):
                ag[jg][ig] = ag[jg][ig] - dg * ag[kg][ig]
            bg[jg] = bg[jg] - dg * bg[kg]

    for kg in range(ng, 0, -1):
        dg = 0
        for jg in range(kg + 1, ng + 1):
            sg = ag[kg][jg] * xg[jg]
            dg = dg + sg
        xg[kg] = (bg[kg] - dg) / ag[kg][kg]

    answerk = 0

    for i in range(1, ng + 1):
        answerk = answerk + xg[i] * (fun(knots[i - 1]))

    answer = answer + answerk

sh2 = answer
answer = 0

for iii in range(1, k3 + 1):
    h = (bstart - aend) / k3
    bkstart = aend + (iii) * h
    akend = aend + (iii - 1) * h
    ii = 3
    amount_of_knots = ii
    gap_between_knots = (bkstart - akend) / (amount_of_knots - 1)

    for i in range(amount_of_knots):
        knots[i] = akend + gap_between_knots * i

    for i in range(amount_of_knots):
        moments[i] = pow((bkstart - 0.1), i + 0.8) / (i + 0.8) - pow((akend - 0.1), i + 0.8) / (i + 0.8)

    ng = amount_of_knots

    for i in range(1, ng + 1):
        xg[i] = 0

    bg[0] = 0

    for i in range(1, amount_of_knots + 1):
        for j in range(1, amount_of_knots + 1):
            ag[i][j] = pow(knots[j - 1] - 0.1, i - 1)

    for i in range(1, amount_of_knots + 1):
        bg[i] = moments[i - 1]

    ng = amount_of_knots

    for kg in range(1, ng + 1):
        for jg in range(kg + 1, ng + 1):
            dg = ag[jg][kg] / ag[kg][kg]
            for ig in range(kg, ng + 1):
                ag[jg][ig] = ag[jg][ig] - dg * ag[kg][ig]
            bg[jg] = bg[jg] - dg * bg[kg]

    for kg in range(ng, 0, -1):
        dg = 0
        for jg in range(kg + 1, ng + 1):
            sg = ag[kg][jg] * xg[jg]
            dg = dg + sg
        xg[kg] = (bg[kg] - dg) / ag[kg][kg]

    answerk = 0

    for i in range(1, ng + 1):
        answerk = answerk + xg[i] * (fun(knots[i - 1]))

    answer = answer + answerk

sh3 = answer
m=(-1)*(math.log((sh3-sh2)/(sh2-sh1)))/math.log(L)
print("m полученное по процессу Эйткена", m)

Rh1 = (sh2 - sh1) / (1 - pow(L, -m))
Rh2 = (sh2 - sh1) / (pow(L, m) - 1)
hopt = h2 * pow((epsilon / abs(Rh2)), 1 / m)

#print("answer", answer)
print("Погрешность", epsilon)
print("Шаг оптимальный h=", hopt)
print("Число частичных отрезков такой длины k=", math.ceil((bstart - aend) / hopt))

Amount_of_otrezkov=math.ceil((bstart - aend) / hopt)


#
k = Amount_of_otrezkov#####
array_of_amount_of_chastichn_otrezkov=[]
array_of_pogreshnost=[]
for iii in range(1, k + 1):

    step = (bstart - aend) / iii

    array_of_amount_of_chastichn_otrezkov.append(iii)
    bkstart = aend + (iii) * h
    akend = aend + (iii - 1) * h
    ii = 3
    amount_of_knots = ii
    gap_between_knots = (bkstart - akend) / (amount_of_knots - 1)
    for i in range(amount_of_knots):
        knots[i] = akend + gap_between_knots * i
    for i in range(amount_of_knots):
        moments[i] = pow((bkstart - 0.1), i + 0.8) / (i + 0.8) - pow((akend - 0.1), i + 0.8) / (i + 0.8)
    ng = amount_of_knots
    for i in range(1, ng + 1):
        xg[i] = 0
    bg[0] = 0
    for i in range(1, amount_of_knots + 1):
        for j in range(1, amount_of_knots + 1):
            ag[i][j] = pow(knots[j - 1] - 0.1, i - 1)
    for i in range(1, amount_of_knots + 1):
        bg[i] = moments[i - 1]
    ng = amount_of_knots
    for kg in range(1, ng + 1):
        for jg in range(kg + 1, ng + 1):
            dg = ag[jg][kg] / ag[kg][kg]
            for ig in range(kg, ng + 1):
                ag[jg][ig] = ag[jg][ig] - dg * ag[kg][ig]
            bg[jg] = bg[jg] - dg * bg[kg]
    for kg in range(ng, 0, -1):
        dg = 0
        for jg in range(kg + 1, ng + 1):
            sg = ag[kg][jg] * xg[jg]
            dg = dg + sg
        xg[kg] = (bg[kg] - dg) / ag[kg][kg]
    answerk = 0
    for i in range(1, ng + 1):
        answerk = answerk + xg[i] * (fun(knots[i - 1]))
    answer = answer + answerk
    if k >= 1:
        y = -math.log10(Rh1 * pow((step / h1), m))#Оценки методич погрешности
        print(iii, step, y)
    array_of_pogreshnost.append(y)
    if step < hopt:
        break
#print(array_of_sum)
fig, (ax1) = plt.subplots(1)
#(ax1) = plt.subplots(2)
ax1.plot(array_of_amount_of_chastichn_otrezkov, array_of_pogreshnost)
# display the graph
#plt.show()
#plt.figure(2)
#ax2.plot([1,2], [1,2])
# display the graph
plt.show()


#Вывести на каждой итерации число частичных отрезком, константу Cm и m полученное по эйткину