a = 0.25; b = 0.25; c = 0.1; d = 0.25; u = 1.0; y = 0.0
println("|-------------------------------|")
println("        Линейная модель")
println("        ===============")
function linear_mod(y, n, t)
    if n < t
        println(y)
        return linear_mod(a * y + b * u, n+1, t)
    end
    println(y)
    return a * y + b * u
end
println(linear_mod(y, 0, 10))
println("|-------------------------------|")
println("         Нелинейная модель")
println("         =================")
function not_linear_mod(y, y_input_temperature, u, u_input_warm, i, t)
    if i == 1
        println(y)
        return not_linear_mod(a*y - b*y_input_temperature^2 + c*1 + d*sin(1), y, u, u, i + 1, t)
    elseif i < t
        println(y)
        return not_linear_mod(a*y - b*y_input_temperature^2 + c*u + d*sin(u_input_warm), y, u, u, i + 1, t)
    end
    println(y)
    return a*y - b*y_input_temperature^2 + c*u + d*sin(u_input_warm)
end
println(not_linear_mod(y, y, u, u, 0, 10))
println("|-------------------------------|")
return 0


