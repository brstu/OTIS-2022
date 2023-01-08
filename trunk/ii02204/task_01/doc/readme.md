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
Дубина Н.С. <br/>

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
using Plots #подключение пакетов
using Printf

#массивы, которые хранят значения 
unlinearr=[] #нелинейный массив
linearr=[] #линейный массив

function linear(sec, fx, kof1, kof2, kof3) #функция для линейной модели
    k = 1 #счетчик
    X = 1:sec
    linearr = [] #массив для значений y
    while k <= sec
        push!(linearr, fx)
        println(fx) #выведение значений линейной модели
        fx = kof1 * fx + kof2 * kof3 #формула 1
        k += 1
    end
    plot(X, linearr, color = :green , label = "Linear_model") #построение графика линейной модели
end

function unlinear(sec, fx, kof1, kof2, kof3, kof4, kof5) #функция для нелинейной модели
    k = 1
    X = 1:sec
    unlinearr = [] #массив для значений y
    while k <= sec
        println(fx) #выведение значений нелинейной модели
        fx = kof1 * fx - kof2 * fx^2 + kof4 * kof3 + kof5 * sin(kof3) #формула 2
        push!(unlinearr, fx)
        k += 1
    end
    plot!(X, unlinearr, color = :blue , label = "UnLinear_model") #построение графика нелинейной модели
    savefig("lab1.png") #сохранение графика
end

fx = 0.0 #Значение y
sec = 25 #Значение времени
kof1 = 0.6 #Значение констант
kof2 = 1.1
kof3 = 0.3
kof4 = 2.0
kof5 = 0.7

@printf("Линейная модель принимает значения за %d секунд: ",sec) #вывод линейной модели
linear(sec, fx, kof1, kof2, kof3)
@printf("Нелинейная модель принимает значения за %d секунд: ",sec) #вывод нелинейной модели
unlinear(sec, fx, kof1, kof2, kof3, kof4, kof5)
```