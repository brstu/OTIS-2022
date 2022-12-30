#pragma once

#include <SFML/Graphics.hpp>
#include<Windows.h>
#include<vector>
#include<string>
#include<iostream>
#include<conio.h>
#include<iomanip>
#include<cmath>

#define pi 3.1415

using std::vector;
using std::string;
using std::cout;
using std::cerr;
using std::endl;
using std::to_string;
using std::stoi;
using std::setw;

extern float WIN_WIDTH;
extern float WIN_HEIGHT;
extern float FPS;
extern float FONT_SIZE;
extern float PADDING_LEFT;
extern float MARGIN;
extern float OUTL;
extern float BG_H;
extern float BTN_H;
extern float BTN_W;
extern float TOOLBAR_W;
extern float RAD;
extern sf::Font FONT;
extern sf::RenderWindow WINDOW;
extern sf::Event event; 

class Graph;
class Vertex;
class Branch;

class NotIntaractive;
class Intaractive;
class Button;
class Txt;
class Input;
class Page;

class ContentPage;
class Program;
class FlowWindow;

sf::RectangleShape createRectangle(float x, float y, float w, float h, float r, float g, float b);

sf::CircleShape createCircle(float x, float y, float rad, float r, float g, float b);

sf::Text createText(float x, float y, const string& str, float r, float g, float b);

void getMousePos(int& M_x, int& M_y);

float to_deg(float x);

