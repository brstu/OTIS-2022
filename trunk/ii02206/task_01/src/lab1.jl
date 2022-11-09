using Plots

function linear(a, b, y, u, t)
    y = a * y + b * u
    println(y)
    return y
end

function unlinear(a, b, c, d, y, y_last, u, u_last, t)
    y = a * y - b * y_last * y_last + c * u + d * sin(u_last)
    println(y)
    return y
end

function main()
    a = 0.5
    b = 0.4
    c = 0.7
    d = 0.02
    y = 0.0
    u = 1.0
    n = 30
    println("Linear modeling")
    y_linear = []
    y_unlinear = []
    for t in 1:n
        y = linear(a, b, y, u, t)
        push!(y_linear, y)
    end
    println("\nUnlinear model")    
    y_next = 0
    for t in 1:n
        y_prev = y
        y = y_next
        y_next = unlinear(a, b, c, d, y, y_prev, u, u, t)

        push!(y_unlinear, y)
    end
    
    plot([1:n], y_linear, color = :green , label = "linear")
    plot!([1:n], y_unlinear, color = :red, label = "unlinear")
end
plot([1:10],[1:10])
main()
