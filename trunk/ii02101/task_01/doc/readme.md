МИНЕСТЕРСТВО ОБРАЗОВАНИЯ РЕСПУБЛИКИ БЕЛАРУСЬ <br/>
УЧЕРЕЖДЕНИЕ ОБРАЗОВАНИЯ <br/>
«Брестский государственный технический университет» <br/>
Кафедра «Интеллектуальные информационные технологии» <br/>

Лабораторная работа №1 <br/>
По дисциплине «Общая теория интеллектуальных систем» <br/>
Тема: «Modeling controlled object» <br/>

Выполнил: <br/>
студент 2 курса <br/>
группы ИИ-21 <br/>
Богуш А.Д. <br/>

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

## Код программы: ###
```julia

a = 0.5
b = 0.5
c = 0.5
d = 0.5
i = 0

function line(t, u, y, a, b, i)

    if i < t

        print(i + 1 , " time has passed: ")
        resl = a * y + b * u
        println(resl)        
        line(t, u, resl, a, b, i + 1)
    else

        println("end of linear module operation")
    end

end

function nline(t, u, up, y, yp, a, b, c, d, i)
    
    if i == 0       

        yp = 0
        up = 0
        
        print(i + 1 , " time has passed: ")
        resnl = a * y - b * yp^2 + c * u + d * sin(up)
        println(resnl)
        nline(t, u, u, resnl, y, a, b, c, d, i + 1)   
    elseif i < t

        print(i + 1 , " time has passed: ")
        resnl = a * y - b * yp^2 + c * u + d * sin(up)
        println(resnl)
        nline(t, u, up, resnl, y, a, b, c, d, i + 1)
    else 

        println("end of non-linear module operation\n")
    end    
end

function main()
                
    y = 0
    u = 1
    t = 10

    println("\nstart of linear module operation")
    line(t, u, y, a, b, i)

    println("\nstart of non-linear module operation")
    nline(t, u, u, y, y, a, b, c, d, i)    
end

main()

```

## Результат программы ##

``` julia

start of linear module operation
1 time has passed: 0.5
2 time has passed: 0.75
3 time has passed: 0.875
4 time has passed: 0.9375
5 time has passed: 0.96875
6 time has passed: 0.984375
7 time has passed: 0.9921875
8 time has passed: 0.99609375
9 time has passed: 0.998046875
10 time has passed: 0.9990234375
end of linear module operation

start of non-linear module operation
1 time has passed: 0.5
2 time has passed: 1.1707354924039484
3 time has passed: 1.3811032386059225
4 time has passed: 0.9259763151197518
5 time has passed: 0.43000057211994025
6 time has passed: 0.7070197103825415
7 time has passed: 1.181795101583481
8 time has passed: 1.2616946077609823
9 time has passed: 0.8532629652210845
10 time has passed: 0.5514303333879209
end of non-linear module operation

```
## График линейной и не линейной зависимости ##
![graphic linear and non-linear models](https://github.com/offendeddddd/myrepos/blob/main/picutres/photo_2022-09-21_22-09-16.jpg)