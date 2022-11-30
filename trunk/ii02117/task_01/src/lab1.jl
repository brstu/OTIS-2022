using PyPlot
function lineral_model(time,weigth)
    warm=1
    y=1
    result=[]
    for i in 1:time
	y=weigth[1]*y+weigth[2]*warm
	push!(result,y)
    end
    return result
end
function nonlineral_model(time,weigth)
    previous_y=0
    current_y=1
    start_warm=1
    result=[]
    for i in 1:time
	future_y=weigth[1]*current_y-weigth[2]*previous_y^2+weigth[3]*start_warm+weigth[4]*sin(start_warm)
	previous_y=current_y
	current_y=future_y
	push!(result,current_y)
    end
    return result
end
function main()
    weigth_for_lineral=[1,2]
    weigth_for_nonlineral=[0.8,0.09,1,10.1]
    x_line=[i for i in 1:50]
    lineral_result=lineral_model(50,weigth_for_lineral)
    nonlinreal_result=nonlineral_model(50,weigth_for_nonlineral)
    println("Линейная модель ")
    for i in lineral_result
	println(i)
    end
    println("Нелинейная модель ")
    for i in nonlinreal_result
	println(i)
    end
    plot(x_line,lineral_result,color="red",label="lineral")
    plot(x_line,nonlinreal_result,color="blue",label="non_lineral")
end
main()
