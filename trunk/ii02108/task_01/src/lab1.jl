a = 0.5
b = 0.5
c = 0.1
d = 0.5
u = 1.0
y = 0.0

println("Линейная модель")
function linear(y, n, t)
    if n < t
        println(y)
        return linear(a * y + b * u, n+1, t)
    end
    println(y)
    return a * y + b * u
end
println(linear(y, 0, 10))

println("----------------------")

println("Нелинейная модель")
function nonlinear_model(y, y_prev, u, u_prev, i, t)
    if i == 1
        println(y)
        return nonlinear_model(a*y - b*y_prev^2 + c*1 + d*sin(1), y, u, u, i + 1, t)
    elseif i < t
        println(y)
        return nonlinear_model(a*y - b*y_prev^2 + c*u + d*sin(u_prev), y, u, u, i + 1, t)
    end
    println(y)
    return a*y - b*y_prev^2 + c*u + d*sin(u_prev)
end

println(nonlinear_model(y, y, u, u, 0, 10))