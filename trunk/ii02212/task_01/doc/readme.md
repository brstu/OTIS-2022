Министерство образования Республики Беларусь <br/>
Учреждение образования <br/>
«Брестский государственный технический университет» <br/>
Кафедра ИИТ <br/>

Лабораторная работа №1 <br/>
За третий семестр <br/>
По дисциплине: «Общая теория интеллектуальных систем» <br/>
Тема: «Modeling controlled object» <br/>

Выполнила: <br/>
Студент 2 курса <br/>
Группы ИИ-22(I) <br/>
Леваневская Н.И. <br/>

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

value_u_t = 0.5 # input warm
time = 15 # time
this_is_a_constant_a = 1.2  # constant
this_is_a_constant_b = 0.7  # constant
this_is_a_constant_c = -0.32  # constant
this_is_a_constant_d = 0.53 # constant

arr_yt_linear = []  #array for linear dependency
arr_yt_not_linear = [] #array for non-linear dependency

#function for linear dependence
function f1()
    println("linear model")
    _y_t_ = 1 # input temperature
    for i in 1 : time
        _y_t_ = this_is_a_constant_a * yt + this_is_a_constant_b * value_u_t
        println(_y_t_)
        push!(arr_yt_linear, _y_t_)
    end
end

#function for non-linear dependence
function f2()
    _y_t_ = 1.5 # input temperature
    yt_previous = 0 # input temperature
    println("non-linear model")
    for i in 1 : time
        temperature = yt_previous
        _y_t_ = this_is_a_constant_a * _y_t_ - this_is_a_constant_b * yt_previous ^ 2 + this_is_a_constant_c * value_u_t + this_is_a_constant_d * sin(value_u_t)
        yt_previous = temperature
        println(yt)
        push!(arr_yt_not_linear, _y_t_)
    end
end

f1()
f2()
this_is_a_value_x = 1 : time
plot(this_is_a_value_x,arr_yt_linear, title = "Temperature dependence",  label = "linear dependence",  lw = 3)
plot!(this_is_a_value_x,arr_yt_not_linear, label = "non-linear dependence",  lw = 3)
```

## График зависимости ##
![](https://github.com/neonchikCallMe/OTIS-2022/blob/Lab1/trunk/ii02212/task_01/doc/photo_2022-10-27_20-59-24.jpg?raw=true) 
## Результат работы программы ##
linear model\
1.5499999999999998\
2.2099999999999995\
3.0019999999999993\
3.952399999999999\
5.092879999999998\
6.461455999999997\
8.103747199999997\
10.074496639999996\
12.439395967999994\
15.277275161599992\
18.68273019391999\
22.76927623270399\
27.67313147924479\
33.55775777509375\
40.6193093301125\
non-linear model\
1.8940955354602276\
2.3670101780125004\
2.934507749075228\
3.615504834350501\
4.432701336680829\
5.413337139477222\
6.590100102832894\
8.002215658859699\
9.696754326091865\
11.730200726770464\
14.170336407584783\
17.098499224561966\
20.612294604934586\
24.828849061381728\
29.8887144091183
