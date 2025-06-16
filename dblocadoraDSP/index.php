<?php
    include_once 'src/php/config/dbconnect.php';
    include_once 'src/php/classes/Class-Adm.php';
    
    session_start(); 
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
<form method="post" action="">
    <h2>log</h2>
    <label for="nome_adm_log"></label>
    <input type="text" name="nome_adm_log" id="">
    <label for="senha_adm_log"></label>
    <input type="text" name="senha_adm_log" id="">
    <input type="submit" value="Enviar" name="adm_log">

</form>


<form method="post" action="">
    <h1>cad</h1>
    <label for="nome_adm_cad"></label>
    <input type="text" name="nome_adm_cad" id="">
    <label for="senha_adm_cad"></label>
    <input type="text" name="senha_adm_cad" id="">
    <input type="submit" value="Enviar" name="cad_adm">

</form>

<?php 
if(isset($_POST['cad_adm'])){
    $login = $_POST['nome_adm_cad'];
    $senha = $_POST['senha_adm_cad'];

    $_SESSION['login'] = $login;
    $_SESSION['senha'] = $senha;

    $adm = new adm('',$login,$senha,$conexao);
    $adm->insereAdm();
    header("Location:src/php/routes/home.php");

}
if(isset($_POST['adm_log'])){
    $login = $_POST['nome_adm_log'];
    $senha = $_POST['senha_adm_log'];
    $adm = new adm('', $login, $senha, $conexao);
    $loginValido = $adm->buscaAdm();    
   
    if($loginValido){
        
        $_SESSION['login'] = $login;
    
        header("Location:src/php/routes/home.php");
        
        exit();
    }else{
        echo "Login ou senha incorretos!";


    }
}



?>


</body>
</html>