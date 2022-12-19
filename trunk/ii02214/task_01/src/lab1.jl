using Plots

function get_y_func_first()
    
    # функция для получения массива значений линейной функции y
    # для последующего построение графика с помощью библиотеки PLots
    for i in 1 : time_c  
        global  y_func = c1_first[1] * y_func + c1_first[2] * warm_1
        push!(y_mass_1, y_func) 
    end  
end

function get_y_func_second()
    # функция для получения массива значений нелинейной функции y
    # для последующего построение графика с помощью библиотеки PLots
    index = 0     
    while index < 20
        # временная переменная
        tmp = y_nonline
        global y_nonline = c2_second[1]*y_nonline - c2_second[2]*y_prev^2 + c2_second[3]*warm_1 + c2_second[4]*sin(warm_1) 
        global  y_prev = tmp
        push!(y_mass_2, y_nonline)
        index += 1
    end
end

function get_image()
    # фунция для построения графика с помощью библиотека Plots
    # строит график из массивов значений линейной и нелинейной функции
    # сохраняет картинку в текущую дирректорию
    x = range(0, time_c, length=time_c)
    plot(x, [y_mass_1, y_mass_2])
    savefig("plot.png")
end
# константные переменные для линейной функции
c1_first = [0.9, 1.4]
# констатные перменные для нелинейной функции
c2_second = [0.5, 0.4, 1, 0.7 ]
# массив выходных значений y
y_mass_2 = []
y_mass_1 = []

# предыдущий у 
y_prev = 0

y_func = 1 

warm_1 = 1
time_c = 20

function main()
    # функция main для вызова всех функций
    get_y_func_first()

    y_nonline = 1
    get_y_func_second()
    get_image()    
end




