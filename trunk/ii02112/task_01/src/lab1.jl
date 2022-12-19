using Printf
using Plots

#массивы для хранения значений
linY = []
nolinY = []

#функция для линейной/нелинейной модели
function line(const1,const2,const3,y,time)
    i = 1
    x=1:time
    linY=[]
    while i <= time
        push!(linY,y)
        println(y)
        y = const1*y + const2*const3
        i += 1
    end
    plot(x,linY,label="Line",legend=:bottomright)
end

function noline(const1,const2,const4,const5,y,const3,time)
    i = 1
    x=1:time
    nolinY=[]
    while i <= time
        println(y)
        y=const1*y - const2*y^2 + const4*const3 + const5*sin(const3)
        push!(nolinY,y)
        i += 1
    end
    plot!(x,nolinY,label="Not line",legend=:bottomright)
end

#Значения
const1=0.6
const2=0.7
const3=0.6
const4=1.1
const5=0.9
time=30
y=0.0

#вывод
@printf("Значения линейной модели за %d секунд: ",time)
line(const1,const2,const3,y,time)
println(" ")
@printf("Значения нелинейной модели за %d секунд: ",time)
noline(const1,const2,const4,const5,y,const3,time)