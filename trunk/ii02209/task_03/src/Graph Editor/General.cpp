#include "General.h"

sf::RectangleShape createRectangle(float x, float y, float w, float h, float r, float g, float b) 
{
	sf::RectangleShape item;
	item.setPosition(sf::Vector2f(x, y));
	item.setSize(sf::Vector2f(w, h));
	item.setFillColor(sf::Color(r, g, b));
	return item;
}

sf::CircleShape createCircle(float x, float y, float rad, float r, float g, float b)
{
	sf::CircleShape item;
	item.setPosition(sf::Vector2f(x, y));
	item.setRadius(rad);
	item.setFillColor(sf::Color(r, g, b));
	return item;
}

sf::Text createText(float x, float y, const string& str, float r, float g, float b)
{
	sf::Text text;
	text.setFont(FONT);
	text.setString(str);
	text.setCharacterSize(FONT_SIZE);
	text.setFillColor(sf::Color(r, g, b));
	text.setPosition(x, y);
	return text;
}

void getMousePos(int& M_x, int& M_y)
{
	sf::Vector2i pos = sf::Mouse::getPosition(WINDOW);
	M_x = pos.x;
	M_y = pos.y;
}

float to_deg(float x)
{
	return x * 180 / pi;
}