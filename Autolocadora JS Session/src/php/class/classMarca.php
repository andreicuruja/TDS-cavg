<?php
class Marca
{
    private $marca_nome;
    private $conexao;

    public function __construct($marca_desc, $conexao)
    {
        $this->marca_nome = $marca_desc;
        $this->conexao = $conexao;
    }
    public function inserirMarca(){
        $sql = "INSERT INTO tbmarca (marca_descricao) VALUES (?)";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param("s", $this->marca_nome);

        if ($stmt->execute()) {
            echo "Marca Inserida com Sucesso.";
        } else {
            echo "Falha ao Inserir Marca: " . $stmt->error;
        }

        $stmt->close();
    }
    public function listarMarca() {
        $sql = "SELECT marca_codigo, marca_descricao FROM tbmarca";
        $resultado = $this->conexao->query($sql);

        if ($resultado->num_rows > 0) {
            echo "<h3>Listagem de Marcas</h3><div class='cards-container'>";
        
            foreach ($resultado as $row) {
                $id = $row['marca_codigo'];
                $desc = $row['marca_descricao'] ?? 'Não informada';
            
                echo"<div class='card'>
                        <h3>$desc</h3>
                        <p><strong>Código:</strong> $id</p>
                        <form method='post' action='../routes/editar.php'>
                            <input type='hidden' name='entidade' value='marca'>
                            <input type='hidden' name='descricao_marca' value='$desc'>
                            <input type='hidden' name='codigo_marca' value='$id'>
                            <input type='submit' name='editar_marca' value='Editar'>
                        </form>
                        <form method='post' action='../global.php'>
                            <input type='hidden' name='codigo_marca' value='$id'>
                            <input type='submit' name='deletar_marca' value='Deletar'>
                        </form></div>";
            }
            echo "</div>";
        } else {
            echo "Nenhuma marca encontrada.";
        }
    }
    public function editarMarca($marca_codigo) {
        $sql = "UPDATE tbmarca SET marca_descricao = ? WHERE marca_codigo = ?";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('si', $this->marca_nome, $marca_codigo);
        if ($stmt->execute()) {
            echo "Marca editada com sucesso!";
        } else {
            echo "Erro ao editar marca: " . $stmt->error;
        }

        $stmt->close();
    }
    public function deletarMarca($id) {
        $sql = "DELETE FROM tbmarca WHERE marca_codigo = ?";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('i', $id);
        if ($stmt->execute()) {
            echo "Marca deletada com sucesso.";
        } else {
            echo "Erro ao deletar marca: " . $stmt->error;
        }

        $stmt->close();
    }
}
?>