#include "Button.h"

Button::Button(
	float x, float y,
	float w, float h,
	float r_b, float g_b, float b_b,
	string txt,
	float r_t, float g_t, float b_t
) : Intaractive(
	x, y,
	w, h,
	r_b, g_b, b_b,
	txt,
	r_t, g_t, b_t
) {}
