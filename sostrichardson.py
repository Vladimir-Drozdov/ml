import math
import numpy as np
from matplotlib import pyplot as plt
def fun(t):
    xvar = t #+ 0.1#сд может ошибка
    return 2.5 * math.cos(2 * xvar) * math.exp(2 * xvar / 3) + 4 * math.sin(3.5 * xvar) * math.exp(
        (-3) * xvar) + 3 * xvar
r=2
bend = 2.3
astart = 0.1
m=3.4
array_of_pogreshonst=[]
array_of_chislo_chast_otrezkov=[]
array_of_m = []
array_of_Cm = []
for chislo_chast_otrezkov in range(1,20):
    #step=(bend-astart)/chislo_chast_otrezkov

    arr_of_sh_for_m=[]
    #sh1 = 0
    L = 2

    #sh2 = 0
    #sh3 = 0
    #epsilon = 0.000001
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
    answer=0
    k1=chislo_chast_otrezkov
    for l in range(1,4):
        for iii in range(1, k1 + 1):  # считаем составную квадратурную формулу
            h = (bend - astart) / k1
            # print(bend-astart)
            # print("h",h)
            array_of_h_local = []
            for i in range(0, r + 1):
                array_of_h_local.append(pow(h, m + i))
            # print(array_of_h_local)
            bkend = astart + (iii) * h
            akstart = astart + (iii - 1) * h
            ii = 3
            amount_of_knots = ii
            gap_between_knots = (bkend - akstart) / (amount_of_knots - 1)

            for i in range(amount_of_knots):
                knots[i] = akstart + gap_between_knots * i

            for i in range(amount_of_knots):
                moments[i] = pow((bkend - 0.1), i + 0.8) / (i + 0.8) - pow((akstart - 0.1), i + 0.8) / (i + 0.8)

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
            # print("answer", answer)
        skh = answer
        arr_of_sh_for_m.append(skh)

        k1 = k1 * L
        answer = 0
    #print(arr_of_sh_for_m)
    Q=(arr_of_sh_for_m[0]-arr_of_sh_for_m[1])/(arr_of_sh_for_m[1]-arr_of_sh_for_m[2])
    m=math.log(Q)/math.log(L)
    print("m",m)
    array_of_m.append(m)
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
    #k1 = 5
    #k2 = k1 * L
    #k3 = k2 * L
    #h1 = (bstart - aend) / k1
    #print("h1", h1)
    #h2 = (bstart - aend) / k2
    #h3 = (bstart - aend) / k3
    L=2
    arr_of_h=[]
    arr_of_skh=[]
    k1 = chislo_chast_otrezkov
    for number_of_strings in range(1,r+3):

        for iii in range(1, k1 + 1):#считаем составную квадратурную формулу
            h = (bend-astart) / k1
            #print(bend-astart)
            #print("h",h)
            array_of_h_local=[]
            for i in range(0,r+1):
                array_of_h_local.append(pow(h,m+i))
            #print(array_of_h_local)
            bkend = astart + (iii) * h
            akstart = astart + (iii - 1) * h
            ii = 3
            amount_of_knots = ii
            gap_between_knots = (bkend - akstart) / (amount_of_knots - 1)

            for i in range(amount_of_knots):
                knots[i] = akstart + gap_between_knots * i

            for i in range(amount_of_knots):
                moments[i] = pow((bkend - 0.1), i + 0.8) / (i + 0.8) - pow((akstart - 0.1), i + 0.8) / (i + 0.8)

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
            #print("answer", answer)
        skh = answer
        arr_of_skh.append(skh)
        arr_of_h.append(array_of_h_local)
        #print(skh)
        k1=k1*L
        answer = 0
    #print(arr_of_h)
    #print(arr_of_skh)
    #Решаем слау в ричардсоне
    matrix_A=[]
    for i in range(0,len(arr_of_h)):
        arr_of_h_and_J=arr_of_h[i]
        for j in range(0,len(arr_of_h_and_J)):
            arr_of_h_and_J[j]=(-1)*arr_of_h_and_J[j]
        arr_of_h_and_J.insert(0,1)
        matrix_A.append(arr_of_h_and_J)
    matrix_A=np.array(matrix_A)
    print(matrix_A)
    matrix_B=arr_of_skh
    matrix_B = np.array(matrix_B)
    X = np.array(np.linalg.inv(matrix_A).dot(matrix_B), dtype="complex_")
    print(X)
    J=X[0]
    Cm=X[1]
    pogreshost=J-arr_of_skh[0]
    #print(chislo_chast_otrezkov, J, Cm)
    array_of_pogreshonst.append(pogreshost)
    array_of_chislo_chast_otrezkov.append(chislo_chast_otrezkov)
    array_of_Cm.append(Cm)
fig, (ax1, ax2) = plt.subplots(2)
print(array_of_Cm)
print(array_of_pogreshonst)
ax1.plot(array_of_chislo_chast_otrezkov, array_of_Cm)
# display the graph
#plt.show()
#plt.figure(2)
ax2.plot(array_of_chislo_chast_otrezkov, array_of_m)
# display the graph
ax1.ticklabel_format(useOffset=False, style='plain', axis='y')
fig1, (ax3)=plt.subplots(1)
ax3.plot(array_of_chislo_chast_otrezkov,array_of_pogreshonst)
plt.show()