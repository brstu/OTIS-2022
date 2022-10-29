using Plots

yt = 1 # input temperature
ut = 9 # input warm
t = 15 # time
a = 5  # constant
b = 6  # constant
c = 8  # constant
d = 11 # constant
i = 1  # iteratio

arr_yt_lin = []  #array for linear dependency
arr_yt_not_lin = [] #array for non-linear dependency

#function for linear dependence
function f1()
    println("linear model")
    x = 1 : t # graph variable
    for i in i:t
        println(yt)
        push!(arr_yt_lin, yt)
        global yt = a * yt + b * ut
    end
    plot!(x,arr_yt_lin, title = "Temperature dependence",  label = "linear dependence",  lw = 3)
end

#function for non-linear dependence
function f2()
    x = 1 : t
    println("non-linear model")
    for i in i:t
        println(yt)
        push!(arr_yt_lin, yt)
        global yt = a*yt - b*y^2 + c*ut + d*sin(ut)
    end
    plot!(x,arr_yt_not_lin, label = "non-linear dependence",  lw = 3)
    
end

f1()
f2()
