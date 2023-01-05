#include "func.h"
HWND g_hToolBar, g_hStatus;
HMENU g_hMenu;

TCHAR g_szGrafClass[] = TEXT("GrafClass");
TCHAR g_CurName[MAX_PATH] = TEXT("Новый проект");

std::vector<Vertex> g_Ver; // массив вершин
std::vector<POINT> g_Edge; // массив ребер
std::vector<int> g_DelVer; // массив удаленных "вершин"

int g_index;
POINT g_pt;
bool g_Move = false, g_MenuStat = false;
bool g_Saved = true;
HWND g_hMove = NULL, g_hDel = NULL;

int GMAX = 50;
int g_t = 2;
int g_tt = 2;
int g_r = 0, g_b = 0, g_g = 0;
int g_rt = 0, g_bt = 0, g_gt = 0;


// Регистрация нового класса окна
bool AddWindowClass(TCHAR * pClassName, HINSTANCE hInst, LRESULT (WINAPI *pWndProc)(HWND, UINT, WPARAM, LPARAM),
					TCHAR * pMenuName, UINT uStyle, int nBrush, TCHAR *szIcon)
{
	WNDCLASSEX wc;
	wc.cbSize = sizeof(wc);
	wc.cbClsExtra = 0;
	wc.cbWndExtra = 0;
	wc.hbrBackground = (HBRUSH) GetStockObject(nBrush);
	wc.hCursor = LoadCursor(NULL, IDC_ARROW);
	wc.hIcon = LoadIcon(hInst, szIcon);
	wc.hIconSm = LoadIcon(hInst, szIcon);
	
	wc.hInstance = hInst;
	wc.lpfnWndProc = pWndProc;
	wc.lpszClassName = pClassName;
	wc.lpszMenuName = pMenuName;
	wc.style = uStyle;

	if(!RegisterClassEx(&wc)){
		return FALSE;
	}
	
	return TRUE;
}

// Создание новой вершины
Vertex CreateVertex(HWND hwnd) {
	Vertex t;
	POINT pt;
	HWND hTemp = CreateWindow(g_szGrafClass, TEXT(""), WS_CHILD, GMAX, GMAX + 30, GMAX, GMAX, hwnd,
				                      NULL, (HINSTANCE) GetWindowLong(hwnd, GWLP_HINSTANCE), NULL);
	if(!hTemp) {
		MessageBox(NULL, TEXT("Не могу создать вершину."), TEXT("Ошибка"), MB_OK);
		DestroyWindow(hwnd);
	}

	ShowWindow(hTemp, SW_SHOW);
	
	pt.x = GMAX;
	pt.y = GMAX + 30;

	if(g_DelVer.size() != 0) {
		t.num = g_DelVer[g_DelVer.size()-1];
		g_DelVer.pop_back();
	}
	else {
		t.num = g_Ver.size() + 1;
	}

	t.h = hTemp;
	t.pos = pt;

	return t;		
}
// Получение номера вершины
int GetVertexNum(HWND hwnd)
{
	int n = -1;
	for(size_t i=0; i < g_Ver.size(); i++) {
		if(hwnd == g_Ver[i].h)
			n = g_Ver[i].num;
	}
	return n;
}

// Получение описателя вершины
HWND GetVertexHwnd(int num) {
	HWND h = NULL;
	for(size_t i=0; i < g_Ver.size(); i++) {
		if(num == g_Ver[i].num) {
			h = g_Ver[i].h;
		}
	}
	return h;
}

// Получение координат вершины
bool GetVertexPos(int num, POINT &pt){
	bool s = false;
	for(size_t i=0; i < g_Ver.size(); i++) {
		if(num == g_Ver[i].num) {
			pt.x = g_Ver[i].pos.x;
			pt.y = g_Ver[i].pos.y;
			s = true;
		}
	}
	return s;
}

// Установить позицию окна
bool SetVertexPos(HWND hwnd, int x, int y) {
	bool n = false;
	for(size_t i=0; i < g_Ver.size(); i++) {
		if(hwnd == g_Ver[i].h) {
			g_Ver[i].pos.x = x;
			g_Ver[i].pos.y = y;
			n = true;
		}
	}
	
	return n;
}

