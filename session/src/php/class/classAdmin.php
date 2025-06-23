<?php
class adm{
    private $id;
    private $nome;
    private $senha;
    private $conexao;

    public function __construct($id, $nome, $senha, $conexao) {
        $this->id = $id;
        $this->nome = $nome;
        $this->senha = $senha;
        $this->conexao = $conexao;
    }
    public function insereAdm(){
        $sql = "INSERT INTO tbadm (nome, senha) VALUES (?,?)";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('ss',$this->nome, $this->senha);
          if ($stmt->execute()) {
            echo "Admin inserido com sucesso!";
        } else {
            echo "Erro ao inserir admin: " . $stmt->error;
        }
    }
    public function buscaAdm(){
        $sql = "SELECT nome FROM tbadm WHERE nome  = ? AND senha = ?";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('ss', $this->nome, $this->senha);
        $stmt->execute();
        $stmt->store_result();
        if($stmt->num_rows>0){
            $stmt->fetch();
            return true;
        }else{
            echo "Erro". $stmt->error;
        }
    }
}
?>