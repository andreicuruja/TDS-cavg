

<!-- ISSO É O LOGIN.HTML TROCADO PRA INDEX PQ SE NAO N CONSIGO FAZER FUNCIONAR KKKKKKKKKKKKKKKKKK -->
<?php
    include_once 'src/php/config/dbconexao.php';
    include_once 'src/php/class/classAdmin.php';
    session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="src/css/indexstyle.css">
    <title>Sun Sprinter</title>
</head>
<body>
    <header>
        <div class="header-left">
            <img src="src/img/logo.png" alt="Logo" class="logo">

            <button id="toggle-dark" class="nightmode">
                <img src="src/img/moon.png" alt="moon"
                class="moon">
            </button>
        </div>
        <div class="header-center">
            <nav class="nav-links">

            </nav>
        </div>
    
        <div class="header-right">
            <h1>Sun Sprinter<br>Locadora de Veículos</h1>
        </div>
    </header>
    <div class="header-underline"></div>

<form method="post" >
    <h2>Login</h2>
    <label for="nome_adm_log"></label>
    <input type="text" name="nome_adm_log" id="">
    <label for="senha_adm_log"></label>
    <input type="text" name="senha_adm_log" id="">
    <input type="submit" value="Enviar" name="adm_log">
</form>
<form method="post" >
    <h1>Cadastrar</h1>
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
    //$_SESSION['senha'] = $senha;

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
        //exit();   
    }else{
        echo "Login ou senha incorretos!";
    }
}
?>
<script src="src/js/darkmode.js"></script>
</body>
</html>