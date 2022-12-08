using Plots
function first_function(a, b, f, u)
    f = a * f + b * u
    println(f)
    return f
end
function second_function(a, b, c, d, f, f_p, u, u_p)
    f = a * f - b * f_p * f_p + c * u + d * sin(u_p)
    println(f)
    return f
end
function main()
    a = 0.722
    b = 0.421
    c = 0.587
    d = 0.035
    f = 0.0
    u = 1.0
    n = 100
    println("Linear modeling")
    f_linear = []
    f_unlinear = []
    for t in 1:n
        f = first_function(a, b, f, u)
        push!(f_linear, f)
    end
    println("\nUnlinear model")    
    f_n = 0
    for t in 1:n
        f_prev = f
        f = f_n
        f_n = second_function(a, b, c, d, f, f_prev, u, u)
        push!(f_unlinear, f)
    end
    plot([1:n], f_linear, color = :green , label = "linear")
    plot!([1:n], f_unlinear, color = :blue, label = "unlinear")
end
main()