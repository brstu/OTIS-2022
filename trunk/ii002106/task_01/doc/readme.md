<p style=“text-align: center;”>Министерство образования Республики Беларусь</p>
<p style=“text-align: center;”>Учреждение образования</p>
<p style=“text-align: center;”>“Брестский Государственный технический университет”</p>
<p style=“text-align: center;”>Кафедра ИИТ</p>
<div style=“margin-bottom: 10em;”></div>
<p style=“text-align: center;”>Лабораторная работа №1</p>
<p style=“text-align: center;”>По дисциплине “Общая теория интеллектуальных систем”</p>
<p style=“text-align: center;”>Тема: “Моделирования температуры объекта”</p>
<div style=“margin-bottom: 10em;”></div>
<p style=“text-align: right;”>Выполнил:</p>
<p style=“text-align: right;”>Студент 2 курса</p>
<p style=“text-align: right;”>Группы ИИ-21</p>
<p style=“text-align: right;”>Корнейчук А.И.</p>
<p style=“text-align: right;”>Проверил:</p>
<p style=“text-align: right;”>Иванюк Д. С.</p>
<div style=“margin-bottom: 10em;”></div>
<p style=“text-align: center;”>Брест 2022</p>

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

    function main()
       a = 0.5
       b = 0.5
       c = 0.1  
       d = 0.5
       y = 0.0
       u = 1.0
       i = 0
       t = 10
       println("Линейная модель:")
       line_model(a, b, y, u, i, t)
       println("Нелинейная модель:")
       noline_model(a, b, c, d, y, y, u, u, i, t)
     end
     function line_model(a, b, y, u, i, t)
        if i <= t
              println(y)
              line_model(a, b, a*y + b*u, u, i + 1, t)
        else
               println("-------------------")
        end
     end
     function noline_model(a, b, c, d, y, y_1, u, u_1, i, t)
     if i == 1
        println(y)
        noline_model(a, b, c, d, a*y - b*y_1^2 + c*0 + d*sin(0), y, u, u, i + 1, t)
      elseif i <= t
        println(y)
        noline_model(a, b, c, d, a*y - b*y_1^2 + c*u + d*sin(u_1), y, u, u, i + 1, t)
       else
        println("-------------------")
       end
      end
    main()

    Вывод программы:

         Линейная модель:
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
    -------------------
    Нелинейная модель:
    0.0
    0.5207354924039482
    0.2603677462019741
    0.5153366389803441
    0.7445081302629725
    0.7602036317976557
    0.6236911302889425
    0.5436262766492467
    0.5980533177280223
    0.6719973869361977
    0.6779003004492997
    -------------------
![lin](https://user-images.githubusercontent.com/45300214/191748032-2294b7a9-5af0-4db3-9003-754f00f31bd8.png)
![nonlin](https://user-images.githubusercontent.com/45300214/191748039-77c724ae-b101-45bb-b6a2-8f460b6bb4bb.png)
