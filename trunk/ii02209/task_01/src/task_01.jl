using Plots

#models

function linear_heat(time)
    global y = []
    push!(y, 0.0)
    println("Linear heat:")
    for i in 1:time
        push!(y, round(a * y[i] + b * u, digits = 1))
        println("t = ", y[i], " current time is ", i, 's')
    end
end

function nonlinear_heat(time)
    global y = []
    push!(y, 0.0)
    push!(y, 1.0)
    println("nonLinear heat:")
    for i in 2:time
        push!(y, round(a * y[i] - b * y[i - 1] ^ 2 + c * u + d * sin(u), digits = 1))
        println("t = ", y[i], " current time is ", i, 's')
    end
end

#settings

a = 0.923
b = 0.052
c = 0.433
d = 0.254
u = 20
y = []

time = 10


#main

function main() 
    x = 1:time
    linear_heat(time)
    y = 1:10
    plot(x, y)
    nonlinear_heat(time)
    y2 = [ 1, 3, 10]
    plot(x, y)
    plot(x, yz)
end

main()
