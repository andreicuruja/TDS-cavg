<?php
class Cliente
{
    private $nome;
    private $cpf;
    private $endereco;
    private $conexao;

    public function __construct($nome, $cpf, $endereco, $conexao)
    {
        $this->nome = $nome;
        $this->cpf = $cpf;
        $this->endereco= $endereco;
        $this->conexao = $conexao;
    }
    public function inserirCliente(){
        $cpf = trim($this->cpf);
        $sql = "INSERT INTO tbcliente(cliente_nome, cliente_cpf, cliente_endereco) VALUES (?,?,?)";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('sss', $this->nome, $cpf, $this->endereco);
    
        if($stmt->execute()){
            $sql_test = "SELECT * FROM tbcliente WHERE cliente_cpf = ?";
            $stmt_test = $this->conexao->prepare($sql_test);
            $stmt_test->bind_param('s', $cpf);
            $stmt_test->execute();
            $resultado_test = $stmt_test->get_result();
            
            if ($resultado_test->num_rows > 0) {
                echo "Cliente encontrado no banco de dados!";
            } else {
                echo "Erro: Cliente não encontrado no banco de dados.";
            }
    
        } else {
            echo "Erro ao Inserir Cliente: " . $stmt->error;
        }
    
        $stmt->close();
    }
    public function listarCliente() {
        $sql = "SELECT cliente_nome, cliente_cpf, cliente_endereco FROM tbcliente";
        $resultado = $this->conexao->query($sql);
        
        if ($resultado->num_rows > 0) {
            echo "<h3>Listagem de Clientes</h3><div class='cards-container'>";
            foreach ($resultado as $row) {
                $nome = $row['cliente_nome'];
                $cpf = $row['cliente_cpf'];
                $ende = $row['cliente_endereco'];
                
                echo "<div class='card'>
                        <h3>$nome</h3>
                        <p><strong>CPF:</strong> $cpf</p>
                        <p><strong>Endereço:</strong> $ende</p>
                        <form method='post' action='../routes/editar.php'>
                            <input type='hidden' name='entidade' value='cliente'>
                            <input type='hidden' name='cpf' value='$cpf'>
                            <input type='submit' name='editar_cliente' value='Editar'>
                        </form>
                        <form method='post' action='../global.php'>
                            <input type='hidden' name='entidade' value='cliente'>
                            <input type='hidden' name='cpf' value='$cpf'>
                            <input type='submit' name='delete' value='Deletar'>
                        </form>  
                    </div>";
            }
            echo "</div>";
        } else {
            echo "Nenhum cliente encontrado.";
        }
    }
    public function editarCliente(){
        $sql = "UPDATE tbcliente SET cliente_nome = ?, cliente_endereco = ? WHERE cliente_cpf = ?";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('sss', $this->nome, $this->endereco, $this->cpf);
        if($stmt->execute()){
            echo "Cliente atualizado com sucesso.";
            echo "     CPF enviado: " . $this->cpf . "<br>";
        } else {
            echo "Erro ao atualizar cliente: " . $stmt->error;
        }
        $stmt->close();
    }
    public function deletarCliente($cpf){
        $sql = "DELETE FROM tbcliente WHERE cliente_cpf = ?";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('s',$cpf);
        if ($stmt->execute()) {
            echo "O Cliente foi Deletado.";
        } else {
            echo "Não foi Possível deletar: " . $stmt->error;
    }
    $stmt->close();
    }

}
?>