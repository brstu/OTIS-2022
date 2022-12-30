#pragma once
#include "General.h"
#include "Button.h"
#include "Input.h"
#include "Txt.h"

class ContentPage
{
protected:
	bool write;
	bool isVisible;
	vector<Button> btns;
	vector<Txt> txts;
	vector<Input> inputs;
public:
	ContentPage();
	void add_btn(
		float x, float y,
		float w, float h,
		float r_b, float g_b, float b_b,
		const string& text,
		float r_t, float g_t, float b_t
	);
	void add_txt(
		float x, float y,
		const string& txt,
		float r_t, float g_t, float b_t
	);
	void add_input(
		float x, float y,
		float w, float h,
		float r_b, float g_b, float b_b,
		float r_t, float g_t, float b_t
	);
	void offAll();
	void select();
	bool isMouseOnBtn(int& i, int M_x, int M_y);
	bool isMouseOnInput(int& i, int M_x, int M_y);
	void view();
	void hide();
	bool isVis();
	bool isWrite();
	void stopWrite();
	int IndexOfPressedInput();
	int IndexOfPressedButton();
	bool isButtonPressed();
	void setTxt_toInput(int i, const string& txt);
	void setTxt_toTxt(int i, const string& txt);
	string getTxt_fromInput(int i);
	string getTxt_fromTxt(int i);
};

