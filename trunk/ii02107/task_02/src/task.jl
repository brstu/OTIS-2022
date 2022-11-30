using Plots
a = 0.5
b = 0.6
c = 0.7
d = 0.5

K_val = 0.9
Т_0 = 1.3
T_D = 1.2
T_vаluе = 1

Q0 =  K_val * (T_D / Т_0 + 1)  
Q1 = -K_val * (-Т_0 / T_vаluе + 1 + 2 * T_D / Т_0)
Q2 =  K_val * (T_D / Т_0)


Y = 10.0
Yt = [Y, Y]

u2 = 1.0
u1 = 1.0

Wt = 40

E = [Wt - Y, Wt - Y]	

temp=2
while abs(Yt[end] - Wt) > 0.1
    global temp += 1
	push!(E, Wt - Yt[end])
	global u2 = u1 + Q0 * E[end] + Q1 * E[end - 1] + Q2 * E[end - 2]
	push!(Yt, a * Yt[end] - b * Yt[end - 1] + c * u2 + d * sin(u1))
	global u1 = u2
end


for i in 1:length(Yt)
	println(Yt[i])
end

plot(1:temp, Yt)
