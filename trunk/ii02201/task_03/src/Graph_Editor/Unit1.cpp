//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop
#include<myclasses.cpp>
#include "Unit1.h"
#include "Unit2.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TForm1 *Form1;
const float M_RAD_CONV=M_PI/180.0;
int PointSize=5;//Радиус точки графа
int Requrs=0;
int Cycle=0;
//Управляем построением отсортированного графа
int SortLevelDistanceX=8;
int SortLevelDistanceY=8;

//---------------------------------------------------------------------------
//__fastcall TForm1::TForm1(TComponent* Owner)
//     : TForm(Owner)
//{
//}
//---------------------------------------------------------------------------
void __fastcall TForm1::FormCreate(TObject *Sender)
{
nodes=new TTList<GraphNode*>();
PicSmesh.x=0; PicSmesh.y=0;
PicSmeshMouseDelta.x=0;PicSmeshMouseDelta.y=0;
plane=new Graphics::TBitmap();
plane->Width=PB->Width;
plane->Height=PB->Height;
Modified=true;
}
//---------------------------------------------------------------------------
float TForm1::GetAngle(float x1, float y1, float x2, float y2)
{
float res=0;
if(y1==y2)
     {
     if(x2>=x1)
          res=0;
     if(x2<x1)
          res=M_PI;
     }else
if(x1==x2)//Сразу исключаем, если точки одна над другой.
     {
     if(y2==y1)
          res=0;
     if(y2>y1)
          res= 90.0*M_RAD_CONV;
     if(y2<y1)
          res= 270.0*M_RAD_CONV;
     }else
     {
     //float dx=x2-x1;
     //float dy=y2-y1;
     //float angle=atan2(y2-y1,x2-x1);
     res=atan2(y2-y1,x2-x1);
     if(res<0)
          {
          res=res*-1;
          res=M_PI-res+M_PI;
          }
     }
return res;
}

void TForm1::DrawArrow(int x1, int y1, int x2, int y2,int radius)
{
int ArrowCone=30;//Угол конуса стрелки
int ArrowConeLength=10;
float angle=GetAngle(x2,y2,x1,y1);
x2=cos(angle)*radius+x2;
y2=sin(angle)*radius+y2;
x1=cos(angle+M_PI)*radius+x1;
y1=sin(angle+M_PI)*radius+y1;
plane->Canvas->MoveTo(x2,y2);
plane->Canvas->LineTo(x1,y1);
float tangle=angle+(M_PI-ArrowCone*M_RAD_CONV);//Приплюсовуем к углу 180-20 градусов
int tx=cos(tangle)*ArrowConeLength+x1;
int ty=sin(tangle)*ArrowConeLength+y1;
plane->Canvas->LineTo(tx,ty);
tangle=angle+(M_PI+ArrowCone*M_RAD_CONV);//Приплюсовуем к углу 180+20 градусов
tx=cos(tangle)*ArrowConeLength+x1;
ty=sin(tangle)*ArrowConeLength+y1;
plane->Canvas->MoveTo(x1,y1);
plane->Canvas->LineTo(tx,ty);
}
//------------------------------------------------------------------------------
void __fastcall TForm1::PBMouseDown(TObject *Sender, TMouseButton Button,
      TShiftState Shift, int X, int Y)
{
int nX=X/10;
int nY=Y/10;
bool finded=false;
int i;
if(TabControl1->TabIndex==1)
     {
     PicSmeshMouseDelta.x=X-PicSmesh.x;
     PicSmeshMouseDelta.y=Y-PicSmesh.y;

     }
for(i=0;i<nodes->Count;i++)
     {
     if((nodes->Get(i)->pos.x==nX)&&(nodes->Get(i)->pos.y==nY))
          {
          finded=true;
          break;
          }
}
if(btnVertex->Down==true)
     {
     if(!finded)
          {
          GraphNode*newnode=new GraphNode(nX,nY);
          nodes->Add(newnode);
          }else
          {
          DeleteNode(i);
          }
     SynchronizeGraphAndGrid();
     Modified=true;
     }else
if(btnLinks->Down==true)
     {
     if(finded==true)
          {
          if(dragging==true)
               {
               LCV->links->Add(nodes->Get(i));
               }else
               {
               LastClickedVertex.x=nX;
               LastClickedVertex.y=nY;
               LCV=nodes->Get(i);
               NewArrowEnd.x=nX;
               NewArrowEnd.y=nY;
               dragging=true;
               }
          }else
          {
          if(Button==mbRight)
               {
               dragging=false;
               }
          }
     SynchronizeGraphAndGrid();
     Modified=true;
     }else
if(btnMove->Down==true)
     {
     if(finded==true)
          {
          LCV=nodes->Get(i);
          dragging=true;
          }
     }
PaintPB();
}
//---------------------------------------------------------------------------

