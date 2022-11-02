function nonline(yc, uc, t)
    
    yprev = 0.0
    uprev = 0.0
    y = yc
    u = uc
    i = 0       

    while (i != t)
        tempy = y
        tempu = u
        (y, u) = iter(y, yprev, u, uprev)
        yprev = tempy
        uprev = tempu
        println(y)
        i = i + 1
    end    
end

function iter(ycurr, yprev, ucurr, uprev)

    a = 1
    b = 0.04
    c = 0.05
    d = 0.003

    e = [0.001, 0.19, 0.0002]
    q = [0.32, 0.05, 0.12]  
    
    deltauk = q[1] * e[3] + q[2] * e[2] + q[3] * e[1]
    unew = ucurr + deltauk    
    ynew = a * ycurr - b * yprev^2 + c * ucurr + d * sin(uprev)
    e[3] = 10 - yprev
    e[2] = 10 - ycurr
    e[1] = 10 - ynew
    return ynew, unew 
end

function main()

    y = 10.0
    u = 100.0
    t = 100
    nonline(y, u, t)
end

main()