using Plots

ut = 0.5 # input warm
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
    yt = 1 # input temperature
    for i in 1 : time
        yt = this_is_a_constant_a * yt + this_is_a_constant_b * ut
        println(yt)
        push!(arr_yt_linear, yt)
    end
end

#function for non-linear dependence
function f2()
    yt = 1.5 # input temperature
    yt_prev = 0 # input temperature
    println("non-linear model")
    for i in 1 : time
        temp = yt_prev
        yt = this_is_a_constant_a * yt - this_is_a_constant_b * yt_prev ^ 2 + this_is_a_constant_c * ut + this_is_a_constant_d * sin(ut)
        yt_previous = temp
        println(yt)
        push!(arr_yt_not_linear, yt)
    end
end

f1()
f2()
x = 1 : time
plot(x,arr_yt_linear, title = "Temperature dependence",  label = "linear dependence",  lw = 3)
plot!(x,arr_yt_not_linear, label = "non-linear dependence",  lw = 3)