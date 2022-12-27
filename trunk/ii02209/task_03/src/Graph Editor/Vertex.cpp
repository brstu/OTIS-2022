#include "Vertex.h"

Vertex::Vertex
(
	int number,
	const string name,
	const string content,
	float rad,
	float r, float g, float b
) {
	this->number = number;
	this->rad = rad;
	this->x = BTN_W + (WIN_WIDTH - BTN_W) / 2 - MARGIN - rad;
	this->y = WIN_HEIGHT / 2 - rad;
	this->name = name;
	this->content = content;
	this->degree = 0;
	this->r = r;
	this->g = g;
	this->b = b;
	this->field = createCircle(x, y, rad, r, g, b);
	this->field.setOutlineThickness(OUTL);
	this->field.setOutlineColor(sf::Color(r, g, b, 64));
	int k = to_string(number).size();
	this->num = createText(x + rad - FONT_SIZE / 1.55 * k / 2, y + rad - FONT_SIZE / 2 - 2, to_string(number), 255, 255, 255);
}

void Vertex::setName(const string name)
{ 
	this->name = name; 
}

void Vertex::setContent(const string content)
{ 
	this->content = content; 
}

void Vertex::setDegree(const int degree) 
{ 
	this->degree = degree; 
}

void  Vertex::setColor(const float r, const float g, const float b)
{ 
	this->r = r;
	this->g = g;
	this->b = b;
}

void Vertex::setPos(float x, float y)
{ 
	this->x = x - this->rad * 2;
	this->y = y - this->rad * 2;
	field.setPosition(this->x, this->y);
	int k = to_string(number).size();
	num.setPosition(this->x + this->rad - FONT_SIZE / 1.55 * k / 2, this->y + this->rad - FONT_SIZE / 2 - 2);
}

bool Vertex::isCursorOnMe()
{
	int M_x, M_y;
	getMousePos(M_x, M_y);
	bool a = M_x >= this->x;
	bool b = M_x <= this->x + this->rad * 2;
	bool c = M_y >= this->y;
	bool d = M_y <= this->y + this->rad * 2;
	if (a && b && c && d)
	{
		return true;
	}
	return false;
}

float Vertex::getRad()
{
	return this->rad;
}

float Vertex::getX()
{
	return this->x;
}

float Vertex::getY()
{
	return this->y;
}

int Vertex::getNumber()
{
	return this->number;
}

void Vertex::draw()
{
	WINDOW.draw(field);
	WINDOW.draw(num);
}
