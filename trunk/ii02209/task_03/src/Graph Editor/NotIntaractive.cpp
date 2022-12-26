#include "NotIntaractive.h"

NotIntaractive::NotIntaractive(
	float x, float y,
	string txt,
	float r_t, float g_t, float b_t
) {
	this->x = x;
	this->y = y;
	this->h = FONT_SIZE + 4 * OUTL;
	this->text = createText(
		x + OUTL + PADDING_LEFT,
		y + (h - FONT_SIZE) / 2 - 2,
		txt,
		r_t, g_t, b_t
	);
	this->txt = txt;
	this->r_t = r_t;
	this->g_t = g_t;
	this->b_t = b_t;
}

NotIntaractive::NotIntaractive(
	float x, float y,
	float w, float h,
	float r_b, float g_b, float b_b,
	string txt,
	float r_t, float g_t, float b_t
) {
	this->field = createRectangle(
		x + OUTL, y + OUTL,
		w - 2 * OUTL, h - 2 * OUTL,
		r_b, g_b, b_b
	);
	this->field.setOutlineThickness(OUTL);
	this->field.setOutlineColor(sf::Color(50, 0, 50));
	this->x = x;
	this->y = y;
	this->w = w;
	this->h = h;
	this->r_b = r_b;
	this->g_b = g_b;
	this->b_b = b_b;
	this->text = createText(
		x + OUTL + PADDING_LEFT,
		y + (h - FONT_SIZE) / 2 - 2,
		txt,
		r_t, g_t, b_t
	);
	this->txt = txt;
	this->r_t = r_t;
	this->g_t = g_t;
	this->b_t = b_t;
}

NotIntaractive::NotIntaractive(const NotIntaractive& obj)
{
	this->field = createRectangle(
		obj.x + OUTL, obj.y + OUTL,
		obj.w - 2 * OUTL, obj.h - 2 * OUTL,
		obj.r_b, obj.g_b, obj.b_b
	);
	this->field.setOutlineThickness(OUTL);
	this->field.setOutlineColor(sf::Color(50, 0, 50));
	this->x = obj.x;
	this->y = obj.y;
	this->w = obj.w;
	this->h = obj.h;
	this->r_b = obj.r_b;
	this->g_b = obj.g_b;
	this->b_b = obj.b_b;
	this->text = createText(
		obj.x + OUTL + PADDING_LEFT,
		obj.y + (obj.h - FONT_SIZE) / 2 - 2,
		obj.txt,
		obj.r_t, obj.g_t, obj.b_t
	);
	this->txt = obj.txt;
	this->r_t = obj.r_t;
	this->g_t = obj.g_t;
	this->b_t = obj.b_t;
}

void NotIntaractive::setX(float x)
{
	this->x = x;
}

void NotIntaractive::setY(float y)
{
	this->y = y;
}

void NotIntaractive::setW(float w)
{
	this->w = w;
}

void NotIntaractive::setH(float h)
{
	this->h = h;
}

void NotIntaractive::setTxt(string str)
{
	this->txt = str;
	this->text.setString(str);
}


void NotIntaractive::setBgColor(float r, float g, float b)
{
	this->r_b = r_b;
	this->g_b = g_b;
	this->b_b = b_b;
}

void NotIntaractive::setTxtColor(float r, float g, float b)
{
	this->r_t = r_t;
	this->g_t = g_t;
	this->b_t = b_t;
}

float NotIntaractive::getX()
{
	return x;
}

float NotIntaractive::getY()
{
	return y;
}

float NotIntaractive::getW()
{
	return w;
}

float NotIntaractive::getH() 
{
	return h;
}

string NotIntaractive::getTxt()
{
	return txt;
}

float NotIntaractive::getBgR()
{
	return r_b;
}

float NotIntaractive::getBgG()
{
	return g_b;
}

float NotIntaractive::getBgB()
{
	return b_b;
}

float NotIntaractive::getTxtR()
{
	return r_t;
}

float NotIntaractive::getTxtG()
{
	return g_t;
}

float NotIntaractive::getTxtB()
{
	return b_t;
}


void NotIntaractive::draw() 
{
	WINDOW.draw(field);
	WINDOW.draw(text);
}

