<p style="text-align: center;">Министерство образования Республики Беларусь</p>
<p style="text-align: center;">Учреждение образования</p>
<p style="text-align: center;">“Брестский Государственный технический университет”</p>
<p style="text-align: center;">Кафедра ИИТ</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: center;">Лабораторная работа №1</p>
<p style="text-align: center;">По дисциплине “Общая теория интеллектуальных систем”</p>
<p style="text-align: center;">Тема: “Моделирования температуры объекта”</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: right;">Выполнил:</p>
<p style="text-align: right;">Студент 2 курса</p>
<p style="text-align: right;">Группы ИИ-21</p>
<p style="text-align: right;">Романко Н.А.</p>
<p style="text-align: right;">Проверил:</p>
<p style="text-align: right;">Иванюк Д. С.</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: center;">Брест 2022</p>

---

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
	
## Вывод программы ##
```julia
Значения линейной модели за 30 секунд: 0.0
0.42
0.6719999999999999
0.8231999999999999
0.9139199999999998
0.9683519999999999
1.0010112
1.02060672
1.032364032
1.0394184192
1.04365105152
1.046190630912
1.0477143785471998
1.0486286271283198
1.049177176276992
1.049506305766195
1.049703783459717
1.0498222700758302
1.049893362045498
1.0499360172272987
1.0499616103363791
1.0499769662018275
1.0499861797210965
1.049991707832658
1.0499950246995948
1.0499970148197568
1.049998208891854
1.0499989253351123
1.0499993552010674
1.0499996131206404
 
Значения нелинейной модели за 30 секунд: 0.0
1.1681782260555318
0.9138369042076766
1.1319118473358287
0.9504682333595833
1.1060862622333008
0.9754312097446485
1.0874107204415853
0.9929012058685818
1.0738219863459824
1.0053058570110995
1.0639138339636167
1.0141876741642886
1.0566871836553666
1.0205790733776945
1.051418518570617
1.0251927063626405
1.0475797902477075
1.0285297083493548
1.0447846983950986
1.0309464988922152
1.0427506468861796
1.0326983760801576
1.0412710965326104
1.0339690364431406
1.0401952700952066
1.034891048162748
1.0394132178560067
1.035560270551491
1.0388448366251524
```
## Код программы ##

```julia
using Printf
using Plots

#массивы для хранения значений
linY = []
nolinY = []

#функция для линейной/нелинейной модели
function line(const1,const2,const3,y,time)
    i = 1
    x=1:time
    linY=[]
    while i <= time
        push!(linY,y)
        println(y)
        y = const1*y + const2*const3
        i += 1
    end
    plot(x,linY,label="Line",legend=:bottomright)
end

function noline(const1,const2,const4,const5,y,const3,time)
    i = 1
    x=1:time
    nolinY=[]
    while i <= time
        println(y)
        y=const1*y - const2*y^2 + const4*const3 + const5*sin(const3)
        push!(nolinY,y)
        i += 1
    end
    plot!(x,nolinY,label="Not line",legend=:bottomright)
end

#Значения
const1=0.6
const2=0.7
const3=0.6
const4=1.1
const5=0.9
time=30
y=0.0

#вывод
@printf("Значения линейной модели за %d секунд: ",time)
line(const1,const2,const3,y,time)
println(" ")
@printf("Значения нелинейной модели за %d секунд: ",time)
noline(const1,const2,const4,const5,y,const3,time)
```
## График
<img src = "C:\work\otis\Снимок экрана 2022-11-03 171630.png" alt = "График">
##