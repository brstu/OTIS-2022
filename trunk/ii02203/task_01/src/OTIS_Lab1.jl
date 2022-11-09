using Plots
function CALC_LINEAR_MODEL(y, kf_a, kf_b, u)
    y = kf_a * y + kf_b * u
    return y
end

function CALC_UNLINEAR_MODEL(y, kf_a, kf_b, PrevY, kf_c, u, kf_d, PrevU)
    y = kf_a * y - kf_b * PrevY^2 + kf_c * u + kf_d * sin(PrevU)
    return y
end

count = 45

#LINEAR MODEL
function LINEAR_M()
    arr_LinY = []
    kf_a = 0.8
    kf_b = 0.3
    y = 0.0
    u = 2.3

    for i in 1:count
        push!(arr_LinY, y)
        y = CALC_LINEAR_MODEL(y, kf_a, kf_b, u)
    end
    plot(1:count, arr_LinY, title = "Model", label = "Linear model", lw = 3, color = :green)
end

#UNLINEAR MODEL
function UNLINEAR_M()
    arr_UnLinY = []
    kf_a = 0.7
    kf_b = 0.1
    kf_c = 0.8
    kf_d = 0.5
    y = 0.0
    u = 3.0
    NextY = 0.0
    PrevY = 0.0

    for i in 1:count
        PrevY = y
        y = NextY
        NextY = CALC_UNLINEAR_MODEL(y, kf_a, kf_b, PrevY, kf_c, u, kf_d, u)
        push!(arr_UnLinY, y)
    end
    plot!(1:count, arr_UnLinY, label = "Unlinear model", lw = 3, color = :red)
end

function main()
    LINEAR_M()
    UNLINEAR_M()
end
main()