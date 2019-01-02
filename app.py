import os
import sys
from random import randint

from utils.termdraw import getch, moldura

os.system('cls' if os.name == 'nt' else 'clear')
term_rows, term_columns = os.popen('stty size', 'r').read().split()

cenario = """                .                                            .                  
     *   .                  .              .        .   *          .           .
  .         .                     .       .           .      .        .         
        o                             .                   .                     
         .              .                  .           .                        
          0     .                  .                                        .   
                 .          .                 ,                ,    ,           
 .          \\          .                         .                              
      .      \\   ,                        .                      .              
   .          o     .                 .                   .            .        
     .         \\                 ,             .                .               
               #\\##\\#      .                              .        .        .   
             #  #O##\\###                .                        .              
   .        #*#  #\\##\\###                       .                     ,         
        .   ##*#  #\\##\\##               .                     .                 
      .      ##*#  #o##\\#         .                             ,       .       
          .     *#  #\\#     .                    .             .          ,     
                      \\          .                         .                    
____^/\\___^--____/\\____O______________/\\/\\---/\\___________---______________^--__
   /\\^   ^  ^    ^                  ^^ ^  '\\ ^          ^       ---             
         --           -            --  -      -         ---  __    ^     --  __ 
   --  __                      ___--  ^  ^                         --  __       """  # noqa: W291

modulo = "▟▙"
base = "▀▀"


def intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    moldura(6, 28, 17, 57, 'JustPyLander', shadow=True)
    sys.stdout.write(f"\033[9;37HInstruções")
    sys.stdout.write(f"\033[11;35H(a) - Esquerda")
    sys.stdout.write(f"\033[12;35H(d) - Direita")
    sys.stdout.write(f"\033[13;35H(s) - Baixo")
    sys.stdout.write(f"\033[14;35H(q) - Sair")
    sys.stdout.write(f"\033[16;30HTecle algo para continuar")
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()


def sair():
    moldura(9, 30, 14, 55, 'Abandonar a nave', shadow=True)
    sys.stdout.write(f"\033[12;36HDeseja sair?")
    sys.stdout.write(f"\033[13;40H(s/n)")
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    answer = getch()

    if answer not in ('s', 'n'):
        sys.stdout.write(f"\033[24;1HInvalid input.")
        sys.stdout.write("\033[?25l")
        sair()
    if answer == 's':
        sys.stdout.write(f"\033[24;1HGoodbye")
        sys.stdout.write("\033[?25h")
        exit()
    else:
        pass
        # main.coluna = randint(5, 75)
        # main.base_local = randint(5, 75)
        # main()


def jogar_novamente():
    sys.stdout.write(f"\033[12;34HJogar  novamente?")
    sys.stdout.write(f"\033[13;40H(s/n)")
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()

    answer = getch()

    if answer not in ('s', 'n'):
        sys.stdout.write(f"\033[24;1HInvalid input.")
        sys.stdout.write("\033[?25l")
        jogar_novamente()
    if answer == 's':
        main.coluna = randint(5, 75)
        main.base_local = randint(5, 75)
        main()
    else:
        sys.stdout.write(f"\033[24;1HGoodbye")
        sys.stdout.write("\033[?25h")


def main():
    coluna = randint(5, 75)
    base_local = randint(5, 75)
    sys.stdout.write(f"\033[1;1H{cenario}")
    sys.stdout.write(f"\033[;{base_local}H{base}")
    sys.stdout.write("\033[?25l")
    posicao_descida = -1
    for _ in range(24):
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.stdout.write(f"\033[1;1H{cenario}")
        sys.stdout.write(f"\033[{_};{coluna}H{modulo}")
        sys.stdout.write(f"\033[24;{base_local}H{base}")
        posicao_descida += 1
        sys.stdout.flush()

        key = getch()
        if key == 'a':
            if coluna != 1:
                coluna -= 1
        elif key == 'd':
            if coluna != 79:
                coluna += 1
        elif key == 'q':
            sair()

    if posicao_descida == 23 and base_local == coluna:
        moldura(9, 30, 14, 55, 'bela aterrissagem', shadow=True)
        jogar_novamente()
    else:
        moldura(9, 30, 14, 55, 'você explodiu', shadow=True)
        jogar_novamente()

    sys.stdout.flush()


if __name__ == "__main__":
    intro()
    getch()
    main()
