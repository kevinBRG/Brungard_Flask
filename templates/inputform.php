<?php
include_once('connection.php')

if(isset($_POST['submit']))
{
    if(!empty($_POST['fname']) && ($_POST['lname']))
    {
        $fname=$_POST['fname'];
        $lname=$_POST['lname'];


        if(mysql_query("insert into name (fname, lname)
        values('$fname','$lname')"));
        {
            echo " Your Data has been saved into database";
            header("referesh:2,url=action_page.php");
        }
        else{
            echo "Please check the Query";
        }
        else{
            echo "Please enter Fill in the Blanks";
        }
    }
}



?>