bool TForm1::DeleteNode(int vertex)
{
GraphNode*temp=nodes->Get(vertex);
for(int i=0;i<nodes->Count;i++)
     {
     if(i==vertex)continue;
     nodes->Get(i)->DeleteLinksTo(temp);//Удаляем со всех вершин исходящие связи неа данную вершину
     }
delete nodes->Get(vertex);
nodes->Delete(vertex);
Modified=true;
return true;
}
//-----------------------------------------------------------------------------
void TForm1::PaintPB()
{
plane->Canvas->FillRect(Rect(0,0,plane->Width,plane->Height));
//if(TabControl1->TabIndex==0)
//     {
     DrawNodes(TabControl1->TabIndex);
//     }
if((dragging==true)&&(btnLinks->Down==true))
     {
     DrawArrow(NewArrowEnd.x*PointSize*2+PointSize,NewArrowEnd.y*PointSize*2+PointSize,LastClickedVertex.x*PointSize*2+PointSize,LastClickedVertex.y*PointSize*2+PointSize,0);
     }
PB->Canvas->Draw(0,0,plane);
}
//-----------------------------------------------------------------------------
void TForm1::DrawNodes(int type)
{
plane->Canvas->Font->Size=9;
int PointDiametr=PointSize*2;
for(int i=0;i<nodes->Count;i++)
     {
     GraphNode*temp=nodes->Get(i);

     int x1; int y1;
     if(type==0)
          {
          x1=temp->pos.x*PointDiametr;
          y1=temp->pos.y*PointDiametr;
          }else
     if(type==1)
          {
          x1=temp->pos2.x*PointDiametr+PicSmesh.x;
          y1=temp->pos2.y*PointDiametr+PicSmesh.y;
          }
     plane->Canvas->Font->Color=clBlue;
     plane->Canvas->Brush->Color=(TColor)nodes->Get(i)->rekursnumber;
     plane->Canvas->Ellipse(x1,y1,x1+PointDiametr,y1+PointDiametr);
     plane->Canvas->Brush->Color=clWhite;
     String text=IntToStr(i);
     SIZE size;
     GetTextExtentPoint32(plane->Canvas->Handle,text.c_str(),text.Length(),&size);
     SetBkMode(plane->Canvas->Handle,TRANSPARENT);
     plane->Canvas->TextOutA(x1-size.cx/2,y1+PointDiametr,text);
     plane->Canvas->TextOutA(x1-size.cx/2,y1-10,IntToStr(temp->level));
     for(int j=0;j<temp->links->Count;j++)
          {
          GraphNode*tlink=temp->links->Get(j);
          int x2;
          int y2;
          if(type==0)
               {
               x2=tlink->pos.x*PointDiametr+PointSize;
               y2=tlink->pos.y*PointDiametr+PointSize;
               }else
          if(type==1)
               {
               x2=tlink->pos2.x*PointDiametr+PointSize+PicSmesh.x;
               y2=tlink->pos2.y*PointDiametr+PointSize+PicSmesh.y;
               }
          DrawArrow(x2,y2,x1+PointSize,y1+PointSize,PointSize);
          }
     }
}
void __fastcall TForm1::PBPaint(TObject *Sender)
{
PaintPB();
}
//---------------------------------------------------------------------------
void __fastcall TForm1::PBMouseMove(TObject *Sender, TShiftState Shift,
      int X, int Y)
{
if((TabControl1->TabIndex==1)&&(Shift.Contains(ssRight)))
     {
     PicSmesh.x=X-PicSmeshMouseDelta.x;
     PicSmesh.y=Y-PicSmeshMouseDelta.y;
     PaintPB();
     return;
     }
if(dragging==false)return;
int nX=X/(PointSize*2);
int nY=Y/(PointSize*2);
if(btnLinks->Down==true)
     {
     NewArrowEnd.x=nX;
     NewArrowEnd.y=nY;
     }else
if(btnMove->Down==true)
     {
     LCV->pos.x=nX;
     LCV->pos.y=nY;
     }
PaintPB();
}
//---------------------------------------------------------------------------
void __fastcall TForm1::PBMouseUp(TObject *Sender, TMouseButton Button,
      TShiftState Shift, int X, int Y)
{
if(btnMove->Down==true)
     {
     dragging=false;
     }
}
//---------------------------------------------------------------------------


