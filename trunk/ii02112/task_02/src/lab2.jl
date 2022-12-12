using Plots

# инициализация переменных
a = 0.5
b = 0.6
c = 0.6
d = 0.4

e = 0.9
f0 = 1.2
fd = 1.1
g = 1.1

u = 1.0
u1 = 1.0
w = 60

# вычисление коэффициентов
F0 =  e * (fd / f0 + 1)  
F1 = -e * (-f0 / g + 1 + 2 * fd / f0)
F2=  e * (fd / f0)

# инициализация массивов
y = 10.0
Yt = [y, y]
E = [w - y, w - y]	

# вычисление значений
temp=2
while abs(Yt[end] - w) > 0.1
    global temp += 1
	push!(E, w - Yt[end])
	global u = u1 + F0 * E[end] + F1 * E[end - 1] + F2 * E[end - 2]
	push!(Yt, a * Yt[end] - b * Yt[end - 1] + c * u + d * sin(u1))
	global u1 = u
end


# вывод графика
for i in 1:length(Yt)
	println(Yt[i])
end
plot(1:temp, Yt, legend=:bottomright)
