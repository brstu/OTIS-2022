using PyPlot
function nonlinear(Times=10,y_start=2.28,w=25,InputTemperature=1,ConstA=0.5,ConstB=0.5,ConstC=0.5,ConstD=0.5,TransmissionRatio_K=1,T_Step=0.5,T_Diff=1,T_Integral=1)
	RegulatorQ0 =  TransmissionRatio_K * (1+ T_Diff / T_Step )  
	RegulatorQ1 = -TransmissionRatio_K * (1+ 2* T_Diff / T_Step -T_Step / T_Integral)
	RegulatorQ2 =  TransmissionRatio_K * T_Diff / T_Step
	y = [y_start]
	InputTemperature_prev = InputTemperature
	e = [w - y_start, w - y_start]
	for i in 1:Times
		push!(e, w - y[end])
		InputTemperature = InputTemperature_prev + RegulatorQ0 * e[end] + RegulatorQ1 * e[end - 1] + RegulatorQ2 * e[end - 2]
		if(length(y)==1)
			push!(y,ConstA * y[end] - ConstB * y[end] + ConstC * InputTemperature + ConstD * sin(InputTemperature_prev))
		else
			push!(y,ConstA * y[end] - ConstB * y[end-1] + ConstC * InputTemperature + ConstD * sin(InputTemperature_prev))
		end
		InputTemperature_prev = InputTemperature
	end
	println("Нелинейная модель:")
	for i in y
		println(i)
	end
	return y
end

function main()
InputTemperature=1.5
ConstA = 0.6
ConstB = 0.5
ConstC = 0.7
ConstD = 0.4
TransmissionRatio_K = 0.9
T_Step = 1.3
T_Diff = 1.2
T_Integral = 1
y_start = 5.67
w=40
plt.grid(true)
plt.ylabel("Значения y")
plt.xlabel("Номер итерации")

y=nonlinear(10,y_start,w,InputTemperature,ConstA,ConstB,ConstC,ConstD,TransmissionRatio_K,T_Step,T_Diff,T_Integral)
plt.plot(1:length(y),y,color="Blue", label="Нелинейная #1")
y=nonlinear(10,y_start,w,InputTemperature,ConstA,ConstB,ConstC,ConstD,1.0,1.5,0.9,1.1)
plt.plot(1:length(y),y,color="Green", label="Нелинейная #2")
y=nonlinear(10,y_start,w,InputTemperature,ConstA,ConstB,ConstC,ConstD,0.5,1.5,0.7,1.3)
plt.plot(1:length(y),y,color="Red", label="Нелинейная #3")
plt.legend(loc="lower right")
plt.savefig("grafik1.png",dpi=300)
end
main()