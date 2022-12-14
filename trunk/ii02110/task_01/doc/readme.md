<p style="text-align: center;">Министерство образования Республики Беларусь</p>
<p style="text-align: center;">Учреждение образования</p>
<p style="text-align: center;">“Брестский Государственный технический университет”</p>
<p style="text-align: center;">Кафедра ИИТ</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: center;">Лабораторная работа №1</p>
<p style="text-align: center;">По дисциплине “Общая теория интеллектуальных систем”</p>
<p style="text-align: center;">Тема: “Моделирования температуры объекта”</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: right;">Выполнил:</p>
<p style="text-align: right;">Студент 2 курса</p>
<p style="text-align: right;">Группы ИИ-21</p>
<p style="text-align: right;">Пучинский А.А.</p>
<p style="text-align: right;">Проверил:</p>
<p style="text-align: right;">Иванюк Д. С.</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: center;">Брест 2022</p>

---

# Общее задание #
1. Написать отчет по выполненной лабораторной работе №1 в .md формате (readme.md) и с помощью запроса на внесение изменений (**pull request**) разместить его в следующем каталоге: trunk\ii0xxyy\task_01\doc (где xx - номер группы, yy - номер студента, например **ii02102**).
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

---

# Выполнение задания #

Код программы:
```julia
A = 0.5
B = 0.5
C = 0.1
D = 0.5
U = 1.0
Y = 0.0


function линейная_модель(Y, N, T)
    if N < T
        println(Y)
        return линейная_модель(A * Y + B * U, N+1, T)
    end
    println(Y)
    return A * Y + B * U
end
println(линейная_модель(Y, 0, 10))

println("----------------------")


function нелинейная_модель(Y, Y_pre, U, U_pre, I, T)
    if I == 1
        println(Y)
        return нелинейная_модель(A*Y - B*Y_pre^2 + C*1 + D*sin(1), Y, U, U, I + 1, T)
    elseif I < T
        println(Y)
        return нелинейная_модель(A*Y - B*Y_pre^2 + C*U + D*sin(U_pre), Y, U, U, I + 1, T)
    end
    println(Y)
    return A*Y - B*Y_pre^2 + C*U + D*sin(U_pre)
end

println(нелинейная_модель(Y, Y, U, U, 0, 10))
```
    Вывод:
    0.0
    0.5
    0.75
    0.875
    0.9375
    0.96875
    0.984375
    0.9921875
    0.99609375
    0.998046875
    0.9990234375
    0.99951171875
    ----------------------
    0.0
    0.5207354924039482
    0.7811032386059223
    0.7757043851823182
    0.6035265503147771
    0.5216401209657977
    0.5994334044194195
    0.684397986713052
    0.6832742825935466
    0.6281723315922821
    0.6013897855732264
    0.6241301461015194

Графики:

Линейный
<br>
![linear](https://user-images.githubusercontent.com/113106251/206787844-72a07469-5883-4f0b-a485-3a72078fee34.png)

Нелинейный
<br>
![nonlinear](https://user-images.githubusercontent.com/113106251/206787895-4852aafd-2907-4b20-b250-91936425b94a.png)
