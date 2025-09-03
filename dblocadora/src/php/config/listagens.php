<?php

$marca_desc = "";
$marca = new Marca($marca_desc, $conexao);
    
$veic_desc = ""; $veic_placa=""; $veic_marca="";
$veiculo = new Veiculo($veic_placa, $veic_marca, $veic_desc, $conexao);

$loc_veiculo = ""; $loc_cliente = ""; $loc_dt_inicio = ""; $loc_dt_fim = "";
$locacao = new Locacao($loc_veiculo, $loc_cliente, $loc_dt_inicio, $loc_dt_fim, $conexao);

$nome="";$endereco="";$cpf='';
$cliente = new Cliente($nome, $cpf, $endereco, $conexao);
?>