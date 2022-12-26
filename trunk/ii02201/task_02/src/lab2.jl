using Plots
global Arr2 = []
global I = 0
global prevErr = 0
function getNumber()
    num = chomp(readline())
    try
        return parse(Int,num)
    catch
        return Nothing
    end
end

function PID_controller(coeff_P,coeff_I,coeff_D,set_val,current_val,dt)
    Err = set_val - current_val
    P = Err
    global I = I + Err*dt 
    global prevErr
    D = (Err - prevErr) / dt
    control_signal = P * coeff_P + I * coeff_I + D * coeff_D
    prevErr = Err
    push!(Arr2,(control_signal-current_val))
    return control_signal
end

function Linear_model(у_curr, u, t, dt, setting, Arr2)
    а = 0.925
    b = 0.75
    coef_P = 0.19
    coef_I = 0.27
    coef_D = 0.0006
    Аrr1 = []
    Arr3 = []
    push!(Аrr1,у_curr)
    for i in 1:t
        if ((i % dt)==0)
            y=PID_controller(coef_P,coef_I,coef_D, setting, у_curr, dt)
            у_next = а * y  + b * u
            push!(Аrr1,у_next)
            у_curr = у_next
            push!(Arr3,setting)
        else
            у_next = а * у_curr + b * u
            push!(Аrr1,у_next)
            push!(Arr3,setting)
            у_curr = у_next
        end
    end
    println("Current value: ",Аrr1)
    plot([1:(t+1)], Аrr1, color = :green , label = "Current value")
    plot!([1:t], Arr2, color = :red , label = "Control signal")
    plot!([1:t], Arr3, color = :blue , label = "Setting")
end

function main()
    println("Enter initial setting: ")
    setting = getNumber()               #(100)setting stores the value the controller is aiming for
    println("Enter process duration: ")
    duration = getNumber()              #(90)
    println("Enter discretization value: ")
    dis_time = getNumber()              #(1) stores the call period for counting a new control signal
    Linear_model(0, 0, duration, dis_time, setting, Arr2)
end

main()