using Plots
kp = 0.1
ki = 2.0 #PID кооф.
kd = 1.02
dt = 1  
K0 = kp * (1 + kd/dt)           
K1 = -kp * (1 + 2kd/dt - dt/ki)  
K2 = (kp * kd)/dt               
function fanc(f, c1, c2, s)
    f = c1 * f + c2 * s
    return f
end
duration = 100
aim = 20
function main()
    Yarr = [] 
    Sarr = [] 
    c1 = 0.73
    c2 = 0.29
    f = 0.0
    prev_s = 0.0 
    s = 0.0
    ds = 0.0
    errs = [0.0, 0.0, 0.0] 
    for i in 1:duration
        errs[3] = errs[2] 
        errs[2] = errs[1]
        errs[1] = abs(aim - f)
        ds = K0 * errs[1] + K1 * errs[2] + K2 * errs[3]
        prev_s = s
        s = prev_s + ds
        f = fanc(f, c1, c2, s)
        push!(Yarr, f)
        push!(Sarr, s)
        println(i, ". f = ", f, "\t| s = ", s)
    end
    plot(1:duration, range(aim, aim, duration), title="PID", label="Target value",lw=3, color=:black, legend=:outerbottom)
    plot!(1:duration, Sarr, label="Control value", lw=3, color=:yellow)
    plot!(1:duration, Yarr, label="Current value", lw=3, color=:red)
end
main()