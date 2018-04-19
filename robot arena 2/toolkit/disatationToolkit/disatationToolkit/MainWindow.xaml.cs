
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
using System.Windows.Navigation;
using System.Windows.Shapes;


namespace disatationToolkit
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
    public MainWindow()
        {
            InitializeComponent();
        }
        /// <summary>
        /// sets the bots a.i type to and axe bot style
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
           //testing writting 

        //for testing read in
        //private void Test_Button2_Clicked(object sender, RoutedEventArgs e)
        //{
        //    int i = 0;
        //    string testline;
        //    //read the file in line by line
        //    System.IO.StreamReader file =
        //        new System.IO.StreamReader(@"B:\OneDrive\uni\year 3\disatation\toolkit\testdoc2.txt");
        //    while ((testline = file.ReadLine()) != null)
        //    {
        //        //prints out the last line read in from the source file
        //        System.IO.File.WriteAllText(@"B:\OneDrive\uni\year 3\disatation\toolkit\testWrite.txt", testline);

        //        i++;//increment the counter by one.
        //    }
        //    //after done reading close off the orignal file
        //    file.Close();
        //    MessageBox.Show("Document read and rewritten");
        //}

  
        /// <summary>
        /// Opens the next window and closes the last page
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Basic_Button_Clicked(object sender, System.Windows.RoutedEventArgs e)
        {
            Window Basic = new Basic();
            Basic.Show();
            this.Close();
        } 
        /// <summary>
        /// closes the application
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Exit_Program_Click(object sender, RoutedEventArgs e)
        {
            this.Close();//ends the program
        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }
  
    }
}
