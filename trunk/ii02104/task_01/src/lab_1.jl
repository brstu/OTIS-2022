using PyPlot
y_lin = [] # лист для хранения значений y в линейной модели
y_nonlin = [] # лист для хранения значений y в НЕлинейной модели

function nonlinear(a, b, c, d, y, y_prev, u, i, t, u_prev=0)
    if i <= t
        println(y)
        push!(y_nonlin, y)
        nonlinear(a, b, c, d,
                        a*y - b*y_prev^2 + c*u + d*sin(u_prev), y,
                        u, 
                        i + 1, t,u)
    else
        println("End.")
    end
end

function linear(a, b, y, u, i, t)
    if i <= t
        println(y)
        push!(y_lin, y)
        linear(a, b, a*y + b*u, u, i + 1, t) 
    else
        println("End.")
    end
end

function main()
    a = 0.5 # Константа
    b = 0.5 # Константа
    c = 0.5 # Константа
    d = 0.5 # Константа
    i = 1 # Начальное время
    y = 0.0 # Начальная температура
    u = 1.0 # Вводная температура
    t = 15 # Конечное время

    println("Нелинейная модель:")
    nonlinear(a, b, c, d, y, y, u, i, t,u)
    println("Линейная модель:")
    linear(a, b, y, u, i, t)
    plt.grid(true)
    plt.plot(1:t, y_lin,color="blue", label="Линейная")
    plt.plot(1:t, y_nonlin,color="green", label="Нелинейная")
    plt.ylabel("Значения y")
    plt.xlabel("Значения t")
    plt.legend(loc="lower right")
    plt.savefig("grafik1.png",dpi=300)
    #хранится в папке пользователя
    #бывает баг с дублированием  графиков при перезапуске программы 
end

main()
