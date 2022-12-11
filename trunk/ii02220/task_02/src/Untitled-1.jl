using Plots
kp = 0.1
ki = 2.0
kd = 1.02
dt = 1  
K0 = kp * (1 + kd/dt)           
K1 = -kp * (1 + 2kd/dt - dt/ki)  
K2 = (kp * kd)/dt               
function line_mod(y, c1, c2, s)
    y = c1 * y + c2 * s
    return y
end
duration = 100
aim = 20
function main()
    Yarr = [] 
    Sarr = [] 
    c1 = 0.73
    c2 = 0.29
    y = 0.0
    prev_s = 0.0 
    s = 0.0
    ds = 0.0
    arr_err = [0.0, 0.0, 0.0] 
    for i in 1:duration
        arr_err[3] = arr_err[2] 
        arr_err[2] = arr_err[1]
        arr_err[1] = abs(aim - y)
        ds = K0 * arr_err[1] + K1 * arr_err[2] + K2 * arr_err[3]
        prev_s = s
        s = prev_s + ds
        y = line_mod(y, c1, c2, s)
        push!(Yarr, y)
        push!(Sarr, s)
        println(i, ". y = ", y, "\t| s = ", s)
    end
    plot(1:duration, range(aim, aim, duration), title="PID", label="Target value",lw=3, color=:black, legend=:outerbottom)
    plot!(1:duration, Sarr, label="Control value", lw=3, color=:yellow)
    plot!(1:duration, Yarr, label="Current value", lw=3, color=:red)
end
main()