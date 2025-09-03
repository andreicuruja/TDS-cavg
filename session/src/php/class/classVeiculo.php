<?php
class Veiculo
{
    private $veiculo_nome;
    private $veiculo_placa;
    private $veiculo_marca;
    private $conexao;

    public function __construct($veiculo_nome, $veiculo_marca, $veiculo_placa, $conexao)
    {
        $this->veiculo_nome  = $veiculo_nome;
        $this->veiculo_marca = $veiculo_marca;
        $this->veiculo_placa = $veiculo_placa;
        $this->conexao = $conexao;
    }
    public function inserirVeiculo(){
        $sql = "INSERT INTO tbveiculo(veiculo_placa, veiculo_descricao, veiculo_marca) VALUES (?,?,?)";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('ssi', $this->veiculo_nome, $this->veiculo_placa, $this->veiculo_marca);

        if($stmt->execute()){
            echo "Veículo Inserido.";
        }else{
            echo "Erro ao Inserir Veículo.". $stmt->error;
        }

        $stmt->close();
        /*<-- se der problema apaga o close-->*/
    }
    public function listarVeiculo(){
        $sql = "SELECT veiculo_placa, veiculo_marca, veiculo_descricao, marca_descricao FROM tbveiculo INNER JOIN tbmarca ON tbveiculo.veiculo_marca = tbmarca.marca_codigo";
        $resultado = $this->conexao->query($sql);
        
        if ($resultado->num_rows > 0) {
            echo "<h3>Listagem de Veículos</h3>";
            echo "<div class='veiculos-grid'>";
    
            foreach($resultado as $row){
                $desc = $row['veiculo_descricao'];
                $placa = $row['veiculo_placa'];
                $marca = $row['marca_descricao'];
                $idmarca = $row['veiculo_marca'];

                echo "<div class='card'>";
                echo "<p><strong>Marca:</strong> $marca</p>";
                echo "<p><strong>Veículo:</strong> $desc</p>";
                echo "<p><strong>Placa:</strong> $placa</p>";
                echo "<p><strong>Código da Marca:</strong> $idmarca</p>";
                echo "<div class='acoes'>";
                echo "<form method='post' action='../routes/editar.php'>
                            <input type='hidden' name='entidade' value='veiculo'>
                            <input type='hidden' name='veiculo_placa' value='$placa'>
                            <input type='submit' name='editar_veiculo' value='Editar'>
                        </form>";
                echo "<form method='post' action='../global.php'>
                            <input type='hidden' name='plc' value='$placa'>
                            <input type='submit' name='deletar_veiculo' value='Deletar'>
                        </form>";
                echo "</div>";
                echo "</div>";
            }
            echo "</div>";
        } else {
            echo "<p>Nenhum veículo encontrado.</p>";
        }

    }
    public function editarVeiculo(){
        $sql = "UPDATE tbveiculo SET veiculo_descricao = ? WHERE veiculo_placa = ? ";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('ss', $this->veiculo_nome, $this->veiculo_placa);
        if ($stmt->execute()) {
            echo "Veículo editado com sucesso!";
        } else {
            echo "Erro ao deletar: " . $stmt->error;
        }
    }
    public function deletarVeiculo($placa) {
        $sql = "DELETE FROM tbveiculo WHERE veiculo_placa = ?";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('s', $placa);
        if ($stmt->execute()) {
            echo "O Veículo foi Deletado.";
        } else {
            echo "Não foi Possível Deletar: " . $stmt->error;
        }
    }
}
?>