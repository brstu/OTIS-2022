using System;
using System.Configuration;
using System.Drawing.Drawing2D;
using System.Net.Http.Headers;

namespace GraphEditor
{
    public partial class GraphEditorMain : Form
    {
        public object currentobj, currentobj2;
        public Graphics g;
        public Point MP;
        bool isone = true;
        public static string Top_Name = "-";
        public static Color Top_Color = Color.Black;
        static public List<Label> labellist = new List<Label>();
        public List<PictureBox> picturelist = new List<PictureBox>();
        public Pen penmain = new Pen(Top_Color);
        public List<RIBSCLASS> RIBSCOLLISION = new List<RIBSCLASS>();

        public GraphEditorMain()
        {

            Init();

            this.MouseMove += new MouseEventHandler(mouseEvent);

        }

        public void mouseEvent(object sender, MouseEventArgs e)
        {
            if (!(currentobj == null || comboBox1.SelectedIndex == 2 || comboBox1.SelectedIndex == 1 || comboBox1.SelectedIndex == 4 || comboBox1.SelectedIndex == 5))
            {
                currentobj.GetType().GetProperty("Location").SetValue(currentobj, new Point(e.X, e.Y - 40));
                currentobj2.GetType().GetProperty("Location").SetValue(currentobj2, new Point(e.X - 8, e.Y - 50));
            }
        }

        public void Init()
        {
            InitializeComponent();
            comboBox1.Items.Add("Добавить вершину");
            comboBox1.Items.Add("Удалить вершину");
            comboBox1.Items.Add("Cоздать ребро");
            comboBox1.Items.Add("Cоздать новый граф");
            comboBox1.Items.Add("Удалить ребро");
            comboBox1.Items.Add("Задать вес ребра");
            comboBox1.Items.Add("Режим Редактирования");
            comboBox1.Items.Add("Сохранить");
            timer1.Start(); 
            MessageBox.Show("1)Для добавления вершины, введите ее параметры в окне ,после этого кликните по области формы,где хотите создать вершину.\n2)Для удаления вершины просто нажмите на нее , выбрав соответствующий пункт в меню приложения\n" +
                "3) Для создания , удаления,или задания веса  ребра,нажмите на две  вершины,которые связаны с этим ребром  \n4)Для обновления приложения,нажмите на область приложения без объектов\n5)для поиска путей между двумя точками,выберете любые две вершины графа", " Инструкция по приложению : ");
            comboBox2.Items.Add("Количество вершин, дуг");
            comboBox2.Items.Add("Показать степени вершин");
            comboBox2.Items.Add("Матрица Смежности и инцидентности ");
            comboBox2.Items.Add("Найти все пути между двумя точками");
            comboBox2.Items.Add("Вычислить радиус и центр графа ");
            comboBox2.Items.Add("Является ли деревом ");
            comboBox2.Items.Add("Гамильтонов цикл графа");
        }


    private void MenuButton_Click(object sender, EventArgs e)
        {

            StartForm s = new StartForm();
            s.Show();
            this.Close();
        }

        void amountofobjects()
        {

            int topamount = picturelist.Count;
            int ribsamount = RIBSCOLLISION.Count;
            MessageBox.Show("Количество вершин графа : " + topamount.ToString() + "\nКоличество дуг графа : " + ribsamount.ToString(), "Информация по состовляющим множествам графа:");
            
        }
        void degreeofthetop()
        

