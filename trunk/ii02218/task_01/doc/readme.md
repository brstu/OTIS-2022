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
Группы ИИ-22(I) <br/>
Полиенко В.Э. <br/>

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
A=0.7   #
B=0.2   #   Коэффициенты
C=0.9   #
D=0.4   #
    function LinearModel(current_y,t,warm) # функция линейной модели 
        Mass_y=[] # создаем массив для  значений y 
        println("Liner date ")
        println(current_y)
        push!(Mass_y,current_y)
        for i in 1:t
            New_y=A*current_y+B*warm    # вычисляем новые значениие У линейной функции
            push!(Mass_y,New_y) # заполняем массив новыми значениями У линейной модели
            current_y=New_y
            println(New_y)  # выводим полученые значения У линейной модели 
        end
        plot([1:(t+1)], Mass_y, color = :red , label = "Linear_model") #  строим график линейной модели 
    end
    function UnlinearModel(middle_y,t,middle_warm) # функция нелинейной модели 
        last_y=0
        last_warm=0
        Mass_y=[] # создаем массив для  значений y 
        println("UnLiner date ")
        println(middle_y)
        push!(Mass_y,middle_y)
        for i in 1:t
            New_y=A*middle_y-B*last_y^2+C*middle_warm+D*sin(last_warm) #вычисляем новые значениие У нелинейной функции
            push!(Mass_y,New_y)# заполняем массив новыми значениями У нелинейной модели
            last_y=middle_y
            middle_y=New_y
            last_warm=middle_warm
            middle_warm=middle_warm+0.005
            println(New_y)# выводим полученые значения У нелинейной модели 
        end
        plot!([1:(t+1)], Mass_y, color = :purple , label = "UnLinear_model") #  строим график нелинейной модели 
    end
    function main()
        println("Start")
        LinearModel(0,10,4)
        UnlinearModel(1,10,1)
        println("End") 
    end
    main()
```