import sys
import time


def digitar(texto):
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(0.03)
    print()


def inicio():
    digitar("🏫 BEM-VINDO AO COLEGIAL HIGH TECH! 🏫")
    digitar("Você acabou de entrar na nova escola de tecnologia.")
    digitar("No primeiro dia de aula, você senta na última fileira.")
    digitar(
        "Uma pessoa super estilosa senta ao seu lado, olha o seu notebook e diz:"
    )
    digitar(
        "'Nossa, você programa em Python? Que cringe... ou talvez baseado?'"
    )

    print("\nO que você responde?")
    print("[1] 'Cringe é você não usar modo escuro.'")
    print("[2] 'Sim! Quer que eu te ensine a criar um bot?'")
    print("[3] (Ficar nervoso e derrubar o estojo no chão)")

    escolha = input("\nEscolha (1, 2 ou 3): ")

    if escolha == "1":
        fase_nerd_ironico()
    elif escolha == "2":
        fase_romantico()
    elif escolha == "3":
        fase_desastrado()
    else:
        digitar("\nVocê travou e o sinal da aula tocou. Tente novamente!")
        inicio()


def fase_nerd_ironico():
    digitar("\n😎 ROTA: O NERD IRÔNICO")
    digitar("A pessoa ri alto! O professor olha feio para vocês.")
    digitar("Ela te passa um bilhete: 'Me encontra no laboratório no intervalo.'")
    digitar("Chegando lá, ela te desafia a hackear o Wi-Fi da escola.")

    print("\nVocê aceita?")
    print("[1] 'Com certeza, vou mudar a senha para 12345.'")
    print("[2] 'Não valeu, prefiro não ser expulso no primeiro dia.'")

    escolha = input("\nEscolha (1 ou 2): ")

    if escolha == "1":
        digitar("\n🏆 FINAL DEUS DO HACK: Vocês conseguiram!")
        digitar("Agora vocês controlam a escola e viraram a dupla mais famosa.")
    else:
        digitar("\n😢 FINAL FLOPADO: Ela te achou careta.")
        digitar("Você passou o resto do ano almoçando sozinho.")


def fase_romantico():
    digitar("\n💖 ROTA: O ROMÂNTICO TECH")
    digitar("Os olhos dela brilham! 'Sério? Eu sempre quis criar um bot.'")
    digitar("Vocês passam a aula inteira conversando sobre códigos e memes.")
    digitar("No fim do dia, ela te pede o @ do Instagram.")

    print("\nComo você reage?")
    print("[1] Passa o @ na hora e já manda um Reels de gatinho.")
    print("[2] Diz que só usa Discord e manda o seu ID.")

    escolha = input("\nEscolha (1 ou 2): ")

    if escolha == "1":
        digitar("\n💘 FINAL CASAL DO ANO: O Reels rendeu assunto!")
        digitar("Vocês estão namorando e programando juntos.")
    else:
        digitar("\n👾 FINAL DISCORD MODERATOR: Comunicação muito nerd.")
        digitar("Vocês viraram melhores amigos de jogos, mas nada mais.")


def fase_desastrado():
    digitar("\n🤡 ROTA: O CLOWN")
    digitar("As canetas rolam por toda a sala. Todo mundo olha para você.")
    digitar("A pessoa te ajuda a juntar e diz: 'Calma, eu não mordo!'")
    digitar("Ela te oferece metade de um salgadinho para quebrar o gelo.")

    print("\nVocê aceita?")
    print("[1] 'Aceito, estava morrendo de fome.'")
    print("[2] 'Não mordo comida de estranhos.'")

    escolha = input("\nEscolha (1 ou 2): ")

    if escolha == "1":
        digitar("\n🍕 FINAL AMIZADE SINCERA: O salgadinho uniu vocês.")
        digitar("Você ganhou uma parceria para todos os trabalhos em dupla.")
    else:
        digitar("\n🥶 FINAL CLIMA FRIO: Ficou um silêncio constrangedor.")
        digitar("Ela mudou de lugar na aula seguinte.")


# Inicia o jogo
inicio()