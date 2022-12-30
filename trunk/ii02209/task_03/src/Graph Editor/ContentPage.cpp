#include "ContentPage.h"

ContentPage::ContentPage() {
	this->isVisible = true;
	this->write = false;
}

void ContentPage::add_btn(
	float x, float y,
	float w, float h,
	float r_b, float g_b, float b_b,
	const string& text,
	float r_t, float g_t, float b_t
) {
	Button btn(x, y, w, h, r_b, g_b, b_b, text, r_t, g_t, b_t);
	btns.push_back(btn);
}

void ContentPage::add_txt(
	float x, float y,
	const string& txt,
	float r_t, float g_t, float b_t
) {
	Txt text(x, y, txt, r_t, g_t, b_t);
	txts.push_back(text);
}

void ContentPage::add_input(
	float x, float y,
	float w, float h,
	float r_b, float g_b, float b_b,
	float r_t, float g_t, float b_t
) {
	Input input(x, y, w, h, r_b, g_b, b_b, r_t, g_t, b_t);
	inputs.push_back(input);
}

void ContentPage::offAll()
{
	for (vector<Button>::iterator btn = this->btns.begin(); btn != this->btns.end(); btn += 1)  {
		btn->off();
	}
	for (vector<Input>::iterator input = this->inputs.begin(); input != this->inputs.end(); input += 1) {
		input->off();
	}
}

bool ContentPage::isMouseOnBtn(int& i, int M_x, int M_y) {
	int k = 0;
	for (vector<Button>::iterator btn = btns.begin(); btn != btns.end(); btn += 1) {
		if (btn->isCursorOnMe(M_x, M_y)) {
			i = k;
			return true;
		}
		k++;
	}
	return false;
}

bool ContentPage::isMouseOnInput(int& i, int M_x, int M_y) {
	int k = 0;
	for (vector<Input>::iterator input = inputs.begin(); input != inputs.end(); input += 1) {
		if (input->isCursorOnMe(M_x, M_y)) {
			i = k;
			return true;
		}
		k++;
	}
	return false;
}

void ContentPage::select() {
	int x, y;
	getMousePos(x, y);
	int i;
	if (isMouseOnBtn(i, x, y)) {
		offAll();
		btns[i].on();
	} 
	else if (isMouseOnInput(i, x, y)) {
		offAll();
		inputs[i].clear();
		inputs[i].on();
		this->write = true;
	}
}

bool ContentPage::isVis()
{
	return this->isVisible;
}

bool ContentPage::isWrite()
{
	return this->write;
}

void ContentPage::stopWrite()
{
	this->write = false;
}

void ContentPage::view() 
{
	this->isVisible = true;
}

void ContentPage::hide() 
{
	for (vector<Input>::iterator input = this->inputs.begin(); input != this->inputs.end(); input += 1) {
		input->clear();
	}
	this->isVisible = false;
}

int ContentPage::IndexOfPressedButton()
{
	for (int i = 0; i < btns.size() - 1; i++) {
		if (btns[i].isPressed())
		{
			return i;
		}
	}
}

int ContentPage::IndexOfPressedInput()
{
	for (int i = 0; i < inputs.size() - 1; i++) {
		if (inputs[i].isPressed())
		{
			return i;
		}
	}
}

bool ContentPage::isButtonPressed()
{
	for (vector<Button>::iterator btn = this->btns.begin(); btn != this->btns.end(); btn += 1) {
		if (btn->isPressed())
			return true;
	}
	return false;
}

void ContentPage::setTxt_toInput(int i, const string& txt)
{
	this->inputs[i].setTxt(txt);
}

void ContentPage::setTxt_toTxt(int i, const string& txt)
{
	this->txts[i].setTxt(txt);
}

string ContentPage::getTxt_fromInput(int i)
{
	return this->inputs[i].getTxt();
}

string ContentPage::getTxt_fromTxt(int i)
{
	return this->txts[i].getTxt();
}
