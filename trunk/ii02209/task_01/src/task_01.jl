using Plots

#models

function linear_heat(time)
    global heat_array = [0.0]
    println("Linear heat:")
    for iterator in 1:time - 1
        push!(heat_array, round(a_value * y[iterator] + b_value * room_temprature, digits = 1))
        println("t = ", heat_array[iterator], " current time is ", iterator, 's')
    end
end

function nonlinear_heat(time)
    global heat_array = [0.0, 1.0]
    println("nonLinear heat:")
    for iterator in 2:time - 1
        push!(heat_array, round(a_value * heat_array[iterator] - b_value * heat_array[iterator - 1] ^ 2 + c_value * room_temprature + d_value * sin(room_temprature), digits = 1))
        println("t = ", heat_array[iterator], " current time is ", iterator, 's')
    end
end

#settings

a_value = 0.923
b_value = 0.052
c_value = 0.433
d_value = 0.254
room_temprature = 12
heat_array = []

time = 10


#main

time_points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
linear_heat(time)
plot(time_points, heat_array, color="green", labal="linear")
nonlinear_heat(time)
plot!(time_points, heat_array, color="blue", labal="not linear")

