#pragma once
#include "General.h"
#include "Intaractive.h"
#include "Graph.h"

class Page : public Intaractive 
{
public:
	Page(
		float x, float y,
		float w, float h,
		float r_b, float g_b, float b_b,
		const string txt,
		float r_t, float g_t, float b_t,
		bool pressed
	);
	void draw();
};
