using Plots


#функция подсчёта линейной модели
function LinearModel(current_y, C, D, u)
    current_y = C * current_y + D * u #формула линейной модели
    return current_y
end

time = 100 #количество итераций
w = 50.0 #желаемое значение
function main()
    K = 0.09   #пропорциональная составляющая
    T = 2  #интегральная составляющая
    TD = 1.0    #дифференциальная составляющая

    To = 1      #шаг

    q0 = K * (1 + TD/To)           #
    q1 = -K * (1 + 2TD/To - To/T)  #коэффициенты для подсчёта изменения управляющего сигнала
    q2 = (K * TD)/To               #

    println("START")
    MASS_Y = [] #массив текущих значений
    MASS_U = []    #массив управляющих сигналов
    C = 0.8
    D = 0.3
    current_y = 0.0
    U = 0.0
    MASS_E = [0.0, 0.0, 0.0] #массив разности желаемого значения и текущего значения
    #цикл вычисления Y для линейной модели
    for i in 1:time
        MASS_E[3] = MASS_E[2] 
        MASS_E[2] = MASS_E[1]
        MASS_E[1] = w - current_y
        U = U + q0 * MASS_E[1] + q1 * MASS_E[2] + q2 * MASS_E[3]
        current_y = LinearModel(current_y, C, D, U) #вычисление текущего значения y
        push!(MASS_Y, current_y)     #добавляем в массив текущее значение
        push!(MASS_U, U)  
        println(i, ". y = ", current_y, "\t| u = ", U)
    end
    plot(1:time, range(w, w, time), label="Target",lw=3, color=:blue, legend=:outerbottom)
    plot!(1:time, MASS_U, label="Control",  color=:red)
    plot!(1:time, MASS_Y, label="Current",  color=:green)
    savefig("PID.png")
end
main()