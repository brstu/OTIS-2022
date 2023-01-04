using Plots

# веса для рассчёта нагревания 
a_value = 0.923
b_value = 0.052
c_value = 0.433
d_value = 0.254
# комнатная температура
room_warm = 12

heat_array_for_building_plot = []

# дискретные моменты времени
time_points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# массив температур
heat_array_for_building_plot = [0.0]
# рассчёт линейного нагрева
println("Linear heat:")
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[1] + b_value * room_warm, digits = 1))
println("T = ", heat_array_for_building_plot[1], " current time is ", 1, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[2] + b_value * room_warm, digits = 1))
println("T = ", heat_array_for_building_plot[2], " current time is ", 2, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[3] + b_value * room_warm, digits = 1))
println("T = ", heat_array_for_building_plot[3], " current time is ", 3, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[4] + b_value * room_warm, digits = 1))
println("T = ", heat_array_for_building_plot[4], " current time is ", 4, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[5] + b_value * room_warm, digits = 1))
println("T = ", heat_array_for_building_plot[5], " current time is ", 5, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[6] + b_value * room_warm, digits = 1))
println("T = ", heat_array_for_building_plot[6], " current time is ", 6, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[7] + b_value * room_warm, digits = 1))
println("T = ", heat_array_for_building_plot[7], " current time is ", 7, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[8] + b_value * room_warm, digits = 1))
println("T = ", heat_array_for_building_plot[8], " current time is ", 8, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[9] + b_value * room_warm, digits = 1))
println("T = ", heat_array_for_building_plot[9], " current time is ", 9, 's')
# график линейного изменения температуры
plot(time_points, heat_array_for_building_plot, color="green", labal="linear")
# массив температур
heat_array_for_building_plot = [0.0, 1.0]
# рассчёт нелинейного нагрева
println("nonLinear heat:")
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[2] - b_value * heat_array_for_building_plot[1] ^ 2 + c_value * room_warm + d_value * sin(room_warm), digits = 1))
println("T = ", heat_array_for_building_plot[2], " current time is ", 2, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[3] - b_value * heat_array_for_building_plot[2] ^ 2 + c_value * room_warm + d_value * sin(room_warm), digits = 1))
println("T = ", heat_array_for_building_plot[3], " current time is ", 3, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[4] - b_value * heat_array_for_building_plot[3] ^ 2 + c_value * room_warm + d_value * sin(room_warm), digits = 1))
println("T = ", heat_array_for_building_plot[4], " current time is ", 4, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[5] - b_value * heat_array_for_building_plot[4] ^ 2 + c_value * room_warm + d_value * sin(room_warm), digits = 1))
println("T = ", heat_array_for_building_plot[5], " current time is ", 5, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[6] - b_value * heat_array_for_building_plot[5] ^ 2 + c_value * room_warm + d_value * sin(room_warm), digits = 1))
println("T = ", heat_array_for_building_plot[6], " current time is ", 6, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[7] - b_value * heat_array_for_building_plot[6] ^ 2 + c_value * room_warm + d_value * sin(room_warm), digits = 1))
println("T = ", heat_array_for_building_plot[7], " current time is ", 7, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[8] - b_value * heat_array_for_building_plot[7] ^ 2 + c_value * room_warm + d_value * sin(room_warm), digits = 1))
println("T = ", heat_array_for_building_plot[8], " current time is ", 8, 's')
push!(heat_array_for_building_plot, round(a_value * heat_array_for_building_plot[9] - b_value * heat_array_for_building_plot[8] ^ 2 + c_value * room_warm + d_value * sin(room_warm), digits = 1))
println("T = ", heat_array_for_building_plot[9], " current time is ", 9, 's')
# график нелинейного изменения температуры
plot!(time_points, heat_array_for_building_plot, color="blue", labal="not linear")