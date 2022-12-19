void setup(){
  size(1750, 750);
  background(255);
  frameRate(60);
  surface.setTitle("Graphs");
  smooth(5);
  img = loadImage("color_wheel.png"); 
  G.setName("1");
}
String text;
Graph G = new Graph();

Graph[] GR = new Graph[1];
int index = 0;
Vertex V1;
Vertex V2;
int mode = 1;
color st_color = 0xFF227722;

Button b1 = new Button(10,10,220,50,"Создать/удалить вершину",200);
Button b2 = new Button(10,70,200,50,"Создать/удалить ребро",200);
Button b3 = new Button(10,130,100,50,"Сохранить",200);
Button b4 = new Button(120,130,140,50,"Открыть",200);
Button b5 = new Button(10,190,0,0,"Информация о графе",200);
Button b6 = new Button(380,720,25,25,"+",200);
Button b7 = new Button(410,720,100,27,"",200);
PImage img;
/*интерфейс*/
void draw(){
  
  background(255); //фон
  noFill();
  stroke(0xFF000000);
  
  strokeWeight(1);
  rect(380,10,890,700); //область для рисования
  b1.display();          //отображение кнопкок
  b2.display();
  b3.display();
  b4.display();
  b5.display();
  b6.display();
  b7.display();
  image(img,10,510,200,200); // цветовой круг
  fill(st_color);
  noStroke();
  circle(110,610, 50);
  fill(0xFF000000);
  textAlign(LEFT, TOP);
  text = 
    "Кол-во вершин - " +G.vertexs.length+"\n"+
    "Кол-во ребер - " +G.edges.length+"\nМатрица смежности";
  if(text != null)text(text,1290,10, 480, 100);
  int[][] temp = G.getMatrixSm();
  textAlign(CENTER, CENTER);
  if(temp.length != 0)
  {
    int s = 2;
    int w = (300- s * (G.vertexs.length - 1))/G.vertexs.length;
    int h = w;
    text("v",1290,100);
    for(int i =0;i<G.vertexs.length;i++)text(G.vertexs[i].name,1320+(w+s)*i,100,w,20);
    for(int i =0;i<G.vertexs.length;i++)text(G.vertexs[i].name,1290,130+(w+s)*i,20,h);
    for(int i=0,j=0;j<temp.length&&i<temp[j].length;i = (i+1)%temp[j].length,j += (i==0)?1:0 )text(str(temp[j][i]),1320+(w+s)*i,130+(h+s)*j,w,h);
  }
  textAlign(LEFT, TOP);
  text("Матрица инциндентности",1290,430);
  temp = G.getMatrixIn();
  textAlign(CENTER, CENTER);
  if(temp.length != 0 && temp[0].length != 0)
  {
    int s = 2;
    int w = (300- s * (G.edges.length - 1))/G.edges.length;
    int h = (200- s * (G.vertexs.length - 1))/G.vertexs.length;
    println(w);
    for(int i =0;i<G.edges.length;i++)text(str(i),1320+(w+s)*i,450,w,20);
    for(int i =0;i<G.vertexs.length;i++)text(G.vertexs[i].name,1290,480+(h+s)*i,20,h);
    
    
    for(int i=0,j=0;j<temp.length&&i<temp[j].length;i = (i+1)%temp[j].length,j += (i==0)?1:0 )
      {
        text(str(temp[j][i]),1320+(w+s)*i,480+(h+s)*j,w,h);
        println(1320+(w+s)*i,480+(h+s)*j, w);
      }  
  }
  textAlign(LEFT, CENTER);
  text("ЛКМ - создание\nПКМ - удаление\nСКМ - ор. дуга", 250,10,130,110);
  if(b1.clicked())          //обработка нажатия кнопок
  {
    mode = 1;
    println("mode="+mode);
  }
  if(b2.clicked())
  {
    mode = 2;
    V1=V2=null;
    println("mode="+mode);
  }
  if(b6.clicked()){
    GR = (Graph[])append(GR, new Graph());
    GR[GR.length-1].setName(str(GR.length));
    
  }
  if(b7.clicked()){
    GR[index++] = G;
    if(index == GR.length)index = 0;
    G = GR[index];
  }
  if(b5.clicked())
  {
    mode = 3;
  }
  if(mouseX > (380) && mouseX < (380+890) && mouseY > (10) && mouseY < (10 + 710) && mode==2 && V1!=null)
  {
    stroke(2);
    line(V1.x,V1.y,mouseX, mouseY);
  } 
  b7.setName(G.name);
  G.update();
}

