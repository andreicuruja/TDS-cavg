<?php  
include_once '../global.php';
include_once '../config/listagens.php';
include_once '../config/logout.php';
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
        </div>
    
        <div class="header-center">
            <nav class="nav-links">
                <a href="home.php">Início</a>
                <a href="form.php">Cadastros</a>
            </nav>
        </div>
    
        <div class="header-right">
            <h1>Sun Sprinter<br>Locadora de Veículos</h1>
        </div>
    </header>
    <div class="header-underline"></div>
    
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

    $sql_locados = "
        SELECT v.veiculo_placa, v.veiculo_descricao, m.marca_descricao
        FROM tbveiculo v
        INNER JOIN tblocacao l ON v.veiculo_placa = l.locacao_veiculo
        INNER JOIN tbmarca m ON v.veiculo_marca = m.marca_codigo
        WHERE l.locacao_data_fim >= CURDATE()
    ";

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
<script src="../../js/darkmode.js"></script>
</body>
</html>
