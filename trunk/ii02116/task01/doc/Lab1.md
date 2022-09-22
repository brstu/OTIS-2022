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
Шнур А.А.  <br/>

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
    # для первой линейной модели 
    a=0.11; b=1.5 # константы a и b 
    y_lin=20; u_lin=15 #входящая температура и тепло 
    i=0 # счётчик 
    t=12 # время 
    
    println("Linear model") 
    for i in i:t # цикл 
        println(y_lin)# вывод значений 
        y_lin=a * y_lin + b * u_lin # формула линейной модели 
    end 
    # нелинейная модель 
    an=0.001; bn=0.009; c=20.5; d=-0.005 # константы 
    y_nonlin1=10; y_nonlin2=12
    u_nonlin=1
    u_nonlin_1=0 
    println("\n\n","Nonlinear model") 
    for i in i:t 
        y_nonlin3=an * y_nonlin2 - bn * abs2(y_nonlin1)+ c * u_nonlin + d * sin(u_nonlin_1)# формула нелинейной модели 
        println(y_nonlin3) # вывод значений 
        y_nonlin1=y_nonlin2 
        y_nonlin2=y_nonlin3 
        u_nonlin_1=u_nonlin 
    end 
     
end 
main()  
```
