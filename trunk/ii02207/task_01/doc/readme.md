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
Группы ИИ-22(I) <br/>
Исаенко Н. Д. <br/>

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
#расчёт линейной модели
function ToCalculateLinear(y, koef_A, koef_B, u)
    y = koef_A * y + koef_B * u
    return y
end

#расчёт нелинейной модели
function ToCalculateUnlinear(y, koef_A, koef_B, YPrev, koef_C, u, koef_D, UPrev)
    y = koef_A * y - koef_B * YPrev^2 + koef_C * u + koef_D * sin(UPrev)
    return y
end

#количество итераций
quantity = 50 

function main()
    LinY = []
    koef_A = 0.8
    koef_B = 1.5
    y = 0.0
    u = 3.3
    #Y линейная модель
    for i = 1:quantity
        push!(LinY, y)
        y = ToCalculateLinear(y, koef_A, koef_B, u)
    end
    plot(1:quantity, LinY, title = "Model", label = "Linear", lw = 2, color = :blue)

    #UNLINEAR
    UnLinY = []
    koef_A = 0.75
    koef_B = 0.1
    koef_C = 2.2
    koef_D = 8.5
    y = 0.0
    u = 0.3
    #Y нелинейная модель
    Ynext = 0.0
    Yprev = 0.0
    for i = 1:quantity
        Yprev = y
        y = Ynext
        Ynext = ToCalculateUnlinear(y, koef_A, koef_B, Yprev, koef_C, u, koef_D, u)
        push!(UnLinY, Ynext)
    end
    plot!(1:quantity, UnLinY, label = "Unlinear", lw = 2, color = :black)
end
main()
```