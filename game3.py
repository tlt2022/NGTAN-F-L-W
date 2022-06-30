
from random import randint
import colorama

# colorama = one of the built-in Python modules to display the text in different colors
#The Colorama module offers three main formatting options: Fore, Back, and Style. These allow us to change the foreground or background text color and style. The colors available for the foreground and
#background are black, red, green, yellow, blue, magenta, cyan, and white."""
# fire burns logs
# logs make a bridge over water
# water puts out fire
# fire -> _M_
# logs -> @@@
# water -> ~~~

def main():
    
    from colorama import Fore,Back,Style
    colorama.init(autoreset=True) # auto resets your settings after every output
    print(Fore.WHITE+Back.BLACK+'***********Welcome to Fire,Logs, Water Game**********')
    
    chosen = randint(1,3)
    player=True
    ans=None
    while player == True:
        
        
        player = input('fire (f), logs (l) or water (w)?')

        if player == 'f':
          print('_M_', end=' ')
  
        elif player == 'l':
          print('@@@', end=' ')
  
        elif player == 'w':
          print('~~~', end=' ')
  
        else:
          print('??')
  
        print('vs', end=' ')
        
        if chosen == 1 :
            computer = 'f'
            print('_M_')
  
        elif chosen == 2 :
            computer = 'l'
            print('@@@')
  
        else:
            computer = 'w'
            print('~~~')

        
        

        if player == computer:
            print('DRAW!')
  
        elif player == 'f' and computer == 'l':
           print('Player wins!')
  
        elif player == 'f' and computer == 'w':
           print('Computer wins!')
  
        elif player == 'l' and computer == 'f':
           print('Computer wins!')
  
        elif player == 'l' and computer == 'w':
           print('Player wins!')

        elif player == 'w' and computer == 'f':
           print('Player wins!')
  
        elif player == "w" and computer == 'l':
           print('Computer wins!')

        else:
           print('Huh?')
           
      
        ans=input("Do you want to play again? yes (y)")
        if ans=="y":
           player = True
        else:
           print("Thanks for playing 😃, have a nice day! 😎")
           break
        
  
main()
