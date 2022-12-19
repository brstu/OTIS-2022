function nonliney(A,B,C,D,K,T0,TD,T,w,ys)
#ПИН регулятор
	q0 =  K * (1 + (TD / T0))  
	q1 = -K * (1 + 2 * (TD / T0) - (T0 / T))
	q2 =  K * (TD / T0)
	y = [ys, ys]
	u = 1.0
	u_prev = 1.0
	e = [w - ys, w - ys]
	um = [u,u]
#подсчет значений
	while abs(y[end] - w) > 0.1
		push!(e, w - y[end])
		 u = u_prev + q0 * e[end] + q1 * e[end - 1] + q2 * e[end - 2]
		push!(y, A * y[end] - B * y[end - 1] + C * u + D * sin(u_prev))
	    u_prev = u
		push!(um,u)
	end
#вывод
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
#Инициализация параметров
	A = 0.5
	B = 0.6
	C = 0.6
	D = 0.6
	K = 0.8
	T0 = 1.1
	TD = 1
	T = 1.1
#начальное значение и требуемый результат 
	ys = 2.0
	w = 20
	nonliney(A,B,C,D,K,T0,TD,T,w,ys)
end
main()