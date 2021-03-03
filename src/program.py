# IMPORTANTE: Indique o seu número de estudante em string, na variável de módulo
# `number`
# TODO: Assume-se que a resolução é par/ímpar
import jogo_galo as jg
number = "INDICAR NÚMERO DE ESTUDANTE"


def main():
    jogo = {
        "jogadores": [],
        "tabuleiro": None,
        "em_curso": None
    }

    while True:
        line = input()
        if line == "":
            break

        commands = line.split(" ")
        if commands[0] == "RJ":  # RJ Alice Smith
            name = " ".join(commands[1:])
            if jg.existe_jogador(jogo, name):
                print("Ocorreu um erro.")
            else:
                jg.registar_jogador(jogo, name)
                print("Jogador registado.")
        elif commands[0] == "IJ":  # IJ Alice X Bob O
            first_name = commands[1]
            first_tag = commands[2]
            second_name = commands[3]
            second_tag = commands[4]
            if not jg.existe_jogador(jogo, first_name) or not jg.existe_jogador(jogo, second_name) or jg.existe_jogo_em_curso(jogo):
                print("Ocorreu um erro.")
            else:
                jg.iniciar_jogo(jogo, first_name, first_tag,
                                second_name, second_tag)
                print("Jogo iniciado.")
        elif commands[0] == "CP":
            name = commands[1]
            row = commands[2]
            column = commands[3]
            if not jg.existe_jogo_em_curso(jogo) or not jg.localizacao_valida(row, column):
                print("Ocorreu um erro.")
            else:
                jg.colocar_peca(jogo, name, row, column)
                if jg.verificar_vitoria(jogo):
                    print("Jogo terminado.")
                else:
                    print("Peça colocada com sucesso.")
        elif commands[0] == "LJ":
            for jogador in jg.jg.obter_jogadores(jogo):
                print(
                    f"{jogador['nome']} {jogador['jogos']} {jogador['vitorias']}")


if __name__ == "__main__":
    main()
