а = 0.4; б = 0.7; в = 0.8 #укажем здесь наши параметры
 г = 0.5; л = 0.7; т9 = 1.1
 хр = 1; х = 1.1; ус = 2.0; к = 20
 #наш рассмотренный выше ПИД-руегулятор
 qn0 = л * (1 + (хр / т9)) 
 qn1 = -л * (1 + 2 * (хр / т9) - (т9 / х))
 qn2 = л * (хр / т9)
 y = [ус, ус]; u = 1.0; u_p = 1.0; e = [к - ус, к - ус]; им = [u,u]
 #при помощи этого сможем посчитать все нужное
 while abs(y[end] - к) > 0.1
  push!(e, к - y[end])
   u = u_p + qn0 * e[end] + qn1 * e[end - 1] + qn2 * e[end - 2]
  push!(y, а * y[end] - б * y[end - 1] + в * u + г * sin(u_p))
     u_p = u
  push!(им,u)
 end
 #для вывода нужно это :Х
println("У"); println("Е"); println("И")
 for i in 1:length(у); for i in 1:length(е); for i in 1:length(им)
  println(y[i]); println(e[i]); println(им[i])
    end 
   end
  end
 end
end
main()
