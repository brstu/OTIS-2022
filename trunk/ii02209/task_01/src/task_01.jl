using Plots

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
        println("t = ", heat_array[iterator], " current time is ", iterator, 's')
    end
plot(time_points, heat_array, color="green", labal="linear")
heat_array = [0.0, 1.0]
    println("NonLinear heat:")
    for iterator in 2:9
        push!(heat_array, round(a_value * heat_array[iterator] - b_value * heat_array[iterator - 1] ^ 2 + c_value * room_warm + d_value * sin(room_warm), digits = 1))
        println("t = ", heat_array[iterator], " current time is ", iterator, 's')
    end
plot!(time_points, heat_array, color="blue", labal="not linear")