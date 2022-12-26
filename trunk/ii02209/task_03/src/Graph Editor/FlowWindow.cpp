#include "FlowWindow.h"

FlowWindow::FlowWindow(
	float x, float y,
	float w, float h,
	float r_b, float g_b, float b_b
) {
	this->dark = createRectangle(
		0, 0,
		WIN_WIDTH, WIN_HEIGHT,
		50, 0, 50
	);
	this->dark.setFillColor(sf::Color(50, 0, 50, 150));
	this->bg = createRectangle(
		x + OUTL, y + OUTL,
		w - 2 * OUTL, h - 2 * OUTL,
		r_b, g_b, b_b
	);
	this->bg.setOutlineThickness(OUTL);
	this->bg.setOutlineColor(sf::Color(50, 0, 50));
	this->x = x;
	this->y = y;
	this->w = w;
	this->h = h;
	this->r_b = r_b;
	this->g_b = g_b;
	this->b_b = b_b;
	this->isVisible = false;
}

bool FlowWindow::isCursorInWindow()
{
	int M_x, M_y;
	getMousePos(M_x, M_y);
	return((x <= M_x && M_x <= x + w && y <= M_y && M_y <= y + h) ? true : false);
}

void FlowWindow::draw()
{
	if (this->isVisible)
	{
		WINDOW.draw(dark);
		WINDOW.draw(bg);
		for (vector<Button>::iterator btn = btns.begin(); btn != btns.end(); btn++)
		{
			btn->draw();
		}
		for (vector<Txt>::iterator txt = txts.begin(); txt != txts.end(); txt++)
		{
			txt->draw();
		}
		for (vector<Input>::iterator input = inputs.begin(); input != inputs.end(); input++)
		{
			input->draw();
		}
	}
}