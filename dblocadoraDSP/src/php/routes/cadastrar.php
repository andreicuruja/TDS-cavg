<?php
include_once '../config/dbconnect.php';
include_once '../config/logout.php';
session_start(); 
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro Geral - Moon Runner</title>
    <link rel="stylesheet" href="../../css/cadastrarstyle.css">
</head>
<body>

<header>
    <div class="header-left">
        <img src="../../img/logo.png" alt="Logo" class="logo">
    </div>

    <div class="header-center">
        <nav class="nav-links">
            <a href="home.php">Início</a>
            <a href="verificar-registros.php">Verificar Registros</a>
        </nav>
    </div>

    <div class="header-right">
        <h1>Moon Runner<br>Locadora de Veículos</h1>
    </div>
</header>

<!-- Container de formulários -->
<div class="form-container">

    <!-- Cliente -->
    <div class="form">
        <h3>Cadastro de Cliente</h3>
        <form action="../global.php" method="post">
            <input type="text" name="cliente-cpf" placeholder="Seu nome">
            <input type="text" name="nome-cliente" placeholder="Seu CPF">
            <input type="text" name="cliente-endereco" placeholder="Seu endereço">
            <div class="form-buttons">
                <input type="submit" value="Cadastrar" name="cadastrar-cliente">
                <!-- <input type="submit" value="Listar" name="listar-cliente"> -->
            </div>
        </form>
    </div>

    <!-- Carro -->
    <div class="form">
        <h3>Cadastro de Carro</h3>
        <form action="../global.php" method="post">
            <input type="text" name="carro_desc" placeholder="Carro">
            <select name="carro_marca">
                <option value="">Informe a Marca</option>
                <?php
                $sql = "SELECT marca_codigo, marca_descricao FROM tbmarca";
                $resultado = $conexao->query($sql);
                if ($resultado->num_rows > 0) {
                    foreach($resultado as $row){
                        $codigo = $row['marca_codigo'];
                        $desc = $row['marca_descricao'];
                        echo "<option value='$codigo'>$desc</option>";
                    }
                }
                ?>
            </select>
            <input type="text" name="carro_placa" placeholder="Placa do veículo">
            <div class="form-buttons">
                <input type="submit" value="Cadastrar" name="cadastrar-carro">
                <!-- <input type="submit" value="Listar" name="listar-carro"> -->
            </div>
        </form>
    </div>

    <!-- Locação -->
    <div class="form">
        <h3>Cadastro de Locação</h3>
        <form action="../global.php" method="post">
            <select name="cliente_loc">
                <option value="">Informe o Cliente</option>
                <?php
                $sql = "SELECT cliente_nome, cliente_cpf FROM tbcliente";
                $resultado = $conexao->query($sql);
                if ($resultado->num_rows > 0) {
                    foreach($resultado as $row){
                        $nome = $row['cliente_nome'];
                        $cpf = $row['cliente_cpf'];
                        echo "<option value='$cpf'>$nome</option>";
                    }
                }
                ?>
            </select>

            <select name="veiculo_loc">
                <option value="">Informe o Veículo</option>
                <?php
                $sql = "SELECT veiculo_placa, veiculo_descricao FROM tbveiculo";
                $resultado = $conexao->query($sql);
                if ($resultado->num_rows > 0) {
                    foreach($resultado as $row){
                        $veiculo = $row['veiculo_descricao'];
                        $placa = $row['veiculo_placa'];
                        echo "<option value='$placa'>$veiculo - $placa</option>";
                    }
                }
                ?>
            </select>

            <input type="date" name="dt_inicio">
            <input type="date" name="dt_fim"><br><br>

            <div class="form-buttons">
                <input type="submit" value="Cadastrar" name="cadastrar-locacao">
                <!-- <input type="submit" value="Listar" name="listar-locacao"> -->
            </div>
        </form>
    </div>

    <!-- Marca -->
    <div class="form">
        <h3>Cadastro de Marca</h3>
        <form action="../global.php" method="post">
            <input type="text" name="marca_nome" placeholder="Marca">
            <div class="form-buttons">
                <input type="submit" name="cadastrar_marca" value="Cadastrar Marca">
            </div>
        </form>
    </div>

</div>

</body>
</html>
