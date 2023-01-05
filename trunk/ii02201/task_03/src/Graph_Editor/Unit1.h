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
     TPoint PicSmesh;//�������� ����� �������(��� ����������)
     TPoint PicSmeshMouseDelta;
     TPoint NewArrowEnd;
     TPoint LastClickedVertex; //������� �������, �� ����� �� �������� � ��������� ���
     GraphNode*LCV;//����� ���� �����, �� ������ ��������� �� ���
     bool dragging;//����� �� �� ���-��;
     bool Modified;//���� ��� �������.
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
TPoint pos2;//��������������� �������
int Svyaznost;//�������������� ������� ���������
TTList<GraphNode*>*links; //��� �� ������� ����� ��������� �� �����
int level; //��� ���������� - �� ����� ������ ��������� �������.
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
bool IsLinkTo_Exist(GraphNode*vertex)//���� �� � ������ ������� ����� � ��������� ��������
     {
     for(int i=0;i<links->Count;i++)
          {
          if(links->Get(i)==vertex)
               return true;//�� ����� ����������� �������
          }
     return false;
     }
bool DeleteLinksTo(GraphNode*vertex)//������� ����� � ��������� ��������
     {
     for(int i=0;i<links->Count;i++)
          {
          if(links->Get(i)==vertex)
               {
               links->Delete(i);//�� ����� ����������� �������
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
