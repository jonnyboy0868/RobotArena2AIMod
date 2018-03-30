using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;

namespace disatationToolkit
{
    /// <summary>
    /// Interaction logic for Advanced.xaml
    /// </summary>
    public partial class Page_Advanced : Window
    {
        public Page_Advanced()
        {
            InitializeComponent();
        }

        private void Exit_Program_Click(object sender, RoutedEventArgs e)
        {
            this.Close();//ends the program
        }
        /// <summary>
        /// moving user to the main menu
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void main_menu_Click(object sender, RoutedEventArgs e)
        {
            Window mainMenu = new MainWindow();//create a new MainWindow
            mainMenu.Show();//shows the window that was just made.
            this.Close();//removes the current window
        }
    }
}
