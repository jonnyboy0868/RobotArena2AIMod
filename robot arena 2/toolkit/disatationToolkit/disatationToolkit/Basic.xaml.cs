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
    /// Interaction logic for Basic.xaml
    /// </summary>
    public partial class Basic : Window
    {
        //varibles that are going to be used to write out the final bindings line
        string bindings = "";//type of bot
        string bot_name = "";//name of the bot in the .botfile
        string final_printout = ""; //the final line that will be printed into the bindings.py file
        string direction = "";//the direction the bot if facing (in dregrees)
        string radius = "";// the size of the circle around the bot used for looking out for hazzards.
        string turnSpeed = " '2.5' "; //turnspeed - turning in radians/second AI will attempt not to exceed (default 2.5)
        string throttle = "100"; //maximum value the bot can accelerate by(default 100).
        string topSpeed = "";//max speed the bot will go too default =(4.0).
        string weapons = ""; //the binding location of the weapons on the bot.

        public Basic()
        {
            InitializeComponent();
        }

        //starting the code for the selection box

        /// <summary>
        /// will set the bot to be an axe box or '"Chopper"';
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Axe_Selected(object sender, RoutedEventArgs e)
        {//this \"\" creates a speach mark as a string using ascii code 
            bindings = "\"Chopper\"";
            //adds the all the varibles together as one string to be printed into the bindings.py file
            final_printout = System.String.Concat(bindings, "," , bot_name);
        }
        /// <summary>
        /// sets the bot type to '"Flipper"';
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Flipper_Selected(object sender, RoutedEventArgs e)
        {
            bindings = "\"Flipper\"";
        }

        private void Full_Spinner_Selected(object sender, RoutedEventArgs e)
        {
            bindings = "\"Spinner\"";
        }
        /// <summary>
        /// sets the bot type to '""DirectionalSpinner""'
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Directional_Spinner_Selected(object sender, RoutedEventArgs e)
        {
            bindings = "\"DirectionalSpinner\"";
        }
        /// <summary>
        /// sets the bot type to Rammer
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Rammer_Selected(object sender, RoutedEventArgs e)
        {
            bindings = "\"Rammer\"";
        }

        private void Piston_Selected(object sender, RoutedEventArgs e)
        {
            bindings = "\"Piston\"";
        }
        

        /// <summary>
        /// sets the name of the bot being aied for the writter when creating the listing in the bindings.py file
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void bot_name_TextChanged(object sender, TextChangedEventArgs e)
        {
            bot_name = System.String.Concat("\"", bot_name_button.Text, "\"", ",");
            //system.string.concat adds two strings and makes them into one value
        }
        /// <summary>
        /// example of how to write all lines into a document in windows, (in the example the document is called testdoc.txt)
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Save_clicked(object sender, RoutedEventArgs e)
        {
            //adds the all the varibles together as one string to be printed into the bindings.py file
            final_printout = System.String.Concat("    ","list.append( (" , bot_name, bindings,", {" ,radius , direction , topSpeed , turnSpeed,"'weapons':(0.0 , 0.0) } )  )") ;// feeding in each line to an array 
            System.IO.File.WriteAllText(@"..\..\..\..\testdoc.txt", final_printout);//writing the document. currently writing into  testdoc.txt needs to be changed to bindings.py before full release.
            //file path needs to be changed before publishing.
            MessageBox.Show("Bots bindings written and ready to use");//printing out a message to let the user know that the code has written
        }
        /// <summary>
        /// closes the appliaction
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
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

        private void forward_Selected(object sender, RoutedEventArgs e)
        {
            direction = "'nose' : math.pi ,";
        }
        /// <summary>
        /// to make the bot face forward e3
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void backwards_Selected(object sender, RoutedEventArgs e)
        {
            direction = "'-nose' : math.pi*2 ,";
        }

        private void Facing_Left_Selected(object sender, RoutedEventArgs e)
        {
            direction = "'nose' : math.pi/2 ,";
        }
        /// <summary>
        /// to make the bot face right
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Facing_Right_Selected(object sender, RoutedEventArgs e)
        {
            direction = "'nose' : -math.pi/2 ,";
        }

        private void TopSpeed_TextChanged(object sender, TextChangedEventArgs e)
        {
            topSpeed = System.String.Concat("'topspeed': ", TopSpeed.Text , ","); ;
        }

        private void TurnSpeed_TextChanged(object sender, TextChangedEventArgs e)
        {
            turnSpeed = System.String.Concat("'turnspeed': ", TurnSpeed.Text , ", ");
        }

        private void RadiusBox_TextChanged(object sender, TextChangedEventArgs e)
        {
            radius = System.String.Concat("'radius': ", RadiusBox.Text, ", ");
        }

        private void test_bot_Selected(object sender, RoutedEventArgs e)
        {
            bindings = "\"JonsBot\"";
        }

    }
}

                                                                             