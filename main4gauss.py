import math
import numpy as np
from matplotlib import pyplot as plt

def fun(t):
    imag=0
    if(t.imag>0):
        imag=(2.5 * math.cos(2 * abs(t.imag)) * math.exp(2 * abs(t.imag) / 3) + 4 * math.sin(3.5 * abs(t.imag)) * math.exp(
        (-3) * abs(t.imag)) + 3 * abs(t.imag))
    xvar = t + 0.1 #может здесь проблема
    #print(abs(imag))
    return (2.5 * math.cos(2 * xvar) * math.exp(2 * xvar / 3) + 4 * math.sin(3.5 * xvar) * math.exp(
        (-3) * xvar) + 3 * xvar) + abs(imag)

#print(fun(0.9777))
PI = 3.1415926535
xvar = 0.5

f = 2.5 * math.cos(2 * xvar) * math.exp(2 * xvar / 3) + 4 * math.sin(3.5 * xvar) * math.exp(-3 * xvar) + 3 * xvar
intfunction = f / ((pow((xvar - 0.1), 0.2)))

moments = [0] * 100
arra = [0] * 60
arrx = [0] * 30
bstart = 2.3
aend = 0.1
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
for ii in range(1, 19):#с 39 появляются комплексные числа, метод гаусса должен! сломаться из-за появления коэфф отриц, комплекс, выходящ за пределы интегрирования. Объяснить почему он меняется в таком случае. в чм коэф>0всегда, в вычисл математике нет. Объяснить плохую обусловленность на пересечении двух прямых:1)перпендик.-хорошо обусл, 2)параллельных-при внесения возмущения решение(точка пересечения)меняется сильно-плохо обусловленный случай
    amount_of_knots = ii
    array_of_nodes.append(amount_of_knots)
    #if ii>=14:
    #    amount_of_knots+=25
    #    ii+=25
    n = 2 * ii - 1
    for i in range(n + 1):
        moments[i] = pow((bstart - aend), i + 0.8) / (i + 0.8)
    #for i in range(n + 1):
    #     print(moments[i], end=" ")

    a1 = [[0] * 40 for _ in range(30)]
    a = [[0] * 60 for _ in range(60)]
    b = [0] * 60
    x = [0] * 60
    b[0] = 0
    print()
    for i in range(1, amount_of_knots + 1):
        for j in range(1, amount_of_knots + 1):
            a[i][j] = moments[j - 2 + i]
            #print(a[i][j])
    for i in range(1, amount_of_knots + 1):
        b[i] = (-1) * moments[ii + i - 1]
        #print(b[i])
    for k in range(1, ii + 1):
        for j in range(k + 1, ii + 1):
            d = a[j][k] / a[k][k]
            for i in range(k, ii + 1):
                a[j][i] = a[j][i] - d * a[k][i]
            b[j] = b[j] - d * b[k]

    for k in range(ii, 0, -1):
        d = 0
        for j in range(k + 1, ii + 1):
            s = a[k][j] * x[j]
            d = d + s
        x[k] = (b[k] - d) / a[k][k]

    for i in range(1, ii + 1):
        pass

    arra[0] = 1

    for i in range(1, ii + 1):
        arra[i] = x[ii - i + 1]
        #print("а малые")
        #print(arra[i], end=" ")
    array = (np.roots(arra))
    #print(array)#решения уравнения n-ой степени в этом массиве
    arrayfixed=[]
    for i in range(0, len(array)):
        if array[i] != 0:
            arrayfixed.append(array[i])
    #print(arrayfixed)#решения уравнения n-ой степени в этом массиве
    arrayfixedbig=[[0] * len(arrayfixed) for _ in range(ii)]
    for i in range(0, len(arrayfixed)):
        for j in range(0, ii):
            arrayfixedbig[i][j] = (arrayfixed[j]**i)
    #print(arrayfixedbig)
    A = np.array(np.array(arrayfixedbig))
    B = np.array(moments[:(ii)])
    X = np.array(np.linalg.inv(A).dot(B), dtype = "complex_")
    print("---")
    print("Число узлов: ",ii)#на 15 шаге появляются компл числа и отриц из-за плохой обусловленности матрицы, значит алгоритм надо прервать на этом же шаге, он ломается и поэтому мы используем скф, а не кф типа гаусса и икф
    print(X)#коэффициенты Aj
    sum=0
    imagall=0
    for i in range(0, len(X)):
        #sum=sum+abs(math.sqrt(pow(abs(X[i].real),2)+pow(abs(X[i].imag), 2)))
        sum=sum+abs(X[i])
        imagall=imagall+abs(X[i].imag)
        #print(X[i].imag)
    #print(imagall)
    #print(math.frexp(imagall))
    imagal=math.frexp(imagall)[0]*pow(2,29+math.frexp(imagall)[1])
    #print(imagal)
    sum=sum+imagal
    #print(sum)
    array_of_sum.append(np.round(sum,2))
    integral=0
    for i in range(0, ii):
        integral = integral+(abs(X[i])+abs(imagal))*fun(arrayfixed[i])
        #print(fun(arrayfixed[i]))
    array_of_integral.append(np.round(integral,2))
    #print("X",X)
    #print("int")
    #print(integral)
#print(array_of_sum)

fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(array_of_nodes, array_of_sum)
# display the graph
#plt.show()
#plt.figure(2)
ax2.plot(array_of_nodes, array_of_integral)
# display the graph
ax1.ticklabel_format(useOffset=False, style='plain', axis='y')

plt.show()
#может дело в комплексных числах