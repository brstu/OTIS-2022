#pragma once
#include "General.h"
#include "Vertex.h"
#include "Branch.h"

class Graph
{
private:
	vector<Vertex> vertices;
	vector<Branch> branches;
	float** matrix;
public:
	Graph();
	~Graph();
	int amountOfVertices();
	int amountOfBranches();
	void refreshInfo();
	void setAdjacenciesMatrix();
	string getAdjacenciesMatrixAsStr();
	string getTranscendenceMatrixAsStr();
	void addVertex(const string& name, const string& content, int rad, float r, float g, float b);
	void getVertexPos(int num, float& x, float& y);
	void tryMoveVertex();
	void addBranch(int start, int end, float weight, bool oriented);
	void draw();
};
