using Plots

function noLin(alpha, beta, gamma, delta, f, w, k)
    x = 1:k
    alpharr_y1=[]
    println("noLin")
    for i in x
        println(f)
        f = alpha * f - beta * f^2 + gamma * w + delta * sin(w)
        push!(alpharr_y1, f)
    end
    plot!(x, alpharr_y1, label="noLin")
end

function lin(alpha, beta, w, f, k)
    x = 1:k
    alpharr_y = []
    for i in x
        push!(alpharr_y, f)
        println(f)
        f = alpha * f + beta * w
    end
    plot(x, alpharr_y, label="liner_model")

end

function main()
    alpha = 0.5
beta = 0.6
gamma = 0.7
delta = 0.8
k = 20
f = 0.0
w = 1.0

lin(alpha, beta, w, f, k)
noLin(alpha, beta, gamma, delta, f, w, k)
end

main()