<?php
class Locacao
{
    private $veiculo_placa;
    private $cliente_cpf;
    private $data_locacao;
    private $data_devolucao;
    private $conexao;
    private $loc_codigo;

    public function __construct($veiculo_placa, $cliente_cpf, $data_locacao, $data_devolucao, $conexao, $loc_codigo = null)
    {
        $this->veiculo_placa = $veiculo_placa;
        $this->cliente_cpf = $cliente_cpf;
        $this->data_locacao = $data_locacao;
        $this->data_devolucao = $data_devolucao;
        $this->conexao = $conexao;
        $this->loc_codigo = $loc_codigo;
    }

    public function inserirLocacao(){
        $sql = "INSERT INTO tblocacao (locacao_veiculo, locacao_cliente, locacao_data_inicio, locacao_data_fim) VALUES (?, ?, ?, ?)";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('ssss', $this->veiculo_placa, $this->cliente_cpf, $this->data_locacao, $this->data_devolucao);

        if ($stmt->execute()) {
            echo "Locação Registrada e Inserida com Sucesso.";
        } else {
            echo "Erro ao Inserir sua Locação: " . $stmt->error;
        }
    }

    public function listarLocacao() {
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
                INNER JOIN tbveiculo ON tblocacao.locacao_veiculo = tbveiculo.veiculo_placa
                INNER JOIN tbcliente ON tblocacao.locacao_cliente = tbcliente.cliente_cpf
                INNER JOIN tbmarca ON tbveiculo.veiculo_marca = tbmarca.marca_codigo";

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
                        <th>Ações</th>
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
                    <td class='acoes'>
                        <div class='form-buttons'>
                            <form method='post' action='../routes/editar.php'>
                                <input type='hidden' name='entidade' value='locacao'>
                                <input type='hidden' name='loc_codigo' value='$loc_codigo'>
                                <input type='hidden' name='loc_dt-inicio' value='$loc_dt_inicio'>
                                <input type='hidden' name='loc_dt-fim' value='$loc_dt_fim'>
                                <input type='submit' name='editar_locacao' value='Editar'>
                            </form>
                            <form method='post' action='../global.php'>
                                <input type='hidden' name='loc_codigo' value='$loc_codigo'>
                                <input type='submit' name='deletar_locacao' value='Deletar'>
                            </form>
                        </div>
                    </td>
                </tr>";
            }
            echo "</table>";
        } else {
            echo "Nenhuma locação encontrada.";
        }
    }

    public function editarLocacao(){
        $sql = "UPDATE tblocacao SET locacao_data_inicio = ?, locacao_data_fim = ? WHERE locacao_codigo = ?";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('ssi', $this->data_locacao, $this->data_devolucao, $this->loc_codigo);

        if ($stmt->execute()) {
            echo "Locação editada com sucesso!";
        } else {
            echo "Erro ao editar locação: " . $stmt->error;
        }
    }

    public function deletarLocacao($loc_codigo){
        $sql = "DELETE FROM tblocacao WHERE locacao_codigo = ?";
        $stmt = $this->conexao->prepare($sql);
        $stmt->bind_param('i', $loc_codigo);

        if ($stmt->execute()) {
            echo "A Locação foi Deletada.";
        } else {
            echo "Não foi possível deletar: " . $stmt->error;
        }
    }
}
?>
