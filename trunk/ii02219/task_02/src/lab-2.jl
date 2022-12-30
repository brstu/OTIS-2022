
using Plots
w = 25
e = [0.0,0.0,0.0]
global y = 0.0
constants = [2,0.9]
u = [0.0,0.0]
time = 20
K = 0.01
T = 1.1
T0 = 1
Td = 1
q0 = K * (1  + Td/T0)
q1 = -K * (1 + 2*Td/T0 - T0/T)  
q2 = (K * Td)/T0
y_linear= []
u_mas = []
for i in 1 : time
    global y
    e[3] = e[2]
    e[2] = e[1]
    e[1] = w - y
    delta_u = q0 * e[1] + q1*e[2] + q2*e[3]
    u[2] = u[1]
    u[1] = u[2] + delta_u
    y = constants[1] * y + constants[2] * u[1]
    push!(y_linear,y)
    push!(u_mas,u[1])
end
x = range(0,time,length=time)
plot(x,[range(w,w,time),y_linear,u_mas],Color =["blue" "green" "red"])
savefig("plot.png")