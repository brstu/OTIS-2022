Министерство образования Республики Беларусь <br/>
Учреждение образования <br/>
«Брестский государственный технический университет» <br/>
Кафедра ИИТ <br/>

Лабораторная работа №1 <br/>
За третий семестр <br/>
По дисциплине: «Общая теория интеллектуальных систем» <br/>
Тема: «Modeling controlled object» <br/>

Выполнил: <br/>
Студент 1 курса <br/>
Группы ИИ-21(II) <br/>
Корпач Д.Р.<br/>

Проверил: <br/>
Иванюк Д.С. <br/>

Брест 2022 <br/>

# Общее задание #
1. Написать отчет по выполненной лабораторной работе №1 в .md формате (readme.md) и с помощью запроса на внесение изменений (**pull request**) разместить его в следующем каталоге: **trunk\ii0xxyy\task_01\doc** (где **xx** - номер группы, **yy** - номер студента, например **ii02102**).
2. Исходный код написанной программы разместить в каталоге: **trunk\ii0xxyy\task_01\src**.

## Task 1. Modeling controlled object ##
Let's get some object to be controlled. We want to control its temperature, which can be described by this differential equation:

$$\Large\frac{dy(\tau)}{d\tau}=\frac{u(\tau)}{C}+\frac{Y_0-y(\tau)}{RC} $$ (1)

where $\tau$ – time; $y(\tau)$ – input temperature; $u(\tau)$ – input warm; $Y_0$ – room temperature; $C,RC$ – some constants.

After transformation we get these linear (2) and nonlinear (3) models:

$$\Large y_{\tau+1}=ay_{\tau}+bu_{\tau}$$ (2)
$$\Large y_{\tau+1}=ay_{\tau}-by_{\tau-1}^2+cu_{\tau}+d\sin(u_{\tau-1})$$ (3)

where $\tau$ – time discrete moments ($1,2,3{\dots}n$); $a,b,c,d$ – some constants.

Task is to write program (**Julia**), which simulates this object temperature.


## Код программы ##


``` julia
using Plots

function lin_model(a,b,u,y,t)
    x=1:t
    arr_y=[]
    for i in 1:t
        push!(arr_y,y)
        println(y)
        y = a*y + b*u
    end
    plot(x,arr_y,label="liner_model")

end
function not_liner_model(a,b,c,d,y,u,t)
    x=1:t
    arr_y1=[]
    println("not_liner_model")
    for i in 1:t
        println(y)
        y=a*y - b*y^2 + c*u + d*sin(u)
        push!(arr_y1,y)
    end
    plot!(x,arr_y1,label="not_liner_model")
end


a=0.5
b=0.6
c=0.7
d=0.8
t=20
y=0.0
u=1.0


lin_model(a,b,u,y,t)
not_liner_model(a,b,c,d,y,u,t) 
```
'''
0.0     
0.6
0.8999999999999999
1.0499999999999998
1.125
1.1625
1.18125
1.1906249999999998
1.1953125
1.19765625
1.198828125
1.1994140624999998
1.19970703125
1.199853515625
1.1999267578125
1.1999633789062498
1.199981689453125
1.1999908447265626
1.1999954223632812
1.1999977111816404
not_liner_model
0.0
1.3731767878463172
0.9283964873615181
1.320223008879953
0.987495016380672
1.281836451610655
1.0282322004449678
1.252936013249661
1.0577356024923752
1.23076182622456
1.0796928972236288
1.2135811850690397
1.0962998047286923
1.200202733101762
1.1089861940702348
1.189759657698404
1.118739790843545
1.1815994514980945
1.1262701553270058
1.1752211878416294
'''
![image](https://user-images.githubusercontent.com/102619109/195598427-341ff985-ecfb-4604-b0f1-15e8ad4f6b2d.png)
