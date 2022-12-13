using Plots

function get_y_func_first()
    for i in 1 : time_c  
        global  y_func = constants_1[1] * y_func + constants_1[2] * warm_1
        push!(y_mass_1, y_func) 
    end  
end
function get_y_func_second()
    for i in 1 : time_c
        tmp = y_nonline
        global y_nonline = constants_2[1]*y_nonline - constants_2[2]*y_prev^2 + constants_2[3]*warm_1 + constants_2[4]*sin(warm_1) 
        global  y_prev = tmp
        push!(y_mass_2, y_nonline)
    end
end

function get_image()

    x = range(0, time_c, length=time_c)

    plot(x, [y_mass_1, y_mass_2])
    savefig("plot.png")
    
end

constants_1 = [0.9, 1.4]
constants_2 = [0.5, 0.4, 1, 0.7 ]
# массив выходных значений y
y_mass_2 = []
y_mass_1 = []

# предыдущий у 
y_prev = 0

y_func = 1 

warm_1 = 1
time_c = 20

get_y_func_first()

y_nonline = 1
get_y_func_second()
get_image()


