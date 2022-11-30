using Plots
include("param.jl")

function nonlinear_model(time)
    function l(p)
        return last(y) - p
    end
    i = 0
    while i < time
        e[1] = w - (0)
        e[2] = w - l(1)
        e[3] = w - l(2)
        u[1] = u[2] + q_0 * e[1] + q_1 * e[2] + q_2 * e[3]
        next = p[1]*l(0) - p[2]*l(1)^2 + p[3]*u[1] + p[4]*sin(u[2])
        push!(y, next)
        u[2] = u[1]
        
        i += 1
    end
end


global w = 100
nonlinear_model(50) 
for el in y
    println(el)  
end
plot(1:length(y), y)