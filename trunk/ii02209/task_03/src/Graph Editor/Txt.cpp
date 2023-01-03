#include "Txt.h"

Txt::Txt(
	float x, float y,
	const string& txt,
	float r_t, float g_t, float b_t
) : NotIntaractive(
	x, y,
	0, FONT_SIZE + 4 * OUTL,
	0, 0, 0,
	txt,
	r_t, g_t, b_t
) {}

void Txt::draw()
{
	WINDOW.draw(text);
}
