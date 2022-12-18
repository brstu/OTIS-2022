# program simulating PID controller
using Plots

u = 0.0 # control action
_this_is_a_value_time_ = 15 # time
constant_To = 0.1 # step
constant_w_t = 10 # system functioning algorithm
constant_a = 0.2  # constant
constant_K = 5 # transmission ratio
constant_b = 0.3  # constant
constant_c = -0.32  # constant
constant_T = 0.1# constant of integration
constant_d = 0.53 # constant
constant_td = 0 # constant of differentiation
array_yt_linear = [] #array for linear dependency

#function for linear dependence
function f()
    global yt
    yt = 1.5 # input temperature
    yt_prev = 0 # input temperature
    println("linear model")
    for i in 1 : 15
        global u
        err = constant_w_t - yt # error
        e_early = err # previous error
        e_2early = e_early # twice previous error
        q_0 = constant_K * (1 + (constant_td / constant_To))
        q_1 = -constant_K * (1 + 2*(constant_td / constant_To) - (constant_To / constant_T))
        q_2 = constant_K * (constant_td / constant_To)
        D_u = q_0 * err + q_1 * e_early + q_2 * e_2early 
        u_early = u
        u = u_early + D_u
        temp = yt_prev
        yt = constant_a * yt + constant_b * u
        yt_prev = temp
        println(yt)
        push!(array_yt_linear, yt)
    end
end

f()
plot(1:15, array_yt_linear, title = "Temperature dependence with PID controller", label = "linear dependence",  lw = 3)