void mousePressed( ){
  switch(mode)
  {
   case 1:
   {
    if(mouseX > (380+rad) && mouseX < (380+890-rad) && mouseY > (10+rad) && mouseY < (10 + 710 - rad))
    {
      if(mouseButton == LEFT){      
        float min_v = 2000;
        for(int i = 0;i<G.vertexs.length;i++)
        {
            float l  = sqrt(pow(mouseX-G.vertexs[i].x,2)+pow(mouseY-G.vertexs[i].y,2));
            if(l<min_v)min_v=l;
        }
        if(min_v > rad)G.addV(new Vertex(mouseX, mouseY, st_color));
      }
      else if(mouseButton == RIGHT)
      {
        int j = G.getVertexByPos(mouseX, mouseY);
        if(j!=-1 && G.getLengthToVertex(mouseX, mouseY) < rad/2)
        {
          G.deleteV(j);  
        }
      }
    }
    break; 
   }
   
   case 2:
   {
    if(mouseX > (380+rad) && mouseX < (380+890-rad) && mouseY > (10+rad) && mouseY < (10 + 710 - rad))
    {
      int j = G.getVertexByPos(mouseX, mouseY);
      boolean flag = false;
      if(j!=-1 && G.getLengthToVertex(mouseX, mouseY) < rad/2 && mouseButton == LEFT)
      {
        if(V1==null)V1=G.vertexs[j];
        else {V2=G.vertexs[j];flag = false;}
      }
      if(j!=-1 && G.getLengthToVertex(mouseX, mouseY) < rad/2 && mouseButton == CENTER)
      {
        if(V1==null)V1=G.vertexs[j];
        else V2=G.vertexs[j];
        flag = true;
      }
      if(V1!=null && V2==null && mouseButton==RIGHT)V1=null;
      if(V1 != null && V2 != null)
      {
        G.addE(new Edge(V1,V2,st_color,flag));
        V1=V2=null;
      }
      int i = G.getEdgePos(mouseX, mouseY);
      if(mouseButton == RIGHT && i!= -1)
      {
        G.deleteE(G.edges[i]);
      }
    }
    break; 
   }
   
   case 3:
   {
    if(mouseX > (380+rad) && mouseX < (380+890-rad) && mouseY > (10+rad) && mouseY < (10 + 710 - rad))
    {
      int j ;
      j = G.getVertexByPos(mouseX, mouseY);
      if(j!=-1 && G.getLengthToVertex(mouseX, mouseY) <= rad/2)
      {
        
      }
    }
    break; 
   }
   
  }
  if(sqrt(pow(mouseX-110,2)+pow(mouseY-610,2))< 100){st_color = get(mouseX, mouseY);}
  b1.clicked( mouseX, mouseY);
  b2.clicked( mouseX, mouseY);
  b3.clicked( mouseX, mouseY);
  b4.clicked( mouseX, mouseY);
  b5.clicked( mouseX, mouseY);
  b6.clicked( mouseX, mouseY);
  b7.clicked( mouseX, mouseY);
}

void mouseDragged()
{
  if(mode==1 && mouseX > (380+rad) && mouseX < (380+890-rad) && mouseY > (10+rad) && mouseY < (10 + 710 - rad)){
    int j ;
    j = G.getVertexByPos(mouseX, mouseY);
    if(j!=-1 && G.getLengthToVertex(mouseX, mouseY) < rad/2 && mouseButton == LEFT)
    {
        G.vertexs[j].x = mouseX;
        G.vertexs[j].y = mouseY;
    }  
  }
}

