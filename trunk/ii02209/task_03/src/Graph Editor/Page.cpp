#include "Page.h"

Page::Page(
	float x, float y,
	float w, float h,
	float r_b, float g_b, float b_b,
	const string& txt,
	float r_t, float g_t, float b_t,
	bool pressed = false
) : Intaractive(
	x, y,
	w, h,
	r_b, g_b, b_b,
	txt,
	r_t, g_t, b_t
) {
	this->pressed = pressed;
	if (pressed)
	{
		on();
	}
}

void Page::draw()
{
	NotIntaractive::draw();
}
