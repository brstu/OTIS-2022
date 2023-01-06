#include "Graph.h"

// Graph 

Graph::Graph()
{
	this->matrix = NULL;
}

Graph::~Graph()
{
	int amountOfVertices = this->vertices.size();
	for (int i = 0; i < amountOfVertices; i++)
	{
		delete[] this->matrix[i];
	}
	delete[] this->matrix;
}

void Graph::setAdjacenciesMatrix()
{
	int amountOfVertices = this->vertices.size();
	this->matrix = new float* [amountOfVertices];
	for (int i = 0; i < amountOfVertices; i++)
	{
		this->matrix[i] = new float[amountOfVertices];
		for (int j = 0; j < amountOfVertices; j++)
		{
			this->matrix[i][j] = 0;
		}
	}
	for (vector<Branch>::iterator branch = branches.begin(); branch != branches.end(); branch += 1)
	{
		if (branch->isOriented())
		{
			this->matrix[branch->getStart()][branch->getEnd()] = branch->getWeight();
		}
		else
		{
			this->matrix[branch->getStart()][branch->getEnd()] = branch->getWeight();
			this->matrix[branch->getEnd()][branch->getStart()] = branch->getWeight();
		}
	}
}

string Graph::getAdjacenciesMatrixAsStr()
{
	int amountOfVertices = this->vertices.size();
	string str = "";
	for (int i = 0; i < amountOfVertices; i++)
	{
		for (int j = 0; j < amountOfVertices; j++)
		{
			string temp = to_string(this->matrix[i][j]);
			while (temp.size() != 18)
			{
				temp = " " + temp;
			}
			str += temp + ' ';
		}
		str += '\n';
	}
	return str;
}

string Graph::getTranscendenceMatrixAsStr()
{
	int amountOfVertices = this->vertices.size();
	int amountOfBranches = this->branches.size();
	int** m = new int* [amountOfBranches];
	for (int i = 0; i < amountOfBranches; i++)
	{
		m[i] = new int[amountOfVertices];
		for (int j = 0; j < amountOfVertices; j++)
		{
			m[i][j] = 0;
		}
	}
	for (int i = 0; i < amountOfBranches; i++)
	{
		m[i][branches[i].getStart()] = -1;
		m[i][branches[i].getEnd()] = 1;
	}
	string str = "";
	for (int i = 0; i < amountOfVertices; i++)
	{
		for (int j = 0; j < amountOfBranches; j++)
		{
			string temp = to_string(m[j][i]);
			while (temp.size() != 18)
			{
				temp = " " + temp;
			}
			str += temp + ' ';
		}
		str += '\n';
	}
	for (int i = 0; i < amountOfBranches; i++)
	{
		delete[] m[i];
	}
	delete[] m;
	return str;
}

int Graph::amountOfVertices()
{
	return this->vertices.size();
}

int Graph::amountOfBranches()
{
	return this->branches.size();
}

void Graph::addVertex(const string& name, const string& content, int rad, float r, float g, float b)
{
	int number = amountOfVertices();
	string temp = name;
	if (temp == "")
	{
		temp = to_string(amountOfVertices());
	}
	Vertex vertex(number, temp, content, rad, r, g, b);
	this->vertices.push_back(vertex);
	setAdjacenciesMatrix();
}

void Graph::getVertexPos(int num, float& x, float& y)
{
	x = this->vertices[num].getX();
	y = this->vertices[num].getY();
}

void Graph::tryMoveVertex()
{
	int M_x, M_y;
	getMousePos(M_x, M_y);
	if (M_x <= BTN_W + 2 * MARGIN + RAD + OUTL ||
		//M_x >= WIN_WIDTH - BTN_W - 2 * MARGIN - RAD - OUTL ||
		M_y <= RAD + OUTL ||
		M_y >= WIN_HEIGHT - RAD - OUTL)
	{		
		return;
	}
	for (vector<Vertex>::iterator vertex = vertices.begin(); vertex != vertices.end(); vertex += 1)
	{
		if (vertex->isCursorOnMe())
		{
			vertex->setPos(M_x + vertex->getRad(), M_y + vertex->getRad());
			int n = vertex->getNumber();
			for (vector<Branch>::iterator branch = branches.begin(); branch != branches.end(); branch += 1)
			{
				int start = branch->getStart();
				int end = branch->getEnd();
				if (n == start)
				{
					branch->setStartPos(M_x, M_y);
					branch->moveArrow(
						this->vertices[start].getX() + RAD, this->vertices[start].getY() + RAD,
						this->vertices[end].getX() + RAD, this->vertices[end].getY() + RAD);
					branch->moveWeight(
						this->vertices[start].getX() + RAD, this->vertices[start].getY() + RAD,
						this->vertices[end].getX() + RAD, this->vertices[end].getY() + RAD);
				}
				if (n == end)
				{
					branch->setEndPos(M_x, M_y);
					branch->moveArrow(
						this->vertices[start].getX() + RAD, this->vertices[start].getY() + RAD,
						this->vertices[end].getX() + RAD, this->vertices[end].getY() + RAD);
					branch->moveWeight(
						this->vertices[start].getX() + RAD, this->vertices[start].getY() + RAD,
						this->vertices[end].getX() + RAD, this->vertices[end].getY() + RAD);
				}
			}
			return; 
		}
	}
}

void Graph::addBranch(int start, int end, float weight, bool oriented)
{
	Branch branch(
		start, 
		this->vertices[start].getX() + this->vertices[start].getRad(),
		this->vertices[start].getY() + this->vertices[start].getRad(),
		end,
		this->vertices[end].getX() + this->vertices[start].getRad(),
		this->vertices[end].getY() + this->vertices[start].getRad(),
		weight, 
		oriented
	);
	branches.push_back(branch);
	setAdjacenciesMatrix();
}

void Graph::draw()
{
	if (this->branches.size() > 0)
	{
		for (vector<Branch>::iterator branch = branches.begin(); branch != branches.end(); branch += 1)
		{
			branch->draw();
		}
	}

	if (this->vertices.size() > 0)
	{
		for (vector<Vertex>::iterator vertex = vertices.begin(); vertex != vertices.end(); vertex += 1)
		{
			vertex->draw();
		}
	}
}