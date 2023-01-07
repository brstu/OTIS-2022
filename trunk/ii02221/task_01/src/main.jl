using Plots
D=0.74
C=0.19
K=1.78
S=0.43
    function Linear_Model(current_y,t,warm)
        MASS_y=[]
        println("Liner date ")
        println(current_y)
        push!(MASS_y,current_y)
        for i in 1:t
            New_y=D*current_y+C*warm
            push!(MASS_y,New_y)
            current_y=New_y
            println(New_y)
        end
        plot([1:(t+1)], MASS_y, color = :blue , label = "Linear_model")
        #println("Liner date ", MASS_y)
    end
    function Unlinear_Model(middle_y,t,middle_warm)
        last_y=0
        last_warm=0
        MASS_y=[]
        println("UnLiner date ")
        println(middle_y)
        push!(MASS_y,middle_y)
        for i in 1:t
            New_y=D*middle_y-C*last_y^2+K*middle_warm+S*sin(last_warm)
            push!(MASS_y,New_y)
            last_y=middle_y
            middle_y=New_y
            last_warm=middle_warm
            middle_warm=middle_warm+0.005
            println(New_y)
        end
        plot!([1:(t+1)], MASS_y, color = :green , label = "UnLinear_model")
        savefig("tam.png")
        #println("UnLiner date ", MASS_y)
    end
    Linear_Model(0,8,2)
    Unlinear_Model(1,6,1)