bool IsStay(int n, int m)
{
	bool status = false;
	for(size_t i=0;i<g_Edge.size();i++) {
		if(n == g_Edge[i].x && m == g_Edge[i].y) {
			status = true;
			g_index = i;
		}
		else if(n == g_Edge[i].y && m == g_Edge[i].x) {
			status = true;
			g_index = i;
		}
	}
	return status;
}
// Сохранить файл?
void DoYouWantSaveIt(HWND h) {
	int n = MessageBox(NULL, TEXT("Сохранить проект перед выходом?"),
		               TEXT("Выход"), MB_YESNOCANCEL | MB_ICONINFORMATION);

	switch(n) {
	case IDYES:
		SendMessage(h, WM_COMMAND, MAKEWPARAM(ID_GSAVE, 0), (LPARAM)h);
		break;
	case IDNO:
		DestroyWindow(h);
		break;
	case IDCANCEL:
		break;
	}
}
// Создание панели инструментов
HWND InitToolBar(HWND hWnd) 
{
	HWND hToolBar;
	int nButId[NUM_BUTTONS] = {ID_GNEW, ID_GOPEN, ID_GSAVE, ID_SEP, ID_GVER, ID_GDUGA, ID_GTABLE, ID_SEP, ID_EXIT};
	int nButStyle[NUM_BUTTONS] = {TBSTYLE_BUTTON, TBSTYLE_BUTTON, TBSTYLE_BUTTON, TBSTYLE_SEP,
		                          TBSTYLE_BUTTON, TBSTYLE_BUTTON, TBSTYLE_BUTTON, TBSTYLE_SEP, TBSTYLE_BUTTON};


	TBBUTTON tbb[NUM_BUTTONS];

	const TCHAR* str[NUM_BUTTONS] = {TEXT("Новый"), TEXT("Открыть"), TEXT("Сохранить"), TEXT(""),
		                      TEXT("Вершина"), TEXT("Ребро"), TEXT("Настройки"), TEXT(""), TEXT("Выход")};

	memset(tbb, 0, sizeof(tbb));

	for(int i=0; i < NUM_BUTTONS; i++) {
		if(nButId[i] == ID_SEP)
			tbb[i].iBitmap = SEPARATOR_WIDTH;
		else
			tbb[i].iBitmap = i;

		tbb[i].idCommand = nButId[i];
		tbb[i].fsState = TBSTATE_ENABLED;
		tbb[i].fsStyle = nButStyle[i];
		tbb[i].iString = (INT_PTR) str[i];
	}

	hToolBar = CreateToolbarEx(hWnd, WS_CHILD | WS_VISIBLE | WS_BORDER | TBSTYLE_TOOLTIPS | TBSTYLE_WRAPABLE,
		ID_TOOLBAR, NUM_BUTTONS, GetModuleHandle(NULL), IDR_TOOLBAR1, 
		tbb, NUM_BUTTONS, 0, 0, 0, 0, sizeof(TBBUTTON));

	return hToolBar;
}


// Процедура основного окна
LRESULT CALLBACK WndProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
	
	switch(uMsg) {
		HANDLE_MSG(hwnd, WM_PAINT, Cls_OnPaint);
		HANDLE_MSG(hwnd, WM_CREATE, Cls_OnCreate);
		HANDLE_MSG(hwnd, WM_SIZE, Cls_OnSize);
		HANDLE_MSG(hwnd, WM_RBUTTONDOWN, Cls_OnRButtonDown);
		HANDLE_MSG(hwnd, WM_RBUTTONUP, Cls_OnRButtonUp);
		HANDLE_MSG(hwnd, WM_LBUTTONDOWN, Cls_OnLButtonDown);
		HANDLE_MSG(hwnd, WM_LBUTTONUP, Cls_OnLButtonUp);
		HANDLE_MSG(hwnd, WM_MOUSEMOVE, Cls_OnMouseMove);
		
		HANDLE_MSG(hwnd, WM_CLOSE, Cls_OnClose);
		HANDLE_MSG(hwnd, WM_DESTROY, Cls_OnDestroy);
		HANDLE_MSG(hwnd, WM_COMMAND, Cls_OnCommand);
	default:
		return DefWindowProc(hwnd, uMsg, wParam, lParam);
		break;
	}
	return 0;
}

