<?php 
include_once '../global.php';
include_once '../config/logout.php';
include_once '../config/listagem-constructor.php';

session_start(); 

?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verificar Registros - Moon Runner</title>
    <link rel="stylesheet" href="../../css/verificarstyle.css">
</head>
<body>

<header>
    <div class="header-left">
        <img src="../../img/logo.png" alt="Logo" class="logo">
    </div>

    <div class="header-center">
        <nav class="nav-links">
            <a href="home.php">Início</a>
            <a href="cadastrar.php">Cadastrar</a>
        </nav>
    </div>

    <div class="header-right">
        <h1>Moon Runner<br>Locadora de Veículos</h1>
    </div>
</header>
<div class="form_container">
    <div class="tabelas-superiores">
        <!-- Marca -->
        <div>
            <?php $marca->listarMarca(); ?>
        </div>

        <!-- Carro -->
        <div>
            <?php $carro->listarVeiculos(); ?>
        </div>

        <!-- Cliente -->
        <div>
            <?php $cliente->listarCliente(); ?>
        </div>
    </div>

    <!-- Locações (embaixo) -->
    <div class="locacoes-grid">
        <?php $locacao->listarLocacoes(); ?>
    </div>
</div>





</body>
</html>