#include "General.h"
#include "Program.h"

float WIN_WIDTH = 1920;
float WIN_HEIGHT = 1000;
float FPS = 1000;
float FONT_SIZE = 24;
float PADDING_LEFT = 12;
float MARGIN = 12;
float OUTL = 4;
float BTN_H = 50;
float BTN_W = 400;
float RAD = 40;
sf::Font FONT;
sf::RenderWindow WINDOW;
sf::Event event;
vector<Graph> graph;

void run_btn_func(Program& program, int i);
template<class T>
void texting(string& str, T& win);

// Add FlowWindow
FlowWindow vertexCreator(WIN_WIDTH / 2 - 700 / 2, WIN_HEIGHT / 2 - 600 / 2, 700, 600, 205, 170, 205);
FlowWindow branchCreator(WIN_WIDTH / 2 - 500 / 2, WIN_HEIGHT / 2 - 400 / 2, 500, 400, 205, 170, 205);
FlowWindow graphInfo(WIN_WIDTH / 2 - 1600 / 2, WIN_HEIGHT / 2 - 900 / 2, 1600, 900, 205, 170, 205);

int main()
{
    // Load font
    if (!FONT.loadFromFile("D:/Graph Editor/fonts/Roboto/Roboto-Medium.ttf"))
    {
        cerr << "Error: can't load font!" << endl;
        return 0;
    }
    // Set constants
    WINDOW.create(sf::VideoMode(WIN_WIDTH, WIN_HEIGHT), "GraphEditor");
    WINDOW.setFramerateLimit(FPS);

    Program program;

    // Add buttons
    program.add_btn(MARGIN, MARGIN, BTN_W / 4, BTN_H, 100, 10, 100, "SAVE", 255, 205, 255);
    program.add_btn(MARGIN, 2 * MARGIN + BTN_H, BTN_W / 4, BTN_H, 100, 10, 100, "LOAD", 255, 205, 255);
    program.add_btn(MARGIN, 3 * MARGIN + BTN_H * 2, BTN_W / 2 - MARGIN / 2, BTN_H, 100, 10, 100, "ADD VERTEX", 255, 205, 255);
    program.add_btn(MARGIN, 4 * MARGIN + BTN_H * 3, BTN_W / 2 - MARGIN / 2, BTN_H, 100, 10, 100, "ADD BRANCH", 255, 205, 255);
    program.add_btn(2 * MARGIN + BTN_W / 2 - MARGIN / 2, 3 * MARGIN + BTN_H * 2, BTN_W / 2 - MARGIN / 2, BTN_H, 100, 10, 100, "REMOVE", 255, 205, 255);
    program.add_btn(2 * MARGIN + BTN_W / 2 - MARGIN / 2, 4 * MARGIN + BTN_H * 3, BTN_W / 2 - MARGIN / 2, BTN_H, 100, 10, 100, "PICK OUT", 255, 205, 255);
    program.add_btn(MARGIN, 5 * MARGIN + BTN_H * 4, BTN_W, BTN_H, 100, 10, 100, "SHOW GRAPH'S INFO", 255, 205, 255);
  
    program.add_btn(MARGIN, WIN_HEIGHT - BTN_H - 2 * OUTL - MARGIN, BTN_W, BTN_H, 100, 10, 100, "ADD PAGE", 255, 205, 255);

    // Add text
    program.add_txt(MARGIN, 6 * MARGIN + BTN_H * 5, "VERTICES:", 255, 205, 255);
    program.add_txt(MARGIN + BTN_W / 2, 6 * MARGIN + BTN_H * 5, "0", 255, 205, 255);
    program.add_txt(MARGIN, 6 * MARGIN + BTN_H * 6, "BRANCHES:", 255, 205, 255);
    program.add_txt(MARGIN + BTN_W / 2, 6 * MARGIN + BTN_H * 6, "0", 255, 205, 255);

    // Add input
    program.add_input(MARGIN * 2 + BTN_W / 4, MARGIN, BTN_W / 4 * 3 - MARGIN, BTN_H, 205, 170, 205, 100, 10, 100);
    program.add_input(MARGIN * 2 + BTN_W / 4, 2 * MARGIN + BTN_H, BTN_W / 4 * 3 - MARGIN, BTN_H, 205, 170, 205, 100, 10, 100);
  
    program.add_input(MARGIN, WIN_HEIGHT - 2 * BTN_H - 4 * OUTL - MARGIN, BTN_W, BTN_H, 205, 170, 205, 100, 10, 100);

    // Add Page
    program.add_page(WIN_WIDTH - BTN_W - MARGIN - OUTL, MARGIN + OUTL, BTN_W, BTN_H, 100, 10, 100, "main", 255, 205, 255, true);
    program.onPage(0);

    // VertexCreator
    vertexCreator.add_txt(WIN_WIDTH / 2 - BTN_W / 3.1, WIN_HEIGHT / 2 - 600 / 2 + MARGIN, "VERTEX CREATOR", 100, 10, 100);
    vertexCreator.add_txt(WIN_WIDTH / 2 - 700 / 2 + MARGIN, WIN_HEIGHT / 2 - 600 / 2 + MARGIN * 2 + BTN_H, "NAME", 100, 10, 100);
    vertexCreator.add_input(WIN_WIDTH / 2, WIN_HEIGHT / 2 - 600 / 2 + MARGIN * 2 + BTN_H, 700 / 2 - MARGIN, BTN_H, 205, 170, 205, 100, 10, 100);
    vertexCreator.add_txt(WIN_WIDTH / 2 - 700 / 2 + MARGIN, WIN_HEIGHT / 2 - 600 / 2 + MARGIN * 3 + BTN_H * 2, "CONTENT", 100, 10, 100);
    vertexCreator.add_input(WIN_WIDTH / 2, WIN_HEIGHT / 2 - 600 / 2 + MARGIN * 3 + BTN_H * 2, 700 / 2 - MARGIN, BTN_H, 205, 170, 205, 100, 10, 100);
    vertexCreator.add_txt(WIN_WIDTH / 2 - 700 / 2 + MARGIN, WIN_HEIGHT / 2 - 600 / 2 + MARGIN * 4 + BTN_H * 3, "RGB", 100, 10, 100);
    vertexCreator.add_input(WIN_WIDTH / 2, WIN_HEIGHT / 2 - 600 / 2 + MARGIN * 4 + BTN_H * 3, 700 / 6 - MARGIN, BTN_H, 205, 170, 205, 100, 10, 100);
    vertexCreator.add_input(WIN_WIDTH / 2 + 700 / 6, WIN_HEIGHT / 2 - 600 / 2 + MARGIN * 4 + BTN_H * 3, 700 / 6 - MARGIN, BTN_H, 205, 170, 205, 100, 10, 100);
    vertexCreator.add_input(WIN_WIDTH / 2 + 700 / 6 * 2, WIN_HEIGHT / 2 - 600 / 2 + MARGIN * 4 + BTN_H * 3, 700 / 6 - MARGIN, BTN_H, 205, 170, 205, 100, 10, 100);
    vertexCreator.add_btn(WIN_WIDTH / 2 + 700 / 2 - BTN_W / 3.5 - MARGIN, WIN_HEIGHT / 2 + 600 / 2 - BTN_H * 2 - MARGIN, BTN_W / 3.5, BTN_H * 2, 100, 10, 100, "APPLY", 255, 205, 255);

    // BranchCreator
    branchCreator.add_txt(WIN_WIDTH / 2 - BTN_W / 3.1, WIN_HEIGHT / 2 - 400 / 2 + MARGIN, "BRANCH CREATOR", 100, 10, 100);
    branchCreator.add_txt(WIN_WIDTH / 2 - 500 / 2 + MARGIN, WIN_HEIGHT / 2 - 400 / 2 + MARGIN * 2 + BTN_H, "VERTIX", 100, 10, 100);
    branchCreator.add_input(WIN_WIDTH / 2, WIN_HEIGHT / 2 - 400 / 2 + MARGIN * 2 + BTN_H, 500 / 4 - MARGIN, BTN_H, 205, 170, 205, 100, 10, 100);
    branchCreator.add_input(WIN_WIDTH / 2 + 500 / 4, WIN_HEIGHT / 2 - 400 / 2 + MARGIN * 2 + BTN_H, 500 / 4 - MARGIN, BTN_H, 205, 170, 205, 100, 10, 100);
    branchCreator.add_txt(WIN_WIDTH / 2 - 500 / 2 + MARGIN, WIN_HEIGHT / 2 - 400 / 2 + MARGIN * 3 + BTN_H * 2, "WEIGHT", 100, 10, 100);
    branchCreator.add_input(WIN_WIDTH / 2, WIN_HEIGHT / 2 - 400 / 2 + MARGIN * 3 + BTN_H * 2, 500 / 2 - MARGIN, BTN_H, 205, 170, 205, 100, 10, 100);
    branchCreator.add_txt(WIN_WIDTH / 2 - 500 / 2 + MARGIN, WIN_HEIGHT / 2 - 400 / 2 + MARGIN * 4 + BTN_H * 3, "ORIENTED", 100, 10, 100);
    branchCreator.add_input(WIN_WIDTH / 2, WIN_HEIGHT / 2 - 400 / 2 + MARGIN * 4 + BTN_H * 3, 500 / 2 - MARGIN, BTN_H, 205, 170, 205, 100, 10, 100);
    branchCreator.add_btn(WIN_WIDTH / 2 + 500 / 2 - BTN_W / 3.5 - MARGIN, WIN_HEIGHT / 2 + 400 / 2 - BTN_H * 2 - MARGIN, BTN_W / 3.5, BTN_H * 2, 100, 10, 100, "APPLY", 255, 205, 255);

    // GraphInfo 
    graphInfo.add_btn(WIN_WIDTH / 2 - 1600 / 2 + MARGIN, WIN_HEIGHT / 2 - 900 / 2 + MARGIN, BTN_W, BTN_H, 100, 10, 100, "ADJACENCIES MATRIX", 255, 205, 255);
    graphInfo.add_btn(WIN_WIDTH / 2 - 1600 / 2 + MARGIN * 2 + BTN_W, WIN_HEIGHT / 2 - 900 / 2 + MARGIN, BTN_W, BTN_H, 100, 10, 100, "TRANSCENDENCE MATRIX", 255, 205, 255);
    graphInfo.add_txt(WIN_WIDTH / 2 - 1600 / 2 + MARGIN, WIN_HEIGHT / 2 - 900 / 2 + MARGIN * 2 + BTN_H, "", 100, 10, 100);

    graph.push_back(Graph());

    while (WINDOW.isOpen())
    {
        while (WINDOW.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                WINDOW.close();
        }
        // Switching menu items
        if (sf::Mouse::isButtonPressed(sf::Mouse::Left)) 
        {
            program.setTxt_toTxt(1, to_string(graph[program.getCurrentPage()].amountOfVertices()));
            program.setTxt_toTxt(3, to_string(graph[program.getCurrentPage()].amountOfBranches()));

            graph[program.getCurrentPage()].tryMoveVertex();

            program.select();
            // Vertex Creator 
            if (vertexCreator.isVis())
            {
                if (vertexCreator.isCursorInWindow())
                {
                    vertexCreator.select();
                    if (vertexCreator.isButtonPressed())
                    {
                        int vc_i = vertexCreator.IndexOfPressedButton();
                        switch (vc_i)
                        {
                        case 0:
                            // Apply
                            graph[program.getCurrentPage()].addVertex(vertexCreator.getTxt_fromInput(0), vertexCreator.getTxt_fromInput(1), RAD, stoi(vertexCreator.getTxt_fromInput(2)), stoi(vertexCreator.getTxt_fromInput(3)), stoi(vertexCreator.getTxt_fromInput(4)));
                            vertexCreator.offAll();
                            vertexCreator.hide();
                            break;
                        default:
                            cerr << "Error: " << vc_i << " button doesn't exist!" << endl;
                            break;
                        }
                    }
                }
                else 
                {
                    vertexCreator.hide();
                }
            }
            // Branch Creator 
            if (branchCreator.isVis())
            {
                if (branchCreator.isCursorInWindow())
                {
                    branchCreator.select();
                    if (branchCreator.isButtonPressed())
                    {
                        int bc_i = branchCreator.IndexOfPressedButton();
                        switch (bc_i)
                        {
                        case 0:
                            // Apply
                            graph[program.getCurrentPage()].addBranch(stoi(branchCreator.getTxt_fromInput(0)), stoi(branchCreator.getTxt_fromInput(1)), stoi(branchCreator.getTxt_fromInput(2)), stoi(branchCreator.getTxt_fromInput(3)));
                            branchCreator.offAll();
                            branchCreator.hide();
                            break;
                        default:
                            cerr << "Error: " << bc_i << " button doesn't exist!" << endl;
                            break;
                        }
                    }
                }
                else
                {
                    branchCreator.hide();
                }
            }
            // Graph Info  
            if (graphInfo.isVis())
            {
                if (graphInfo.isCursorInWindow())
                {
                    graphInfo.select();
                    if (graphInfo.isButtonPressed())
                    {
                        int gi_i = graphInfo.IndexOfPressedButton();
                        switch (gi_i)
                        {
                        case 0:
                            // ADJACENCIES MATRIX
                            graphInfo.setTxt_toTxt(0, graph[program.getCurrentPage()].getAdjacenciesMatrixAsStr());
                            break;
                        case 1:
                            // TRANSCENDENCE MATRIX
                            graphInfo.setTxt_toTxt(0, graph[program.getCurrentPage()].getTranscendenceMatrixAsStr());
                            break;

                        default:
                            cerr << "Error: " << gi_i << " button doesn't exist!" << endl;
                            break;
                        }
                    }
                }
                else
                {
                    graphInfo.setTxt_toTxt(0, "");
                    graphInfo.offAll();
                    graphInfo.hide();
                }
            }
        }
        else if (program.isButtonPressed())
        {
            run_btn_func(program, program.IndexOfPressedButton());
        }
        // Writing to inputs
        else if (program.isWrite())
        {
            int index = program.IndexOfPressedInput();
            string str = program.getTxt_fromInput(index);
            texting(str, program);
            program.setTxt_toInput(index, str);
        }
        if (vertexCreator.isWrite())
        {
            int index = vertexCreator.IndexOfPressedInput();
            string str = vertexCreator.getTxt_fromInput(index);
            texting(str, vertexCreator);
            vertexCreator.setTxt_toInput(index, str);
        }
        if (branchCreator.isWrite())
        {
            int index = branchCreator.IndexOfPressedInput();
            string str = branchCreator.getTxt_fromInput(index);
            texting(str, branchCreator);
            branchCreator.setTxt_toInput(index, str);
        }
        WINDOW.clear();
        program.draw();
        graph[program.getCurrentPage()].draw();
        vertexCreator.draw();
        branchCreator.draw();
        graphInfo.draw();
        WINDOW.display();
    }

    return 0;
}