void Cls_OnPaint(HWND hwnd) {
	
	PAINTSTRUCT pt;
	POINT p1, p2;
	HPEN hPen;
	HDC hdc = BeginPaint(hwnd, &pt);

	hPen = (HPEN) SelectObject(hdc, CreatePen(PS_SOLID, g_t, RGB(g_r, g_g, g_b)));	
	
	if(g_Edge.size() > 0 && g_Move == FALSE) {
		for(size_t i = 0; i < g_Edge.size(); i++) {
			GetVertexPos(g_Edge[i].x, p1);
			GetVertexPos(g_Edge[i].y, p2);

			MoveToEx(hdc, p1.x + GMAX/2, p1.y + GMAX/2, NULL);
			LineTo(hdc, p2.x + GMAX/2, p2.y + GMAX/2);
		}
	}

	DeleteObject(SelectObject(hdc, hPen));
	EndPaint(hwnd, &pt);
	
}
BOOL Cls_OnCreate(HWND hwnd, LPCREATESTRUCT lpCreateStruct) {

	if(!AddWindowClass(g_szGrafClass, GetModuleHandle(NULL), GrafProc, NULL, CS_HREDRAW | CS_VREDRAW, NULL_BRUSH)) {
		MessageBox(NULL, TEXT("Не могу зарегистрировать класс вершин графа."), TEXT("Ошибка"), MB_OK);
		return false;
	}
	g_hMenu = LoadMenu(GetModuleHandle(NULL), MAKEINTRESOURCE(IDR_MENU1));
	g_hMenu = GetSubMenu(g_hMenu, 0);
	TCHAR buf[MAX_PATH];
	_stprintf(buf, TEXT("%s - %s"), APPNAME, g_CurName);
	SetWindowText(hwnd, buf);
	g_hToolBar = InitToolBar(hwnd);
	SendMessage(g_hToolBar, TB_AUTOSIZE, 0, 0);
	g_hStatus = CreateStatusWindow(WS_CHILD | WS_VISIBLE, TEXT(""), hwnd, ID_STATUS);
	SendMessage(g_hStatus, SB_SETTEXT, 0, (LONG) g_CurName);

	return true;
}

void Cls_OnClose(HWND hwnd) {
	if(!g_Saved)
		DoYouWantSaveIt(hwnd);
	else
		DestroyWindow(hwnd);
}

void Cls_OnSize(HWND hwnd, UINT state, int cx, int cy) {
	SendMessage(g_hToolBar, TB_AUTOSIZE, 0, 0);
	SendMessage(g_hStatus, WM_SIZE, cx, cy);
}

void Cls_OnRButtonDown(HWND hwnd, BOOL fDoubleClick, int x, int y, UINT keyFlags) {
	POINT pt;
	GetCursorPos(&pt);

	if(g_MenuStat) {
		EnableMenuItem(g_hMenu, ID_DEL, MF_BYCOMMAND | MF_ENABLED);
		EnableMenuItem(g_hMenu, ID_INFO, MF_BYCOMMAND | MF_ENABLED);
	}
	TrackPopupMenuEx(g_hMenu, 0, pt.x, pt.y, hwnd, NULL);
	if(g_MenuStat) {
		ScreenToClient (hwnd, &pt);
		g_pt.x = pt.x;
		g_pt.y = pt.y;
	}

	EnableMenuItem(g_hMenu, ID_DEL, MF_BYCOMMAND | MF_DISABLED);
	EnableMenuItem(g_hMenu, ID_INFO, MF_BYCOMMAND | MF_DISABLED);
	g_MenuStat = false;
}
void Cls_OnRButtonUp(HWND hwnd, int x, int y, UINT flags) {
}
void Cls_OnLButtonDown(HWND hwnd, BOOL fDoubleClick, int x, int y, UINT keyFlags) {

	POINT pt;
    GetCursorPos (&pt);
    ScreenToClient (hwnd, &pt);

	g_hMove = ChildWindowFromPoint(hwnd, pt);
	if(g_hMove != NULL && g_hMove != hwnd) {
		g_Move = true;
		InvalidateRect(hwnd, NULL, true);
	}
}

void Cls_OnLButtonUp(HWND hwnd, int x, int y, UINT keyFlags) {
	g_Move = false;
	if(g_hMove != NULL && g_hMove != hwnd) {
		POINT pt;
		GetCursorPos (&pt);
		ScreenToClient (hwnd, &pt);
		SetVertexPos(g_hMove, pt.x, pt.y);
		g_hMove = NULL;
	}
	
	InvalidateRect(hwnd, NULL, true);
}

void Cls_OnMouseMove(HWND hwnd, int x, int y, UINT keyFlags) {
	if(g_Move == true) {
		MoveWindow(g_hMove, x, y, GMAX, GMAX, true);
	}
}

void Cls_OnDestroy(HWND hwnd) {
	PostQuitMessage(0);
}

