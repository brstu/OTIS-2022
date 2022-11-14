using Plots

value_u_t = 0.5 # input warm
time = 15 # time
this_is_a_constant_a = 1.2  # constant
this_is_a_constant_b = 0.7  # constant
this_is_a_constant_c = -0.32  # constant
this_is_a_constant_d = 0.53 # constant

arr_yt_linear = []  #array for linear dependency
arr_yt_not_linear = [] #array for non-linear dependency

#function for linear dependence
function f1()
    println("linear model")
    _y_t_ = 1 # input temperature
    for i in 1 : time
        _y_t_ = this_is_a_constant_a * yt + this_is_a_constant_b * value_u_t
        println(_y_t_)
        push!(arr_yt_linear, _y_t_)
    end
end

#function for non-linear dependence
function f2()
    _y_t_ = 1.5 # input temperature
    yt_previous = 0 # input temperature
    println("non-linear model")
    for i in 1 : time
        temperature = yt_previous
        _y_t_ = this_is_a_constant_a * _y_t_ - this_is_a_constant_b * yt_previous ^ 2 + this_is_a_constant_c * value_u_t + this_is_a_constant_d * sin(value_u_t)
        yt_previous = temperature
        println(yt)
        push!(arr_yt_not_linear, _y_t_)
    end
end

f1()
f2()
this_is_a_value_x = 1 : time
plot(this_is_a_value_x,arr_yt_linear, title = "Temperature dependence",  label = "linear dependence",  lw = 3)
plot!(this_is_a_value_x,arr_yt_not_linear, label = "non-linear dependence",  lw = 3)