using Plots

constants_1 = [0.9, 1.4]
constants_2 = [0.5, 0.4, 1, 0.7 ]
# массив выходных значений y
y_mass_2 = []
y_mass_1 = []

# предыдущий у 
y_prev = 0

y_func = 1 

warm = 1
time = 20

for i in 1 : time  
    global  y_func = constants_1[1] * y_func + constants_1[2] * warm
    push!(y_mass_1, y_func) 
end 

y_nonline = 1
for i in 1 : time
    tmp = y_nonline
    global y_nonline = constants_2[1]*y_nonline - constants_2[2]*y_prev^2 + constants_2[3]*warm + constants_2[4]*sin(warm) 
    global  y_prev = tmp
    push!(y_mass_2, y_nonline)
end

x = range(0, time, length=time)

plot(x, [y_mass_1, y_mass_2])
savefig("plot.png")