void Cls_OnCommand(HWND hwnd, int id, HWND hwndCtl, UINT codeNotify) {
	TCHAR buf[100];
	int n, m;

	OPENFILENAME ofn;
	TCHAR szFile[MAX_PATH];
	TCHAR szDefExt[MAX_PATH];
	TCHAR szPath[MAX_PATH];
	HANDLE hFile;
	DWORD dw;

	GetCurrentDirectory(MAX_PATH, szPath);

	ZeroMemory(&ofn, sizeof(ofn));
	ofn.lStructSize = sizeof(ofn);
	ofn.hwndOwner = NULL;
	ofn.lpstrFile = szFile;
	ofn.lpstrFile[0] = '\0';
	ofn.nMaxFile = sizeof(szFile);
	ofn.lpstrFilter = TEXT("Проект графа\0*.grph\0");
	ofn.lpstrDefExt = szDefExt;
	ofn.nFilterIndex = 1;
	ofn.lpstrFileTitle = NULL;
	ofn.nMaxFileTitle = 0;
	ofn.lpstrInitialDir = szPath;
	ofn.Flags = 0;

	Vertex vert = {0};
	POINT pt;

	switch(id) {
	case ID_GNEW:
		if(!g_Saved) {
			n = MessageBox(NULL, TEXT("Сохранить проект перед продолжением?"),
		              TEXT(""), MB_YESNO | MB_ICONINFORMATION);
			switch(n) {
			case IDYES:
				SendMessage(hwnd, WM_COMMAND, MAKEWPARAM(ID_GSAVE, 0), (LPARAM)hwnd);
				break;
			case IDNO:
				break;
			}
		}

		_stprintf(buf, TEXT("Выполняется создание пустого проекта..."));
	    SetWindowText(g_hStatus, buf);

		g_Edge.clear(); // массив ребер
		g_DelVer.clear(); // массив удаленных "вершин"
		
		for(size_t t=0; t<g_Ver.size(); t++) {
			DestroyWindow(g_Ver[t].h);
		}
		g_Ver.clear();

		InvalidateRect(hwnd, NULL, TRUE);
		_stprintf(buf, TEXT("%s - %s"), APPNAME, g_CurName);
		SetWindowText(hwnd, buf);
		SendMessage(g_hStatus, SB_SETTEXT, 0, (LONG) g_CurName);
	    g_Saved = true;
		break;
	case ID_GOPEN:
		if(!g_Saved) {
			n = MessageBox(NULL, TEXT("Сохранить проект перед продолжением?"),
		              TEXT(""), MB_YESNO | MB_ICONINFORMATION);
			switch(n) {
			case IDYES:
				SendMessage(hwnd, WM_COMMAND, MAKEWPARAM(ID_GSAVE, 0), (LPARAM)hwnd);
				break;
			case IDNO:
				break;
			}
		}


		if(!GetOpenFileName(&ofn)) {
			SetWindowText(g_hStatus, TEXT("Открытие проекта отменено!"));
		}
		else {
			g_Edge.clear(); // массив ребер
			g_DelVer.clear(); // массив удаленных "вершин"
			for(size_t t=0; t<g_Ver.size(); t++) {
				DestroyWindow(g_Ver[t].h);
			}
			g_Ver.clear();
			InvalidateRect(hwnd, NULL, TRUE);

			hFile = CreateFile(ofn.lpstrFile, GENERIC_READ | GENERIC_WRITE, 0, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);

			SetWindowText(g_hStatus, TEXT("Выполняется загрузка..."));

			SetFilePointer(hFile,0,0,FILE_BEGIN);

			ReadFile(hFile,&n,sizeof(n),&dw,NULL);

			for(int k=0;k<n;k++) {

				ReadFile(hFile,&vert,sizeof(vert),&dw,NULL);

				vert.h = CreateWindow(g_szGrafClass, TEXT(""), WS_CHILD, vert.pos.x, vert.pos.y, GMAX, GMAX, hwnd,
				                      NULL, (HINSTANCE) GetWindowLong(hwnd, GWLP_HINSTANCE), NULL);
				if(!vert.h) {
					MessageBox(NULL, TEXT("Не могу создать вершину."), TEXT("Ошибка"), MB_OK);
					DestroyWindow(hwnd);
				}
				ShowWindow(vert.h, SW_SHOW);
				g_Ver.push_back(vert);
			}

			ReadFile(hFile,&n,sizeof(n),&dw,NULL);

			for(int k=0;k<n;k++) {

				ReadFile(hFile,&pt,sizeof(pt),&dw,NULL);

				g_Edge.push_back(pt);
			}

			ReadFile(hFile,&n,sizeof(n),&dw,NULL);

			for(int k=0;k<n;k++) {

				ReadFile(hFile,&m,sizeof(m),&dw,NULL);

				g_DelVer.push_back(m);
			}

			SetWindowText(g_hStatus, TEXT("Успешно: Проект загружен!"));
			InvalidateRect(hwnd, NULL, TRUE);
			_stprintf(buf, TEXT("%s - %s"), APPNAME, ofn.lpstrFile);
			SetWindowText(hwnd, buf);
			g_Saved = true;
			CloseHandle(hFile);

		}



		break;
	case ID_GSAVE:

		if(g_Saved)
			SetWindowText(g_hStatus, TEXT("Проект уже сохранен!"));
		else if(!GetSaveFileName(&ofn)) {
			SetWindowText(g_hStatus, TEXT("Сохранение проекта отменено!"));
		}
		else {
			hFile = CreateFile(ofn.lpstrFile, GENERIC_READ | GENERIC_WRITE, 0, NULL, OPEN_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);

			SetWindowText(g_hStatus, TEXT("Выполняется сохранение..."));

			SetFilePointer(hFile,0,0,FILE_BEGIN);

			n = g_Ver.size();

			WriteFile(hFile,&n,sizeof(n),&dw,NULL);

			for(int k=0; k<n;k++) {

				vert.num = g_Ver[k].num;
				vert.pos.x = g_Ver[k].pos.x;
				vert.pos.y = g_Ver[k].pos.y;

				dw = 0;
				WriteFile(hFile,&vert,sizeof(vert),&dw,NULL);
			}

			n = g_Edge.size();

			WriteFile(hFile,&n,sizeof(n),&dw,NULL);

			for(int k=0; k<n;k++) {

				pt.x = g_Edge[k].x;
				pt.y = g_Edge[k].y;

				dw = 0;
				WriteFile(hFile,&pt,sizeof(pt),&dw,NULL);
			}

			n = g_DelVer.size();

			WriteFile(hFile,&n,sizeof(n),&dw,NULL);

			for(int k=0; k<n;k++) {

				m = g_DelVer[k];

				dw = 0;
				WriteFile(hFile,&m,sizeof(m),&dw,NULL);
			}

			SetWindowText(g_hStatus, TEXT("Успешно: проект сохранен!"));
			g_Saved = true;
			CloseHandle(hFile);


		}

		break;
	case ID_GVER:
		if(g_Ver.size() + 1 > GMAX) {
		    _stprintf(buf, TEXT("Ошибка: Достигнуто максимальное количество вершин."));
	        SetWindowText(g_hStatus, buf);
		}
		else {
			g_Ver.push_back(CreateVertex(hwnd));
			_stprintf(buf, TEXT("Успешно: Вершина %d создана."), g_Ver[g_Ver.size()-1].num);
	        SetWindowText(g_hStatus, buf);
			g_Saved = false;
		}
		break;
	case ID_DEL:
		int k;
		g_hDel = ChildWindowFromPoint(hwnd, g_pt);
		// удаляем связи
		for(size_t j=0; j<g_Ver.size();j++) {
			if(IsStay(GetVertexNum(g_hDel), g_Ver[j].num))
				g_Edge.erase(g_Edge.begin() + g_index);
			if(g_Ver[j].h == g_hDel)
				k = j;
		}
		// отмечаем как удаленную
		g_DelVer.push_back(g_Ver[k].num);
		//удаляем из вектора
		g_Ver.erase(g_Ver.begin() + k);
		// закрываем окно
		DestroyWindow(g_hDel);
		// Обновляем окно
		InvalidateRect(hwnd, NULL, true);
		g_Saved = false;
		break;
	case ID_GDUGA:
		DialogBox((HINSTANCE) GetWindowLong(hwnd, GWLP_HINSTANCE), MAKEINTRESOURCE(IDD_ADDEDGE), hwnd, EdgeProc);
		g_Saved = false;
		break;
	case ID_INFO:
		DialogBox((HINSTANCE) GetWindowLong(hwnd, GWLP_HINSTANCE), MAKEINTRESOURCE(IDD_DIALOG2), hwnd, PropProc);
		break;
	case ID_GTABLE:
		DialogBox((HINSTANCE) GetWindowLong(hwnd, GWLP_HINSTANCE), MAKEINTRESOURCE(IDD_DIALOG3), hwnd, NastProc);
		break;
	case ID_EXIT:
		SendMessage(hwnd, WM_CLOSE, 0, 0);
		break;
	}
}


