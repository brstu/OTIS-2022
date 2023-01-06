#include "Intaractive.h"

Intaractive::Intaractive(
	float x, float y,
	float w, float h,
	float r_b, float g_b, float b_b,
	const string& txt,
	float r_t, float g_t, float b_t,
	bool pressed
) : NotIntaractive(
	x, y,
	w, h,
	r_b, g_b, b_b,
	txt,
	r_t, g_t, b_t
) {
	this->pressed = pressed;
}

Intaractive::Intaractive(const Intaractive& obj) : NotIntaractive(obj)
{
	this->pressed = obj.pressed;
}

bool Intaractive::isCursorOnMe(int M_x, int M_y) 
{
	return((x <= M_x && M_x <= x + w && y <= M_y && M_y <= y + h) ? true : false);
}

bool Intaractive::isPressed()
{
	return this->pressed;
}

void Intaractive::on() 
{
	int k = 30;
	field.setFillColor(sf::Color(
		((r_b - k > 0) ? r_b - k : 0),
		((g_b - k > 0) ? g_b - k : 0),
		((b_b - k > 0) ? b_b - k : 0)
	));
	text.setFillColor(sf::Color(
		((r_t - k > 0) ? r_t - k : 0),
		((g_t - k > 0) ? g_t - k : 0),
		((b_t - k > 0) ? b_t - k : 0)
	));
	pressed = true;
}

void Intaractive::off() 
{
	field.setFillColor(sf::Color(r_b, g_b, b_b));
	text.setFillColor(sf::Color(r_t, g_t, b_t));
	pressed = false;
}

