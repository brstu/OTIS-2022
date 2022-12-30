#pragma once
#include "General.h"
#include "Intaractive.h"

class Input : public Intaractive
{
public:
	Input(
		float x, float y,
		float w, float h,
		float r_b, float g_b, float b_b,
		float r_t, float g_t, float b_t
	);
	void setTxt(const string& str);
	void clear();
};