// Процедура обработки вершин графа
LRESULT CALLBACK GrafProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
	
	switch(uMsg) {
		HANDLE_MSG(hwnd, WM_CREATE, G_Cls_OnCreate);
		HANDLE_MSG(hwnd, WM_PAINT, G_Cls_OnPaint);
		HANDLE_MSG(hwnd, WM_SIZE, G_Cls_OnSize);
		
		HANDLE_MSG(hwnd, WM_LBUTTONDOWN, G_Cls_OnLButtonDown);
		HANDLE_MSG(hwnd, WM_LBUTTONUP, G_Cls_OnLButtonUp);
		HANDLE_MSG(hwnd, WM_MOUSEMOVE, G_Cls_OnMouseMove);
		HANDLE_MSG(hwnd, WM_RBUTTONDOWN, G_Cls_OnRButtonDown);
		HANDLE_MSG(hwnd, WM_RBUTTONUP, G_Cls_OnRButtonUp);
		HANDLE_MSG(hwnd, WM_CLOSE, G_Cls_OnClose);

	default:
		return DefWindowProc(hwnd, uMsg, wParam, lParam);
		break;
	}
	return 0;
}

void G_Cls_OnPaint(HWND hwnd){
	HDC hDC;
	PAINTSTRUCT ps;
	RECT rc;
	HPEN hPen;
	HFONT hFont;
	TCHAR buf[10] = TEXT("");

	static LOGFONT lf;
	lf.lfPitchAndFamily = FIXED_PITCH | FF_MODERN;
	lf.lfItalic = FALSE;
	lf.lfWeight = FW_BOLD;
	lf.lfHeight = 25;
	lf.lfCharSet = DEFAULT_CHARSET;

	rc.left = 0;
	rc.right = GMAX;
	rc.top = 0;
	rc.bottom = GMAX;

	_stprintf(buf, TEXT("%d"), GetVertexNum(hwnd));

	hDC = BeginPaint(hwnd, &ps);

	hPen = (HPEN) SelectObject(hDC, CreatePen(PS_SOLID, g_tt, RGB(g_r, g_g, g_b)));
	hFont = (HFONT) SelectObject(hDC, CreateFontIndirect(&lf));

	Ellipse(hDC, 0, 0, GMAX-3, GMAX-3);
	DrawText(hDC, buf, _tcslen(buf), &rc, DT_CENTER | DT_VCENTER | DT_SINGLELINE);

	DeleteObject(SelectObject(hDC, hPen));
	DeleteObject(SelectObject(hDC, hFont));
	EndPaint(hwnd, &ps);
}

