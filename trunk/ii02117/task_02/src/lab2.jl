using Plots
using LinearAlgebra
function nonlineral_model(param,time,start_warm=1,desired_temp=100)
    result=[]
    array_of_e=[0.001,0.19,0.00002]
    array_of_q=[0.4,0.1,0.12]
    weigth=[1,0,1,1.0]
    prev_u=weigth[3]
    # e(t) = w(t) - y(t) 
    # - отклонение выходной переменной y(t) от желаемого значения w(t).
    for i in 1:time
        
        param[4]=sin(param[3])
        future_y=weigth[1]*param[1]-weigth[2]*param[2]^2+weigth[3]*param[3]+weigth[4]*param[4]
        param[2]=param[1]
        param[1]=future_y
        array_of_e[3]=desired_temp-future_y
        future_y=weigth[1]*param[1]-weigth[2]*param[2]^2+weigth[3]*param[3]+weigth[4]*param[4]
        param[2]=param[1]
        param[1]=future_y
        array_of_e[2]=desired_temp-future_y
        weigth[3]=prev_u+dot(array_of_q,array_of_e)
        future_y=weigth[1]*param[1]-weigth[2]*param[2]^2+weigth[3]*param[3]+weigth[4]*param[4]
        param[2]=param[1]
        param[1]=future_y
        array_of_e[1]=desired_temp-future_y
        push!(result,param[1])
    end
    return result
end
function main()
    size=200
    param=[1,0,1,1.0]
    y=nonlineral_model(param,size)
    for i in y
        println(i)
    end 
    x=[i for i in 1:size]
    a=plot(x,y,color="red",label="pid")


end
main()