void run_btn_func(Program& program, int i) 
{
    string temp_str;
    int temp_int;
    switch (i) 
    {
    case 0: 
        // Save
        cout << "0" << endl;
        break;
    case 1:
        // Load 
        cout << "1" << endl;
        break;
    case 2:
        // Add vertex
        vertexCreator.view();
        break;
    case 3:
        // Add branch
        branchCreator.view();
        break;
    case 4:
        // Remove 
        cout << "4" << endl;
        break;
    case 5:
        // Pick out 
        cout << "5" << endl;
        break;
    case 6:
        // Show info
        graphInfo.view();
        break;
    case 7:
        // Add Page
        temp_str = program.getTxt_fromInput(2);
        if (temp_str == "")
        {
            return;
        }
        temp_int = program.amountOfPages();
        program.add_page(WIN_WIDTH - BTN_W - MARGIN - OUTL, MARGIN + 2 * OUTL * (temp_int + 1) + BTN_H * temp_int - OUTL, BTN_W, BTN_H, 100, 10, 100, temp_str, 255, 205, 255);
        graph.push_back(Graph());
        Sleep(120);
        program.offAll();
        break;
    default: 
        cerr << "Error: " << i << " button doesn't exist!" << endl;
    }
}

template<class T>
void texting(string& str, T& win)
{
    if (event.type == sf::Event::TextEntered) // if press button
    {
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Enter))
        {
            win.offAll();
            win.stopWrite();
        }
        else if (sf::Keyboard::isKeyPressed(sf::Keyboard::BackSpace))
        {
            string temp = "";
            int length = (str.size() - 1 > 0) ? str.size() - 1 : 0;
            for (int i = 0; i < length; i++)
                temp += str[i];
            str = temp;
            Sleep(120);
            return;
        }
        else
        {
            char ch = '\0';
            if (event.text.unicode < 128) {
                ch = static_cast<char>(event.text.unicode);
                Sleep(120);
            }
            str += ch;
        }
    }
}
