#pragma once
#include "General.h"

class Vertex
{
private:
	sf::CircleShape field;
	sf::Text num;
	int number;
	string name;
	string content;
	int degree;
	float r;
	float g;
	float b;
	float x;
	float y;
	float rad;
public:
	Vertex(int number, const string& name, const string& content, float rad, float r, float g, float b);
	void setName(const string& name);
	void setContent(const string& content);
	void setDegree(const int degree);
	void setColor(const float r, const float g, const float b);
	void setPos(float x, float y);
	float getRad();
	float getX();
	float getY();
	int getNumber();
	bool isCursorOnMe();
	void draw();
};

