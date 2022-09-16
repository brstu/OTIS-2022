function linear_model(a, b, y, u, i, t)
    if i <= t
        println(y)
        linear_model(a, b, a*y + b*u, u, i + 1, t)
    else
        println("OFF")
    end
end

function nonlinear_model(a, b, c, d, y, y_prev, u, u_prev, i, t)
    if i == 1
        println(y)
        nonlinear_model(a, b, c, d, 
                        a*y - b*y_prev^2 + c*0 + d*sin(0), y, 
                        u, u, 
                        i + 1, t)
    elseif i <= t
        println(y)
        nonlinear_model(a, b, c, d,
                        a*y - b*y_prev^2 + c*u + d*sin(u_prev), y,
                        u, u, 
                        i + 1, t)
    else
        println("OFF")
    end
end

function main()
    a = 0.5
    b = 0.5
    c = 0.5
    d = 0.5
    y = 0.0
    u = 1.0
    i = 0
    t = 10
    println("Linear Model")
    linear_model(a, b, y, u, i, t)
    println("Nonlinear Model")
    nonlinear_model(a, b, c, d, y, y, u, u, i, t)

end

main()