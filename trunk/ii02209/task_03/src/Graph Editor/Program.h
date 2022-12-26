#pragma once
#include "General.h"
#include "ContentPage.h"
#include "Page.h"
#include "FlowWindow.h"

class Program : public ContentPage
{
private:
	int page;
	vector<Page> pages;
	sf::RectangleShape bg;
	sf::RectangleShape tools_bg;
	sf::RectangleShape vertex_and_branch_info_bg;
	sf::RectangleShape info_bg;
public:
	Program();
	void add_page(
		float x, float y,
		float w, float h,
		float r_b, float g_b, float b_b,
		string text,
		float r_t, float g_t, float b_t,
		bool pressed = false
	);
	void offAll();
	void offAllPages();
	void select();
	int getCurrentPage();
	bool isMouseOnPage(int& i, int M_x, int M_y);
	int amountOfPages();
	void onPage(int i);
	void draw();
};
