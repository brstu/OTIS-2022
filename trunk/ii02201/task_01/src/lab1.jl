function pow(value,degree)
    result= 1
    for i in 1:degree
        result= result * value
    end
    return result
end

function Linear_Model(a,b,y_current,u_current)
    println(a*y_current+b*u_current)
    return (a*y_current+b*u_current)
end

function UnLinear_Model(a, b, c, d, y_current, y_prev, u_current, u_prev)
    y_new = a*y_current - b * pow(y_prev,2) + c*u_current + d*sin(u_prev)
    println(y_new)
    return y_new
end

function main()
    a= 
    b=
    c=
    d=
    y=0.0
    u=0.0
end

main()