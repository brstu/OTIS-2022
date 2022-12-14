J = 0.4; G = 0.7; V = 0.8 #укажем здесь наши параметры
 B = 0.5; L = 0.7; T9 = 1.1
 HP = 1; H = 1.1; SS = 2.0; Q = 20
 #наш рассмотренный выше ПИД-руегулятор
 qn0 = L * (1 + (HP / T9)) 
 qn1 = -L * (1 + 2 * (HP / T9) - (T9 / H))
 qn2 = L * (HP / T9)
 y = [SS, SS]; u = 1.0; u_p = 1.0; e = [Q - SS, Q - SS]; mm = [u,u]
 #при помощи этого сможем посчитать все нужное
 while abs(y[end] - Q) > 0.1
  push!(e, Q - y[end])
   u = u_p + qn0 * e[end] + qn1 * e[end - 1] + qn2 * e[end - 2]
  push!(y, J * y[end] - G * y[end - 1] + V * u + B * sin(u_prev))
     u_p = u
  push!(mm,u)
 end
 #для вывода нужно это :Х
println("P"); println("O"); println("U")
 for i in 1:length(p); for i in 1:length(o); for i in 1:length(um)
  println(y[i]); println(e[i]); println(um[i])
    end 
   end
  end
 end
end
main()
