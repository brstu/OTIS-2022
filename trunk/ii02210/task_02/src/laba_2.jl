a = 0.25; b = 0.25; c = 0.25; d = 0.25 #константы
K = 0.9; T0 = 1; TD = 1.1;T = 1 #константы
q_num_0 =  K * (TD / T0 + 1)  
q_num_1 = -K * (-T0 / T + 1 + 2 * TD / T0)
q_num_2 =  K * (TD / T0)
y_ = 10.0
y = [y_, y_]
u_1 = 1.0
u_p = 1.0
w = 30
e = [w - y_, w - y_]	
println("|---------------------|")
println("         ВЫВОД:")
while abs(y[end] - w) > 0.1
	push!(e, w - y[end])
	global u_1 = u_p + q_num_0 * e[end] + q_num_1 * e[end - 1] + q_num_2 * e[end - 2]
	push!(y, a * y[end] - b * y[end - 1] + c * u_1 + d * sin(u_p))
	global u_p = u_1
end
for i in 1:length(y)
	println(y[i])
end
println("|---------------------|")
return 0
