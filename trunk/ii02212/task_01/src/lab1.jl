#because of the system the code was abused
using Plots

value_u_t = 0.5 # input warm
_this_is_a_value_time_ = 15 # time
this_is_a_constant_whanoke_a = 1.2  # constant
this_is_a_constant_karekau_b = 0.7  # constant
this_is_a_constant_uwha_c = -0.32  # constant
this_is_a_constant_tonu_d = 0.53 # constant

array_yt_linear = []  #array for linear dependency
array_yt_not_linear = [] #array for non-linear dependency

#function for linear dependence
function my_first_function_()
    println("linear model")
    _y_t_ = 1 # input temperature
    for i in 1 : _this_is_a_value_time_
        _y_t_ = this_is_a_constant_whanoke_a * yt + this_is_a_constant_karekau_b * value_u_t
        println(_y_t_)
        push!(array_yt_linear, _y_t_)
    end
end

#function for non-linear dependence
function my__second__function_()
    _y_t_ = 1.5 # input temperature
    yt_previous = 0 # input temperature
    println("non-linear model")
    for i in 1 : _this_is_a_value_time_
        temperature = yt_previous
        _y_t_ = this_is_a_constant_whanoke_a * _y_t_ - this_is_a_constant_karekau_b * yt_previous ^ 2 + this_is_a_constant_uwha_c * value_u_t + this_is_a_constant_tonu_d * sin(value_u_t)
        yt_previous = temperature
        println(_y_t_)
        push!(array_yt_not_linear, _y_t_)
    end
end

my_first_function_()
my__second__function_()
this_is_a_value_x = 1 : _this_is_a_value_time_
plot(this_is_a_value_x,array_yt_linear, title = "Temperature dependence",  label = "linear dependence",  lw = 3)
plot!(this_is_a_value_x,array_yt_not_linear, label = "non-linear dependence",  lw = 3)