BOOL G_Cls_OnCreate(HWND hwnd, LPCREATESTRUCT lpCreateStruct) {

	return true;
}

void G_Cls_OnClose(HWND hwnd) {
	DestroyWindow(hwnd);
}

void G_Cls_OnSize(HWND hwnd, UINT state, int cx, int cy) {

}


void G_Cls_OnLButtonDown(HWND hwnd, BOOL fDoubleClick, int x, int y, UINT keyFlags) {
	SendMessage(GetParent(hwnd), WM_LBUTTONDOWN, 0, 0);
	InvalidateRect(hwnd, NULL, true);
}

void G_Cls_OnLButtonUp(HWND hwnd, int x, int y, UINT keyFlags) {
	SendMessage(GetParent(hwnd), WM_LBUTTONUP, 0, 0);
	InvalidateRect(hwnd, NULL, true);
}

void G_Cls_OnMouseMove(HWND hwnd, int x, int y, UINT keyFlags) {
	POINT pt;
    GetCursorPos (&pt);
    ScreenToClient (GetParent(hwnd), &pt);

	if(g_Move == true) {
		MoveWindow(g_hMove, pt.x, pt.y, GMAX, GMAX, true);
	}

}

void G_Cls_OnRButtonDown(HWND hwnd, BOOL fDoubleClick, int x, int y, UINT keyFlags) {
	g_MenuStat = true;
	SendMessage(GetParent(hwnd), WM_RBUTTONDOWN, 0, 0);
	InvalidateRect(hwnd, NULL, true);
}

void G_Cls_OnRButtonUp(HWND hwnd, int x, int y, UINT flags) {
	SendMessage(GetParent(hwnd), WM_RBUTTONUP, 0, 0);
}

BOOL CALLBACK AboutProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
	switch(uMsg)
	{
	case WM_INITDIALOG:
		return TRUE;
		break;
	case WM_COMMAND:
		switch(LOWORD(wParam)) {
		case IDOK:
		case IDCANCEL:
			EndDialog(h, 0);
			return TRUE;
		}
		break;
	}
	return FALSE;
}

