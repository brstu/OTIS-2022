#include "General.h"
#include "NotIntaractive.h"

class Txt : public  NotIntaractive
{
public:
	Txt(
		float x, float y,
		const string txt,
		float r_t, float g_t, float b_t
	);
	void draw();
};