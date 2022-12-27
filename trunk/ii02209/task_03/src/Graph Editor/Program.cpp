#include "Program.h"

Program::Program() : ContentPage()
{
	bg = createRectangle(OUTL, OUTL, WIN_WIDTH - OUTL * 2, WIN_HEIGHT - OUTL * 2, 205, 190, 205);
	bg.setOutlineThickness(OUTL);
	bg.setOutlineColor(sf::Color(50, 0, 50));
	tools_bg = createRectangle(OUTL, OUTL, BTN_W - OUTL * 2 + 2 * MARGIN, BTN_H * 5 + MARGIN * 6, 120, 10, 120);
	tools_bg.setOutlineThickness(OUTL);
	tools_bg.setOutlineColor(sf::Color(50, 0, 50));
	vertex_and_branch_info_bg = createRectangle(
		OUTL, BTN_H * 5 + MARGIN * 6,
		BTN_W - OUTL * 2 + 2 * MARGIN, BTN_H * 2,
		120, 10, 120
	);
	vertex_and_branch_info_bg.setOutlineThickness(OUTL);
	vertex_and_branch_info_bg.setOutlineColor(sf::Color(50, 0, 50));
	info_bg = createRectangle(
		OUTL, BTN_H * 7 + MARGIN * 6,
		BTN_W - OUTL * 2 + 2 * MARGIN, WIN_HEIGHT - BTN_H * 7 - MARGIN * 7 + OUTL * 2,
		120, 10, 120
	);
	info_bg.setOutlineThickness(OUTL);
	info_bg.setOutlineColor(sf::Color(50, 0, 50));
	this->write = false;
}

void Program::add_page(
	float x, float y,
	float w, float h,
	float r_b, float g_b, float b_b,
	string txt,
	float r_t, float g_t, float b_t,
	bool pressed
) {
	Page pg(x, y, w, h, r_b, g_b, b_b, txt, r_t, g_t, b_t, pressed);
	pages.push_back(pg);
	this->page = pages.size() - 1;
}

void Program::offAll()
{
	for (vector<Button>::iterator btn = this->btns.begin(); btn != this->btns.end(); btn += 1) 
	{
		btn->off();
	}
	for (vector<Input>::iterator input = this->inputs.begin(); input != this->inputs.end(); input += 1) 
	{
		input->off();
	}
}

void Program::offAllPages()
{
	for (vector<Page>::iterator pg = this->pages.begin(); pg != this->pages.end(); pg += 1)
	{
		pg->off();
	}
}

void Program::select()
{
	this->write = false;
	int x, y;
	getMousePos(x, y);
	int i;
	if (isMouseOnBtn(i, x, y)) {
		offAll();
		btns[i].on();
	}
	else if (isMouseOnInput(i, x, y)) 
	{
		offAll();
		inputs[i].clear();
		inputs[i].on();
		this->write = true;
	} 
	else if (isMouseOnPage(i, x, y))
	{
		offAll();
		offAllPages();
		pages[i].on();
		this->page = i;
	}
	else
	{
		offAll();
	}
}

int Program::getCurrentPage()
{
	return this->page;
}

bool Program::isMouseOnPage(int& i, int M_x, int M_y)
{
	int k = 0;
	for (vector<Page>::iterator pg = pages.begin(); pg != pages.end(); pg += 1) {
		if (pg->isCursorOnMe(M_x, M_y))
		{
			i = k;
			return true;
		}
		k++;
	}
	return false;
}

int Program::amountOfPages()
{
	return this->pages.size();
}

void Program::onPage(int i)
{
	this->pages[i].on();
}

void Program::draw() 
{
	WINDOW.draw(bg);
	WINDOW.draw(tools_bg);
	WINDOW.draw(vertex_and_branch_info_bg);
	WINDOW.draw(info_bg);
	for (vector<Button>::iterator btn = btns.begin(); btn != btns.end(); btn += 1)
	{
		btn->draw();
	}
	for (vector<Txt>::iterator txt = txts.begin(); txt != txts.end(); txt += 1)
	{
		txt->draw();
	}
	for (vector<Input>::iterator input = inputs.begin(); input != inputs.end(); input += 1)
	{
		input->draw();
	}
	for (vector<Page>::iterator pg = pages.begin(); pg != pages.end(); pg += 1) 
	{
		pg->draw();
	}
}