BOOL CALLBACK EdgeProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam) {
	static HWND hComboN, hComboC, hBut1, hBut2;
	TCHAR buf[MAX_PATH];
	POINT pt;
	int id, index;
	bool it_del;

	switch(uMsg)
	{
	case WM_INITDIALOG:
		hComboN = GetDlgItem(h, IDC_COMBO2);
		hComboC = GetDlgItem(h, IDC_COMBO3);
		hBut1 = GetDlgItem(h, IDC_BUTTON1);
		hBut2 = GetDlgItem(h, IDC_BUTTON2);

		if(g_Ver.size() > 0) {
			EnableWindow(hBut1, TRUE);
			EnableWindow(hBut2, TRUE);
			
			for(size_t i = 0; i< g_Ver.size(); i++) {
				_stprintf(buf, TEXT("%d"), g_Ver[i].num);
				ComboBox_AddString(hComboN, buf);
				ComboBox_AddString(hComboC, buf);
			}
			
		}
		else {
			ComboBox_AddString(hComboN, TEXT("0"));
			ComboBox_AddString(hComboC, TEXT("0"));
		}
		ComboBox_SetCurSel(hComboN, 0);
		ComboBox_SetCurSel(hComboC, 0);
		return TRUE;
		break;

	case WM_COMMAND:
		switch(LOWORD(wParam)) {
		case IDC_BUTTON1:
			id = SendMessage(hComboN, CB_GETCURSEL, 0, 0);
			pt.x = g_Ver[id].num;
			id = SendMessage(hComboC, CB_GETCURSEL, 0, 0);
			pt.y = g_Ver[id].num;
			if(IsStay(pt.x, pt.y)) {
				_stprintf(buf, TEXT("Ошибка: Связь %d - %d уже существует."), pt.x, pt.y);
				SetWindowText(g_hStatus, buf);
			}
			else {
				g_Edge.push_back(pt);
				_stprintf(buf, TEXT("Успешно: Связь %d - %d добавлена."), pt.x, pt.y);
				SetWindowText(g_hStatus, buf);
			}

			break;
		case IDC_BUTTON2:
			it_del = false;
			id = SendMessage(hComboN, CB_GETCURSEL, 0, 0);
			pt.x = g_Ver[id].num;
			id = SendMessage(hComboC, CB_GETCURSEL, 0, 0);
			pt.y = g_Ver[id].num;

			for(size_t i=0;i<g_Edge.size();i++) {
				if(pt.x == g_Edge[i].x && pt.y == g_Edge[i].y) {
					index = i;
					it_del = true;
				}
				else if(pt.x == g_Edge[i].y && pt.y == g_Edge[i].x) {
					index = i;
					it_del = true;
				}
			}

			if(it_del) {
				g_Edge.erase(g_Edge.begin() + index);
				_stprintf(buf, TEXT("Успешно: Связь %d - %d удалена."), pt.x, pt.y);
				SetWindowText(g_hStatus, buf);
			}
			else {
				_stprintf(buf, TEXT("Ошибка: Связь %d - %d не найдена."), pt.x, pt.y);
				SetWindowText(g_hStatus, buf);
			}

			break;
		case IDOK:
		case IDCANCEL:
			InvalidateRect(GetParent(h), NULL, true);
			EndDialog(h, 0);
			return TRUE;
			break;

		}
		break;
	}

	return FALSE;
}

BOOL CALLBACK PropProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
	g_hDel = ChildWindowFromPoint(GetParent(h), g_pt);
	TCHAR buf[MAX_PATH] = TEXT(""), bum[MAX_PATH] = TEXT("");
	HDC hdc;
	PAINTSTRUCT ps;
	RECT rc;
	GetWindowRect(h, &rc);
	rc.top = 40;
	rc.left = 10;
	
	switch(uMsg)
	{
	case WM_INITDIALOG:
		return TRUE;
		break;
	case WM_PAINT:
		_stprintf(buf, TEXT("Вершина: %d"), GetVertexNum(g_hDel));
	    _stprintf(bum, TEXT("Связи: "));

		
		for(size_t hh=0; hh<g_Ver.size(); hh++) {
			if(IsStay(GetVertexNum(g_hDel), g_Ver[hh].num))
				_stprintf(bum, TEXT("%s %d"), bum, g_Ver[hh].num);
		}
		
		hdc = BeginPaint(h, &ps);
		TextOut(hdc, 10, 20, buf, _tcslen(buf));
		DrawText(hdc, bum, _tcslen(bum), &rc, DT_LEFT | DT_WORDBREAK);
		EndPaint(h, &ps);
		break;
	case WM_COMMAND:
		switch(LOWORD(wParam)) {
		case IDOK:
		case IDCANCEL:
			EndDialog(h, 0);
			return TRUE;
		}
		break;
	}
	return FALSE;
}

