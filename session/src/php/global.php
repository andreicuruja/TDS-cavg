<?php
include_once 'config/dbconexao.php';
include_once 'class/classMarca.php';
include_once 'class/classVeiculo.php';
include_once 'class/classCliente.php';
include_once 'class/classLocacao.php';

if(isset($_POST['cadastrar-cliente'])){
    $nome = $_POST['nome-cliente'];
    $cpf = $_POST['cliente-cpf'];
    $endereco = $_POST['cliente-endereco'];
    $cliente = new Cliente($nome, $cpf, $endereco, $conexao);
    $cliente->inserirCliente();
    
}if(isset($_POST['cadastrar-veiculo'])){
    $veic_desc = $_POST['veic_desc'];
    $veic_marca = $_POST['veic_marca'];
    $veic_placa = $_POST['veic_placa'];
    $veic_desc; $veic_placa; $veic_marca;
    $veiculo = new Veiculo($veic_placa, $veic_marca, $veic_desc, $conexao);
    $veiculo->inserirVeiculo();

}if(isset($_POST['cadastrar-locacao'])){
    $loc_veiculo = $_POST['veiculo_loc'];
    $loc_cliente = $_POST['cliente_loc'];
    $loc_dt_inicio = $_POST['dt_inicio'];
    $loc_dt_fim = $_POST['dt_fim'];
    $locacao = new Locacao($loc_veiculo, $loc_cliente, $loc_dt_inicio, $loc_dt_fim, $conexao);
    $locacao->inserirLocacao();

}if(isset($_POST['cadastrar_marca'])){
    $marca_desc = $_POST['marca_nome'];
    $marca = new Marca($marca_desc, $conexao);
    $marca->inserirMarca();
}
//////////////////////////////////////////////////////////////////////////////////////////////
if (isset($_POST['delete'])) {
    $cpf = $_POST['cpf'];
    $cliente = new Cliente($cpf, "", "", $conexao);
    $cliente->deletarCliente($cpf);
}

if (isset($_POST['deletar_veiculo'])) {
    $placa = $_POST['plc'];
    $veiculo = new Veiculo($placa, '', '', $conexao);
    $veiculo->deletarVeiculo($placa);
}

if (isset($_POST['deletar_locacao'])) {
    $loc_codigo = $_POST['loc_codigo'];
    $locacao = new Locacao('', '', '', '', $conexao); 
    $locacao->deletarLocacao($loc_codigo);
}

if (isset($_POST['deletar_marca'])) {
    $codigo = $_POST['codigo_marca'];
    $marca = new Marca('', $conexao);
    $marca->deletarMarca($codigo);
}

if (isset($_POST['atualizar_marca'])) {
    $nome_marca = $_POST['nome_marca'];
    $codigo = $_POST['codigo_marca'];
    
    $marca = new Marca($nome_marca, $conexao);
    $marca->editarMarca($codigo);
}

if (isset($_POST['atualizar_veiculo'])) {
    $plc = $_POST['placa'];
    $desc = $_POST['descricao'];
    $veiculo = new Veiculo($desc, '', $plc, $conexao);
    $veiculo->editarVeiculo();

}if (isset($_POST['atualizar_cliente'])) {
    $cpf = $_POST['cpf'];
    $nome = $_POST['nome'];
    $endereco = $_POST['endereco'];
    $cliente = new Cliente($nome, $cpf, $endereco, $conexao);
    $cliente->editarCliente();
    
}if (isset($_POST['atualizar_locacao'])) {
    $loc_codigo = $_POST['loc_codigo'];
    $data_locacao = $_POST['loc_dt_inicio'];
    $data_devolucao = $_POST['loc_dt_fim'];
    $locacao = new Locacao("", "", $data_locacao, $data_devolucao, $conexao, $loc_codigo);
    $locacao->editarLocacao();
    }
?>