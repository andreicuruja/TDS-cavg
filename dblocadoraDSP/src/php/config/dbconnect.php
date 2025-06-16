<?php
$host ="localhost";
$password ="";  
$user ="root"; 
$db = "autolocadora";
// $db = "bdautolocadora2025";
// $db = "autolocadora2";
// $db = "db_moonrunner";
$conexao = new mysqli($host, $user, $password, $db);


if($conexao->connect_errno){
    echo "Falha ao conectar MySQL".$conexao->connect_error;
    exit();
}
?>