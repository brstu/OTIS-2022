function main()
    a = 0.5
    b = 0.5
    c = 0.1  
    d = 0.5
    y = 0.0
    u = 1.0
    i = 0
    t = 10
    println("Линейная модель:")
    line_model(a, b, y, u, i, t)
    println("Нелинейная модель:")
    noline_model(a, b, c, d, y, y, u, u, i, t)
end
function line_model(a, b, y, u, i, t)
    if i <= t
        println(y)
        line_model(a, b, a*y + b*u, u, i + 1, t)
    else
        println("-------------------")
    end
end
function noline_model(a, b, c, d, y, y_1, u, u_1, i, t)
    if i == 1
        println(y)
        noline_model(a, b, c, d, a*y - b*y_1^2 + c*0 + d*sin(0), y, u, u, i + 1, t)
    elseif i <= t
        println(y)
        noline_model(a, b, c, d,
                        a*y - b*y_1^2 + c*u + d*sin(u_1), y, u, u, i + 1, t)
    else
        println("-------------------")
    end
end
main()