import math
import numpy
from matplotlib import pyplot as plt
def fun1(x, y1, y2, y3, y4):
    return 2*x*pow(y2,-0.5)*y4
def fun2(x,y1,y2, y3,y4):
    if(abs(y3)>60):
        y3=60*numpy.sign(y3)
    return 2*(-2)*x*(math.exp((-1)*(y3.real+2)))*y4
def fun3(x,y1,y2,y3,y4):
    return 4*x*y4
def fun4(x,y1,y2,y3,y4):
    return (-2)*x*math.log(abs(y1.real))###
def y1accurate(x):
    return math.exp(math.sin(pow(x, 2)))
def y2accurate(x):
    return math.exp((-2)*math.sin(pow(x, 2)))
def y3accurate(x):
    return 2*(math.sin(pow(x, 2)))-2
def y4accurate(x):
    return math.cos(pow(x, 2))
x0=0
y10=1
y20=1
y30=-2
y40=1
h=0.01 #0.1-повляеются комплексные и работает не очень, 0.01-хорошо работает и комплексные пропадают, 0.001-оч хорошо
k2 = [0]*4
#Метод второго порядка
b1 = (-7) / 3
b2 = 10 / 3
for i in range(1,500):
    k1=[fun1(x0,y10,y20,y30,y40), fun2(x0,y10,y20,y30,y40),
        fun3(x0,y10,y20,y30,y40), fun4(x0,y10,y20,y30,y40)]
    k2[0]=fun1(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[1]=fun2(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[2]=fun3(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[3]=fun4(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    y11=y10+h*(b1*k1[0]+b2*k2[0])
    y21=y20+h*(b1*k1[1]+b2*k2[1])
    y31=y30+h*(b1*k1[2]+b2*k2[2])
    y41=y40+h*(b1*k1[3]+b2*k2[3])
    #print(h*i, y11,y21,y31,y41)
    #h=h+0.1
    x0=x0+h
    y10=y11
    y20=y21
    y30=y31
    y40=y41
#первый метод Рунге-Кутты 3-го порядка
x0=0
y10=1
y20=1
y30=-2
y40=1
h=0.01
k2 = [0]*4
k3=[0]*4
for i in range(1,500):
    k1 = [fun1(x0, y10, y20, y30, y40), fun2(x0, y10, y20, y30, y40),
          fun3(x0, y10, y20, y30, y40), fun4(x0, y10, y20, y30, y40)]
    k2[0] = fun1(x0 + 1/3 * h, y10 + h * 1/3 * fun1(x0, y10, y20, y30, y40),
                 y20 + h * 1/3 * fun2(x0, y10, y20, y30, y40), y30 + h * 1/3 * fun3(x0, y10, y20, y30, y40),
                 y40 + h * 1/3 * fun4(x0, y10, y20, y30, y40))
    k2[1] = fun2(x0 + 1/3 * h, y10 + h * 1/3 * fun1(x0, y10, y20, y30, y40),
                 y20 + h * 1/3 * fun2(x0, y10, y20, y30, y40), y30 + h * 1/3 * fun3(x0, y10, y20, y30, y40),
                 y40 + h * 1/3 * fun4(x0, y10, y20, y30, y40))
    k2[2] = fun3(x0 + 1/3 * h, y10 + h * 1/3 * fun1(x0, y10, y20, y30, y40),
                 y20 + h * 1/3 * fun2(x0, y10, y20, y30, y40), y30 + h * 1/3 * fun3(x0, y10, y20, y30, y40),
                 y40 + h * 1/3 * fun4(x0, y10, y20, y30, y40))
    k2[3] = fun4(x0 + 1/3 * h, y10 + h * 1/3 * fun1(x0, y10, y20, y30, y40),
                 y20 + h * 1/3 * fun2(x0, y10, y20, y30, y40), y30 + h * 1/3 * fun3(x0, y10, y20, y30, y40),
                 y40 + h * 1/3 * fun4(x0, y10, y20, y30, y40))
    k3[0]=fun1(x0+2/3*h, y10+2/3*h*k2[0],y20+2/3*h*k2[1],y30+2/3*h*k2[2],y40+2/3*h*k2[3])
    k3[1]=fun2(x0+2/3*h, y10+2/3*h*k2[0],y20+2/3*h*k2[1],y30+2/3*h*k2[2],y40+2/3*h*k2[3])
    k3[2]=fun3(x0+2/3*h, y10+2/3*h*k2[0],y20+2/3*h*k2[1],y30+2/3*h*k2[2],y40+2/3*h*k2[3])
    k3[3]=fun4(x0+2/3*h, y10+2/3*h*k2[0],y20+2/3*h*k2[1],y30+2/3*h*k2[2],y40+2/3*h*k2[3])
    b1=1/4
    b3=3/4
    y11 = y10 + h * (b1 * k1[0] + b3 * k3[0])
    y21 = y20 + h * (b1 * k1[1] + b3 * k3[1])
    y31 = y30 + h * (b1 * k1[2] + b3 * k3[2])
    y41 = y40 + h * (b1 * k1[3] + b3 * k3[3])
    #print(h*i, y11, y21, y31, y41)
    # h=h+0.1
    x0 = x0 + h
    y10 = y11
    y20 = y21
    y30 = y31
    y40 = y41
#Построение графика для двухэтапного метода Ругне-Кутты
array_of_tolerance=[]
array_of_h=[]
for k in range(5, 11):
    x0 = 0
    y10 = 1
    y20 = 1
    y30 = -2
    y40 = 1
    h = 1/pow(2, k)
    array_of_h.append(math.log2(h))
    k2 = [0]*4
    b1 = (-7) / 3
    b2 = 10 / 3
    end = 5/h
    full_tolerance=0
    for i in range(1, round(end)+1):
        k1=[fun1(x0,y10,y20,y30,y40), fun2(x0,y10,y20,y30,y40), fun3(x0,y10,y20,y30,y40), fun4(x0,y10,y20,y30,y40)]
        k2[0]=fun1(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
        k2[1]=fun2(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
        k2[2]=fun3(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
        k2[3]=fun4(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
        y11=y10+h*(b1*k1[0]+b2*k2[0])
        y21=y20+h*(b1*k1[1]+b2*k2[1])
        y31=y30+h*(b1*k1[2]+b2*k2[2])
        y41=y40+h*(b1*k1[3]+b2*k2[3])
        if(i>(end-1)):
           # print(h*i, y11,y21,y31,y41)
            full_tolerance=math.sqrt(pow((y1accurate(h*i)-y11.real),2)+pow((y2accurate(h*i)-y21.real),2)+pow((y3accurate(h*i)-y31.real),2)
            +pow((y4accurate(h*i)-y41.real),2))
           # print(full_tolerance)
            array_of_tolerance.append(math.log2(full_tolerance))
        #h=h+0.1
        x0=x0+h
        y10=y11
        y20=y21
        y30=y31
        y40=y41
fig, (ax1, ax2) = plt.subplots(2)
ax1.plot(array_of_h, array_of_tolerance)#прямая с наклоном 2
# display the graph
#plt.show()
#plt.figure(2)
#ax2.plot(array_of_nodes, array_of_integral)
# display the graph
ax1.ticklabel_format(useOffset=False, style='plain', axis='y')

#plt.show()


#Построение графика для трехэтапного метода Ругне-Кутты
array_of_tolerance_3=[]
array_of_h_3=[]
for k in range(5, 11):
    x0 = 0
    y10 = 1
    y20 = 1
    y30 = -2
    y40 = 1
    h = 1/pow(2,k)
    array_of_h_3.append(math.log2(h))
    k2 = [0] * 4
    k3 = [0] * 4
    end = 5 / h
    full_tolerance = 0
    for i in range(1, round(end) + 1):
        k1 = [fun1(x0, y10, y20, y30, y40), fun2(x0, y10, y20, y30, y40),
              fun3(x0, y10, y20, y30, y40), fun4(x0, y10, y20, y30, y40)]
        k2[0] = fun1(x0 + 1 / 3 * h, y10 + h * 1 / 3 * fun1(x0, y10, y20, y30, y40),
                     y20 + h * 1 / 3 * fun2(x0, y10, y20, y30, y40), y30 + h * 1 / 3 * fun3(x0, y10, y20, y30, y40),
                     y40 + h * 1 / 3 * fun4(x0, y10, y20, y30, y40))
        k2[1] = fun2(x0 + 1 / 3 * h, y10 + h * 1 / 3 * fun1(x0, y10, y20, y30, y40),
                     y20 + h * 1 / 3 * fun2(x0, y10, y20, y30, y40), y30 + h * 1 / 3 * fun3(x0, y10, y20, y30, y40),
                     y40 + h * 1 / 3 * fun4(x0, y10, y20, y30, y40))
        k2[2] = fun3(x0 + 1 / 3 * h, y10 + h * 1 / 3 * fun1(x0, y10, y20, y30, y40),
                     y20 + h * 1 / 3 * fun2(x0, y10, y20, y30, y40), y30 + h * 1 / 3 * fun3(x0, y10, y20, y30, y40),
                     y40 + h * 1 / 3 * fun4(x0, y10, y20, y30, y40))
        k2[3] = fun4(x0 + 1 / 3 * h, y10 + h * 1 / 3 * fun1(x0, y10, y20, y30, y40),
                     y20 + h * 1 / 3 * fun2(x0, y10, y20, y30, y40), y30 + h * 1 / 3 * fun3(x0, y10, y20, y30, y40),
                     y40 + h * 1 / 3 * fun4(x0, y10, y20, y30, y40))
        k3[0] = fun1(x0 + 2 / 3 * h, y10 + 2 / 3 * h * k2[0], y20 + 2 / 3 * h * k2[1], y30 + 2 / 3 * h * k2[2],
                     y40 + 2 / 3 * h * k2[3])
        k3[1] = fun2(x0 + 2 / 3 * h, y10 + 2 / 3 * h * k2[0], y20 + 2 / 3 * h * k2[1], y30 + 2 / 3 * h * k2[2],
                     y40 + 2 / 3 * h * k2[3])
        k3[2] = fun3(x0 + 2 / 3 * h, y10 + 2 / 3 * h * k2[0], y20 + 2 / 3 * h * k2[1], y30 + 2 / 3 * h * k2[2],
                     y40 + 2 / 3 * h * k2[3])
        k3[3] = fun4(x0 + 2 / 3 * h, y10 + 2 / 3 * h * k2[0], y20 + 2 / 3 * h * k2[1], y30 + 2 / 3 * h * k2[2],
                     y40 + 2 / 3 * h * k2[3])
        b1 = 1 / 4
        b3 = 3 / 4
        y11 = y10 + h * (b1 * k1[0] + b3 * k3[0])
        y21 = y20 + h * (b1 * k1[1] + b3 * k3[1])
        y31 = y30 + h * (b1 * k1[2] + b3 * k3[2])
        y41 = y40 + h * (b1 * k1[3] + b3 * k3[3])
        if (i > (end - 1)):
            #print(h * i, y11, y21, y31, y41)
            full_tolerance = math.sqrt(
                pow((y1accurate(h * i) - y11.real), 2) + pow((y2accurate(h * i) - y21.real), 2) + pow(
                    (y3accurate(h * i) - y31.real), 2)
                + pow((y4accurate(h * i) - y41.real), 2))
          #  print(full_tolerance)
            array_of_tolerance_3.append(math.log2(full_tolerance))
        x0 = x0 + h
        y10 = y11
        y20 = y21
        y30 = y31
        y40 = y41
#fig, (ax1, ax2) = plt.subplots(2)
ax2.plot(array_of_h_3, array_of_tolerance_3)#прямая с наклоном 3
# display the graph
#plt.show()
#plt.figure(2)
#ax2.plot(array_of_nodes, array_of_integral)
# display the graph
#ax1.ticklabel_format(useOffset=False, style='plain', axis='y')

#plt.show()
"""
#Полная погрешность по правилу рунге
#шаг первый
array_of_solution=[]
solutionh=[]
x0=0
y10=1
y20=1
y30=-2
y40=1
h=0.0001 #0.1-повляеются комплексные и работает не очень, 0.01-хорошо работает и комплексные пропадают, 0.001-оч хорошо
k2 = [0]*4
#Метод второго порядка
b1 = (-7) / 3
b2 = 10 / 3
for i in range(1,50000):
    k1=[fun1(x0,y10,y20,y30,y40), fun2(x0,y10,y20,y30,y40),
        fun3(x0,y10,y20,y30,y40), fun4(x0,y10,y20,y30,y40)]
    k2[0]=fun1(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[1]=fun2(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[2]=fun3(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[3]=fun4(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    y11=y10+h*(b1*k1[0]+b2*k2[0])
    y21=y20+h*(b1*k1[1]+b2*k2[1])
    y31=y30+h*(b1*k1[2]+b2*k2[2])
    y41=y40+h*(b1*k1[3]+b2*k2[3])
    if(h*i==1):
        solutionh=[y11, y21, y31, y41]

    solution=[y11, y21, y31, y41]
    array_of_solution.append(solution)
    #print(h*i, y11,y21,y31,y41)
    #h=h+0.1
    x0=x0+h
    y10=y11
    y20=y21
    y30=y31
    y40=y41
#шаг второй
array_of_solution2=[]
solution2h=[]
x0=0
y10=1
y20=1
y30=-2
y40=1
h=0.0001/2 #0.1-повляеются комплексные и работает не очень, 0.01-хорошо работает и комплексные пропадают, 0.001-оч хорошо
k2 = [0]*4
#Метод второго порядка
b1 = (-7) / 3
b2 = 10 / 3
for i in range(1,50000*2):
    k1=[fun1(x0,y10,y20,y30,y40), fun2(x0,y10,y20,y30,y40),
        fun3(x0,y10,y20,y30,y40), fun4(x0,y10,y20,y30,y40)]
    k2[0]=fun1(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[1]=fun2(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[2]=fun3(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[3]=fun4(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    y11=y10+h*(b1*k1[0]+b2*k2[0])
    y21=y20+h*(b1*k1[1]+b2*k2[1])
    y31=y30+h*(b1*k1[2]+b2*k2[2])
    y41=y40+h*(b1*k1[3]+b2*k2[3])
    if (h * i == 1):
        solution2h=[y11, y21, y31, y41]
      #  print("solution2h", solution2h)
    solution2=[y11, y21, y31, y41]
    array_of_solution2.append(solution2)
    #print(h*i, y11,y21,y31,y41)
    #h=h+0.1
    x0=x0+h
    y10=y11
    y20=y21
    y30=y31
    y40=y41
substruction_of_solutions=(solution2h+(-1)*solutionh)
for i in range(0,4):
    substruction_of_solutions[i]=substruction_of_solutions[i]*(1/(pow(2, 2)-1))
#print(substruction_of_solutions)
for i in range(0,4):
    substruction_of_solutions[i]=solution2h[i]+substruction_of_solutions[i]
Rsecondh=substruction_of_solutions
Rsecondhmodule=0
for i in range(0, 4):
    Rsecondhmodule+=pow(Rsecondh[i], 2)
Rsecondhmodule=math.sqrt(Rsecondhmodule)
#print("Rsecondh", Rsecondh)
tol=pow(10,-5)
htol=h*pow((tol/Rsecondhmodule),0.5)
#print("htol",htol)
#print
# считаем методом рунге кутты 2 порядка с шагом htol
full_tolerance=0
htol=htol
array_of_full_tolerances=[]
array_of_x=[]
x0=0
y10=1
y20=1
y30=-2
y40=1
h=htol #0.1-повляеются комплексные и работает не очень, 0.01-хорошо работает и комплексные пропадают, 0.001-оч хорошо
k2 = [0]*4
#Метод второго порядка
b1 = (-7) / 3
b2 = 10 / 3
print("Погрешность заданная", pow(10, -3))
print("htol длина шага полученная правилом Рунге", h)
end=5/h
array_of_tol=[]
for i in range(1, math.ceil(end)):
    array_of_tol.append(tol)
    k1=[fun1(x0,y10,y20,y30,y40), fun2(x0,y10,y20,y30,y40),
        fun3(x0,y10,y20,y30,y40), fun4(x0,y10,y20,y30,y40)]
    k2[0]=fun1(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[1]=fun2(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[2]=fun3(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    k2[3]=fun4(x0+0.15*h, y10+h*0.15*fun1(x0,y10,y20,y30,y40),y20+h*0.15*fun2(x0,y10,y20,y30,y40),y30+h*0.15*fun3(x0,y10,y20,y30,y40),y40+h*0.15*fun4(x0,y10,y20,y30,y40))
    y11=y10+h*(b1*k1[0]+b2*k2[0])
    y21=y20+h*(b1*k1[1]+b2*k2[1])
    y31=y30+h*(b1*k1[2]+b2*k2[2])
    y41=y40+h*(b1*k1[3]+b2*k2[3])
    #print(h*i, y11,y21,y31,y41)
    array_of_x.append(h*i)
    full_tolerance = math.sqrt(
        pow((y1accurate(h * i) - y11.real), 2) + pow((y2accurate(h * i) - y21.real), 2) + pow(
            (y3accurate(h * i) - y31.real), 2)
        + pow((y4accurate(h * i) - y41.real), 2))
    array_of_full_tolerances.append(full_tolerance)
    #h=h+0.1
    x0=x0+h
    y10=y11
    y20=y21
    y30=y31
    y40=y41
#fig, (ax3, ax2) = plt.subplots(2)
#print("array_of_h", array_of_x)
#ax3.plot(array_of_x, array_of_full_tolerances)
#ax3.plot(array_of_x, array_of_tol)
"""
plt.show()