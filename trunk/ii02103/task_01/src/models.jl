    using PyPlot

    y_lin = []
    y_nonlin = []
    
    function linear_model(a, b, y, u, i, t)
        if i <= t
            println(y)
            push!(y_lin, y)
            y_2 = a*y + b*u
            linear_model(a, b, y_2, u, i + 1, t) 
        else
            println("END")
        end
    end

    function nonlinear_model(a, b, c, d, y, y_prev, u, u_prev, i, t)
        if i == 1
            println(y)
            push!(y_nonlin, y)
            y_2 = a*y - b*y_prev^2 + c*0 + d*sin(0)
            nonlinear_model(a, b, c, d, 
                            y_2, y, 
                            u, u,
                            i + 1, t)
        elseif i <= t
            println(y)
            push!(y_nonlin, y)
            y_2 = a*y - b*y_prev^2 + c*u + d*sin(u_prev)
            nonlinear_model(a, b, c, d,
                            y_2, y,
                            u, u, 
                            i + 1, t)
        else
            println("END")
        end
    end

    function main()
        i = 1 
        y = 0.0 
        u = 1.0        
        t = 10 
        a = 1
        b = 0.5
        c = 0.001
        d = 0.999

        println("Linear Model:")
        linear_model(a, b, y, u, i, t)
        println("Nonlinear Model:")
        nonlinear_model(a, b, c, d, y, y, u, u, i, t)

        x = 1:t; y = y_lin; y2 = y_nonlin
        plot(x, y, label="linear_model")
        plot(x, y2, label="nonlinear_model")
        plot(x, y, "b.") 
        plot(x, y2, "r.")
        legend()
    end

    main()
