<?php
    $emailAdress = $_POST['emailAdress'];
    $password = $_POST['password'];
    $reTypepassword = $_POST['reTypepassword'];

    //database connection

    $connection = new mysqli('localhost','root','','team_tiger');
    if($connection->connect_error){
        die('connection Failed : ' $connection->connect_error);
    }else{
        $stmt = $connection->prepare("Insert into signin(emailAdress, password, reTypepassword)")
        $stmt->bind_param("sss",$emailAdress,$password,$reTypepassword);
        $stmt ->execute();
        echo "Your signUp was seccessful......"
        $stmt->close();
        $connection->close();
    }

?>