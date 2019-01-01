import os
import sys
import time
from random import randint
from tests import go_last_row, getch


os.system('cls' if os.name == 'nt' else 'clear')
term_rows, term_columns = os.popen('stty size', 'r').read().split()

cenario = """                .                                            .             
     *   .                  .              .        .   *          .       
  .         .                     .       .           .      .        .    
        o                             .                   .                
         .              .                  .           .                   
          0     .                  .                                       
                 .          .                 ,                ,    ,      
 .          \          .                         .                         
      .      \   ,                        .                      .         
   .          o     .                 .                   .            .   
     .         \                 ,             .                .          
               #\##\#      .                              .        .       
             #  #O##\###                .                        .         
   .        #*#  #\##\###                       .                     ,    
        .   ##*#  #\##\##               .                     .            
      .      ##*#  #o##\#         .                             ,       .  
          .     *#  #\#     .                    .             .          ,
                      \          .                         .               
____^/\___^--____/\____O______________/\/\---/\___________---______________
   /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---        
         --           -            --  -      -         ---  __       ^    
   --  __                      ___--  ^  ^                         --  __  """

modulo = "▟▙"
base = "▀▀"
base_local = randint(5, 70)
largura_canario = 75
coluna = randint(5, 70)


if __name__ == "__main__":
    sys.stdout.write(f"\033[1;1H{cenario}")
    sys.stdout.write(f"\033[;{base_local}H{base}")
    sys.stdout.write("\033[?25l")
    posicao_descida = -1
    for _ in range(int(term_rows) - 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.stdout.write(f"\033[1;1H{cenario}")
        sys.stdout.write(f"\033[23;{base_local}H{base}")
        sys.stdout.write(f"\033[{_};{coluna}H{modulo}")
        posicao_descida += 1
        sys.stdout.flush()

        key = getch()
        if key == 'a':
            if coluna != 1:
                coluna -= 1
        elif key == 'd':
            if coluna != 75:
                coluna += 1



    # sys.stdout.write(f"\033[1;1H{cenario}")
    # sys.stdout.write(f"\033[{_};{coluna}H{modulo}")
    # sys.stdout.write("\033[?25h")
    # go_last_row()