//---------------------------------------------------------------------------

#ifndef Unit1H
#define Unit1H
//---------------------------------------------------------------------------
#include <Classes.hpp>
#include <Controls.hpp>
#include <StdCtrls.hpp>
#include <Forms.hpp>
#include <ComCtrls.hpp>
#include <ExtCtrls.hpp>
#include <Grids.hpp>
#include <Buttons.hpp>
//---------------------------------------------------------------------------
class TTList;
class GraphNode;
class TForm1 : public TForm
{
__published:	// IDE-managed Components
     TTabControl *TabControl1;
     TPaintBox *PB;
     TStringGrid *Grid;
     TLabel *Label1;
     TButton *Button1;
     TGroupBox *GroupBox1;
     TSpeedButton *btnVertex;
     TSpeedButton *btnLinks;
     TSpeedButton *btnMove;
     TButton *Button2;
     void __fastcall FormCreate(TObject *Sender);
     void __fastcall PBMouseDown(TObject *Sender, TMouseButton Button,
          TShiftState Shift, int X, int Y);
     void __fastcall PBPaint(TObject *Sender);
     void __fastcall PBMouseMove(TObject *Sender, TShiftState Shift, int X,
          int Y);
     void __fastcall PBMouseUp(TObject *Sender, TMouseButton Button,
          TShiftState Shift, int X, int Y);
     void __fastcall Button1Click(TObject *Sender);
     void __fastcall TabControl1Change(TObject *Sender);
     void __fastcall TabControl1Changing(TObject *Sender,
          bool &AllowChange);
     void __fastcall Button2Click(TObject *Sender);
private:	// User declarations
     TPoint PicSmesh;//Смещение всего рисунка(для скроллинга)
     TPoint PicSmeshMouseDelta;
     TPoint NewArrowEnd;
     TPoint LastClickedVertex; //позиция вершины, на какую мы щелкнули в последний раз
     GraphNode*LCV;//почти тоже самое, но только указатель на нее
     bool dragging;//Тянем ли мы что-то;
     bool Modified;//Граф был изменен.
public:		// User declarations
     __fastcall TForm1(TComponent* Owner);
     TTList<GraphNode*>*nodes;
     float GetAngle(float x1, float y1, float x2, float y2);
     void DrawArrow(int x1, int y1, int x2, int y2,int radius);
     Graphics::TBitmap*plane;
     bool DeleteNode(int vertex);
     void PaintPB();
     void DrawNodes(int type);
     void SynchronizeGraphAndGrid();
     int Deep_Deep(GraphNode* node, int nlevel, int ReqNumber);
     bool GetSortedGraph();
     int Clc;

};
class GraphNode
{
public:
TPoint pos;
TPoint pos2;//Отсортированные позиции
int Svyaznost;//Индентификатор области связности
TTList<GraphNode*>*links; //Это мы описали связи ВЫХОДЯЩИЕ из точки
int level; //При сортировке - на каком уровне находится вершина.
int rekursnumber;
GraphNode(int x,int y)
     {
     pos.x=x;
     pos.y=y;
     links=new TTList<GraphNode*>();
     level=-1;
     rekursnumber=clWhite;
     Svyaznost=0;
     }
~GraphNode()
     {
     links->Clear();
     delete links;
     }
bool IsLinkTo_Exist(GraphNode*vertex)//Есть ли у данной вершины связь с указанной вершиной
     {
     for(int i=0;i<links->Count;i++)
          {
          if(links->Get(i)==vertex)
               return true;//Мы нашли необходимую вершину
          }
     return false;
     }
bool DeleteLinksTo(GraphNode*vertex)//Удалить связь с указанной вершиной
     {
     for(int i=0;i<links->Count;i++)
          {
          if(links->Get(i)==vertex)
               {
               links->Delete(i);//Мы нашли необходимую вершину
               return true;
               }
          }
     return false;
     }
};
//---------------------------------------------------------------------------
extern PACKAGE TForm1 *Form1;
//---------------------------------------------------------------------------
#endif