class Graph{
  String name;
  Edge[] edges;
  Vertex[] vertexs;
  
  Graph()
  {
    vertexs = new Vertex[0];
    edges = new Edge[0];
  }
  
  void setName(String Name)
  {
    name = Name;
  }
  
  int[][] getMatrixSm(){
    int[][] Matrix = new int[vertexs.length][vertexs.length];
    for(int i = 0;i<edges.length;i++){
      int k1 = -1,k2 = -1;
      for(int j = 0;j<vertexs.length;j++)
      {
        if(edges[i].v1==vertexs[j])k1=j;
        if(edges[i].v2==vertexs[j])k2=j;
      }
      Matrix[k1][k2]= 1;
      if(!edges[i].isEnableOrientation)Matrix[k2][k1]= 1;
    }
    return Matrix;
  }
  
  int[][] getMatrixIn(){
    int[][] Matrix = new int[vertexs.length][edges.length];
    for(int i = 0;i<edges.length;i++)
    {
       int V1, V2;
       V1 = V2 = 0;
       for(int j=0;j<vertexs.length;j++)
       {
         if(vertexs[j]==edges[i].v1)V1 = j;
         if(vertexs[j]==edges[i].v2)V2 = j;
       }
       Matrix[V1][i] = edges[i].isEnableOrientation?-1:1;//стрелка
       Matrix[V2][i] = 1;
    }
    return Matrix;
  }
  
  int getEdgePos(int X, int Y)
  {
   float min_v = 2000;
   int j = -1;
   for(int i = 0;i<G.edges.length;i++)
      {
          float l  = 
          abs((G.edges[i].v2.y - G.edges[i].v1.y)*X+ (G.edges[i].v1.x-G.edges[i].v2.x)*Y - G.edges[i].v1.x*(
          G.edges[i].v2.y-G.edges[i].v1.y
          )+G.edges[i].v1.y*(G.edges[i].v2.x-G.edges[i].v1.x))
          /
          sqrt(pow(G.edges[i].v2.x-G.edges[i].v1.x,2)+pow(G.edges[i].v2.y-G.edges[i].v1.y,2));
          if(l<min_v)
          {
            min_v=l;
            j = i;
          }
      }
   if(min_v<8 && 
      X <= max(G.edges[j].v2.x,G.edges[j].v1.x) &&
      X >= min(G.edges[j].v2.x,G.edges[j].v1.x) &&
      Y <= max(G.edges[j].v2.y,G.edges[j].v1.y) &&
      X >= min(G.edges[j].v2.y,G.edges[j].v1.y))return j;
   return -1;
  }
  
  int getVertexByPos(int X, int Y)
  {
   float min_v = 2000;
   int j = -1;
   for(int i = 0;i<G.vertexs.length;i++)
      {
          float l  = sqrt(pow(X-G.vertexs[i].x,2)+pow(Y-G.vertexs[i].y,2));
          if(l<min_v)
          {
            min_v=l;
            j = i;
          }
      }
   return j;
  }
  
  float getLengthToVertex(int X, int Y){
   float min_v = 2000;
   float l = 2000;
   for(int i = 0;i<G.vertexs.length;i++)
      {
          l  = sqrt(pow(X-G.vertexs[i].x,2)+pow(Y-G.vertexs[i].y,2));
          if(l<min_v)
          {
            min_v=l;

          }
      }
   return min_v;
  }
  
  void deleteV(int j)
  {
    Vertex[] temp = vertexs;
    for(int i = 0; i < edges.length;i++)
    {
      if(edges[i].v1== vertexs[j] || edges[i].v2== vertexs[j])deleteE(edges[i--]);
    }
    temp = (Vertex[])concat(subset(vertexs, 0, j),subset(vertexs, j+1));
    vertexs = temp;
  }
  
  void deleteE(Edge e)
  {
    Edge[] temp = edges;
    for(int i = 0; i < edges.length;i++)
    {
      if(e==edges[i])
      {
      temp = (Edge[])concat(subset(edges, 0, i),subset(edges, i+1));
      break;
      }
    }
    edges = temp;
  }
  