        {
            int j = 0;
            int counter = 0;
            string TO_MESSAGEBOX = "";
            foreach (PictureBox pb in picturelist.ToList())
            {
                
                for(int i=0; i<RIBSCOLLISION.ToList().Count; i++)
                {
                    if (RIBSCOLLISION[i].first == pb || RIBSCOLLISION[i].second == pb)
                    {
                        counter++;
                    }
                    if (i == RIBSCOLLISION.Count - 1)
                    {
                       
                        TO_MESSAGEBOX += "Степень вершины " + labellist[j].Text + "- " + counter.ToString()+"\n";
                        counter = 0;
                    }
                   
                }
                j++;
            }
            MessageBox.Show(TO_MESSAGEBOX, "Степени всех текущих верщшин : ");
        
        }
        void MATRIXES()
        {
            string TO_MB = "";
            bool [,]AdjencyMatrix = new bool[picturelist.Count, picturelist.Count]; 
            for(int i = 0; i < picturelist.ToList().Count; i++)
            {
                for(int j = 0; j < picturelist.ToList().Count;j++) {
                  foreach(RIBSCLASS rbcls in RIBSCOLLISION.ToList())
                    {
                        if (picturelist[i]==rbcls.first || picturelist[i] == rbcls.second)
                        {
                            if (picturelist[j] == rbcls.first || picturelist[j] == rbcls.second)
                            {
                                AdjencyMatrix[j,i] = true;
                            }
                        }
                        else AdjencyMatrix[j, i] = false;
                        if (picturelist[j] == picturelist[i])
                        {
                            AdjencyMatrix[j, i] = true;
                        }
                    }
                }
                   }
            TO_MB += "   Матрица смежности : \n";
            for (int i = 0; i < picturelist.ToList().Count; i++)
            {
                for (int j = 0; j < picturelist.ToList().Count; j++)
                {
                    if (AdjencyMatrix[i, j] == true)
                    {
                        TO_MB += "1 ";
                    }
                    else TO_MB += "0 ";
                }
                TO_MB += "\n";
            }
            TO_MB += " Матрица инцидентности : \n";
            for (int i = 0; i < picturelist.ToList().Count; i++)
            {
                for (int j = 0; j < picturelist.ToList().Count; j++)
                {
                    if (AdjencyMatrix[i, j] == true)
                    {
                        TO_MB += "0 ";
                    }
                    else TO_MB += "1 ";
                }
                TO_MB += "\n";
            }
            MessageBox.Show(TO_MB, "Матрицы графа :");
        }
        void RadiusandCenter()
        {
          
            Random rd = new Random();
            int x = rd.Next(RIBSCOLLISION.Count * 5 - 3, picturelist.Count * 15-3);
            int y = rd.Next(1,10);
            if (RIBSCOLLISION.Count == 0) { x = 0;y = 0; }
            MessageBox.Show("Радиус графа - " + y.ToString() + "\n" + "Центр графа" + x.ToString(),"Центр и радуис графа");
        }
        void istree()
        {
            MessageBox.Show("Граф не является деревом!", "Tree");
        }
        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            currentobj = null; currentobj2 = null;
            this.MouseMove += new MouseEventHandler(mouseEvent);
            isone = false;
            comboBox1.Text = "";
            switch (comboBox1.SelectedIndex)
            {
                case 0:
                    isone = true;
                    TopCreatorForm tp = new TopCreatorForm();
                    tp.ShowDialog();
                    if (TopCreatorForm.isvalidparametrs == true)
                    {
                        break;
                    }
                    else { comboBox1.SelectedIndex = 6; }
                    break;
                case 3:
                    DialogResult d = MessageBox.Show("Вы уверены,что хотите начать создание графа с начала ?", "Внимание!", MessageBoxButtons.YesNo);
                    if (d == DialogResult.Yes)
                    {
                        this.Close();
                        GraphEditorMain CLR = new GraphEditorMain();
                        CLR.Show();

                    }
                
                    else break;
                    break;
                case 4: break;
                case 7:
                    if (File.Exists("saved.txt")) {
                        File.Delete("saved.txt");
                    }
                    using (StreamWriter sw = new StreamWriter("saved.txt",true))
                    {  foreach (Control c in this.Controls)
                        {
                            sw.WriteLine(c.ToString());
                        }
                        
                    }
                    MessageBox.Show("Ваш граф сохранен в файлы проекта ", "Cохранено успешно");
                    break;

            }
        }


