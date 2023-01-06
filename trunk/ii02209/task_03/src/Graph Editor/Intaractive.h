#pragma once
#include "General.h"
#include "NotIntaractive.h"

class Intaractive : public NotIntaractive
{
protected:
	bool pressed;
public:
	Intaractive(
		float x, float y,
		float w, float h,
		float r_b, float g_b, float b_b,
		const string& txt,
		float r_t, float g_t, float b_t,
		bool pressed = false
	);
	Intaractive(const Intaractive& obj);
	bool isCursorOnMe(int M_x, int M_y);
	bool isPressed();
	void on();
	void off();
};

