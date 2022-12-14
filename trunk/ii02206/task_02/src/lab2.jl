using Plots

function main()
    # pid setups
    kp = 10
    ki = 1
    kd = 2
    t = 0
    dt = 1
    T = 10
    setpoint = 500
    in = 0
    prevErr = 0

    # models setups
    a = 0.5
    b = 0.04
    
    outs = []
    results = []
    times = []
    setpoints = []
    while T >= t


        # count pid coefficients
        err = setpoint - in 
        out = ki * err + ki * err * dt + kd * (err-prevErr) / dt 
        prevErr = err
        #write data in arrays to draw a graph
        push!(results,in)
        push!(times,t)
        push!(outs,out)
        push!(setpoints,setpoint)
        
        in = a * in + b * out
        t += dt
    end
    println(results)

    plot(times, results, color = :green, label = "results")
    plot(times, outs, color = :red, label = "setup signal")
    #plot!(times, setpoints, color = :blue, label = "setup signal")
end

main()