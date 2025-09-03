<?php
include_once '../config/dbconexao.php';
include_once '../class/classMarca.php';
include_once '../class/classVeiculo.php';
include_once '../class/classCliente.php';
include_once '../class/classLocacao.php';
include_once '../config/logout.php';

    $entidade = $_POST['entidade'] ?? '';
    $dados = $_POST;

    function inputHidden($name, $value){
        return "<input type='hidden' name='$name' value='$value'>";
    }
?>
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../../css/editarstyle.css">
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
    </div>
    
    <div class="header-center">
        <nav class="nav-links">
            <a href="home.php">Início</a>
            <a href="registros.php">Registros</a>
            <a href="form.php">Cadastros</a>
        </nav>
    </div>
    
    <div class="header-right">
        <h1>Sun Sprinter<br>Locadora de Veículos</h1>
    </div>
</header>
<div class="header-underline"></div>
<div class="form-container">
    <form class="form" action="../global.php" method="POST">
        <?php
            echo inputHidden('entidade', $entidade);
            $entidade = $_POST['entidade'] ?? '';

// echo "<pre>Entidade recebida: '$entidade'</pre>";
            switch ($entidade) {
                case 'marca':
                    echo inputHidden('codigo_marca', $dados['codigo_marca'] ?? '');
                    echo "<h3>Editar Marca</h3>";
                    echo "<div class='form-group'>
                            <label>Novo nome da Marca:</label>
                            <input type='text' name='nome_marca' value='" . ($dados['marca_descricao'] ?? '') . "'>
                          </div>
                          <div class='form-buttons'>
                            <input type='submit' name='atualizar_marca' value='Atualizar Marca'>
                          </div>";
                    break;

                case 'veiculo':
                    echo inputHidden('placa', $dados['veiculo_placa'] ?? '');
                    echo "<h3>Editar Veículo</h3>";
                    echo "<div class='form-group'>
                            <label>Novo nome do Veículo:</label>
                            <input type='text' name='descricao' value='" . ($dados['descricao'] ?? '') . "'>
                          </div>
                          <div class='form-buttons'>
                            <input type='submit' name='atualizar_veiculo' value='Atualizar Veículo'>
                          </div>";
                    break;

                case 'cliente':
                    echo inputHidden('cpf', $dados['cpf'] ?? '');
                    echo "<h3>Editar Cliente</h3>";
                    echo "<div class='form-group'>
                            <label>Nome:</label>
                            <input type='text' name='nome' value='" . ($dados['nome'] ?? '') . "'>
                          </div>
                          <div class='form-group'>
                            <label>Endereço:</label>
                            <input type='text' name='endereco' value='" . ($dados['endereco'] ?? '') . "'>
                          </div>
                          <div class='form-buttons'>
                            <input type='submit' name='atualizar_cliente' value='Atualizar Cliente'>
                          </div>";
                    break;

                case 'locacao':
                    echo inputHidden('loc_codigo', $dados['loc_codigo'] ?? '');
                    echo "<h3>Editar Locação</h3>";
                    echo "<div class='form-group'>
                            <label>Nova Data de Início:</label>
                            <input type='date' name='loc_dt_inicio' value='" . ($dados['loc_dt_inicio'] ?? '') . "'>
                          </div>
                          <div class='form-group'>
                            <label>Nova Data de Fim:</label>
                            <input type='date' name='loc_dt_fim' value='" . ($dados['loc_dt_fim'] ?? '') . "'>
                          </div>
                          <div class='form-buttons'>
                            <input type='submit' name='atualizar_locacao' value='Atualizar Locação'>
                          </div>";
                    break;

                default:
                    echo "<p>Entidade não reconhecida.</p>";
                    break;
            }
        ?>
    </form>
</div>
<script src="../../js/darkmode.js"></script>
</body>
</html>