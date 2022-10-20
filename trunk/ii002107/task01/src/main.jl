using Plots

function lin_model(a,b,u,y,t)
    x=1:t
    arr_y=[]
    for i in 1:t
        push!(arr_y,y)
        println(y)
        y = a*y + b*u
    end
    plot(x,arr_y,label="liner_model")

end
function not_liner_model(a,b,c,d,y,u,t)
    x=1:t
    arr_y1=[]
    println("not_liner_model")
    for i in 1:t
        println(y)
        y=a*y - b*y^2 + c*u + d*sin(u)
        push!(arr_y1,y)
    end
    plot!(x,arr_y1,label="not_liner_model")
end


a=0.5
b=0.6
c=0.7
d=0.8
t=20
y=0.0
u=1.0


lin_model(a,b,u,y,t)
not_liner_model(a,b,c,d,y,u,t)