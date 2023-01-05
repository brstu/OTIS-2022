#ifndef FUNC_H
#define FUNC_H

#include <Windows.h>
#include <windowsx.h>
#include <tchar.h>
#include <CommCtrl.h>
#include <vector>
#include <string.h>
#include "resource.h"

// ���������
#define NUM_BUTTONS 9
#define SEPARATOR_WIDTH 30
#define ID_TOOLBAR 201
#define ID_STATUS 202
#define GWND 50

#define APPNAME TEXT("����")


struct Vertex {
	int num; // ����� �������
	HWND h; // ���������
	POINT pos; // �������
};

//// "���������" �������

// ���������� ������ ������
bool AddWindowClass(TCHAR *, HINSTANCE, LRESULT (WINAPI *pWndProc)(HWND, UINT, WPARAM, LPARAM), 
					TCHAR * = NULL, UINT = CS_HREDRAW | CS_VREDRAW, int = WHITE_BRUSH, TCHAR *szIcon = IDI_APPLICATION);
// �������� ����� �������
Vertex CreateVertex(HWND hwnd);
// ��������� ������ �������
int GetVertexNum(HWND hwnd);
// ��������� ��������� �������
HWND GetVertexHwnd(int num);
// ��������� ��������� �������
bool GetVertexPos(int num, POINT &pt);
// ���������� ������� ����
bool SetVertexPos(HWND hwnd, int x, int y);
// ���� �� �����
bool IsStay(int n, int m);
// ��������� ����?
void DoYouWantSaveIt(HWND h);


// �������� ������ ������������
HWND InitToolBar(HWND);
////


//// ��������� ����

// ��������� ��������� ����
LRESULT CALLBACK WndProc(HWND, UINT, WPARAM, LPARAM);

// ��������� ���������:
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

// ��������� ��������� ������ �����
LRESULT CALLBACK GrafProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

// ��������� ���������
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
// �������
BOOL CALLBACK AboutProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam);
BOOL CALLBACK EdgeProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam);
BOOL CALLBACK PropProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam);
BOOL CALLBACK NastProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam);
BOOL CALLBACK ColProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam);

#endif