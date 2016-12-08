using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Runtime.InteropServices;

namespace AutoHaruhi
{
    public partial class AutoHaruhi : Form
    {
        [DllImport("USER32.dll")]
        static extern short GetAsyncKeyState(Keys vKey);
        [DllImport("USER32.dll", CallingConvention = CallingConvention.StdCall)]
        static extern void SetCursorPos(int X, int Y);
        [DllImport("USER32.dll", CallingConvention = CallingConvention.StdCall)]
        static extern void mouse_event(int dwFlags, int dx, int dy, int cButtons, int dwExtraInfo);

        private const int MOUSEEVENTF_LEFTDOWN = 0x2;
        private const int MOUSEEVENTF_LEFTUP = 0x4;

        int input_mouse_cursor_pos_x; // input mouse cursor pos x
        int input_mouse_cursor_pos_y; // input mouse cursor pos y
        int now_mouse_cursor_pos_x; // now mouse cursor pos x
        int now_mouse_cursor_pos_y; // now mouse cursor pos y
        int wait_time = 3; // wait time
        bool automatic_flag = false; // automatic flag (default:false)

        public AutoHaruhi()
        {
            InitializeComponent();
        }

        private async void SleepAsync()
        {
            await Task.Delay(wait_time * 1000);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            textBox1.ReadOnly = true; // lock textbox1
        }

        private async void button2_Click(object sender, EventArgs e)
        {
            if (!int.TryParse(textBox2.Text, out wait_time))
            {
                MessageBox.Show("正しい数値を入力して下さい",
                      "エラー", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
            else
            {
                automatic_flag = true;
            }
            if (automatic_flag == true)
            {
                while (true)
                {
                    await Task.Delay(wait_time * 1000);
                    now_mouse_cursor_pos_x = System.Windows.Forms.Cursor.Position.X;  // get now mouse cursor pos x
                    now_mouse_cursor_pos_y = System.Windows.Forms.Cursor.Position.Y;  // get now mouse cursor pos y
                    SetCursorPos(input_mouse_cursor_pos_x, input_mouse_cursor_pos_y); // set cursor pos -> input mouse cursor pos
                    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0);                    // mouse left button down
                    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0);                      // mouse left button up
                    SetCursorPos(now_mouse_cursor_pos_x, now_mouse_cursor_pos_y);     // set cursor pos -> now mouse cursor pos

                    if (GetAsyncKeyState(Keys.F10) < 0) { this.Close(); }
                }
            }
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (textBox1.ReadOnly == false)
            {
                if (GetAsyncKeyState(Keys.F9) < 0)
                {
                    input_mouse_cursor_pos_x = System.Windows.Forms.Cursor.Position.X; // get mouse cursor pos x
                    input_mouse_cursor_pos_y = System.Windows.Forms.Cursor.Position.Y; // get mouse cursor pos y
                }
                textBox1.Text = ("x : " + input_mouse_cursor_pos_x + " y : " + input_mouse_cursor_pos_y); // show get pos
            }

        }
    }
}
