<?php
$marca_desc = "";
$marca = new Marca("", $marca_desc, $conexao);
    
$carro_desc = ""; $carro_placa=""; $carro_marca="";
$carro = new Veiculo($carro_placa, $carro_marca, $carro_desc, $conexao);


$loc_codigo = ""; $loc_veiculo = ""; $loc_cliente = ""; $loc_dt_inicio = ""; $loc_dt_fim = "";
$locacao = new Locacao($loc_codigo,$loc_veiculo, $loc_cliente, $loc_dt_inicio, $loc_dt_fim, $conexao);


$nome="";$endereco="";$cpf='';
$cliente = new Cliente($cpf, $nome, $endereco, $conexao);
    







?>