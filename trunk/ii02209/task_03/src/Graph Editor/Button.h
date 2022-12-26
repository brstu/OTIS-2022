#pragma once
#include "General.h"
#include "Intaractive.h"

class Button : public Intaractive
{
public:
	Button(
		float x, float y,
		float w, float h,
		float r_b, float g_b, float b_b,
		string text,
		float r_t, float g_t, float b_t
	);
};

