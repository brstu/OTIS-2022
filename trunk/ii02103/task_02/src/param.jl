K = 0.0001
T = 100
T_D = 100
T_0 = 1

q_0 = K * (1 + T_D/T_0)
q_1 = -K * (1 + 2 * T_D / T_0 - T_0 / T)
q_2 = K * T_D / T_0

q = [q_0, q_1, q_2]
e = [0.0, 0.0, 0.0]
y = [0.0, 0.0, 0.0]
u = [1.0, 1.0]

a = 0.5; b = 0.3; c = 0.9; d = 0.1
p = [a, b, c, d]