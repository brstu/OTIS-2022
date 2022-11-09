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
Гузаревич Д. А. <br/>

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
function CALC_LINEAR_MODEL(y, kf_a, kf_b, u)
    y = kf_a * y + kf_b * u
    return y
end

function CALC_UNLINEAR_MODEL(y, kf_a, kf_b, PrevY, kf_c, u, kf_d, PrevU)
    y = kf_a * y - kf_b * PrevY^2 + kf_c * u + kf_d * sin(PrevU)
    return y
end

count = 45

#LINEAR MODEL
function LINEAR_M()
    arr_LinY = []
    kf_a = 0.8
    kf_b = 0.3
    y = 0.0
    u = 2.3

    for i in 1:count
        push!(arr_LinY, y)
        y = CALC_LINEAR_MODEL(y, kf_a, kf_b, u)
    end
    plot(1:count, arr_LinY, title = "Model", label = "Linear model", lw = 3, color = :green)
end

#UNLINEAR MODEL
function UNLINEAR_M()
    arr_UnLinY = []
    kf_a = 0.7
    kf_b = 0.1
    kf_c = 0.8
    kf_d = 0.5
    y = 0.0
    u = 3.0
    NextY = 0.0
    PrevY = 0.0

    for i in 1:count
        PrevY = y
        y = NextY
        NextY = CALC_UNLINEAR_MODEL(y, kf_a, kf_b, PrevY, kf_c, u, kf_d, u)
        push!(arr_UnLinY, y)
    end
    plot!(1:count, arr_UnLinY, label = "Unlinear model", lw = 3, color = :red)
end

function main()
    LINEAR_M()
    UNLINEAR_M()
end
main()
```
