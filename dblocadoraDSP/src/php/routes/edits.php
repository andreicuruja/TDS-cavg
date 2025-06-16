<?php
    session_start(); 
    include_once '../classes/Class-Cliente.php';
    include_once '../classes/Class-Veiculo.php';
    include_once '../classes/Class-Locacao.php';
    include_once '../classes/Class-Marca.php';
    include_once '../config/dbconnect.php';
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
    <link rel="stylesheet" href="../../css/edits.css">
    <title>Editar</title>
</head>
<body>
    <header>
        <div class="header-left">
            <img src="../../../src/img/logo.png" alt="Logo" class="logo">
        </div>
    
        <div class="header-center">
            <nav class="nav-links">
                <a href="home.php">Início</a>
                <a href="cadastrar.php">Cadastrar Veículos</a>
                <a href="verificar-registros.php">Verificar Registros</a>
            </nav>
        </div>
    
        <div class="header-right">
            <h1>Moon Runner<br>Locadora de Veículos</h1>
        </div>
    </header>

    <form action="../global.php" method="POST">
                <?php
            echo inputHidden('entidade', $entidade);

            switch ($entidade) {
                case 'marca':
                    echo inputHidden('codigo_marca', $dados['codigo_marca'] ?? '');
                    echo "<div class='form-group'>
                            <label>Nova Descrição da Marca:</label>
                            <input type='text' name='nome_marca' value='" . ($dados['marca_descricao'] ?? '') . "'>
                          </div>";
                    echo "<button type='submit' name='atualizar_marca'>Atualizar Marca</button>";
                    break;

                case 'veiculo':
                    echo inputHidden('placa', $dados['veiculo_placa'] ?? '');
                    echo "<div class='form-group'>
                            <label>Descrição:</label>
                            <input type='text' name='descricao' value='" . ($dados['descricao'] ?? '') . "'>
                          </div>";
                    echo "<button type='submit' name='atualizar_veiculo'>Atualizar Veículo</button>";
                    break;

                case 'cliente':
                    echo inputHidden('cpf', $dados['cpf'] ?? '');
                    echo "<div class='form-group'>
                            <label>Nome:</label>
                            <input type='text' name='nome' value='" . ($dados['nome'] ?? '') . "'>
                          </div>
                          <div class='form-group'>
                            <label>Endereço:</label>
                            <input type='text' name='endereco' value='" . ($dados['endereco'] ?? '') . "'>
                          </div>";
                    echo "<button type='submit' name='atualizar_cliente'>Atualizar Cliente</button>";
                    break;

                case 'locacao':
                    echo inputHidden('loc_codigo', $dados['loc_codigo'] ?? '');
                    echo "<div class='form-group'>
                            <label>Nova Data de Início:</label>
                            <input type='date' name='loc_dt_inicio' value='" . ($dados['loc_dt_inicio'] ?? '') . "'>
                          </div>
                          <div class='form-group'>
                            <label>Nova Data de Fim:</label>
                            <input type='date' name='loc_dt_fim' value='" . ($dados['loc_dt_fim'] ?? '') . "'>
                          </div>";
                    echo "<button type='submit' name='atualizar_locacao'>Atualizar Locação</button>";
                    break;

                default:
                    echo "<p>Entidade não reconhecida.</p>";
                    break;
            }
        ?>
    </form>

</body>
</html>
