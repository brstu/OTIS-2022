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
Годынюк И.А. <br/>

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
function main()
    a = 0.5
    b = 0.3
    c = 0.2
    d = 0.4
    ylin = 0
    ulin = 1.2
    i = 0
    t = 10
    println("Linear model")
    for i in i:t
        println(ylin)
        ylin = a * ylin + b * ulin
    end
    ynonlin1 = 0
    ynonlin2 = 0
    ynonlin3 = 0
    unonlin = 2
    k = 0
    println("\n\n","Nonlinear model")
    for i in 1:t
        ynonlin3 = a * ynonlin2 - b * (ynonlin1) * (ynonlin1)+c * unonlin+d * sin(unonlin)
        println(ynonlin3)
        ynonlin1=ynonlin2
        ynonlin2=ynonlin3
    end
end


main()  
```

Вывод программы:
```
Linear model
0
0.36
0.54
0.63
0.675
0.6975
0.70875
0.714375
0.7171875
0.7185937499999999
0.719296875


Nonlinear model
0.7637189707302727
1.145578456095409
1.1615281989019852
0.9507780704602832
0.8343636789070674
0.9097071284033528
1.0097237103281484
1.0203107080539846
0.9680117333976123
0.9354146551381919
```
![image](https://user-images.githubusercontent.com/112876032/191744099-2c33122a-6c5c-42eb-9e1d-e4bbeccb8fae.png)
