using Plots

K = 0.097   #пропорциональная составляющая
T = 2.1623  #интегральная составляющая
Td = 1.0    #дифференциальная составляющая

To = 1      #шаг

q0 = K * (1 + Td/To)           #
q1 = -K * (1 + 2Td/To - To/T)  #коэффициенты для подсчёта изменения управляющего сигнала
q2 = (K * Td)/To               #

#функция подсчёта линейной модели
function CALC_LINEAR_MODEL(y, kf_a, kf_b, u)
    y = kf_a * y + kf_b * u #формула линейной модели
    return y
end

count = 100 #количество итераций
point = 29.0 #желаемое значение
function main()
    println("START")
    arr_LinY = [] #массив текущих значений
    arr_u = []    #массив управляющих сигналов
    kf_a = 0.8 
    kf_b = 0.3
    y = 0.0
    PrevU = 0.0 
    u = 0.0
    du = 0.0
    arr_e = [0.0, 0.0, 0.0] #массив разности желаемого значения и текущего значения
    #цикл вычисления Y для линейной модели
    for i in 1:count
        arr_e[3] = arr_e[2] 
        arr_e[2] = arr_e[1]
        arr_e[1] = abs(point - y)
        du = q0 * arr_e[1] + q1 * arr_e[2] + q2 * arr_e[3] #вычисление изменения управлящего сигнала
        PrevU = u
        u = PrevU + du
        y = CALC_LINEAR_MODEL(y, kf_a, kf_b, u) #вычисление текущего значения
        push!(arr_LinY, y)     #добавляем в массив текущее значение
        push!(arr_u, u)        #добавляем в массив управляющий сигнал
        println(i, ". y = ", y, "\t| u = ", u)
    end
    plot(1:count, range(point, point, count), title="PID", label="Target value",lw=3, color=:blue, legend=:outerbottom)
    plot!(1:count, arr_u, label="Control value", lw=3, color=:red)
    plot!(1:count, arr_LinY, label="Current value", lw=3, color=:green)
end
main()