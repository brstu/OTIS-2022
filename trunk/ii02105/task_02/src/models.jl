using Plots
using LinearAlgebra

a = 1 # linear and nonlinear model parameter; can be changed
b = 0.5 # linear and nonlinear model parameter; can be changed
c = 0.001 # nonlinear model parameter; can be changed
d = 0.999 # nonlinear model parameter; can be changed

K = 1
T_D = 0.1
T = 0.01
T_0 = 1
global q_0 = K * (1 + T_D/T_0)
global q_1 = -K * (1 + 2 * T_D / T_0 - T_0 / T)
global q_2 = K * T_D / T_0

global w = 20#parse(Int64, readline())

q = [0.000004,0.0000011,0.000014]
e = [0.001,0.19,0.00002]
y = [0.0, 0.0, 0.0]
u = [1.0, 1.0]

function nonlinear_model(a, b, c, d)
    while w - y[1] > 0.001
        e[1] = w - y[1]
        e[3] = e[2]
        e[2] = e[1]
        
        println(y[1])
        
        u[1] = u[2] + dot(q, e)
        !push(a*y[length(y)] - b*y[length(y) - 1]^2 + c*u[1] + d*sin(u[2]))
        u[2] = u[1]
    end
end

function main()
    println("Nonlinear Model:")
    nonlinear_model(a, b, c, d)
    
    plot(1:length(y_nonlin), y_nonlin, label="nonlinear_model")
    plot(1:length(y_nonlin), y_nonlin, "b.") 
    legend()
end

main()