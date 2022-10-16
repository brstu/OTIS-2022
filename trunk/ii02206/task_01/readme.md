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
Группы ИИ-21(I) <br/>
Заречный А.О. <br/>

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
function linear(a, b, y, u, t)
    y = a * y + b * u
    println(y)
    return y
end
function unlinear(a, b, c, d, y, y_last, u, u_last, t)
    y = a * y - b * y_last * y_last + c * u + d * sin(u_last)
    println(y)
    return y
end
function main()
    a = 0.5
    b = 0.4
    c = 0.7
    d = 0.02
    y = 0.0
    u = 1.0
    n = 30
    println("Linear modeling")
    y_linear = []
    y_unlinear = []
    for t in 1:n
        y = linear(a, b, y, u, t)
        push!(y_linear, y)
    end
    println("\nUnlinear model")    
    y_next = 0
    for t in 1:n
        y_prev = y
        y = y_next
        y_next = unlinear(a, b, c, d, y, y_prev, u, u, t)

        push!(y_unlinear, y)
    end
    
    plot([1:n], y_linear, color = :green , label = "linear")
    plot!([1:n], y_unlinear, color = :red, label = "unlinear")
end
main()
```
## Результат выполнения ##
```
Linear modeling
0.4
0.6000000000000001
0.7000000000000001
0.75
0.775
0.7875000000000001
0.7937500000000001
0.796875
0.7984375
0.7992187500000001
0.7996093750000001
0.7998046875      
0.79990234375
0.7999511718750001
0.7999755859375001
0.79998779296875
0.799993896484375
0.7999969482421876
0.7999984741210938
0.7999992370605469
0.7999996185302735
0.7999998092651368
0.7999999046325684
0.7999999523162842
0.7999999761581421
0.7999999880790711
0.7999999940395356
0.7999999970197678
0.7999999985098839
0.799999999254942

Unlinear model
0.46082942017299494
0.9472441297826554
1.1055059827886942
0.9106738345274249
0.6833089457672317
0.7267531594226202
0.8934415532612577
0.9522821344344826
0.8736753632758437
0.7909305959088421
0.8069712614925079
0.8700865674245254
0.8913916566584968
0.859704994100369
0.8288502825221905
0.8356174902048069
0.8598410484637153
0.8674473079535433
0.854822422223657
0.8432546979776466
0.846168219270453
0.8554821350668356
0.8581702251082438
0.8531746588828751
0.8488342950326618
0.8500837677885246
0.8536634394209818
0.8546041745036351
0.8526349998263513
0.8510076015777176
```
![График](https://github.com/Adryian4ik/OTIS-2022/blob/main/trunk/ii02206/task_01/src/plot_3.png)
