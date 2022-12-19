Министерство образования Республики Беларусь <br/>
Учреждение образования <br/>
«Брестский государственный технический университет» <br/>
Кафедра «Интеллектуальные информационные технологии» <br/>

Лабораторная работа №2 <br/>
По дисциплине: «Общая теория интеллектуальных систем» <br/>
Тема: «ПИД-регуляторы» <br/>

Выполнил: <br/>
Студент 2 курса <br/>
Группы ИИ-21 <br/>
Худик А.А. <br/>

Проверил: <br/>
Иванюк Д.С. <br/>

Брест 2022 <br/>

# Общее задание #
На Julia реализовать программу, моделирующую рассмотренный выше ПИД-регулятор. В качестве объекта управления использовать математическую модель, полученную в предыдущей работе. В отчете также привести графики для разных заданий температуры объекта, пояснить полученные результаты.
## Код программы ##

``` julia
function nonLinearModel()  
    K0 = 1; time=10
    alpha=0.01; beta=0.07; gamma=30.5; delta=-0.09 
    y_nonLin1=15; y_nonLin2=16
    t_nonLin1=1; t_nonLin0=0.025
    l1=0; l2=0; en=0
    Q = 10; P = 0.1; ; TD = 14
    j = 13
    for K0 in K0:time
        q0 = Q * (1 + TD/K0)
        q1 = (-Q )* (1 + 2 * TD / K0 - K0 / P)
        q2 = Q * TD / K0
        l1 = j -  y_nonLin1
        l2 = j -  y_nonLin2
        y_nonlin3=alpha * y_nonLin2 - beta * abs2(y_nonLin1)+ gamma * t_nonLin1 + delta * sin(t_nonLin0)
        y_nonLin1=y_nonLin2
        y_nonLin2=y_nonlin3
        en= j -  y_nonlin3 
        t_nonlin_n=t_nonLin1+q0*en+q1*l2+q2*l1
        l1=l2
        l2=en
        t_nonLin0=t_nonLin1
        t_nonLin1=t_nonlin_n
        println(K0,"    \t",y_nonlin3, " \t :  \t",en) 
        
    end     
end

println()
println("Нелинейная модель: \n")
nonLinearModel() 
```
![image](https://user-images.githubusercontent.com/61494312/206864623-e96727c9-3ae6-4846-b5ca-19ecc0275f21.svg)
