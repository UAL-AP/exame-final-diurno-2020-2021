# Regras
# 1. O número de estudante determina que funcionalidades deve implementar.
#    Verifique no comentário de cada método.
# 2. A variável jogo é um dicionário com a seguinte estrutura mínima:
#
#    jogo = {'jogadores': lista, 'tabuleiro': lista de listas}
#
# 3. Pode aumentar o dicionário jogo, desde que mantenha a estrutura mínima.
# 4. Não pode alterar a assinatura de qualquer método.
# 5. Não pode acrescentar métodos.
# 6. Não pode recorrer a bibliotecas externas à distribuição padrão Python 3.8.5


# IMPORTANTE: Indique o seu número de estudante em string, na variável de módulo
# `number`
number = "INDICAR NÚMERO DE ESTUDANTE"

# IMPORTANTE: A variável de módulo last_digit guarda o último dígito do número de aluno, e
# soma o valor 1. Vai ser utilizada para determinar que funcionalidades deve implementar.
last_digit = int(number[len(number)-1])+1


def registar_jogador(jogo, nome):
    # Um jogador é representado com um dicionário com a seguinte estrutura
    # mínima:
    #
    # jogador = {'nome': string, 'vitorias': int}
    #
    # Se last_digit par: o nome deve ser guardado em maiúsculas, com espaços em branco removidos.
    #
    # Se last_digit ímpar: o nome deve guardado com os espaços em branco
    # convertidos em underscore.
    pass


def existe_jogador(jogo, nome):
    # Retorna True se o jogador com o nome indicado estiver registado.
    pass


def obter_jogadores(jogo):
    # Retorna uma lista de dicionários com a informação dos jogadores.
    pass


def iniciar_jogo(jogo, nome_primeiro_jogador, marca_primeiro_jogador, nome_segundo_jogador, marca_segundo_jogador):
    # Deve criar o tabuleiro no dicionário jogo.
    pass


def existe_jogo_em_curso(jogo):
    # Retorna True se estiver um jogo em curso.
    pass


def localizacao_valida(linha, coluna):
    # Retorna True se as localização indicada for válida, i.e., dentro de uma
    # grelha de 3x3.
    pass


def colocar_peca(jogo, nome_jogador, linha, coluna):
    # Retorna True se o jogo terminou (com vitória ou empate) depois de colocar
    # a peça. Retorna False caso contrário.
    #
    # Não é necessário verificar se já existe alguma peça na localização
    # indicada.
    #
    # Depois de colocar a peça, utiliza a função verificar_vitoria para
    # determinar se algum jogador ganhou.
    #
    # Se todas as posições do tabuleiro estiverem ocupadas, e nenhum jogador
    # ganhou, o jogo termina num empate.
    #
    # Se last_digit par: o empate soma uma vitória a cada jogador.
    #
    # Se last_digit ímpar: o empate não altera o número de vitorias dos
    # jogadores.
    pass


def verificar_vitoria(jogo):
    # Retorna True se o jogo em curso terminou em vitória.
    #
    # Se last_digit par: vitória apenas diagonal
    #
    # Se last_digit ímpar: vitória apenas horizontal e vertical
    pass