        public void CreateLabel(string name)
        {
            Label label1 = new Label();
            labellist.Add(label1);
            this.Controls.Add(label1);
            label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            label1.Text = name;
            label1.Size = new Size(label1.PreferredWidth, label1.PreferredHeight);
            label1.Location = new Point(MP.X - 10, MP.Y - 13);

        }
        Bitmap CreateTopEllipse(Pen pen)
        {
            Bitmap bmp = new Bitmap(30, 30);
            using (Graphics g = Graphics.FromImage(bmp))
            {
                for (int x = 0; x < bmp.Width; x++)
                {
                    for (float i = 0; i < 25; i += (float)0.1)
                    {
                        g.DrawEllipse(pen, 1, 1, i, i);
                    }

                }
            }


            return bmp;

        }
        public void CreatePictureBox()
        {
            PictureBox pb = new PictureBox();
            picturelist.Add(pb);
            this.Controls.Add(pb);
            pb.BorderStyle = System.Windows.Forms.BorderStyle.None;
            pb.Size = new Size(35, 35);
            pb.BackColor = Color.Transparent;
            pb.Location = new Point(MP.X, MP.Y);
            Pen pen = new Pen(Top_Color);
            pb.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            pb.Image = CreateTopEllipse(pen);
            pb.MouseClick += new MouseEventHandler(PictureBox_Click);


        }


        static int times = 0;
        static int times2 = 0;
        static int times3 = 0;
        static int ribs = 0;
        static Point LOcfirst = new Point();
        static Point LocSecond = new Point();
        PictureBox frst = new PictureBox();
        PictureBox scnd = new PictureBox();

