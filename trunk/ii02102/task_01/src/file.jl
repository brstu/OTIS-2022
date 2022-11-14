function main()
    a = 0.5
    b = 0.3
    c = 0.2
    d = 0.4
    ylin = 0
    ulin = 1.2
    i = 0
    t = 10
    println("Linear model")
    for i in i:t
        println(ylin)
        ylin = a * ylin + b * ulin
    end
    ynonlin1 = 0
    ynonlin2 = 0
    ynonlin3 = 0
    unonlin = 2
    k = 0
    println("\n\n","Nonlinear model")
    for i in 1:t
        ynonlin3 = a * ynonlin2 - b * (ynonlin1) * (ynonlin1) + c * unonlin + d * sin(unonlin)
        println(ynonlin3)
        ynonlin1 = ynonlin2
        ynonlin2 = ynonlin3
    end
end


main()
