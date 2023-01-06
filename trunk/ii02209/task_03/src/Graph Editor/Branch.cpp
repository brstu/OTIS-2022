#include "Branch.h"

void Branch::moveArrow(float x1, float y1, float x2, float y2)
{
	if (!this->oriented)
	{
		return;
	}
	float Cos_Ox_br = (double(x1) - x2) / (sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)));
	float Sin_Ox_br = (double(y1) - y2) / (sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2)));
	this->arrow.setPoint(1, sf::Vector2f(
		x2 + Cos_Ox_br * RAD,
		y2 + Sin_Ox_br * RAD
	));
	float w = 10;
	float l = RAD;
	float Cos_Ox_nbr = -(double(y2) - y1) / sqrt(pow(y1 - y2, 2) + pow(x2 - x1, 2));
	float Sin_Ox_nbr = (double(x2) - x1) / sqrt(pow(y1 - y2, 2) + pow(x2 - x1, 2));
	float x_top = x2 + Cos_Ox_br * (RAD + l) + Cos_Ox_nbr * w;
	float y_top = y2 + Sin_Ox_br * (RAD + l) + Sin_Ox_nbr * w;
	float x_bottom = x2 + Cos_Ox_br * (RAD + l) - Cos_Ox_nbr * w;
	float y_bottom = y2 + Sin_Ox_br * (RAD + l) - Sin_Ox_nbr * w;
	this->arrow.setPoint(0, sf::Vector2f(x_top, y_top));
	this->arrow.setPoint(2, sf::Vector2f(x_bottom, y_bottom));
	this->arrow.setFillColor(sf::Color::Black);
}

void Branch::moveWeight(float x1, float y1, float x2, float y2)
{
	float br_len = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
	float Cos_Ox_br = (double(x1) - x2) / br_len;
	float Sin_Ox_br = (double(y1) - y2) / br_len;
	int k = to_string(round(int(this->weight * 10)) / 10).size();
	weight_txt.setPosition(
		x2 + Cos_Ox_br * br_len / 2 + FONT_SIZE - FONT_SIZE / 1.55 * k / 2,
		y2 + Sin_Ox_br * br_len / 2 - FONT_SIZE - FONT_SIZE / 2 - 2
	);
}

Branch::Branch(
	int start, float x1, float y1,
	int end, float x2, float y2,
	float weight,
	bool oriented
) {
	this->start = start;
	this->end = end;
	this->oriented = oriented;
	this->weight = weight;
	this->line[0].position = sf::Vector2f(x1, y1);
	this->line[0].color = sf::Color::Black;
	this->line[1].position = sf::Vector2f(x2, y2);
	this->line[1].color = sf::Color::Black;
	if (this->oriented)
	{
		this->arrow.setPointCount(3);
		moveArrow(x1, y1, x2, y2);
		this->arrow.setFillColor(sf::Color::Black);
	}
	this->weight_txt = createText(x2, y2, to_string(round(int(this->weight * 10)) / 10), 255, 255, 255);
	moveWeight(x1, y1, x2, y2);
}

bool Branch::isOriented()
{
	return this->oriented;
}

void Branch::setWeight(float weight)
{ 
	this->weight = weight;
}

void Branch::setType(bool oriented)
{ 
	this->oriented = oriented;
}

void Branch::setPos(float x1, float y1, float x2, float y2)
{
	this->line[0].position = sf::Vector2f(x1, y1);
	this->line[1].position = sf::Vector2f(x2, y2);
}

void Branch::setStartPos(float x1, float y1)
{
	this->line[0].position = sf::Vector2f(x1, y1);
}

void Branch::setEndPos(float x2, float y2)
{
	this->line[1].position = sf::Vector2f(x2, y2);
}

int Branch::getStart()
{
	return this->start;
}

int Branch::getEnd()
{
	return this->end;
}

float Branch::getWeight()
{
	return this->weight;
}

void Branch::draw()
{
	WINDOW.draw(this->line, 2, sf::Lines);
	if (this->oriented)
	{
		WINDOW.draw(this->arrow);
	}
	WINDOW.draw(this->weight_txt);
}
