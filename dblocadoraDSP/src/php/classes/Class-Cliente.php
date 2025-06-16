<?php

class Cliente{
   
    private $nome;
    private $cpf;
    private $endereco;
    private $conexao;

    public function __construct($cpf, $nome, $endereco, $conexao){

        $this->nome = $nome;
        $this->cpf = $cpf;
        $this->endereco= $endereco;
        $this->conexao = $conexao;
    }
    
    public function insereCliente(){
        $sql = "INSERT INTO tbcliente(cliente_nome, cliente_cpf, cliente_endereco) VALUES (?,?,?)";
        
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('sss', $this->nome, $this->cpf, $this->endereco);
        if($stmt->execute()){

            echo "Cliente Inserido";


        }else{

            echo "Erro ao Inserir". $stmt->error;

        }

    $stmt->close();
    }
    public function listarCliente(){


        $sql = "SELECT cliente_nome, cliente_cpf, cliente_endereco FROM tbcliente";
        
        $resultado = $this->conexao->query($sql);
      
        if ($resultado->num_rows>0) {

            echo "<h3>Listagem de Clientes</h3><table>";
            echo "<th>Nome</th> <th>CPF</th> <th>Endereço</th><th>Editar</th><th>excluir</th>";

            foreach($resultado as $row){
                $nm = $row['cliente_nome'];
                $cpf = $row['cliente_cpf'];
                $end = $row['cliente_endereco'];
                echo "<tr>
                
                <td>$nm</td> 
                <td>$cpf</td>
                <td>$end</td>
                <td>
                    <form method='post' action='../routes/edits.php'>
                        <input type='hidden' name='entidade' value='cliente'>
                        
                        <input type='hidden' name='cpf' value='$cpf'>
                        <input type='submit' name='editar_cliente' value='Editar'>
                    </form>
                </td>
                <td>
                    <form method='post' action='../global.php'>
                        <input type='hidden' name='cpf' value='$cpf'>
                        <input type='submit' name='delete' value='Deletar'>
                    </form>
                </td>
                
                
                </tr>";
            }

            echo "</table>";
        }else{
            echo "<p>Nenhum cliente encontrado.</p>";
        }
       



        
    }   
    public function deletarCliente($cpf){

    $sql = "DELETE FROM tbcliente WHERE cliente_cpf = ?";
    $stmt = $this->conexao->prepare($sql);
    $stmt->bind_param('s',$cpf);
    if ($stmt->execute()) {
        echo "Cliente deletado com sucesso.";
    } else {
        echo "Erro ao deletar: " . $stmt->error;
    }

    $stmt->close();

    }
    public function editarCliente(){
        $sql = "UPDATE tbcliente SET cliente_nome = ?, cliente_endereco = ? WHERE cliente_cpf = ?";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('sss', $this->nome, $this->endereco, $this->cpf);
        if($stmt->execute()){
            echo "Cliente atualizado com sucesso.";
        }else{
            echo "Erro ao atualizar cliente: " . $stmt->error;
        }

    }
}





?>