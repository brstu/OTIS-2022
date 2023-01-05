#ifndef FUNC_H
#define FUNC_H

#include <Windows.h>
#include <windowsx.h>
#include <tchar.h>
#include <CommCtrl.h>
#include <vector>
#include <string.h>
#include "resource.h"

// Константы
#define NUM_BUTTONS 9
#define SEPARATOR_WIDTH 30
#define ID_TOOLBAR 201
#define ID_STATUS 202
#define GWND 50

#define APPNAME TEXT("Граф")


struct Vertex {
	int num; // Номер вершины
	HWND h; // описатель
	POINT pos; // позиция
};

//// "Системные" функции

// Добавление нового класса
bool AddWindowClass(TCHAR *, HINSTANCE, LRESULT (WINAPI *pWndProc)(HWND, UINT, WPARAM, LPARAM), 
					TCHAR * = NULL, UINT = CS_HREDRAW | CS_VREDRAW, int = WHITE_BRUSH, TCHAR *szIcon = IDI_APPLICATION);
// Создание новой вершины
Vertex CreateVertex(HWND hwnd);
// Получение номера вершины
int GetVertexNum(HWND hwnd);
// Получение описателя вершины
HWND GetVertexHwnd(int num);
// Получение координат вершины
bool GetVertexPos(int num, POINT &pt);
// Установить позицию окна
bool SetVertexPos(HWND hwnd, int x, int y);
// Есть ли связь
bool IsStay(int n, int m);
// Сохранить файл?
void DoYouWantSaveIt(HWND h);


// Создание панели инструментов
HWND InitToolBar(HWND);
////


//// Процедуры окон

// Процедура основного окна
LRESULT CALLBACK WndProc(HWND, UINT, WPARAM, LPARAM);

// Обработка сообщений:
void Cls_OnPaint(HWND hwnd);
BOOL Cls_OnCreate(HWND hwnd, LPCREATESTRUCT lpCreateStruct);
void Cls_OnClose(HWND hwnd);
void Cls_OnSize(HWND hwnd, UINT state, int cx, int cy);
void Cls_OnRButtonDown(HWND hwnd, BOOL fDoubleClick, int x, int y, UINT keyFlags);
void Cls_OnRButtonUp(HWND hwnd, int x, int y, UINT flags);
void Cls_OnLButtonDown(HWND hwnd, BOOL fDoubleClick, int x, int y, UINT keyFlags);
void Cls_OnLButtonUp(HWND hwnd, int x, int y, UINT keyFlags);
void Cls_OnMouseMove(HWND hwnd, int x, int y, UINT keyFlags);
void Cls_OnDestroy(HWND hwnd);
void Cls_OnCommand(HWND hwnd, int id, HWND hwndCtl, UINT codeNotify);

// Процедура обработки вершин графа
LRESULT CALLBACK GrafProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

// Обработка сообщений
void G_Cls_OnPaint(HWND hwnd);
BOOL G_Cls_OnCreate(HWND hwnd, LPCREATESTRUCT lpCreateStruct);
void G_Cls_OnClose(HWND hwnd);
void G_Cls_OnSize(HWND hwnd, UINT state, int cx, int cy);
void G_Cls_OnLButtonDown(HWND hwnd, BOOL fDoubleClick, int x, int y, UINT keyFlags);
void G_Cls_OnLButtonUp(HWND hwnd, int x, int y, UINT keyFlags);
void G_Cls_OnMouseMove(HWND hwnd, int x, int y, UINT keyFlags);
void G_Cls_OnRButtonDown(HWND hwnd, BOOL fDoubleClick, int x, int y, UINT keyFlags);
void G_Cls_OnRButtonUp(HWND hwnd, int x, int y, UINT flags);
////
// Диалоги
BOOL CALLBACK AboutProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam);
BOOL CALLBACK EdgeProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam);
BOOL CALLBACK PropProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam);
BOOL CALLBACK NastProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam);
BOOL CALLBACK ColProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam);

#endif