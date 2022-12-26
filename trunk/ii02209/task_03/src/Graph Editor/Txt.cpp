#include "Txt.h"

Txt::Txt(
	float x, float y,
	string txt,
	float r_t, float g_t, float b_t
) : NotIntaractive (
	x, y,
	txt,
	r_t, g_t, b_t
) {}

void Txt::draw()
{
	WINDOW.draw(text);
}
