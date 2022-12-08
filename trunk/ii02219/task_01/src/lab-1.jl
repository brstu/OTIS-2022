
using Plots
constants = [1,0.09,1,3]
y_linear = 0
y_nonlinear_last = 0
y_current = 1
y_nonlinear  = []
warm = 1
time = 35
func = constants[1]*y_linear + constants[2] * warm
y_linear = range(func,step = func,length=time)
for i in 1 : time
    tmp = y_current
   global  y_current = constants[1] * y_current - constants[2] * y_nonlinear_last^2 + constants[3]*warm + constants[4] * sin(warm) 
   global y_nonlinear_last = tmp
   println(y_current)
   
   push!(y_nonlinear,y_current)
end
x = range(0,time,length=time)
plot(x,[y_linear,y_nonlinear],label = ["linear" "nonlinear"])
savefig("plot.png")