function nonlin()   # Нелинейная модель   
    T0 = 1; time=10 # время и шаг
    a=0.01; b=0.07; c=30.5; d=-0.09 # константы
    y_nonlin1=15; y_nonlin2=16
    u_nonlin1=1; u_nonlin0=0.025
    e1=0; e2=0; en=0 # начальное значение отклонения выходной переменной
    K = 10; T = 0.1; ; TD = 14 # постоянные
    w = 13 # желаемое значение
    for T0 in T0:time
        q0 = K * (1 + TD/T0)
        q1 = (-K )* (1 + 2 * TD / T0 - T0 / T)
        q2 = K * TD / T0
        e1 = w -  y_nonlin1
        e2 = w -  y_nonlin2
        y_nonlin3=a * y_nonlin2 - b * abs2(y_nonlin1)+ c * u_nonlin1 + d * sin(u_nonlin0)# формула нелинейной модели
        y_nonlin1=y_nonlin2 # переинициализация
        y_nonlin2=y_nonlin3
        en= w -  y_nonlin3 
        u_nonlin_n=u_nonlin1+q0*en+q1*e2+q2*e1
        e1=e2 # переинициализация
        e2=en
        u_nonlin0=u_nonlin1
        u_nonlin1=u_nonlin_n
        println(T0,"    \t",y_nonlin3, " \t :  \t",en) # вывод значений   
        
    end     
end
function main() 
    println()
    println("Нелинейная модель (время: параметр y: отклонение):")
    nonlin()
end
main()
   