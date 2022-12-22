using Plots

time = 30
required_temp = 20.0

# modeling settings
a = 0.982
b = 0.252
room_warm = 12.0
time_points = 1:time

# PID settings
K = 1.0
T = 1.0
TD = 0.55
T0 = 1.0
q0 = K * (1 + TD / T0)
q1 = -K * (1 + 2 * TD / T0  - T0 / T)
q2 = K * TD / T0
e = []
u = []
y = [0.0]

function PID(t) 
    err = required_temp - y[t]
    push!(e, err)
    e1 = e[t]
    e2 = e[t - 1]
    e3 = e[t - 2]
    u1 = u[t - 1]
    u_val = round(u1 + (q0 * e1) + (q1 * e2) + (q2 * e3), digits=1)
    push!(u, u_val)
    println("t = ", t , " y: ", y[t], " u: ", u[t], " e: ", e[t])
    return (u_val)
end

# init start values 
for i in 1:time - 1
    if (i < 4)
        push!(e, round(required_temp - y[i], digits=1)) 
        push!(u, 1.0) 
        push!(y, round(a * y[i] + b * room_warm, digits = 1))
        println("t = ", i , " y: ", y[i], " u: ", u[i], " e: ", e[i])
    else 
        push!(y, round(PID(i) + a * y[i] + b * room_warm, digits=1))
    end
end

# create plot
required_temp_arr = []
for i in 1:time
    push!(required_temp_arr, required_temp)
end
push!(e, round(required_temp - y[time], digits = 1)) 
push!(u, u[time - 1]) 
plot(time_points, y, color="red", label="y", lw=2)
plot!(time_points, required_temp_arr, color="green", label="y0", lw=2)
plot!(time_points, u, color="blue", label="u", lw=2)

