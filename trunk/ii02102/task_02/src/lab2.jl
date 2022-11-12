function nolin()
    step = 1; time = 10 # шаг; время работы
    a = -0.5; b = 0.3; c = 0.2; d = 0.4 # Постоянные с первой лаб. работы
    ynonlin1 = 5; ynonlin2 = 6
    unonlin1 = 1; unonlin2 = 0.05
    e3=0.0
    K = 10 # - коэффициент передачи
    T = 0.1 # - постоянная интегрирования,
    TD = 40 # - постоянная дифференцирования
    enval = 200.01# желаемое значение
    for step in step:0.5:time
        q1 = K * (1 + TD/step)
        q2 = (-K )* (1 + 2 * TD / step - step / T)
        q3 = K * TD / step
        e1 = enval -  ynonlin1 # - отклонение выходной переменной
        e2 = enval -  ynonlin2
        square=ynonlin1*ynonlin1
        ynonlin3= a* ynonlin2 - b * square + c * unonlin2 + d * sin(unonlin1)  
        parse(Float64,ynonlin1) = ynonlin2
        parse(Float64,ynonlin2) = ynonlin3
        unonlin1=unonlin2
        unonlin2=unonlin1+q1*e3+q2*e2+q3*e1
        e3= enval -  parse(Float64,ynonlin3)
        e1=e2
        e2=e3
        #println(step,"\t",ynonlin3,"\t",e3)
        println(float(ynonlin3)," \t", e3)
    end
end
    
function main() 
    println("\tНелинейная модель")
    println("Step\t\ty\t\t  rejection")
    nolin()
end
main()