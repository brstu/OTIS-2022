//---------------------------------------------------------------------------

#ifndef Unit2H
#define Unit2H
//---------------------------------------------------------------------------
#include <Classes.hpp>
#include <Controls.hpp>
#include <StdCtrls.hpp>
#include <Forms.hpp>
//---------------------------------------------------------------------------
class TTList;
class GraphNode;
class TForm2 : public TForm
{
__published:	// IDE-managed Components
     void __fastcall FormPaint(TObject *Sender);
private:	// User declarations
public:		// User declarations
     __fastcall TForm2(TComponent* Owner);
     TTList<GraphNode*>*nodes;
     void CreateGraph(TTList<GraphNode*>* list);
     void DrawGraph();
     void FindSvyaznost();
     void Obhod(GraphNode* node, int Oblast);
};
//---------------------------------------------------------------------------
extern PACKAGE TForm2 *Form2;
//---------------------------------------------------------------------------
#endif
 