 function main()   
    # Линейная модель
    a=0.27; b=1.7 # константы a и b
    y_lin=18; u_lin=11 #входящая температура и тепло
    i=1
    time=10 
    println("Линейная модель: ")
    for i in i:time 
        println(i,"    ",y_lin)
        y_lin=a * y_lin + b * u_lin # формула линейной модели
    end
    # Нелинейная модель
    an=0.01; bn=0.07; c=30.5; d=-0.09 # константы
    y_nonlin1=15; y_nonlin2=16
    u_nonlin1=1; u_nonlin=0.025
    println()
    println("Нелинейная модель:")
    for i in i:time
        y_nonlin3=an * y_nonlin2 - bn * abs2(y_nonlin1)+ c * u_nonlin1 + d * sin(u_nonlin)# формула нелинейной модели
        println(i,"    ",y_nonlin3) # вывод значений
        y_nonlin1=y_nonlin2 # переинициализация
        y_nonlin2=y_nonlin3
    end     
end
main()   
