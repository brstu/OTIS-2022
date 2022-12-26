#pragma once
#include "General.h"
#include "ContentPage.h"

class FlowWindow : public ContentPage 
{
private:
	sf::RectangleShape dark;
	sf::RectangleShape bg;
	float x;
	float y;
	float w;
	float h;
	float r_b;
	float g_b;
	float b_b;
public:
	FlowWindow(
		float x, float y,
		float w, float h,
		float r_b, float g_b, float b_b
	);
	bool isCursorInWindow();
	void draw();
};

