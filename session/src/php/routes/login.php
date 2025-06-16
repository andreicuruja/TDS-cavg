<?php
session_start();

// Variáveis locais fixas para login e senha
$login_correto = "admin";
$senha_correta = "12345";

if (isset($_POST['botao'])) {
    $login = $_POST['login'] ?? '';
    $senha = $_POST['senha'] ?? '';

    if ($login === $login_correto && $senha === $senha_correta) {
        $_SESSION['login'] = $login;
        $_SESSION['nome'] = "Administrador";
        $_SESSION['ULTIMA_ATIVIDADE'] = time();

        header("Location: index.php");
        exit;
    } else {
        header("Location: login.html");
        exit;
    }
}
?>