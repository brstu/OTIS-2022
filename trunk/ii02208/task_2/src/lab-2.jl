using Plots

k = 0.083
td = 0.99
t = 2
t0 = 1

Q0 = k * (1 + td/t0)
Q1 = -k * (1 + 2td/t0 - t0/t)
Q2 = (k * td)/t0

function Linear_Model(Y, koeff_a, koeff_b, U)
    Y = koeff_a * Y + koeff_b * U
    return Y
end

N = 60
n = 19.0
function main()
    ARR_linY = []
    ARR_U = []
    koeff_a = 0.78
    koeff_b = 0.42
    Y = 0.0
    previous_U = 0.0 
    U = 0.0
    delta_U = 0.0
    ARR_e = [0.0, 0.0, 0.0]

    for i in 1:N
        ARR_e[3] = ARR_e[2] 
        ARR_e[2] = ARR_e[1]
        ARR_e[1] = abs(n - Y)
        delta_U = Q0 * ARR_e[1] + Q1 * ARR_e[2] + Q2 * ARR_e[3]
        previous_U = U
        U = previous_U + delta_U
        Y = Linear_Model(Y, koeff_a, koeff_b, U)
        push!(ARR_linY, Y)
        push!(ARR_U, U)
        println(i, ". Y = ", Y, "\t U = ", U)
    end
    plot(1:N, range(n, n, N), label = "Setting", lw = 3, color = :blue, legend = :outerbottom)
    plot!(1:N, ARR_U, label = "Control Value", lw=3, color=:red)
    plot!(1:N, ARR_linY, label = "Current Value", lw = 3, color = :green)
    savefig("LAB-2.png")
end
main()
