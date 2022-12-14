function nonliney(J,G,V,B,L,T9,HP,H,Q,ys)
#это наш рассмотренный выше ПИд-регулятор
 q0 = L * (1 + (HP / T9)) 
 q1 = -L * (1 + 2 * (HP / T9) - (T9 / H))
 q2 = L * (HP / T9)
 y = [SS, SS]
 u = 1.0
 u_prev = 1.0
 e = [Q - SS, Q - SS]
 um = [u,u]
 #при помощи этого сможем посчитать все нужное
 while abs(y[end] - Q) > 0.1
  push!(e, Q - y[end])
   u = u_prev + q0 * e[end] + q1 * e[end - 1] + q2 * e[end - 2]
  push!(y, J * y[end] - G * y[end - 1] + V * u + B * sin(u_prev))
     u_prev = u
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
#вот такие у нас параметры
function main()
 J = 0.4
 G = 0.7
 V = 0.8
 B = 0.5
 L = 0.7
 T9 = 1.1
 HP = 1
 H = 1.1
#здесь нужно указать значения для нужного нам результата
 SS = 2.0
 Q = 20
 nonliney(J,G,V,B,L,T9,HP,H,Q,SS)
end
#посмотрим какой вывод мы имеем 
main()
