A = 0.5
B = 0.5
C = 0.1
D = 0.5
U = 1.0
Y = 0.0


function линейная_модель(Y, N, T)
    if N < T
        println(Y)
        return линейная_модель(A * Y + B * U, N+1, T)
    end
    println(Y)
    return A * Y + B * U
end
println(линейная_модель(Y, 0, 10))

println("----------------------")


function нелинейная_модель(Y, Y_pre, U, U_pre, I, T)
    if I == 1
        println(Y)
        return нелинейная_модель(A*Y - B*Y_pre^2 + C*1 + D*sin(1), Y, U, U, I + 1, T)
    elseif I < T
        println(Y)
        return нелинейная_модель(A*Y - B*Y_pre^2 + C*U + D*sin(U_pre), Y, U, U, I + 1, T)
    end
    println(Y)
    return A*Y - B*Y_pre^2 + C*U + D*sin(U_pre)
end

println(нелинейная_модель(Y, Y, U, U, 0, 10))