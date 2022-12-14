<p style="text-align: center;">Министерство образования Республики Беларусь</p>
<p style="text-align: center;">Учреждение образования</p>
<p style="text-align: center;">“Брестский Государственный Технический Университет”</p>
<p style="text-align: center;">Кафедра ИИТ</p>
<div style="margin-bottom: 10em;"></div>
<p style="text-align: center;">Лабораторная работа №2</p>
<p style="text-align: center;">По дисциплине “Общая теория интеллектуальных систем”</p>
<p style="text-align: center;">Тема: “ПИД-регуляторы”</p>
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
На Julia реализовать программу, моделирующую рассмотренный выше ПИД-регулятор.  В качестве объекта управления использовать математическую модель, полученную в предыдущей работе.
В отчете также привести графики для разных заданий температуры объекта, пояснить полученные результаты.

---
## Код программы ##


``` julia
using Plots
global Arr2 = []
global I = 0
global prevErr = 0
function getNumber()
    num = chomp(readline())
    try
        return parse(Int,num)
    catch
        return Nothing
    end
end

function PID_controller(coeff_P,coeff_I,coeff_D,set_val,current_val,dt)
    Err = set_val - current_val
    P = Err
    global I = I + Err*dt 
    global prevErr
    D = (Err - prevErr) / dt
    control_signal = P * coeff_P + I * coeff_I + D * coeff_D
    prevErr = Err
    push!(Arr2,(control_signal-current_val))
    return control_signal
end

function Linear_model(у_curr, u, t, dt, setting, Arr2)
    а = 0.925
    b = 0.75
    coef_P = 0.19
    coef_I = 0.27
    coef_D = 0.0006
    Аrr1 = []
    Arr3 = []
    push!(Аrr1,у_curr)
    for i in 1:t
        if ((i % dt)==0)
            y=PID_controller(coef_P,coef_I,coef_D, setting, у_curr, dt)
            у_next = а * y  + b * u
            push!(Аrr1,у_next)
            у_curr = у_next
            push!(Arr3,setting)
        else
            у_next = а * у_curr + b * u
            push!(Аrr1,у_next)
            push!(Arr3,setting)
            у_curr = у_next
        end
    end
    println("Current value: ",Аrr1)
    plot([1:(t+1)], Аrr1, color = :green , label = "Current value")
    plot!([1:t], Arr2, color = :red , label = "Control signal")
    plot!([1:t], Arr3, color = :blue , label = "Setting")
end

function main()
    println("Enter initial setting: ")
    setting = getNumber()               #(100)setting stores the value the controller is aiming for
    println("Enter process duration: ")
    duration = getNumber()              #(90)
    println("Enter discretization value: ")
    dis_time = getNumber()              #(1) stores the call period for counting a new control signal
    Linear_model(0, 0, duration, dis_time, setting, Arr2)
end

main()
```
## Результат работы программы: ##

```
Enter initial setting: 
100
Enter process duration: 
90
Enter discretization value:
1
Current value: Any[0, 42.605500000000006, 49.372713697500004, 60.84743089311165, 68.60649081598682, 75.08542714303516, 80.16987912317906, 84.22963331546734, 87.912091712, 92.06323600107683, 93.68697288350032, 94.97851140565895, 96.00582465691619, 96.82296628996825, 97.47293446228788, 97.98992995531702, 98.40115679091373789257, 99.99736696235644, 99.9979056379805, 99.99833410954858, 99.99867492297398, 99.99894601165197, 99.99916164010396, 99.99933315456799, 99.99946958003085, 
99.99957809511744, 99.99966440982566, 99.99973306598294, 99.99978767623455, 99.99983111413871, 99.99986566537159, 99.99989314799795, 99.99991500813694, 99.9999323960558, 99.9999462266962, 99.99995722781807, 99.99996597829372, 99.99997293856788, 99.99997847488594, 99.99998287856556, 99.99998638132573, 99.99998916747951, 99.99999138363272, 99.99999314639787, 99.99999454853065, 99.99999566381042, 99.99999655092256, 99.99999725654632, 99.99999781781123, 99.99999826425069, 99.99999861935608, 99.99999890181282, 99.99999912648362, 99.99999930519051, 99.99999944733695, 99.9999995604026, 99.99999965033689, 99.99999972187217, 99.99999977877248, 99.99999982403195, 99.99999986003208, 99.99999988866718, 99.99999991144402]
```
> _Начальная_ _установка_, _период_ _дискретизации_ _и_ _время_ _вводятся_ _с_ _клавиатуры._

---
## График: ##
![image](https://raw.githubusercontent.com/psijikk/OTIS-2022/main/trunk/ii02201/task_02/doc/plot_task_02.png)
