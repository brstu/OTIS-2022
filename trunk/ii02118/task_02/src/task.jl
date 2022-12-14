 J = 0.4; G = 0.7; V = 0.8 #укажем здесь наши параметры
 B = 0.5; L = 0.7; T9 = 1.1
 HP = 1; H = 1.1
 #наш рассмотренный выше ПИД-руегулятор
 q_n_0 = L * (1 + (HP / T9)) 
 q_n_1 = -L * (1 + 2 * (HP / T9) - (T9 / H))
 q_n_2 = L * (HP / T9)
 y = [SS, SS]
 u = 1.0
 u_p = 1.0
 e = [Q - SS, Q - SS]
 um = [u,u]
 #при помощи этого сможем посчитать все нужное
 while abs(y[end] - Q) > 0.1
  push!(e, Q - y[end])
   u = u_p + q_n_0 * e[end] + q_n_1 * e[end - 1] + q_n_2 * e[end - 2]
  push!(y, J * y[end] - G * y[end - 1] + V * u + B * sin(u_prev))
     u_p = u
  push!(um,u)
 end
 #для вывода нужно это :Х
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
#здесь нужно указать значения для нужного нам результата
 SS = 2.0
 Q = 20
end
#посмотрим какой вывод мы имеем 
main()