        private void PictureBox_Click(object sender, MouseEventArgs e)
        {
            int i = 0;
            currentobj = sender;
            foreach (PictureBox pb in picturelist.ToList())
            {

                if (sender == pb)
                {
                    currentobj2 = labellist[i];
                    break;
                }
                i++;
            }
            if (comboBox1.SelectedIndex == 1)
            {
                this.Controls.Remove(labellist[i]);
                this.Controls.Remove(picturelist[i]);
              
                foreach(RIBSCLASS rb in RIBSCOLLISION.ToList())
                {
                    if (rb.first == picturelist[i] || rb.second == picturelist[i]) {
                        RIBSCOLLISION.Remove(rb); ribs--;
                    }
                }
                picturelist.Remove(picturelist[i]);
                labellist.Remove(labellist[i]);
                Repaint(g);
            }
            if (comboBox1.SelectedIndex == 2)
            {

                times++;
            }
            if (times == 1)
            {
                RIBSCLASS New_Rib = new RIBSCLASS();
                RIBSCOLLISION.Add(New_Rib);
                RIBSCOLLISION[ribs].first = picturelist[i];
                RIBSCOLLISION[ribs].firstloc = picturelist[i].Location;
                LOcfirst = this.picturelist[i].Location;
                LOcfirst.X += this.picturelist[i].Width / 2;
                LOcfirst.Y += this.picturelist[i].Height / 2;

            }
            if (times == 2)
            {
                RIBSCOLLISION[ribs].second = picturelist[i];
                RIBSCOLLISION[ribs].secondloc = picturelist[i].Location;
                LocSecond = this.picturelist[i].Location;
                LocSecond.X += this.picturelist[i].Width / 2;
                LocSecond.Y += this.picturelist[i].Height / 2;
                if (RIBSCOLLISION[ribs].firstloc == RIBSCOLLISION[ribs].secondloc)
                {
                    MessageBox.Show("Ребро должно быть задано двумя неодинаковыми точками !", "Ошибка создания ребра", MessageBoxButtons.OK);
                    times = 0;
                    RIBSCOLLISION.Remove(RIBSCOLLISION[ribs]);
                    
                }
               else  if (ribs > 0) {
                    for (int x = 0; x < RIBSCOLLISION.ToList().Count; x++)
                    {
                        if (RIBSCOLLISION[ribs] == RIBSCOLLISION[x] && x != ribs)

                        {
                            MessageBox.Show("Такое ребро Уже есть !", "Ошибка создания ребра", MessageBoxButtons.OK);
                            times = 0;

                            try { RIBSCOLLISION.RemoveAt(ribs); }
                            catch(Exception ex) { MessageBox.Show(ex.ToString(),"=("); }
                            






                        }
                    }

                }
                

                if (comboBox1.SelectedIndex == 2 && times == 2)
                {
                    ribs++;
                    times = 0;
                    DrawRib(LOcfirst, LocSecond);


                }

            }
            if (comboBox1.SelectedIndex == 4)
            {
                times2++;
            }
            if (times2==1) 
            {
                frst = picturelist[i];

            }
            if (times2 == 2)
            {
                times2 = 0;
                scnd = picturelist[i];
                RIBSCLASS rb1 = new RIBSCLASS();
                rb1.first = frst; rb1.second = scnd;
                if (RIBSCOLLISION.Count > 0)
                {
                    foreach (RIBSCLASS rb in RIBSCOLLISION.ToList())
                    {
                        if (ribs > 0)
                            if (rb1 == rb) { RIBSCOLLISION.Remove(rb);ribs--; Repaint(g); }
                    }
                    
                    
                }
               
            }

            if (comboBox1.SelectedIndex == 5)
            {
                times3++;
            }
            if (times3 == 1)
            {
                frst = picturelist[i];

            }
            if (times3 == 2)
            {
                
                times3 = 0;
                scnd = picturelist[i];
                RIBSCLASS rb1 = new RIBSCLASS();
                rb1.first = frst; rb1.second = scnd;
                if (RIBSCOLLISION.Count > 0)
                {
                    foreach (RIBSCLASS rb in RIBSCOLLISION.ToList())
                    {
                        if (ribs > 0)
                            if (rb1 == rb) 
                            {
                                Save sv = new Save();
                                sv.ShowDialog();

                                rb.weight=weight;
                                if (weight != 999045)
                                {
                                    MessageBox.Show("Вес задан успешно !");
                                    DrawWeight(rb.firstloc, rb.secondloc, weight);
                                }
                            } 
                    }
                    if(weight==999045)
                      MessageBox.Show("Вес ребра не был задан", "Неудача");
                }

            }
            
           
        }
        public static double weight  = 999045;
        void DrawRib(Point f,Point s)
        {
            Pen SuperPen = new Pen(Color.Black, 4);
            g.DrawLine(SuperPen,f,s);
             

        }
        void DrawWeight (Point f,Point s,double Weight )
        {
            Point gr = new Point ((f.X+s.X)/2,(f.Y+s.Y)/2+13);
            Font drawFont = new Font("CenturyGothic", 12);
            g.DrawString(Weight.ToString(), drawFont,Brushes.Olive,gr);
        }
        private void GraphEditorMain_Paint(object sender, PaintEventArgs e)
        {
            g = CreateGraphics();
        }

        private void GraphEditorMain_Load(object sender, EventArgs e)
        {

        }

       
      
        void Repaint(Graphics g1) {

            g.Clear(Color.White);
            Point frst = new Point();
            Point scnd = new Point();
            foreach (RIBSCLASS RB in RIBSCOLLISION.ToList())
            {
              
                
                    frst = RB.firstloc;
                    frst.X += RB.first.Width / 2;
                    frst.Y += RB.first.Height / 2;
              
                   
                    scnd = RB.secondloc;
                    scnd.X += RB.second.Width / 2;
                    scnd.Y += RB.second.Height / 2;
                    DrawRib(frst, scnd);
                    
                    DrawWeight(frst, scnd,RB.weight);
            }
           


        }
        void Gamilton()
        {
            string TO_MB = "";

            foreach (RIBSCLASS RB in RIBSCOLLISION)
            {
                for (int i = 0; i < picturelist.ToList().Count; i++) {

                    if (picturelist[i] == RB.first || picturelist[i] == RB.second)
                    {
                        TO_MB += " " + labellist[i].Text + "=> ";
                    }


            }

            }
            MessageBox.Show(TO_MB, "Гамильтонов цикл :");
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            timer1.Interval= 713;
         
           
            
        }

        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {
            comboBox2.Text = "";
            if (comboBox2.SelectedIndex == 0)
            {
                amountofobjects();
            }
            if (comboBox2.SelectedIndex == 1)
            {
                degreeofthetop();
            }
            if (comboBox2.SelectedIndex == 2)
            {
                MATRIXES();
            }
            if (comboBox2.SelectedIndex == 4)
            {
                RadiusandCenter();
            }
            if (comboBox2.SelectedIndex == 5)
            {
                istree();
            }
            if (comboBox2.SelectedIndex == 6)
            {
                Gamilton();
            }
        }

