<p style="text-align: center;">Министерство образования Республики Беларусь</p>
<p style="text-align: center;">Учреждение образования</p>
<p style="text-align: center;">“Брестский Государственный технический университет”</p>
<p style="text-align: center;">Кафедра ИИТ</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: center;">Лабораторная работа №2</p>
<p style="text-align: center;">По дисциплине “Общая теория интеллектуальных систем”</p>
<p style="text-align: center;">Тема: “ПИД-регулятор”</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: right;">Выполнил:</p>
<p style="text-align: right;">Студент 2 курса</p>
<p style="text-align: right;">Группы ИИ-21</p>
<p style="text-align: right;">Шпак И.С.</p>
<p style="text-align: right;">Проверил:</p>
<p style="text-align: right;">Иванюк Д. С.</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: center;">Брест 2022</p>

---

# Общее задание #
1.  На Julia реализовать программу, моделирующую рассмотренный выше ПИД-регулятор. В качестве объекта управления использовать математическую модель, полученную в предыдущей работе. В отчете также привести графики для разных заданий температуры объекта, пояснить полученные результаты.
2. Исходный код написанной программы разместить в каталоге: **trunk\ii0xxyy\task_01\src**.

## Задача ##
Задача 
	
## Вывод программы ##
```julia
Линейная модель
3
5
7
9
11
13
15
17
Нелинейная модель 
2.598794871135003
1.9586743582485036
-2.7083255188302235
-0.841161874076169
-3.453343009030214
1.5874179315125154
-6.882925686128028
-0.20541424890777837
```
## Код программы ##

```julia
using Plots
using LinearAlgebra
function nonlineral_model(param,time,start_warm=1,desired_temp=100)
    result=[]
    array_of_e=[0.001,0.19,0.00002]
    array_of_q=[0.4,0.1,0.12]
    weigth=[1,0,1,1.0]
    prev_u=weigth[3]
    # e(t) = w(t) - y(t) 
    # - отклонение выходной переменной y(t) от желаемого значения w(t).
    for i in 1:time
        
        param[4]=sin(param[3])
        future_y=weigth[1]*param[1]-weigth[2]*param[2]^2+weigth[3]*param[3]+weigth[4]*param[4]
        param[2]=param[1]
        param[1]=future_y
        array_of_e[3]=desired_temp-future_y
        future_y=weigth[1]*param[1]-weigth[2]*param[2]^2+weigth[3]*param[3]+weigth[4]*param[4]
        param[2]=param[1]
        param[1]=future_y
        array_of_e[2]=desired_temp-future_y
        weigth[3]=prev_u+dot(array_of_q,array_of_e)
        future_y=weigth[1]*param[1]-weigth[2]*param[2]^2+weigth[3]*param[3]+weigth[4]*param[4]
        param[2]=param[1]
        param[1]=future_y
        array_of_e[1]=desired_temp-future_y
        push!(result,param[1])
    end
    return result
end
function main()
    size=200
    param=[1,0,1,1.0]
    y=nonlineral_model(param,size)
    for i in y
        println(i)
    end 
    x=[i for i in 1:size]
    a=plot(x,y,color="red",label="pid")


end
main()

```
## График
![Снимок экрана от 2022-10-02 20-05-17](https://user-images.githubusercontent.com/113047080/193466804-4a14d329-a95f-48d1-be22-bf203c254794.png)
##