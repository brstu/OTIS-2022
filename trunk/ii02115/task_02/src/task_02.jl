function nonLinearModel()  
    K0 = 1; time=15
    alpha=0.02; beta=0.05; gamma=33.5; delta=-0.07 
    y_nonLin1=18; y_nonLin2=19
    t_nonLin1=1; t_nonLin0=0.025
    l1=0; l2=0; en=0
    Q = 12; P = 0.1; ; TD = 17
    j = 15
    for K0 in K0:time
        q0 = Q * (1 + TD/K0)
        q1 = (-Q )* (1 + 2 * TD / K0 - K0 / P)
        q2 = Q * TD / K0
        l1 = j -  y_nonLin1
        l2 = j -  y_nonLin2
        y_nonlin3=alpha * y_nonLin2 - beta * abs2(y_nonLin1)+ gamma * t_nonLin1 + delta * sin(t_nonLin0)
        y_nonLin1=y_nonLin2
        y_nonLin2=y_nonlin3
        en= j -  y_nonlin3 
        t_nonlin_n=t_nonLin1+q0*en+q1*l2+q2*l1
        l1=l2
        l2=en
        t_nonLin0=t_nonLin1
        t_nonLin1=t_nonlin_n
        println(K0,"    \t",y_nonlin3, " \t :  \t",en) 
        
    end     
end

println()
println("Нелинейная модель: \n")
nonLinearModel()

   