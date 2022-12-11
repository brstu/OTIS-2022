<p align="center"> Министерство образования Республики Беларусь</p>
<p align="center">Учреждение образования</p>
<p align="center">“Брестский Государственный технический университет”</p>
<p align="center">Кафедра ИИТ</p>
<br><br><br><br><br><br><br>
<p align="center">Лабораторная работа №2</p>
<p align="center">По дисциплине “Общая теория интеллектуальных систем”</p>
<p align="center">Тема: “ПИД-регуляторы”</p>
<br><br><br><br><br>
<p align="right">Выполнил:</p>
<p align="right">Студент 2 курса</p>
<p align="right">Группы ИИ-21</p>
<p align="right">Кузьмич В. Н.</p>
<p align="right">Проверил:</p>
<p align="right">Шурина А. А.</p>
<br><br><br><br><br>
<p align="center">Брест 2022</p>


---
# Задание: #
На Julia реализовать программу, моделирующую рассмотренный выше ПИД-регулятор. В качестве объекта управления использовать математическую модель, полученную в предыдущей работе. В отчете также привести графики для разных заданий температуры объекта, пояснить полученные результаты.

---
# Код программы #
```julia
function nonliney(A,B,C,D,K,T0,TD,T,w,ys)
 q0 = K * (1 + (TD / T0)) 
 q1 = -K * (1 + 2 * (TD / T0) - (T0 / T))
 q2 = K * (TD / T0)
 y = [ys, ys]
 u = 1.0
 u_prev = 1.0
 e = [w - ys, w - ys]
 um = [u,u]
 while abs(y[end] - w) > 0.1
  push!(e, w - y[end])
   u = u_prev + q0 * e[end] + q1 * e[end - 1] + q2 * e[end - 2]
  push!(y, A * y[end] - B * y[end - 1] + C * u + D * sin(u_prev))
     u_prev = u
  push!(um,u)
 end
println("Y")
 for i in 1:length(y)
  println(y[i])
 end 
 println(" ")
 println("E")
 for i in 1:length(e)
  println(e[i])
 end
 println(" ")
 println("U")
 for i in 1:length(um)
  println(um[i])
 end
end
function main()
 A = 0.5
 B = 0.6
 C = 0.6
 D = 0.6
 K = 0.8
 T0 = 1.1
 TD = 1
 T = 1.1
 ys = 2.0
 w = 20
 nonliney(A,B,C,D,K,T0,TD,T,w,ys)
end
main()
```

# Вывод #
```
Y
2.0
2.0
9.544882590884736
14.720456262569957
15.842387402415573
16.91428333501587
18.276754241422516
20.091789874818467
E
18.0
18.0
18.0
10.455117409115264
5.279543737430043
4.157612597584427
3.0857166649841297
1.7232457585774839
U
1.0
1.0
15.399999999999997
18.276906588466943
24.2236753378288
30.497869075416055
33.00283164903632
34.17010100222095
```
---
# График #
![Линейная](images/picture.png)
