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
<p style="text-align: right;">Литвинюк Т.В.</p>
<p style="text-align: right;">Проверил:</p>
<p style="text-align: right;">Иванюк Д. С.</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: center;">Брест 2022</p>

---

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

---

# Выполнение задания #

Код программы:

    a = 0.5
    b = 0.5
    c = 0.1
    d = 0.5
    u = 1.0
    y = 0.0

    println("Линейная модель")
    function linear(y, n, t)
        if n < t
            println(y)
            return linear(a * y + b * u, n+1, t)
        end
        println(y)
        return a * y + b * u
    end
    println(linear(y, 0, 10))

    println("----------------------")

    println("Нелинейная модель")
    function nonlinear_model(y, y_prev, u, u_prev, i, t)
        if i == 1
            println(y)
            return nonlinear_model(a*y - b*y_prev^2 + c*1 + d*sin(1), y, u, u, i + 1, t)
        elseif i < t
            println(y)
            return nonlinear_model(a*y - b*y_prev^2 + c*u + d*sin(u_prev), y, u, u, i + 1, t)
        end
        println(y)
        return a*y - b*y_prev^2 + c*u + d*sin(u_prev)
    end

    println(nonlinear_model(y, y, u, u, 0, 10))

Вывод:
    Линейная модель
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
    Нелинейная модель
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