void TForm1::SynchronizeGraphAndGrid()
{
Grid->RowCount=nodes->Count+1;
Grid->ColCount=nodes->Count+1;
for(int i=0;i<nodes->Count;i++)
     {
     Grid->Cells[i+1][0]=IntToStr(i);
     Grid->Cells[0][i+1]=IntToStr(i);
     }
for(int j=0;j<nodes->Count;j++)
          for(int i=0;i<nodes->Count;i++)
               Grid->Cells[i+1][j+1]="";
for(int i=0;i<nodes->Count;i++)
     {
     GraphNode*tn=nodes->Get(i);
     for(int j=0;j<tn->links->Count;j++)//Пройдемся по всем связям данной вершины
          {
          int v=nodes->IndexOf(tn->links->Get(j));//Находим индекс вершины, на которую ссылаемся
          Grid->Cells[v+1][i+1]="1";
          Grid->Cells[i+1][v+1]="-1";
          }
     }
}
void __fastcall TForm1::Button1Click(TObject *Sender)
{
Clc=0;
for(int i=0;i<nodes->Count;i++)
     {
     nodes->Get(i)->level=-1;           //Очищаем все данные о уровнях и "цветах" вершин
     nodes->Get(i)->rekursnumber=(int)clWhite;
     }
//В этом цикле мы пройдем по матрице инцеденций, для того, чтобы найти те
//вершины, в которые не входит ни одна стрелка. Если таковых нету, тогда граф циклический,
//и НИЧЕГО ДЕЛАТЬ НЕ БУДЕМ.
int FirstLevelCount=0;
//bool DugaFinded=false;
//int arrowsInLine=0;
for(int j=0;j<nodes->Count;j++)
     {
     arrowsInLine=0;
     DugaFinded=false;
     for(int i=0;i<nodes->Count;i++)
          {
          if(Grid->Cells[i+1][j+1]=="I")
               {
               DugaFinded=true;
               }
          if(Grid->Cells[i+1][j+1]!="")arrowsInLine++;
          }

     if(arrowsInLine==0)//Обязательно должна быть хотя бы одна связь.
          {
          ShowMessage("Вершина "+IntToStr(j)+" не связана с остальными");
          break;
          }else
     if(DugaFinded==false)//Нет ни одной входящей дуги - 1 уровень.
          {
          FirstLevelCount++;
          Cycle=0;
          Requrs=0;
          Deep_Deep(nodes->Get(j),0,0);
          }
     }
if(Cycle!=0||Clc!=0)
     {
     ShowMessage("В графе обнаружен цикл. Работа прекращена");
     }
if(FirstLevelCount==0)
     {
     ShowMessage("Не найдено ни одной вершины первого уровня.");
     }

GetSortedGraph();
PaintPB();
Modified=false;
}
//---------------------------------------------------------------------------


int TForm1::Deep_Deep(GraphNode* node, int nlevel, int ReqNumber)
{
     if((node->level>=nlevel)||(Cycle!=0))return 0;
     if(ReqNumber==node->rekursnumber)
          {
          Cycle=1;
          Clc=1;
          return 0;
          }
     node->level=nlevel;
     node->rekursnumber=ReqNumber;
     for(int i=0;i<node->links->Count;i++)
          {
          Deep_Deep(node->links->Get(i),nlevel+1,ReqNumber);
          ReqNumber=random(10000000);//Выбираем случайное число для идентификации рекурсивной ветки
          }
return 0;
}
//-------------------------------------------------------------------------------
bool TForm1::GetSortedGraph()
{
for(int i=0;i<nodes->Count;i++) //Сначала посмотри, отсортирован ли у нас граф
     {
     if(nodes->Get(i)->level==-1)
          return -1;//Не должно быть ниодного -1 уровня.
     }
int levelx=1;
//int levely=14;
//int Vert_On_Level=0;
int UpDown=1;//Мы раскидываем по одной, то вверх, то вниз
for(int level=0;level<nodes->Count;level++)
     {
     Vert_On_Level=0;
     levely=14+random(28);
      for(int i=0;i<nodes->Count;i++)
          {
          if(nodes->Get(i)->level==level)
               {
               nodes->Get(i)->pos2.x=levelx;
               nodes->Get(i)->pos2.y=levely+(Vert_On_Level*SortLevelDistanceY*UpDown)+random(20)*UpDown;
               if(UpDown==1)
               Vert_On_Level++;

               UpDown*=-1;
               }
          }
     levelx+=SortLevelDistanceX;
     }
return true;
}
void __fastcall TForm1::TabControl1Change(TObject *Sender)
{
PicSmesh.x=0;
PicSmesh.y=0;
PicSmeshMouseDelta.x=0;
PicSmeshMouseDelta.y=0;
dragging=false;
PaintPB();
if(TabControl1->TabIndex==1)
     {
   //  Button1->Enabled=false;
     btnLinks->Down=false;
     btnLinks->Enabled=false;
     btnMove->Down=false;
     btnMove->Enabled=false;
     btnVertex->Down=false;
     btnVertex->Enabled=false;
     }else
     {
     Button1->Enabled=true;
     btnLinks->Down=false;
     btnLinks->Enabled=true;
     btnMove->Down=false;
     btnMove->Enabled=true;
     btnVertex->Down=false;
     btnVertex->Enabled=true;
     }
}
//---------------------------------------------------------------------------
void __fastcall TForm1::TabControl1Changing(TObject *Sender,
      bool &AllowChange)
{
if(Modified==true)AllowChange=false;
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button2Click(TObject *Sender)
{
Form2->CreateGraph(nodes);
Form2->ShowModal();
}
//---------------------------------------------------------------------------

