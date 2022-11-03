Министерство образования Республики Беларусь <br/>
Учреждение образования <br/>
«Брестский государственный технический университет» <br/>
Кафедра ИИТ <br/>

Лабораторная работа №2 <br/>
За третий семестр <br/>
По дисциплине: «Общая теория интеллектуальных систем» <br/>
Тема: «ПИД-регуляторы» <br/>

Выполнил: <br/>
Студент 1 курса <br/>
Группы ИИ-21(II) <br/>
Годынюк И.А. <br/>

Проверил: <br/>
Иванюк Д.С. <br/>

Брест 2022 <br/>

# Общее задание #
1. Написать отчет по выполненной лабораторной работе №2 в .md формате (*readme.md*) и с помощью **pull request** разместить его в следующем каталоге: **trunk\as000xxyy\task_02\doc**.
2. Исходный код написанной программы разместить в каталоге: **trunk\as000xxyy\task_02\src**.
На Julia реализовать программу, моделирующую рассмотренный выше ПИД-регулятор.  В качестве объекта управления использовать математическую модель, полученную в предыдущей работе.
## Код программы ##
```
function nolin()
    a = -0.5; b = 0.03; c = 0.02; d = 0.04 # Постоянные с первой лаб. работы
    e3=0.0
    K = 10 # - коэффициент передачи
    T = 0.1 # - постоянная интегрирования,
    TD = 40 # - постоянная дифференцирования
    ynonlin1 = 5; ynonlin2 = 6
    unonlin1 = 1; unonlin2 = 0.05
    step = 1; time = 10 # шаг; время работы
    enval = 20.01# желаемое значение
    for step in step:0.5:time
        q1 = K * (1 + TD/step)
        q2 = (-K )* (1 + 2 * TD / step - step / T)
        q3 = K * TD / step
        e1 = enval -  ynonlin1 # - отклонение выходной переменной
        e2 = enval -  ynonlin2
        square=ynonlin1*ynonlin1
        ynonlin3= a* ynonlin2 - b * square + c * unonlin2 + d * sin(unonlin1)  
        parse(Float64,ynonlin1) = ynonlin2
        parse(Float64,ynonlin2) = ynonlin3
        unonlin1=unonlin2
        unonlin2=unonlin1+q1*e3+q2*e2+q3*e1
        e3= enval -  parse(Float32,ynonlin3)
        e1=e2
        e2=e3
        println(step,"\t",ynonlin3,"\t",e3)
    end
end
    
function main() 
    println("\tНелинейная модель")
    println("Step\t\ty\t\t  rejection")
    nolin()
end
main()
```
![image](https://user-images.githubusercontent.com/112876032/199717398-5ddf7043-c903-4bdb-9892-80bfe26a9878.png)
