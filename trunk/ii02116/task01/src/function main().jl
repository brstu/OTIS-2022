function main() 
    # для первой линейной модели 
    a=0.11; b=1.5 # константы a и b 
    y_lin=20; u_lin=15 #входящая температура и тепло 
    i=0 # счётчик 
    t=12 # время 
    
    println("Linear model") 
    for i in i:t # цикл 
        println(y_lin)# вывод значений 
        y_lin=a * y_lin + b * u_lin # формула линейной модели 
    end 
    # нелинейная модель 
    an=0.001; bn=0.009; c=20.5; d=-0.005 # константы 
    y_nonlin1=10; y_nonlin2=12
    u_nonlin=1
    u_nonlin_1=0 
    println("\n\n","Nonlinear model") 
    for i in i:t 
        y_nonlin3=an * y_nonlin2 - bn * abs2(y_nonlin1)+ c * u_nonlin + d * sin(u_nonlin_1)# формула нелинейной модели 
        println(y_nonlin3) # вывод значений 
        y_nonlin1=y_nonlin2 
        y_nonlin2=y_nonlin3 
        u_nonlin_1=u_nonlin 
    end 
     
end 
main()