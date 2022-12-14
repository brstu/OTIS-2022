function nonliney(J,G,V,B,L,T0,TD,T,w,ys)
#ПИН регулятор
 q0 = L * (1 + (TD / T0)) 
 q1 = -L * (1 + 2 * (TD / T0) - (T0 / T))
 q2 = L * (TD / T0)
 y = [ys, ys]
 u = 1.0
 u_prev = 1.0
 e = [w - ys, w - ys]
 um = [u,u]
 #подсчитаем значения
 while abs(y[end] - w) > 0.1
  push!(e, w - y[end])
   u = u_prev + q0 * e[end] + q1 * e[end - 1] + q2 * e[end - 2]
  push!(y, J * y[end] - G * y[end - 1] + V * u + B * sin(u_prev))
     u_prev = u
  push!(um,u)
 end
 #сделаем вывод
println("P")
 for i in 1:length(p)
  println(y[i])
 end 
 println(" ")
 println("O")
 for i in 1:length(o)
  println(e[i])
 end
 println(" ")
 println("U")
 for i in 1:length(um)
  println(um[i])
 end
end
function main()
#инициализируем параметры
 J = 0.4
 G = 0.7
 V = 0.8
 B = 0.5
 L = 0.7
 T0 = 1.1
 TD = 1
 T = 1.1
 #укажем начальные значения и требуемый результат
 ys = 2.0
 w = 20
 nonliney(J,G,V,B,L,T0,TD,T,w,ys)
end
main()
