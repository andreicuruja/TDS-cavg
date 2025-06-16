<?php 

class Locacao {
    private $loc_codigo;
    private $veiculoPlaca;
    private $clienteCpf;
    private $dataLocacao;
    private $dataDevolucao;
    private $conexao;

    public function __construct($loc_codigo,$veiculoPlaca, $clienteCpf, $dataLocacao, $dataDevolucao, $conexao) {
        $this->loc_codigo = $loc_codigo;
        $this->veiculoPlaca = $veiculoPlaca;
        $this->clienteCpf = $clienteCpf;
        $this->dataLocacao = $dataLocacao;
        $this->dataDevolucao = $dataDevolucao;
        $this->conexao = $conexao;
    }

    public function inserirLocacao() {
        $sql = "INSERT INTO tblocacao (locacao_veiculo, locacao_cliente, locacao_data_inicio, locacao_data_fim) 
                VALUES (?, ?, ?, ?)";

        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('ssss', $this->veiculoPlaca, $this->clienteCpf, $this->dataLocacao, $this->dataDevolucao);

        if ($stmt->execute()) {
            echo "Locação inserida com sucesso!";
        } else {
            echo "Erro ao inserir locação: " . $stmt->error;
        }
    }


    

    public function listarLocacoes() {
        $sql = "SELECT 
                    tblocacao.locacao_codigo, 
                    tblocacao.locacao_veiculo, 
                    tblocacao.locacao_cliente, 
                    tblocacao.locacao_data_inicio, 
                    tblocacao.locacao_data_fim,
                    tbveiculo.veiculo_descricao, 
                    tbcliente.cliente_nome, 
                    tbmarca.marca_descricao
                FROM tblocacao
                INNER JOIN tbveiculo 
                    ON tblocacao.locacao_veiculo = tbveiculo.veiculo_placa
                INNER JOIN tbcliente 
                    ON tblocacao.locacao_cliente = tbcliente.cliente_cpf
                INNER JOIN tbmarca 
                    ON tbveiculo.veiculo_marca = tbmarca.marca_codigo";

        $resultado = $this->conexao->query($sql);

        if ($resultado->num_rows > 0) {
            echo "<h3>Listagem de Locações</h3>";
            echo "<table>
                    <tr>
                        <th>Código</th>
                        <th>Cliente (CPF)</th>
                        <th>Nome do Cliente</th>
                        <th>Data de Locação</th>
                        <th>Data de Devolução</th>
                        <th>Veículo</th>
                        <th>Placa</th>
                        <th>Marca</th>
                        <th>Editar</th>
                        <th>Excluir</th>

                    </tr>";

            foreach ($resultado as $row) {
                $loc_codigo = $row['locacao_codigo'];
                $loc_veiculo_placa = $row['locacao_veiculo'];
                $loc_cliente_cpf = $row['locacao_cliente'];
                $loc_dt_inicio = $row['locacao_data_inicio'];
                $loc_dt_fim = $row['locacao_data_fim'];
                $loc_carro_desc = $row['veiculo_descricao'];
                $loc_cliente_nome = $row['cliente_nome'];
                $loc_marca = $row['marca_descricao'];

                echo "<tr>
                        <td>$loc_codigo</td> 
                        <td>$loc_cliente_cpf</td>
                        <td>$loc_cliente_nome</td>
                        <td>$loc_dt_inicio</td>
                        <td>$loc_dt_fim</td>
                        <td>$loc_carro_desc</td>
                        <td>$loc_veiculo_placa</td>
                        <td>$loc_marca</td>

                         <td>                            
                            <form method='post' action='../routes/edits.php'>
                                <input type='hidden' name='entidade' value='locacao'>
                                <input type='hidden' name='loc_codigo' value='$loc_codigo'>
                                <input type='hidden' name='loc_dt-inicio' value='$loc_dt_inicio'>
                                <input type='hidden' name='loc_dt-fim' value='$loc_dt_fim'>
                                <input type='submit' name='editar_locacao' value='Editar'>
                            </form>
                        <td>
                            <form method='post' action='../global.php'>
                                <input type='hidden' name='loc_codigo' value='$loc_codigo'>
                                <input type='submit' name='deletar_locacao' value='Deletar'>
                            </form>
                        </td>
                      </tr>";
            }

            echo "</table>";
        } else {
            echo "Nenhuma locação encontrada.";
        }
    }
    public function deletarLocacao($loc_codigo){
        $sql = "DELETE FROM tblocacao WHERE locacao_codigo = ?";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('i', $loc_codigo);  
        if($stmt->execute()){

            echo "locação Deletada";


        }else{

            echo "Erro ao deletar". $stmt->error;

        }



    }
    public function editarLocacao(){
        $sql = "UPDATE tblocacao SET locacao_data_inicio = ?, locacao_data_fim = ? WHERE locacao_codigo = ?";
        $stmt = $this->conexao->prepare($sql);   
        $stmt->bind_param('ssi',$this->dataLocacao, $this->dataDevolucao, $this->loc_codigo);
        if($stmt->execute()){
            echo "Locação editada com sucesso!";
        }else{
            echo "Erro ao editar locação: " . $stmt->error;
        }


    }
}
?>
