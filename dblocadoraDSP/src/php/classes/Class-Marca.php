<?php 
class Marca{
    private $marca_codigo;
    private $nome_marca;
    private $conexao;

    public function __construct($marca_codigo, $nome_marca, $conexao){
        $this->marca_codigo = $marca_codigo;
        $this->nome_marca = $nome_marca;
        $this->conexao = $conexao;
    }

    public function inserirMarca(){
        $sql = "INSERT INTO tbmarca(marca_descricao) VALUES (?)";
        
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('s', $this->nome_marca);
        if($stmt->execute()){

            echo "Marca Inserida";


        }else{

            echo "Erro ao Inserir". $stmt->error;

        }

    }

    public function listarMarca() {
        $sql = "SELECT marca_codigo, marca_descricao FROM tbmarca ORDER BY marca_codigo ASC";
        $resultado = $this->conexao->query($sql);
    
        if ($resultado->num_rows > 0) {
            echo "<h3>Listagem de Marcas</h3><table>";
            echo "<tr><th>Código</th>
            <th>Descrição</th>
            <th>Editar</th>
            <th>Excluir</th>";
    
            foreach ($resultado as $row) {
                $codigo = $row['marca_codigo'];
                $descricao = $row['marca_descricao'] ?? 'Não informado';
    
                echo "<tr>
                        <td>$codigo</td>
                        <td>$descricao</td>
                        <td>                            
                            <form method='post' action='../routes/edits.php'>
                                <input type='hidden' name='entidade' value='marca'>
                                <input type='hidden' name='descricao_marca' value='$descricao'>
                                <input type='hidden' name='codigo_marca' value='$codigo'>

                                <input type='submit' name='editar_marca' value='Editar'>
                            </form>

                        </td>
                        <td>
                            <form method='post' action='../global.php'>
                                <input type='hidden' name='codigo_marca' value='$codigo'>
                                <input type='submit' name='deletar_marca' value='Deletar'>
                            </form>
                            
                        </td>
                        

                      </tr>";
            }
    
            echo "</table>";
        } else {
            echo "<p>Nenhuma marca encontrada.</p>";
        }
    }
    public function deletarMarca($codigo){
        $sql = "DELETE FROM tbmarca WHERE marca_codigo = ?";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('i', $codigo);
        
        if($stmt->execute()){

            echo "Marca Deletada";


        }else{

            echo "Erro ao deletar". $stmt->error;

        }

    } public function editarMarca(){
        $sql = "UPDATE tbmarca SET marca_descricao = ? WHERE marca_codigo  = ?";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('si',$this->nome_marca, $this->marca_codigo);
        if ($stmt->execute()) {
            echo "marca editada com sucesso!";
        } else {
            echo "Erro ao deletar: " . $stmt->error;
        }
        



    }

}
?>