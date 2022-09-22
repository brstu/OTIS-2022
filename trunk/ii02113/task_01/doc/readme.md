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
Соболева П.С. <br/>

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
    # Линейная модель
    a=0.27; b=1.7 # константы a и b
    y_lin=18; u_lin=11 #входящая температура и тепло
    i=1
    time=10 
    println("Линейная модель: ")
    for i in i:time 
        println(i,"    ",y_lin)
        y_lin=a * y_lin + b * u_lin # формула линейной модели
    end
    # Нелинейная модель
    a=0.01; b=0.07; c=30.5; d=-0.09 # константы
    y_nonlin1=15; y_nonlin2=16
    u_nonlin1=1; u_nonlin=0.025
    println()
    println("Нелинейная модель:")
    for i in i:time
        y_nonlin3=a * y_nonlin2 - b * abs2(y_nonlin1)+ c * u_nonlin1 + d * sin(u_nonlin)# формула нелинейной модели
        println(i,"    ",y_nonlin3) # вывод значений
        y_nonlin1=y_nonlin2 # переинициализация
        y_nonlin2=y_nonlin3
    end     
end
main()   
```
![image](https://user-images.githubusercontent.com/113055441/191745002-d62c52cf-6124-4c95-9242-8cacf3a872d2.png)
