using Plots

function Linear_model(y_curr, u, t)
    a = 0.925
    b = 0.75
    Arr1 = []
    push!(Arr1,y_curr)
    for i in 1:t
        y_next = a * y_curr + b * u
        push!(Arr1,y_next)
        y_curr = y_next
    end
    println(Arr1)
    plot([1:(t+1)], Arr1, color = :green , label = "Linear_model")
end

function Unlinear_model(y_curr, u_curr, t)
    a = 1.37
    b = 0.0043
    c = 0.45
    d = 0.75
    y_prev = 0
    u_prev = 0
    Arr2 = []
    push!(Arr2,y_curr)
    for i in 1:t
        y_next= a * y_curr - b * y_prev^2 + c * u_curr + d * sin(u_prev)
        push!(Arr2,y_next)
        y_prev = y_curr
        y_curr = y_next
        u_prev = u_curr
        u_curr = u_curr + 0.035
    end
    println(Arr2)
    plot!([1:(t+1)], Arr2, color = :red , label = "Unlinear_model")
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
