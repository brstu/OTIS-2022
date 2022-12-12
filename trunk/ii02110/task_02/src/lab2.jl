function нелинейный(A,B,C,D,K,T0,TD,T,W,YS)
        q0 =  K * (1 + (TD / T0))  
        q1 = -K * (1 + 2 * (TD / T0) - (T0 / T))
        q2 =  K * (TD / T0)
        y = [YS, YS]
        U = 1.0
        U_pre = 1.0
        E = [W - YS, W - YS]
        um = [U,U]
    #counting values
        while abs(y[end] - W) > 0.1
            push!(E, W - y[end])
             U = U_pre + q0 * E[end] + q1 * E[end - 1] + q2 * E[end - 2]
            push!(y, A * y[end] - B * y[end - 1] + C * U + D * sin(U_pre))
            U_pre = U
            push!(um,U)
        end
    #conclesion
    println("Y")
        for i in 1:length(y)
            println(y[i])
        end	
        println(" ")
        println("E")
        for i in 1:length(E)
            println(E[i])
        end
        println(" ")
        println("U")
        for i in 1:length(um)
            println(um[i])
        end
    end
    function main()
    #parameter initialization
        A = 0.5
        B = 0.6
        C = 0.6
        D = 0.6
        K = 0.8
        T0 = 1.1
        TD = 1
        T = 1.1
    #initial value and sedired result 
        YS = 2.0
        W = 20
        нелинейный(A,B,C,D,K,T0,TD,T,W,YS)
    end
    main()