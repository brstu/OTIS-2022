myRound(value, amount = 3) = floor(value * 10 ^ amount) / 10 ^ amount

const time_speed = 1 #time speed in seconds

const a = 0.523
const b = 0.253
const c = 2.234
const d = 0.923

u = 1 #warm

println("Input values:")
println("a = $(a)")
println("b = $(b)")
println("c = $(c)")
println("d = $(d)")
println("warm = $(u)")

y = 1 #tempreture for linear model

function linear_tInc_modele(time)
    println("\nLinear model has been started: tempreture is rising (start value = $(y)).")
    for i = 1:time 
        prev_y = y
        global y = a * y + b * u
        println((prev_y < y) ? "Tempreture is rising (now: $(myRound(y))). $(time - i) seconds left." : "Tempreture is dropping (now: $(myRound(y))). $(time - i) seconds left.")
        sleep(time_speed)
    end 
end

linear_tInc_modele(10)

y = 1 #tempreture for unlinear model
prev_y = 0 #previous tempreture (1 second ago)

function unlinear_tInc_modele(time) 
    println("\nUnlinear model has been started: tempreture is rising (start values[pver_y, y] = $(prev_y), $(y)).")
    for i = 1:time
        new_y = a * y - b * prev_y ^ 2 + c * u + d * sin(u)
        global prev_y = y
        global y = new_y
        println((prev_y < y) ? "Tempreture is rising (now: $(myRound(y))). $(time - i) seconds left." : "Tempreture is dropping (now: $(myRound(y))). $(time - i) seconds left.")
        sleep(time_speed)
    end
end

unlinear_tInc_modele(10)

println("\nThe program is over!")

end_time = 30
println("Window will be closed for $(end_time) seconds.")
for i = 1:end_time
    print("[]")
    sleep(1)
end
