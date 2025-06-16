<?php

class Veiculo {
    private $veiculoDesc;
    private $veiculoPlaca;
    private $veiculoMarca;
    private $conexao;

    public function __construct($veiculoDesc, $veiculoPlaca,$veiculoMarca, $conexao) {
        $this->veiculoDesc = $veiculoDesc;
        $this->veiculoMarca = $veiculoMarca;
        $this->veiculoPlaca = $veiculoPlaca;
        $this->conexao = $conexao;
    }

    public function inserirVeiculo() {
        $sql = "INSERT INTO tbveiculo(veiculo_placa, veiculo_descricao, veiculo_marca) VALUES (?, ?, ?)";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('ssi', $this->veiculoPlaca, $this->veiculoDesc, $this->veiculoMarca);

        if ($stmt->execute()) {
            echo "Carro inserido com sucesso!";
        } else {
            echo "Erro ao inserir: " . $stmt->error;
        }
    }

    public function listarVeiculos() {
        $sql = "SELECT veiculo_placa, veiculo_marca, veiculo_descricao, marca_descricao 
                FROM tbveiculo 
                INNER JOIN tbmarca ON tbveiculo.veiculo_marca = tbmarca.marca_codigo";
        $resultado = $this->conexao->query($sql);

        if ($resultado->num_rows > 0) {
            echo "<h3>Listagem de Veículos</h3><table>";
            echo "<tr><th>Carro</th><th>Placa</th><th>Marca</th><th>Código da Marca</th><th>Editar</th>
            <th>Excluir</th>";

            foreach ($resultado as $row) {
                $desc = $row['veiculo_descricao'];
                $plc = $row['veiculo_placa'];
                $marca = $row['marca_descricao'];
                $cod_marca = $row['veiculo_marca'];
            
                echo "<tr>
                
                        <td>$desc</td>
                        <td>$plc</td>
                        <td>$marca</td>
                        <td>$cod_marca</td>
                         <td>                            
                          <form method='post' action='../routes/edits.php'>
                                <input type='hidden' name='entidade' value='veiculo'>
                                <input type='hidden' name='veiculo_placa' value='$plc'>
                                <input type='submit' name='editar_veiculo' value='Editar'>
                            </form>
                        <td>

                            <form method='post' action='../global.php'>
                                <input type='hidden' name='plc' value='$plc'>
                                <input type='submit' name='deletar_veiculo' value='Deletar'>
                            </form>
                        </td>
                      </tr>";
            }

            echo "</table>";
        } else {
            echo "<p>Nenhum veículo encontrado.</p>";
        }
    }

    public function deletarVeiculo($plc) {
        $sql = "DELETE FROM tbveiculo WHERE veiculo_placa = ?";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('s', $plc);

        if ($stmt->execute()) {
            echo "Veículo deletado com sucesso!";
        } else {
            echo "Erro ao deletar: " . $stmt->error;
        }
    }

    public function editarVeiculo(){
        $sql = "UPDATE tbveiculo SET veiculo_descricao = ? WHERE veiculo_placa = ? ";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('ss', $this->veiculoDesc, $this->veiculoPlaca);
        if ($stmt->execute()) {
            echo "Veículo editado com sucesso!";
        } else {
            echo "Erro ao deletar: " . $stmt->error;
        }
    
    }
}

?>
