<?php
include_once '../config/dbconexao.php';
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../../css/formstyle.css">
    <title>Sun Sprinter</title>
    </head>
<body>
    <header>
        <div class="header-left">
            <img src="../../img/logo.png" alt="Logo" class="logo">
            <button id="toggle-dark" class="nightmode">
                <img src="../../img/moon.png" alt="moon"
                class="moon">
            </button>
            <!-- 🌙 Modo Noturno e o Script pra ele na linha 36 -->
        </div>
    
        <div class="header-center">
            <nav class="nav-links">
                <a href="../../../index.html">Início</a>
                <a href="registros.php">Registros</a>
            </nav>
        </div>
    
        <div class="header-right">
            <h1>Sun Sprinter<br>Locadora de Veículos</h1>
        </div>
    </header>
    <div class="header-underline"></div>

    <script>
// Função para definir um cookie
function setCookie(nome, valor, dias) {
    const d = new Date();
    d.setTime(d.getTime() + (dias * 24 * 60 * 60 * 1000));
    const expira = "expires=" + d.toUTCString();
    document.cookie = nome + "=" + valor + ";" + expira + ";path=/";
}

function getCookie(nome) {
    const nomeEQ = nome + "=";
    const cookies = decodeURIComponent(document.cookie).split(';');
    for (let i = 0; i < cookies.length; i++) {
        let c = cookies[i].trim();
        if (c.indexOf(nomeEQ) === 0) return c.substring(nomeEQ.length, c.length);
    }
    return "";
}

if (getCookie("modoNoturno") === "true") {
    document.body.classList.add("dark-mode");
}

const toggleButton = document.getElementById("toggle-dark");
toggleButton.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    const modoAtivo = document.body.classList.contains("dark-mode");
    setCookie("modoNoturno", modoAtivo, 30);
});
</script>

<div class="form-container">

    <!-- Parte sobre o Cliente -->
    <div class="form">
        <h3>Cadastro do Cliente</h3>
        <form action="../global.php" method="post">
            <input type="text" name="nome-cliente" placeholder="Seu nome">
            <input type="text" name="cliente-cpf" placeholder="Seu CPF">
            <input type="text" name="cliente-endereco" placeholder="Seu endereço">
            <div class="form-buttons">
                <input type="submit" value="Cadastrar" name="cadastrar-cliente">
            </div>
        </form>
    </div>

    <!-- Parte sobre o Veículo -->
    <div class="form">
        <h3>Cadastro do Veículo</h3>
        <form action="../global.php" method="post">
            <input type="text" name="veic_desc" placeholder="Veículo">
            <select name="veic_marca">
                <option value="">Informe a Marca do Veículo</option>
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
            <input type="text" name="veic_placa" placeholder="Placa do veículo">
            <div class="form-buttons">
                <input type="submit" value="Cadastrar" name="cadastrar-veiculo">
            </div>
        </form>
    </div>

    <!-- Parte da Locação -->
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
            </div>
        </form>
    </div>
    
    <!-- Parte da Marca -->
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