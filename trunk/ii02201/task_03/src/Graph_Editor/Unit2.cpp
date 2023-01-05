//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include<myclasses.cpp>
#include "Unit2.h"
#include "Unit1.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TForm2 *Form2;
extern int PointSize;
int Area;
TColor*colors;
//---------------------------------------------------------------------------
__fastcall TForm2::TForm2(TComponent* Owner)
     : TForm(Owner)
{
nodes=new TTList<GraphNode*>();
}
//---------------------------------------------------------------------------

void TForm2::CreateGraph(TTList<GraphNode*>* list)
{
//Тут мы просто копируем граф. Пока еще граф ориентированный
nodes->DeleteAll();
for(int i=0;i<list->Count;i++)
     {
     GraphNode*node=new GraphNode(list->Get(i)->pos.x,list->Get(i)->pos.y);
     node->Svyaznost=-1;
     nodes->Add(node);
     }
for(int i=0;i<list->Count;i++)
     {
     for(int j=0;j<list->Get(i)->links->Count;j++)
          {
          GraphNode*node=nodes->Get(i);
          node->links->Add(nodes->Get(list->Find(list->Get(i)->links->Get(j))));
          }
     }
//А тут мы его пытаемся обнеориентирить
for(int i=0;i<nodes->Count;i++)
     {
     GraphNode*n=nodes->Get(i);
     for(int j=0;j<nodes->Count;j++)
          {
          if(i==j)continue;//Саму себя мы не смотрим
          if(n->IsLinkTo_Exist(nodes->Get(j)))continue; //Если туда уже есть связь, то ничего не делаем
          if(nodes->Get(j)->IsLinkTo_Exist(n))//А если есть связь оттуда, то мы делаем связь и туда
               {
               n->links->Add(nodes->Get(j));
               }
          }
     }
//После всех этих манипуляций у нас выходит неориентированный граф
FindSvyaznost();
}
//------------------------------------------------------------------------------
void TForm2::FindSvyaznost()
{
Area=1;
for(int i=0;i<nodes->Count;i++)
     {
     if(nodes->Get(i)->Svyaznost!=-1)continue;//Это значит, что вершина уже принадлежит какой-то области связности
     Obhod(nodes->Get(i),Area);
     Area++;
     }
colors = new TColor[Area];
for(int i=0;i<Area;i++)
     {
     colors[i]=(TColor)RGB(random(256),random(256),random(256));
     }
}
//------------------------------------------------------------------------------

void TForm2::Obhod(GraphNode* node, int Oblast)
{

if(node->Svyaznost!=-1)return;
node->Svyaznost=Oblast;
for(int i=0;i<node->links->Count;i++)
     {
     Obhod(node->links->Get(i),Oblast);
     }
}
//------------------------------------------------------------------------------

void TForm2::DrawGraph()
{
Canvas->Font->Size=9;
int PointDiametr=PointSize*2;
for(int i=0;i<nodes->Count;i++)
     {
     int x1; int y1;
     GraphNode*temp=nodes->Get(i);
     x1=temp->pos.x*PointDiametr;
     y1=temp->pos.y*PointDiametr;
     Canvas->Font->Color=clBlue;
     //Canvas->TextOutA(x1,y1-PointDiametr-5,IntToStr(temp->Svyaznost));
   //  Canvas->Brush->Color=(TColor)nodes->Get(i)->rekursnumber;
     Canvas->Brush->Color=colors[temp->Svyaznost];
     Canvas->Ellipse(x1,y1,x1+PointDiametr,y1+PointDiametr);


     for(int j=0;j<temp->links->Count;j++)
          {
          GraphNode*tlink=temp->links->Get(j);
          int x2; int y2;
          x2=tlink->pos.x*PointDiametr+PointSize;
          y2=tlink->pos.y*PointDiametr+PointSize;
          Canvas->MoveTo(x2,y2);
          Canvas->LineTo(x1+PointSize,y1+PointSize);
          }
     }
}
//------------------------------------------------------------------------------

void __fastcall TForm2::FormPaint(TObject *Sender)
{
DrawGraph();
}
//------------------------------------------------------------------------------

