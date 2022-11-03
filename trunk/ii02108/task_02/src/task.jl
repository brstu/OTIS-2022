A = 0.5
B = 0.5
C = 0.5
D = 0.5

K = 0.9
T0 = 1.3
TD = 1.2
T = 1

q0 =  K * (TD / T0 + 1)  
q1 = -K * (-T0 / T + 1 + 2 * TD / T0)
q2 =  K * (TD / T0)


y_ = 10.0
y = [y_, y_]

u = 1.0
u_prev = 1.0

w = 40

e = [w - y_, w - y_]	


while abs(y[end] - w) > 0.1
	push!(e, w - y[end])
	global u = u_prev + q0 * e[end] + q1 * e[end - 1] + q2 * e[end - 2]
	push!(y, A * y[end] - B * y[end - 1] + C * u + D * sin(u_prev))
	global u_prev = u
end

for i in 1:length(y)
	println(y[i])
end
