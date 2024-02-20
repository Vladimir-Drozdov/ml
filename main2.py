import math
import numpy as np
from matplotlib import pyplot as plt
def fun(t):
    xvar = t + 0.1 #может здесь проблема
    return 2.5 * math.cos(2 * xvar) * math.exp(2 * xvar / 3) + 4 * math.sin(3.5 * xvar) * math.exp(
        (-3) * xvar) + 3 * xvar

print("Word: ",fun(2.2))
PI = 3.1415926535
xvar = 0.5

f = 2.5 * math.cos(2 * xvar) * math.exp(2 * xvar / 3) + 4 * math.sin(3.5 * xvar) * math.exp(-3 * xvar) + 3 * xvar
intfunction = f / ((pow((xvar - 0.1), 0.2)))
bstart = 2.3
aend = 0.1
moments = [0] * 100
arra = [0] * 60
arrx = [0] * 30

a1g = [[0] * 4 for _ in range(3)]
ag = [[0] * 60 for _ in range(60)]
bg = [0] * 60
xg = [0] * 60
ng = 0
ig = 0
jg = 0
kg = 0
dg = 0
sg = 0
array_of_nodes = []
array_of_sum = []
array_of_integral = []

answer = 0
for ii in range(2, 19):#20
    knots = [0] * ii
    amount_of_knots = ii
    array_of_nodes.append(amount_of_knots)
    gap_between_knots = (bstart - aend) / (amount_of_knots - 1)
    for i in range(amount_of_knots):
        #knots[i] = 0.1 + gap_between_knots * i
        knots[i] = float(0 + gap_between_knots * i)

    moments = [0] * amount_of_knots
    for i in range(amount_of_knots):
        moments[i] = pow((bstart - aend), i + 0.8) / (i + 0.8)

    print("Нулевой момент:", moments[0], end=" ")
    knotsclear=[]
    for i in range(0,len(knots)):
        #if(knots[i] != 0):
            knotsclear.append(knots[i])
    arrayfixedbig=[[0] * len(knotsclear) for _ in range(ii)]
    for i in range(0, len(knotsclear)):
        for j in range(0, ii):
            arrayfixedbig[i][j] = (knotsclear[j]**i)
    A = np.array(np.array(arrayfixedbig))
    B = np.array(moments[:(ii)])
    X = np.linalg.inv(A).dot(B)
    print("---")
    print(X)#коэффициенты Aj
    integral=0
    sum=0
    for i in range(0, ii):
        sum=sum+abs(X[i])
        integral = integral+X[i]*fun(knotsclear[i])
        #if(ii==2):
            #integral=11.03
    print(integral)
    array_of_sum.append(round(sum,2))
    array_of_integral.append(round(integral,2))

fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(array_of_nodes, array_of_sum)
# # display the graph
#plt.show()
# #plt.figure(2)
ax2.plot(array_of_nodes, array_of_integral)
# # display the graph
plt.show()
# #может дело в комплексных числах















#что такое интерполюционный, итерация, квадратурный процесс - последовательность квадартурных формул, она определяется двумя треугольными матрицами ущлов и коэффициентами, он сходится когда, сказали делать составную КФ и гаусса, почему начинает расти значение кв суммы не спрашивал, спрашивал описать формулу-интерпол и ньют-котеса и АСТ, если у икф p=1