using Plots
function linear_func(A, B, Y, U, t)
    Y = A * Y + B * U
    println(Y)
    return Y
end
function unlinear_func(A, B, C, D, Y, Y_l, U, U_l, t)
    Y = A * Y - B * Y_l * Y_l + C * U + D * sin(U_l)
    println(Y)
    return Y
end
function main()
    A = 0.479
    B = 0.533
    C = 0.651
    D = 0.032
    Y = 0.0
    U = 2.0
    N = 50
    println("Linear modeling")
    Y_linear = []
    Y_unlinear = []
    for t in 1:N
        Y = linear_func(A, B, Y, U, t)
        push!(Y_linear, Y)
    end
    println("\nUnlinear modeling")    
    Y_next = 0
    for t in 1:N
        Y_prev = Y
        Y = Y_next
        Y_next = unlinear_func(A, B, C, D, Y, Y_prev, U, U, t)

        push!(Y_unlinear, Y)
    end
    plot([1:N], Y_linear, color = :red , label = "Linear")
    plot!([1:N], Y_unlinear, color = :blue, label = "Unlinear")
    savefig("A.png")
end
main()