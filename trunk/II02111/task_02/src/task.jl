A = 0.5; B = 0.5; C = 0.5; D = 0.5;
K = 1; T₀ = 1; Tᴰ = 1; T = 1;

q₁ =  K * (Tᴰ / T₀ + 1)  ;
q₂ = -K * (-T₀ / T + 1 + 2 * Tᴰ / T₀);
q₃ =  K * (Tᴰ / T₀);

print("Enter start temperature: ");
start_y = parse(Float64, readline());
y = [start_y, start_y];

uᵏ = 0.0; uᵏ⁻¹ = 0.0;

print("Enter desired temperature: ");
w = parse(Float64, readline());

e = [w - start_y, w - start_y]	;

println(y[end]);
while abs(w - y[end]) > 0.1
	push!(e, w - y[end]);

	Δu = q₁ * e[end] + q₂ * e[end - 1] + q₃ * e[end - 2];
	global uᵏ = uᵏ⁻¹ + Δu;

	push!(y, A * y[end] - B * y[end - 1] + C * uᵏ + D * sin(uᵏ⁻¹));
	global uᵏ⁻¹ = uᵏ;

	println(y[end]);
end
