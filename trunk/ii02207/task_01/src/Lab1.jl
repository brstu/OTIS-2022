using Plots
#расчёт линейной модели
function ToCalculateLinear(y, koef_A, koef_B, u)
    y = koef_A * y + koef_B * u
    return y
end

#расчёт нелинейной модели
function ToCalculateUnlinear(y, koef_A, koef_B, YPrev, koef_C, u, koef_D, UPrev)
    y = koef_A * y - koef_B * YPrev^2 + koef_C * u + koef_D * sin(UPrev)
    return y
end

#количество итераций
quantity = 50 

function main()
    LinY = []
    koef_A = 0.8
    koef_B = 1.5
    y = 0.0
    u = 3.3
    #Y линейная модель
    for i = 1:quantity
        push!(LinY, y)
        y = ToCalculateLinear(y, koef_A, koef_B, u)
    end
    plot(1:quantity, LinY, title = "Model", label = "Linear", lw = 2, color = :blue)

    #UNLINEAR
    UnLinY = []
    koef_A = 0.75
    koef_B = 0.1
    koef_C = 2.2
    koef_D = 8.5
    y = 0.0
    u = 0.3
    #Y нелинейная модель
    Ynext = 0.0
    Yprev = 0.0
    for i = 1:quantity
        Yprev = y
        y = Ynext
        Ynext = ToCalculateUnlinear(y, koef_A, koef_B, Yprev, koef_C, u, koef_D, u)
        push!(UnLinY, Ynext)
    end
    plot!(1:quantity, UnLinY, label = "Unlinear", lw = 2, color = :black)
end
main()