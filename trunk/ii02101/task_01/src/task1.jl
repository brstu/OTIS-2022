a = 0.5
b = 0.5
c = 0.5
d = 0.5
i = 0

function line(t, u, y, a, b, i)

    if i < t

        print(i + 1 , " time has passed: ")
        resl = a * y + b * u
        println(resl)        
        line(t, u, resl, a, b, i + 1)
    else

        println("end of linear module operation")
    end

end

function nline(t, u, up, y, yp, a, b, c, d, i)
    
    if i == 0       

        yp = 0
        up = 0
        
        print(i + 1 , " time has passed: ")
        resnl = a * y - b * yp^2 + c * u + d * sin(up)
        println(resnl)
        nline(t, u, u, resnl, y, a, b, c, d, i + 1)   
    elseif i < t

        print(i + 1 , " time has passed: ")
        resnl = a * y - b * yp^2 + c * u + d * sin(up)
        println(resnl)
        nline(t, u, up, resnl, y, a, b, c, d, i + 1)
    else 

        println("end of non-linear module operation\n")
    end    
end

function main()
                
    y = 0
    u = 1
    t = 10

    println("\nstart of linear module operation")
    line(t, u, y, a, b, i)

    println("\nstart of non-linear module operation")
    nline(t, u, u, y, y, a, b, c, d, i)    
end

main()