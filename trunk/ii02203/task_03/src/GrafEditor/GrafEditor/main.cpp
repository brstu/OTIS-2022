#include "func.h"

HINSTANCE g_hInst;


int WINAPI WinMain(HINSTANCE hInst, HINSTANCE, LPSTR lpCmdLine, int nCmdShow)
{
	HWND hWnd;
	MSG msg;

	g_hInst = hInst;

	TCHAR szClassName[] = TEXT("MainClass");
	

	if(!AddWindowClass(szClassName, hInst, WndProc, MAKEINTRESOURCE(IDR_MENU2), CS_HREDRAW | CS_VREDRAW, WHITE_BRUSH, MAKEINTRESOURCE(IDI_ICON1))) {
		MessageBox(NULL, TEXT("Не могу зарегистрировать основной класс."), TEXT("Ошибка"), MB_OK);
		return 0;
	}
	

	hWnd = CreateWindow(szClassName, APPNAME, WS_OVERLAPPEDWINDOW, CW_USEDEFAULT, 0, CW_USEDEFAULT, 0, 
		                NULL, NULL, hInst, NULL);
	if(!hWnd) {
		MessageBox(NULL, TEXT("Не могу создать основное окно."), TEXT("Ошибка"), MB_OK);
		return 0;
	}

	ShowWindow(hWnd, SW_SHOW);

	while (GetMessage(&msg, NULL, 0, 0)) {
		TranslateMessage(&msg);
		DispatchMessage(&msg);
	}
	return 0;
} 

