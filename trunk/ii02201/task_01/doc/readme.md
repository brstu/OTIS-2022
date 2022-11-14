<p style="text-align: center;">Министерство образования Республики Беларусь<br/>
<p style="text-align: center;">Учреждение образования</p>
<p style="text-align: center;">“Брестский Государственный Технический Университет”</p>
<p style="text-align: center;">Кафедра ИИТ</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: center;">Лабораторная работа №1</p>
<p style="text-align: center;">По дисциплине “Общая теория интеллектуальных систем”</p>
<p style="text-align: center;">Тема: “Modeling controlled object”</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: right;">Выполнил:</p>
<p style="text-align: right;">Студент 2 курса</p>
<p style="text-align: right;">Группы ИИ-22(I)</p>
<p style="text-align: right;">Борейша О.С.</p>
<p style="text-align: right;">Проверил:</p>
<p style="text-align: right;">Иванюк Д. С.</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: center;">Брест 2022</p>

---
## Общее задание ##
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

---
## Код программы ##


``` julia
using Plots

function Linear_model(у_curr, u, t)
    а = 0.925
    b = 0.75
    Аrr1 = []
    push!(Аrr1,у_curr)
    for i in 1:t
        у_next = а * у_curr + b * u
        push!(Аrr1,у_next)
        у_curr = у_next
    end
    println("Linear: ",Аrr1)
    plot([1:(t+1)], Аrr1, color = :green , label = "Linear_model")
end

function Unlinear_model(у_curr, u_curr, t)
    а = 1.37
    b = 0.0043
    c = 0.45
    d = 0.75
    у_prev = 0
    u_prev = 0
    Аrr2 = []
    push!(Аrr2,у_curr)
    for i in 1:t
        у_next= а * у_curr - b * у_prev^2 + c * u_curr + d * sin(u_prev)
        push!(Аrr2,у_next)
        у_prev = у_curr
        у_curr = у_next
        u_prev = u_curr
        u_curr = u_curr + 0.035
    end
    println("Unlinear: ",Аrr2)
    plot!([1:(t+1)], Аrr2, color = :red , label = "Unlinear_model")
end

function getInt()
    x = chomp(readline())
    try
        return parse(Int,x)
    catch
        return Nothing
    end
end

function main()
    println("Enter ambient temperature: ")
    start_temp = getInt()                    # the initial temperature value is equal to the ambient temperature (0)
    println("Enter warm input value: ")
    warm = getInt()                          # warm input value of the corresponding simulation object (10)
    println("Enter process duration: ")
    duration = getInt()
    Linear_model(start_temp, warm, duration)
    Unlinear_model(start_temp, warm, duration)
end

main()
```
## Результат работы программы: ##

```
Enter ambient temperature: 
0
Enter warm input value: 
10
Enter process duration: 
60

Linear: [0, 7.5, 14.4375, 20.8546875, 26.7905859375, 32.281291992187505, 37.360195092773445, 42.058180460815436, 46.40381692625428, 50.42353065678521, 54.14176585752632, 57.58113341821185, 60.76254841184596, 63.70535728095752, 66.42745548488571, 68.94539632351929, 71.27449159925536, 73.42890472931121, 75.42173687461288, 77.26510660901691, 78.97022361334065, 80.54745684234011, 82.00639757916461, 83.35591776072727, 84.60422392867272, 85.75890713402228, 86.82698909897061, 87.81496491654782, 88.72884254780674, 89.57417935672123, 90.35611590496714, 91.07940721209461, 91.74845167118751, 92.36731779584845, 92.93976896115981, 93.46928628907283, 93.95908981739237, 94.41215808108794, 94.83124622500635, 95.21890275813088, 95.57748505127107, 95.90917367242574, 96.21598564699381, 96.49978672346928, 96.76230271920909, 97.0051300152684, 97.22974526412328, 97.43751436931404, 97.62970079161549, 97.80747323224433, 97.97191273982601, 98.12401928433907, 98.26471783801364, 98.39486400016261, 98.51524920015042, 98.62660551013914, 98.72961009687872, 98.82488933961281, 98.91302263914186, 98.99454594120623, 99.06995499561576]

Unlinear: [0, 4.5, 10.272734166832974, 18.088283728566683, 28.42339182751542, 41.62442272311826, 57.638446762213505, 75.59767312085181, 93.36340615765623, 107.4108582877735, 113.74666828116463, 110.29802927739675, 99.54777478545198, 88.14264465838403, 82.219047598754, 83.31029428005797, 89.14730211093637, 96.37072077928526, 101.94252821937852, 103.81867771640347, 101.64359955281364, 97.01057259315131, 92.59264647118789, 90.50622389220432, 91.25916519166476, 93.94371538030504, 97.04428654369451, 99.16630463702037, 99.54017951850146, 98.2759942013259, 96.2394894575157, 94.54060660579657, 93.93322246159819, 94.51242855492409, 95.8167390804912, 97.15376722819062, 97.93839781503196, 97.92518284476648, 97.27102043633414, 96.4090002926312, 95.80103008753521, 95.71082012167518, 96.11537649936537, 96.77040602985575, 97.36142776850059, 97.65598812678272, 97.59512032696209, 97.29445624828845, 96.96415427090415, 96.79485970583306, 96.87081808735505, 97.1486296469756, 97.49936567775845, 97.782159276742, 97.910731065085, 97.88473923094823, 97.77686925509967, 97.68747484691994, 97.69281439042282, 97.81284282711879, 98.01087020148029]
```
> _Начальная_ _температура,_ _входное_ _тепло_ _и_ _время_ _вводятся_ _с_ _клавиатуры._

---
## График: ##
![image](https://raw.githubusercontent.com/psijikk/OTIS-2022/main/trunk/ii02201/task_01/doc/plot_task_01.png)