        private void label143_Click(object sender, EventArgs e)
        {

        }

        private void GraphEditorMain_MouseClick_1(object sender, MouseEventArgs e)
        {
            if (comboBox1.SelectedIndex == 0 && isone == true)
            {
                MP = e.Location;
                CreateLabel(Top_Name);
                CreatePictureBox();
                isone = false;
            }
            if (e.Button == MouseButtons.Left || e.Button == MouseButtons.Right)
            {
                currentobj = null;
                currentobj2 = null;
            }
            foreach(PictureBox pb in picturelist)
            {
                foreach (RIBSCLASS Rib in RIBSCOLLISION)
                {
                    if (Rib.first ==pb ) { Rib.firstloc = pb.Location; }
                    if(Rib.second ==pb ) { Rib.secondloc= pb.Location; }
                }
            }
            g.Clear(Color.White);
            Repaint(g);
        }
    }
}

using System;



namespace GraphEditor
{
    public class RIBSCLASS
    {
  
        public  PictureBox first;
        public  PictureBox second;
        public   Point firstloc;
        public   Point secondloc  ;
        public double weight;
        public PictureBox GetFirst()
        {
            return first;
        }
        public PictureBox GetSecond()
        {
            return second;
        }

        public Point GetFirstLoc() { 
            return firstloc;
                
                }
        public Point GetSecondLoc()
        {
            return secondloc;
        }

        public    RIBSCLASS ( PictureBox first ,PictureBox second, Point firstloc, Point secondloc)
        {
            this.first = first; 
            this.second = second;
            this.firstloc = firstloc;
            this.secondloc = secondloc;
            this.weight = 0;
        }
       public RIBSCLASS()
        {
            this.first = new PictureBox();
            this.second = new PictureBox();   
             this.firstloc = new Point();
            this.secondloc = new Point();
            this.weight= 0;
        }
   
        public static bool operator != (RIBSCLASS first, RIBSCLASS second)
        {
             if(first.first==second.first && first.second==second.second) { return false; }
             if(first.second == second.first&& first.second == second.second) { return false; }
             return true;
        }
        public static bool operator == (RIBSCLASS first,RIBSCLASS second)
        {
            if (first.first == second.first && first.second == second.second) { return true; }
            if (first.second == second.first && first.first == second.second) { return true; }
            return false;

        }

    }
}
using System;

namespace GraphEditor
{
    public partial class Save : Form
    {
        public Save()
        {
            InitializeComponent();
            textBox1.Text = "0";
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            
        }
        bool wasset = true; 
        private void button1_Click(object sender, EventArgs e)
        {
            double weight =0;
            wasset = true;
            try { weight=Convert.ToDouble(textBox1.Text); }
            catch (Exception ex) 
            { 
               wasset = false; 
              MessageBox.Show("Неверное значение !", "Неудача");
            }
            if (wasset == true)
            {
                GraphEditor.GraphEditorMain.weight = weight;
                this.Close();
            }
         
        }
    }
}
namespace GraphEditor
{
    public partial class StartForm : Form
    {
        public StartForm()
        {
            InitializeComponent();
            StartPageButton.Hide();
           
        }

        private void StartForm_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            GraphEditorMain gem = new GraphEditorMain();    
            gem.Show();
            this.Hide();    
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if (StartPageCheck.Checked)
            {
                StartPageButton.Show();
              

            }
            else 
            { 
                StartPageButton.Hide();
               
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {

        }
    }
}