BOOL CALLBACK NastProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
	TCHAR b1[10], b2[10], b3[10];
	int d, t, tt;

	HBRUSH hBrush;
	HDC hDC;
	PAINTSTRUCT ps;
	RECT rc;

	rc.left = 149;
	rc.top = 170;
	rc.right = 191;
	rc.bottom = 189;

	switch(uMsg)
	{
	case WM_INITDIALOG:
		_stprintf(b1, TEXT("%d"), GMAX);
		_stprintf(b2, TEXT("%d"), g_t);
		_stprintf(b3, TEXT("%d"), g_tt);

		SetDlgItemText(h, IDC_EDIT1, b1);
		SetDlgItemText(h, IDC_EDIT2, b2);
		SetDlgItemText(h, IDC_EDIT3, b3);

		return TRUE;
		break;
	case WM_PAINT:
		hDC = BeginPaint(h, &ps);

		hBrush = CreateSolidBrush(RGB(g_rt, g_gt, g_bt));
		FillRect(hDC, &rc, hBrush);
		EndPaint(h, &ps);
		break;
	case WM_COMMAND:
		switch(LOWORD(wParam)) {
		case IDC_BUTTON1:
			DialogBox((HINSTANCE) GetWindowLong(h, GWLP_HINSTANCE), MAKEINTRESOURCE(IDD_DIALOG4), h, ColProc);
			break;
		case IDOK:

			GetDlgItemText(h, IDC_EDIT1, b1, 10);
			GetDlgItemText(h, IDC_EDIT2, b2, 10);
			GetDlgItemText(h, IDC_EDIT3, b3, 10);

			d = _tstoi(b1);
			t = _tstoi(b2);
			tt = _tstoi(b3);

			if( d>=50 && d<=100)
				GMAX = d;
			if(t>=1 && t<=10)
				g_t = t;
			if(tt>=1 && tt<=5)
				g_tt = tt;

			g_r = g_rt;
			g_g = g_gt;
			g_b = g_bt;

		case IDCANCEL:
			g_rt = g_r;
			g_gt = g_g;
			g_bt = g_b;
			InvalidateRect(GetParent(h), NULL, true);
			EndDialog(h, 0);
			return TRUE;
		}
		break;
	}
	return FALSE;
}

BOOL CALLBACK ColProc(HWND h, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
	HWND hCtrl;
	int CtrID, Index;
	HWND hR, hG, hB;	

	int rgb[3];
	rgb[0] = g_rt;
	rgb[1] = g_gt;
	rgb[2] = g_bt;
	RECT rc;

	rc.left = 35;
	rc.top = 210;
	rc.right = 212;
	rc.bottom = 236;

	HBRUSH hBrush;
	HDC hDC;
	PAINTSTRUCT ps;

	switch(uMsg)
	{
	case WM_INITDIALOG:

		hR = GetDlgItem(h, IDC_RED);
		hG = GetDlgItem(h, IDC_GREEN);
		hB = GetDlgItem(h, IDC_BLUE);

		SetScrollRange(hR, SB_CTL, 0, 255, FALSE);
		SetScrollPos(hR, SB_CTL, rgb[0], FALSE);

		SetScrollRange(hG, SB_CTL, 0, 255, FALSE);
		SetScrollPos(hG, SB_CTL, rgb[1], FALSE);

		SetScrollRange(hB, SB_CTL, 0, 255, FALSE);
		SetScrollPos(hB, SB_CTL, rgb[2], FALSE);

		return TRUE;
		break;

	case WM_PAINT:
		hDC = BeginPaint(h, &ps);
		hBrush = CreateSolidBrush(RGB(rgb[0], rgb[1], rgb[2]));
		FillRect(hDC, &rc, hBrush);
		DeleteObject(hBrush);
		EndPaint(h, &ps);
		break;

	case WM_VSCROLL:
		hCtrl = (HWND) lParam;
		CtrID = GetDlgCtrlID(hCtrl);

		Index = CtrID - IDC_RED;

		switch(LOWORD(wParam)) {

		case SB_LINEUP:
			rgb[Index] = max(0, rgb[Index]-1);
			break;
		case SB_LINEDOWN:
			rgb[Index] = min(255, rgb[Index]+1);
			break;
		case SB_PAGEUP:
			rgb[Index] -= 15;
			break;
		case SB_PAGEDOWN:
			rgb[Index] += 15;
		    break;
		case SB_THUMBTRACK:
			rgb[Index] = HIWORD(wParam);
			break;
			
        case SB_THUMBPOSITION:
            rgb[Index] = HIWORD(wParam);
            break;
		}

		SetScrollPos(hCtrl, SB_CTL, rgb[Index], TRUE);

		g_rt = rgb[0];
		g_gt = rgb[1];
		g_bt = rgb[2];
		InvalidateRect(h, &rc, true);
		break;

	case WM_COMMAND:
		switch(LOWORD(wParam)) {
		case IDOK:
			InvalidateRect(GetParent(h), NULL, true);
			EndDialog(h, 0);
			return TRUE;
			break;
		case IDCANCEL:
			g_rt = g_r;
			g_bt = g_b;
			g_gt = g_g;
			InvalidateRect(GetParent(h), NULL, true);
			EndDialog(h, 0);
			return TRUE;
		}
		break;
	}
	return FALSE;
}
