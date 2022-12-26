#pragma once
#include "General.h"
#include "Vertex.h"

class Branch {
private:
	float weight;
	bool oriented;
	int start;
	int end;
	sf::Vertex line[2];
	sf::ConvexShape arrow;
	sf::Text weight_txt;
public:
	Branch(
		int start, float x1, float y1,
		int end, float x2, float y2,
		float weight,
		bool oriented
	);
	bool isOriented();
	void setWeight(float weight);
	void setType(bool oriented);
	void setPos(float x1, float y1, float x2, float y2);
	void setStartPos(float x1, float y1);
	void setEndPos(float x2, float y2);
	int getStart();
	int getEnd();
	float getWeight();
	void moveArrow(float x1, float y1, float x2, float y2);
	void moveWeight(float x1, float y1, float x2, float y2);
	void draw();
};
