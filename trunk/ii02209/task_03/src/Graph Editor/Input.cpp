#include "Input.h"

Input::Input(
	float x, float y,
	float w, float h,
	float r_b, float g_b, float b_b,
	float r_t, float g_t, float b_t
) : Intaractive(
	x, y,
	w, h,
	r_b, g_b, b_b,
	"",
	r_t, g_t, b_t
) {}

void Input::setTxt(const string& str)
{
	this->txt = str;
	string temp = "";
	float length = this->w / (FONT_SIZE / 1.5);
	for (int i = (str.size() - length > 0) ? str.size() - length - 1 : 0; i < str.size(); i++)
	{
		temp += str[i];
	}
	this->text.setString(temp);
}

void Input::clear()
{
	this->txt = "";
	this->text.setString("");
}

