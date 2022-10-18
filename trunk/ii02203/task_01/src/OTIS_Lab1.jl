using Plots
function LINEAR(y, a, b, u)
    y = a * y + b * u
    return y
end

function UNLINEAR(y, a, b, PrevY, c, u, d, PrevU)
    y = a * y - b * PrevY^2 + c * u + d * sin(PrevU)
    return y
end

function main()
    a = 0.8
    b = 0.3
    y = 0
    u = 1.8

    n = 45
    #LINEAR MODEL
    LinY = []

    for i in 1:n 
        y = LINEAR(y, a, b, u)
        push!(LinY, y)
    end

    #UNLINEAR MODEL
    UnLinY = []
    a = 0.7
    b = 0.1
    c = 0.8
    d = 0.5
    y = 0.0
    u = 3
    NextY = 0
    PrevY = 0.0
    for i in 1:n
        PrevY = y
        y = NextY
        NextY = UNLINEAR(y, a, b, PrevY, c, u, d, u)
        push!(UnLinY, y)
    end

    plot(1:n, LinY, title = "Model", label = "Linear", lw = 3, color = :green)
    plot!(1:n, UnLinY, label = "Unlinear", lw = 3, color = :red)
end
main()