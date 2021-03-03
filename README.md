# Algoritmia e Programação 2020 2021 - Exame Final - Parte Prática

- [Algoritmia e Programação 2020 2021 - Exame Final - Parte Prática](#algoritmia-e-programação-2020-2021---exame-final---parte-prática)
  - [Jogo do Galo](#jogo-do-galo)
  - [Instruções](#instruções)
    - [**Registar jogador (RJ)**](#registar-jogador-rj)
    - [**Iniciar jogo (IJ)**](#iniciar-jogo-ij)
    - [**Colocar peça (CP)**](#colocar-peça-cp)
    - [**Listar jogadores (LJ)**](#listar-jogadores-lj)
  - [Tarefas](#tarefas)
  - [Regras](#regras)
    - [Comunicação enviada](#comunicação-enviada)
  - [<span style="color: green;">Entrega<span>](#span-stylecolor-greenentregaspan)

## Jogo do Galo

O jogo do galo envolve dois jogadores um joga com `X` e outro com `O`.

O tabuleiro tem 3 linhas e 3 colunas (i.e., 3x3).

Ganha o jogador que primeiro conseguir alinhar três símbolos. O alinhamento dos símbolos pode ser na vertical, horizontal ou diagonal, e vai depender das regras de implementação descritas neste enunciado. Se a grelha ficar completamente preenchida, e nenhum jogador conseguir alinhar 3 símbolos, o jogo termina com um empate.

Pretende-se o jogo do galo com as instruções que se seguem.

## Instruções

<span style="color: red;">**IMPORTANTE:**</span> Na instrução `RJ`, o nome do jogador pode conter espaços. No entanto, estes espaços serão convertidos de acordo com a regra de implementação indicada no comentário do método `registar_jogador`, do módulo `jogo_galo`.

Nas restantes instruções, o nome indicado será relativo ao nome com os espaços convertidos.

### **Registar jogador (RJ)**

Regista um novo jogador. Cada jogador tem um nome único. Não existe limite para o número de jogadores registados.

Entrada:

`RJ Nome`

Saída com com sucesso:

`Jogador registado.`

Saída com insucesso:

- No caso de já existir um jogador com o mesmo nome:

    `Ocorreu um erro.`

### **Iniciar jogo (IJ)**

É necessário indicar os nomes dos participantes do jogo e as marcas que vão utilizar (`X` ou `O`). Os jogadores têm que estar previamente registados.

Entrada:

`IJ Nome1 Marca1 Nome2 Marca2`

Saída com sucesso:

`Jogo iniciado.`

Saída com insucesso:

- No caso de algum jogador não existir, ou se já existir um jogo em curso:

    `Ocorreu um erro.`

### **Colocar peça (CP)**

O jogador deve indicar o número da coluna onde deseja colocar a peça. Cada jogador só pode colocar a peça se for a sua vez e se existir jogo em curso. Se nenhum jogador tiver colocado peças no jogo em curso, qualquer um pode ser o primeiro.

Em caso de vitória deve ser indicado o nome do vencedor, bem como a localização (linha e coluna) de todas as peças que colocou no tabuleiro. Só devem ser consideradas vitórias na horizontal ou vertical.

Entrada:

`CP Nome Linha Coluna`

Saída com sucesso (apenas uma deve surgir):

- Quando o jogo não terminou:

    `Peça colocada com sucesso.`

- Quando o jogo terminou com vitória ou empate:

    `Jogo terminado.`

Saída com insucesso:

- No caso de não existir um jogo em curso, ou a localização indicada por fora de grelha:

    `Ocorreu um erro.`

### **Listar jogadores (LJ)**

Deve ser possível listar os jogadores registados, indicando o seu nome, número de jogos jogados, e número de vitórias.

Entrada:

`LJ`

Saída com sucesso:

`Nome NumJogos NumVitórias`
`Nome NumJogos NumVitórias`
`Nome NumJogos NumVitórias`
`...`

Não são considerados cenários de insucesso.

## Tarefas

1. (**30%**) Implemente a lógica de interação no módulo `program`.
   - O ficheiro encontra-se vazio, e deve ser escrito na totalidade.
   - Deve apenas tratar da interação com o utilizador. A lógica do jogo está disponível no módulo `jogo_galo`. Não deve utilizar funções que não constem nesse módulo.
   - A implementação de lógica de jogo no módulo `program` não será considerada na avaliação.
   - Os métodos em `jogo_galo` têm regras de implementação condicionais ao número de estudante (ver comentários dos métodos). Devem ser utilizados de acordo com essas regras.
2. (**70%**) Implemente as regras do jogo no módulo `jogo_galo`.
   - O ficheiro encontra-se incompleto, sendo necessário implementar o código das funções descritas. Os nomes das funções não devem ser alterados.
   - As funções devem ser chamadas pelo módulo `program.py`, mesmo que não cheguem a ser implementadas.

   **IMPORTANTE:** A estratégia de implementação destas funções é condicional ao número de aluno (ver secção de [Regras](#regras)). Os detalhes condicionais estão descritos em comentários nas funções do módulo.


## Regras

O número de estudante determina a estratégia de implementação das funções pedidos em `jogo_galo.py`. A implementação deste módulo deve iniciar com a definição da variável de módulo `number`.

O ficheiro `jogo_galo.py` contém, na linha 16,

`number = "INDICAR NÚMERO DE ESTUDANTE"`

Assumindo que o número de estudante é `40004242`, a variável deve ser alterada para

`number = "40004242"`

<span style="color: red">**IMPORTANTE:**</span> A variável `number` é do tipo `string`. Não pode ser declarada com qualquer outro tipo.

O módulo vai capturar o último dígito do número de estudante (no exemplo, `2`), e vai somar `1` (no exemplo, resulta em `3`). O resultado desta operação ficará guardado na variável de módulo `last_digit`. Esta variável vai ser, necessariamente par ou ímpar. O objetivo das várias funções será condicional a esta caraterística.

Exemplos:

| Número   | number       | last_digit | Paridade |
|----------|--------------|------------|----------|
| 30002222 | `"30002222"` | `2+1 = 3`  | Ímpar    |
| 30001000 | `"30001000"` | `0+1 = 1`  | Ímpar    |
| 30001009 | `"30001009"` | `9+1 = 10` | Par      |

É também necessário indicar o número de estudante na variável de módulo `number` (também string) em `program.py`.

### Comunicação enviada

A parte prática do exame vai envolver a escrita de algumas funções. Para a realizar será necessário indicar o número de estudante numa variável, num módulo entregue durante a prova.

Vai ser definida outra variável com o último dígito do número de estudante, somado com 1. O valor resultante será par ou ímpar. Os requisitos de implementação das várias funções serão condicionais a esta caraterística.

Exemplos:

| Número de estudante &nbsp;&nbsp; | &nbsp;&nbsp;Último dígito + 1 | &nbsp;&nbsp;Paridade |
|----------------------------------|-------------------------------|----------------------|
| 30002222                         | &nbsp;&nbsp;`2+1 = 3`         | &nbsp;&nbsp;Ímpar    |
| 30001000                         | &nbsp;&nbsp;`0+1 = 1`         | &nbsp;&nbsp;Ímpar    |
| 30001009                         | &nbsp;&nbsp;`9+1 = 10`        | &nbsp;&nbsp;Par      |

**IMPORTANTE:** Recomenda-se que determine esta paridade antes de iniciar o exame.

---

## <span style="color: green;">Entrega<span>

Devem ser entregues os ficheiros `program.py` e `jogo_galo.py`, ambos com a variável de módulo `number` definida com o número de estudante.

Os ficheiros devem ser entregues individualmente, com a extensão `.py`, sem recorrer a qualquer tipo de compressão.

---
