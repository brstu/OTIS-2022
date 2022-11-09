using Plots

function Linear_model(y_curr, u, t)
    a = 0.8
    b = 0.3
    Arr = []
    push!(Arr,y_curr)
    for i in 1:t
        y_next = a * y_curr + b * u
        push!(Arr,y_next)
        y_curr = y_next
    end
    println(Arr)
    plot([1:(t+1)], Arr, color = :orange , label = "Linear_model")
end

function Unlinear_model(y_curr, u_curr, t)
    a = 1
    b = 1
    c = 1
    d = 1
    y_prev = 0
    u_prev = 0
    Arr = []
    push!(Arr,y_curr)
    for i in 1:t
        y_next= a * y_curr - b * y_prev^2 + c * u_curr + d * sin(u_prev)
        push!(Arr,y_next)
        y_prev = y_curr
        y_curr = y_next
        u_prev = u_curr
        u_curr = u_curr - 1
    end
    println(Arr)
    plot([1:(t+1)], Arr, color = :blue , label = "Unlinear_model")
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
    start_temp = getInt()                    # the initial temperature value is equal to the ambient temperature
    println("Enter warm input value: ")
    warm = getInt()                          # warm input value of the corresponding simulation object
    println("Enter process duration: ")
    duration = getInt()
    Linear_model(start_temp, warm, duration)
    Unlinear_model(start_temp, warm, duration)
end

main()
