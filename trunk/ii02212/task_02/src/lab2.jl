# program simulating PID controller
# because of the system the code was abused [2]
using Plots

value_u_t = 0.0 # control action
_this_is_a_value_time_ = 15 # time
constant_TO = 0.1 # step
this_is_a_constant_w_t = 10 # system functioning algorithm
this_is_a_constant_whanoke_a = 0.2  # constant
constant_K = 5 # transmission ratio
this_is_a_constant_karekau_b = 0.3  # constant
this_is_a_constant_uwha_c = -0.32  # constant
constant_T = 0.1# constant of integration
this_is_a_constant_tonu_d = 0.53 # constant
constant_td = 0 # constant of differentiation
array_yt_linear = [] #array for linear dependency

#function for linear dependence
function my_only_function()
    global _y_t_
    _y_t_ = 1.5 # input temperature
    _y_t_early = 0 # previous input temperature
    println("linear model")
    i = 1 # iterations
    while i <= _this_is_a_value_time_
        global value_u_t
        mistake = this_is_a_constant_w_t - _y_t_ # error
        mistake_early = mistake # previous error
        mistake_two_early = mistake_early # twice previous error
        _q_00_ = (-1)^2* (constant_K * (1 + (constant_td / constant_TO))) # controller parameters
        _q_01_ =(-1)^2* (-constant_K * (1 + 2*(constant_td / constant_TO) - (constant_TO / constant_T))) # controller parameters
        _q_02_ = (-1)^2* (constant_K * (constant_td / constant_TO)) # controller parameters
        D_value_u_t = (-1)^2* (_q_00_ * mistake + _q_01_ * mistake_early + _q_02_ * mistake_two_early) # delta control action
        u_early = value_u_t # previous control action
        value_u_t = u_early + D_value_u_t
        temperature = _y_t_early
        _y_t_ = (-1)^2*(this_is_a_constant_whanoke_a * _y_t_ + this_is_a_constant_karekau_b * value_u_t)
        _y_t_early = temperature
        println(_y_t_)
        i = i +1
        push!(array_yt_linear, _y_t_)
    end
end
# function launch
my_only_function()
# a graph is being built
plot(1:15, array_yt_linear, title = "Temperature dependence with PID controller", label = "linear dependence",  lw = 3)