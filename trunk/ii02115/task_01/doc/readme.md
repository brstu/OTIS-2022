Министерство образования Республики Беларусь <br/>
Учреждение образования <br/>
«Брестский государственный технический университет» <br/>
Кафедра ИИТ <br/>

Лабораторная работа №1 <br/>
За третий семестр <br/>
По дисциплине: «Общая теория интеллектуальных систем» <br/>
Тема: «Modeling controlled object» <br/>

Выполнил: <br/>
Студент 2 курса <br/>
Группы ИИ-21(II) <br/>
Худик А.А. <br/>

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

function noLin(alpha, beta, gamma, delta, f, w, k)
    x = 1:k
    alpharr_y1=[]
    println("noLin")
    for i in x
        println(f)
        f = alpha * f - beta * f^2 + gamma * w + delta * sin(w)
        push!(alpharr_y1, f)
    end
    plot!(x, alpharr_y1, label="noLin")
end

function lin(alpha, beta, w, f, k)
    x = 1:k
    alpharr_y = []
    for i in x
        push!(alpharr_y, f)
        println(f)
        f = alpha * f + beta * w
    end
    plot(x, alpharr_y, label="liner_model")

end

function main()
    alpha = 0.5
beta = 0.6
gamma = 0.7
delta = 0.8
k = 20
f = 0.0
w = 1.0

lin(alpha, beta, w, f, k)
noLin(alpha, beta, gamma, delta, f, w, k)
end

main()  
```
![image](https://user-images.githubusercontent.com/113055441/191745002-d62c52cf-6124-4c95-9242-8cacf3a872d2.png)