```                    
                                          МИНИСТЕРСТВО ОБРАЗОВАНИЯ РЕСПУБЛИКИ БЕЛАРУСЬ
                                                      УЧРЕЖДЕНИЕ ОБРАЗОВАНИЯ
                                      “БРЕСТСКИЙ ГОСУДАРСТВЕННЫЙ ТЕХНИЧЕСКИЙ УНИВЕРСИТЕТ”
                                            ИНТЕЛЕКТУАЛЬНЫЕ ИНФОРМАЦИОННЫЕ ТЕХНОЛОГИИ
                                            
                                                              ОТЧЁТ
                                                    По лабораторной работе № 2
                                                    
                                                    
                                                                          Выполнил:
                                                                          Студент группы ИИ-22
                                                                          Копанчук Евгений Романович 
                                                                          Проверил: Иванюк Д. С.
                                                                          
                                                                          
                                                          Брест - 2022
```
#### Цель работы:
Реализовать PID регулятор для моледи из предыдущей лабораторной.  

#### Ход работы 
С помощью матетриала данного в методическом пособии и дополнительной информации реализовал PID регулятор для температуры 20 градусов. 
Настроил значения TD для корректрой стабилизации температуры. Использовал достаточный промежуток времени для фиксации успешного результата.

#### Код программы 

```
using Plots

time = 30
required_temp = 20.0

# modeling settings
a = 0.982
b = 0.252
room_warm = 12.0
time_points = 1:time

# PID settings
K = 1.0
T = 1.0
TD = 0.55
T0 = 1.0
q0 = K * (1 + TD / T0)
q1 = -K * (1 + 2 * TD / T0  - T0 / T)
q2 = K * TD / T0
e = []
u = []
y = [0.0]

function PID(t) 
    err = required_temp - y[t]
    push!(e, err)
    e1 = e[t]
    e2 = e[t - 1]
    e3 = e[t - 2]
    u1 = u[t - 1]
    u_val = round(u1 + (q0 * e1) + (q1 * e2) + (q2 * e3), digits=1)
    push!(u, u_val)
    println("t = ", t , " y: ", y[t], " u: ", u[t], " e: ", e[t])
    return (u_val)
end

# init start values 
for i in 1:time - 1
    if (i < 4)
        push!(e, round(required_temp - y[i], digits=1)) 
        push!(u, 1.0) 
        push!(y, round(a * y[i] + b * room_warm, digits=1))
        println("t = ", i , " y: ", y[i], " u: ", u[i], " e: ", e[i])
    else 
        push!(y, round(PID(i) + a * y[i] + b * room_warm, digits=1))
    end
end

# create plot
required_temp_arr = []
for i in 1:time
    push!(required_temp_arr, required_temp)
end
push!(e, round(required_temp - y[time], digits=1)) 
push!(u, u[time - 1]) 
plot(time_points, y, color="red", label="y", lw=2)
plot!(time_points, required_temp_arr, color="green", label="y0", lw=2)
plot!(time_points, u, color="blue", label="u", lw=2)

```

#### График значений

![image](https://github.com/Corowka/OTIS-2022/blob/Lab2/trunk/ii02209/task_02/doc/plot.png?raw=true)
  
#### Вывод программы:
  
t = 1 y: 0.0 u: 1.0 e: 20.0\
t = 2 y: 3.0 u: 1.0 e: 17.0\
t = 3 y: 6.0 u: 1.0 e: 14.0\
t = 4 y: 8.9 u: 12.2 e: 11.1\
t = 5 y: 24.0 u: 1.5 e: -4.0\
t = 6 y: 28.1 u: -0.6 e: -8.100000000000001\
t = 7 y: 30.0 u: -9.4 e: -10.0\
t = 8 y: 23.1 u: -7.7 e: -3.1000000000000014\
t = 9 y: 18.0 u: -6.7 e: 2.0\
t = 10 y: 14.0 u: -1.3 e: 6.0\
t = 11 y: 15.5 u: 0.2 e: 4.5\
t = 12 y: 18.4 u: 1.0 e: 1.6000000000000014\
t = 13 y: 22.1 u: -1.5 e: -2.1000000000000014\
t = 14 y: 23.2 u: -3.3 e: -3.1999999999999993\
t = 15 y: 22.5 u: -4.8 e: -2.5\
t = 16 y: 20.3 u: -4.3 e: -0.3000000000000007\
t = 17 y: 18.7 u: -3.3 e: 1.3000000000000007\
t = 18 y: 18.1 u: -2.0 e: 1.8999999999999986\
t = 19 y: 18.8 u: -1.5 e: 1.1999999999999993\
t = 20 y: 20.0 u: -1.8 e: 0.0\
t = 21 y: 20.9 u: -2.5 e: -0.8999999999999986\
t = 22 y: 21.0 u: -3.1 e: -1.0\
t = 23 y: 20.5 u: -3.3 e: -0.5\
t = 24 y: 19.9 u: -3.1 e: 0.10000000000000142\
t = 25 y: 19.5 u: -2.7 e: 0.5\
t = 26 y: 19.5 u: -2.4 e: 0.5\
t = 27 y: 19.8 u: -2.4 e: 0.1999999999999993\
t = 28 y: 20.1 u: -2.5 e: -0.10000000000000142\
t = 29 y: 20.3 u: -2.7 e: -0.3000000000000007
