using Plots

<<<<<<< Updated upstream
a_value = 0.923
b_value = 0.052
c_value = 0.433
d_value = 0.254
room_warm = 12
heat_array = []

time_points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
heat_array = [0.0]
    println("Linear heat:")
    for iterator in 1:9
        push!(heat_array, round(a_value * heat_array[iterator] + b_value * room_warm, digits = 1))
        println("T = ", heat_array[iterator], " current time is ", iterator, 's')
    end
plot(time_points, heat_array, color="green", labal="linear")
heat_array = [0.0, 1.0]
    println("nonLinear heat:")
    for iterator in 2:9
        push!(heat_array, round(a_value * heat_array[iterator] - b_value * heat_array[iterator - 1] ^ 2 + c_value * room_warm + d_value * sin(room_warm), digits = 1))
        println("T = ", heat_array[iterator], " current time is ", iterator, 's')
    end
plot!(time_points, heat_array, color="blue", labal="not linear")
=======
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


>>>>>>> Stashed changes
