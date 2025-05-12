<?php  
include_once '../global.php';
include_once '../config/listagens.php';
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../../css/registrosstyle.css">
    <title>Registros - Sun Sprinter</title>
</head>
<body>
    <header>
        <div class="header-left">
            <img src="../../img/logo.png" alt="logo" class="logo">

            <button id="toggle-dark" class="nightmode">
                <img src="../../img/moon.png" alt="moon" class="moon">
            </button>
            <!-- 🌙 Modo Noturno e o Script pra ele na linha 37 -->
        </div>
    
        <div class="header-center">
            <nav class="nav-links">
                <a href="../../../index.html">Início</a>
                <a href="form.php">Cadastros</a>
            </nav>
        </div>
    
        <div class="header-right">
            <h1>Sun Sprinter<br>Locadora de Veículos</h1>
        </div>
    </header>
    <div class="header-underline"></div>

    <script>
// Função para definir um cookie com nome, valor e dias de validade
function setCookie(nome, valor, dias) {
    const d = new Date();
    d.setTime(d.getTime() + (dias * 24 * 60 * 60 * 1000));
    const expira = "expires=" + d.toUTCString();
    document.cookie = nome + "=" + valor + ";" + expira + ";path=/";
}

// Função para obter o valor de um cookie pelo nome
function getCookie(nome) {
    const nomeEQ = nome + "=";
    const cookies = decodeURIComponent(document.cookie).split(';');
    for (let i = 0; i < cookies.length; i++) {
        let c = cookies[i].trim();
        if (c.indexOf(nomeEQ) === 0) return c.substring(nomeEQ.length, c.length);
    }
    return "";
}

// Aplica o modo escuro se o cookie estiver setado como "true"
if (getCookie("modoNoturno") === "true") {
    document.body.classList.add("dark-mode");
}

// Alterna o modo escuro e salva a preferência no cookie
const toggleButton = document.getElementById("toggle-dark");
toggleButton.addEventListener("click", () => {
    document.body.classList.toggle("dark-mode");
    const modoAtivo = document.body.classList.contains("dark-mode");
    setCookie("modoNoturno", modoAtivo, 30); // 30 dias de validade
});
</script>

    
    <!-- Container para Listagens -->
    <div class="cards-container">
        <div class="card">
            <div class="veiculos-grid">
                <?php
                    $veiculo->listarVeiculo();
                ?>
            </div>
        </div>

        <div class="card">
            <div class="marcas-grid">
                <?php
                    $marca->listarMarca();
                ?>
            </div>
        </div>
        <div class="card">
            <div class="clientes-grid">
                <?php
                    $cliente->listarCliente();
                ?>
            </div>
        </div>
<div class="cardvi">
<div class="visualizacao-grid">
    <?php
    include '../config/dbconexao.php';

    // Consulta para pegar veículos LOCADOS (com locação atual)
    $sql_locados = "
        SELECT v.veiculo_placa, v.veiculo_descricao, m.marca_descricao
        FROM tbveiculo v
        INNER JOIN tblocacao l ON v.veiculo_placa = l.locacao_veiculo
        INNER JOIN tbmarca m ON v.veiculo_marca = m.marca_codigo
        WHERE l.locacao_data_fim >= CURDATE()
    ";

    // Consulta para pegar veículos DISPONÍVEIS (sem locação ativa)
    $sql_disponiveis = "
        SELECT v.veiculo_placa, v.veiculo_descricao, m.marca_descricao
        FROM tbveiculo v
        INNER JOIN tbmarca m ON v.veiculo_marca = m.marca_codigo
        WHERE v.veiculo_placa NOT IN (
            SELECT locacao_veiculo
            FROM tblocacao
            WHERE locacao_data_fim >= CURDATE()
        )
    ";

    $res_disp = $conexao->query($sql_disponiveis);
    $res_loc = $conexao->query($sql_locados);

    // Exibindo veículos disponíveis
    echo "<h2>Veículos Disponíveis 🚗</h2>";
    if ($res_disp->num_rows > 0) {
        echo "<table>";
        echo "<thead>
                <tr>
                    <th>Descrição</th>
                    <th>Placa</th>
                    <th>Marca</th>
                </tr>
              </thead><tbody>";
        while ($row = $res_disp->fetch_assoc()) {
            echo "<tr>
                    <td>{$row['veiculo_descricao']}</td>
                    <td>{$row['veiculo_placa']}</td>
                    <td>{$row['marca_descricao']}</td>
                  </tr>";
        }
        echo "</tbody></table>";
    } else {
        echo "<p>Nenhum veículo disponível.</p>";
    }?>
<br><br>
<?php
include '../config/dbconexao.php';
    // Exibindo veículos locados
    echo "<h2>Veículos Locados 🔒</h2>";
    if ($res_loc->num_rows > 0) {
        echo "<table>";
        echo "<thead>
                <tr>
                    <th>Descrição</th>
                    <th>Placa</th>
                    <th>Marca</th>
                </tr>
              </thead><tbody>";
        while ($row = $res_loc->fetch_assoc()) {
            echo "<tr>
                    <td>{$row['veiculo_descricao']}</td>
                    <td>{$row['veiculo_placa']}</td>
                    <td>{$row['marca_descricao']}</td>
                  </tr>";
        }
        echo "</tbody></table>";
    } else {
        echo "<p>Nenhum veículo locado.</p>";
    }
    ?>
</div>
</div>
<div class="locacoes-grid">

            <?php
                $locacao->listarLocacao();
            ?>
        </div>
<br>
</body>
</html>
