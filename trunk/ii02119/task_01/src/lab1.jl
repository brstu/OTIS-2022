function LinearModels(a, b, yt,ut ,time) i = 1
    for i in i:time 
        yt = a * yt + b * ut
        println(i,")",yt)    
    end
end

function NoLinearModels(a, b, c, d, yt, ut, time) i = 1
    y=0.0
    for i in i : time 
        ut1 = ut
        yt1 = y
        y = yt
        yt = a * yt - b * yt1 ^ 2 + c * ut + d * sin(ut1)
        println( i,")",yt)  
    end
end

function main()   
    time=12

    a=1.1;b=1;yt=1.5;ut=4  

    println("\nЛинейная модель:\n")
    LinearModels(a,b,yt,ut,time)

    a=0.5; b=-0.1 ;c = 1;d=0.1;yt=0.1;ut=1.8

    println("\nНелинейная модель:\n")
    NoLinearModels(a, b, c, d, yt, ut,time)    
end
main()   