#pragma once
#include "General.h"

class NotIntaractive
{
protected:
	sf::RectangleShape field;
	float x;
	float y;
	float w;
	float h;
	float r_b;
	float g_b;
	float b_b;
	sf::Text text;
	float r_t;
	float g_t;
	float b_t;
	string txt;
public:
	NotIntaractive(
		float x, float y,
		string txt,
		float r_t, float g_t, float b_t
	);
	NotIntaractive(
		float x, float y,
		float w, float h,
		float r_b, float g_b, float b_b,
		string txt,
		float r_t, float g_t, float b_t
	);
	NotIntaractive(const NotIntaractive& obj);
	void setX(float x);
	void setY(float y);
	void setW(float w);
	void setH(float h);
	void setTxt(string str);
	void setBgColor(float r, float g, float b);
	void setTxtColor(float r, float g, float b);
	float getX();
	float getY();
	float getW();
	float getH();
	string getTxt();
	float getBgR();
	float getBgG();
	float getBgB();
	float getTxtR();
	float getTxtG();
	float getTxtB();
	void draw();
};