  void addV(Vertex V1)
  {
    vertexs = (Vertex[]) append(vertexs, V1);
    vertexs[vertexs.length-1].setName(str(vertexs.length));
  }
  void addE(Edge E){edges = (Edge[]) append(edges, E);}
  
  void update()
  {
    for(int i = 0;i<edges.length;i++)
    {
      stroke(edges[i].col);
      strokeWeight(1);
      if(mode == 2)
      {
        int j = G.getEdgePos(mouseX, mouseY);
        if(j != -1 && j == i)strokeWeight(3);
      }
      line(edges[i].v1.x, edges[i].v1.y, edges[i].v2.x, edges[i].v2.y);
      if(edges[i].isEnableOrientation)
      {
         Vertex v1 = edges[i].v1;
         Vertex v2 = edges[i].v2;
         float l = sqrt(pow(v2.x-v1.x,2)+pow(v2.y-v1.y,2));
         int x3 = round(v2.x - (v2.x-v1.x)/l*(rad/2+size)); 
         int y3 = round(v2.y - (v2.y-v1.y)/l*(rad/2+size)); 
         float a1 = 1;
         float b1 = -a1*(v2.x-v1.x)/(v2.y-v1.y);
         float l2 = sqrt(pow(a1,2)+pow(b1,2));
         strokeCap(ROUND);
         fill(edges[i].col);
         triangle(
         x3+a1*size/(2*l2),
         y3+b1*size/(2*l2),
         round(v2.x - (v2.x-v1.x)/l*rad/2),
         round(v2.y - (v2.y-v1.y)/l*rad/2),
         x3-a1*size/(2*l2),
         y3-b1*size/(2*l2));
      }
    }
    
    for(int i = 0;i<vertexs.length;i++)
    {
     fill(vertexs[i].col);
     noStroke();
     circle(vertexs[i].x, vertexs[i].y, rad);
     fill(0xFF000000);
     textAlign(CENTER,CENTER);
     text(vertexs[i].name, vertexs[i].x-35/2, vertexs[i].y-35/2, 35, 35);
    }
  }
}
int size = 20;
int rad = 50;

class Vertex{
  int x;
  int y;
  color col;
  String name;
  
  Vertex(color Col)
  {
    x = mouseX;
    y = mouseY;
    col = Col;
  }
  
  Vertex(int posX, int posY, color Col)
  {
    x = posX;
    y = posY;
    col = Col;
  }
  
  void setName(String Name){name = Name;}
}

class Edge{
  Vertex v1;
  Vertex v2;
  boolean isEnableOrientation;
  color col;
  
  Edge(Vertex V1, Vertex V2, color Col)
  {
    v1 = V1;
    v2 = V2;
    col = Col;
    isEnableOrientation = false;
  }
  
  Edge(Vertex V1, Vertex V2, color Col, boolean bool)
  {
    v1 = V1;
    v2 = V2;
    col = Col;
    isEnableOrientation = bool;
  }
  
  void changeColor(color Col){col = Col;}
}

class Button
{
  float x,y;
  float w,h;
  color col;
  String label; 
  boolean click;
  
  Button(float x, float y, float w, float h, String label, color col)
  {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
    this.label = label;
    this.col = col;
    this.click = false;
  }
  
  boolean clicked()
  {
    if(click){
    click = false;
    return true;
    }
    return false;
  }
  void display()
  {
    stroke(255);
    fill(col);
    rect(x, y, w, h);
    fill(0);
    textFont(createFont("Arial", 16));
    textAlign(CENTER, CENTER);
    text(label, x , y , w, h);
  }
  
  void clicked( int mx, int my)
  {
    if( mx > x && mx < x + w  && my > y && my < y+h)
    {
    stroke(col+20);
    fill(col+20);
    rect(x, y, w, h);
    fill(0);
    textAlign(CENTER, CENTER);
    text(label, x , y , w, h);
    click = true; 
    }
  }
  void setName(String name)
  {
    label = name;
  }
}
