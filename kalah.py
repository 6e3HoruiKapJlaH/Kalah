import sys
import random  
class Kalah():
    def __init__(self, player_kalah = 0, player_board = [3]*6,ai_kalah=0,  ai_board =[3]*6, player_turn= True):
        self.player_kalah = player_kalah
        self.player_board = player_board
        
        self.ai_kalah = ai_kalah
        self.ai_board = ai_board

        self.__temp = []

        self.player_turn = player_turn

    
    def minimax(self, depth, alpha, beta, minimizing_ai, min_turn = 0, max_turn = 0):
        if (depth==0) or (self.check_is_end_game()):
            print(self.check_is_end_game())
            return (self.ai_kalah-self.player_kalah), max_turn

        if not minimizing_ai:
            max_evaluation = -37
            max_turn = -1

            pos=[]
            for i in range(len(self.ai_board)):
                if self.ai_board[i]:
                    pos.append(i)

            
            for child in pos:

                temp_class = Kalah(self.player_kalah, self.player_board, self.ai_kalah, self.ai_board, False)
                temp_class.make_turn(child)
                if temp_class.player_turn == minimizing_ai:
                    eval = temp_class.minimax(depth-1, alpha, beta, False)
                else:
                    eval = temp_class.minimax(depth, alpha, beta, True)
                if max_evaluation < eval[0]:
                    max_evaluation = eval[0]
                    max_turn = child

                alpha = max(alpha, eval[0])
                if beta <= alpha:
                    break
            return max_evaluation, min_turn, max_turn
        
        else:
            min_evaluation = 37
            min_turn = -1

            pos=[]
            for i in range(len(self.player_board)):
                if self.player_board[i]:
                    pos.append(i)


            for child in pos:

                temp_class = Kalah(self.player_kalah, self. player_board, self.ai_kalah, self.ai_board, True)
                temp_class.make_turn(child)
                if temp_class.player_turn == minimizing_ai:
                    eval = temp_class.minimax(depth, alpha, beta, True)
                else:
                    eval = temp_class.minimax(depth-1, alpha, beta, False)

                if min_evaluation > eval[0]:
                    min_evaluation = eval[0]
                    min_turn = child
                beta = min(beta, eval[0])
                if beta <= alpha:
                    break
            return min_evaluation, min_turn, max_turn



    def check_is_end_game(self):
        if sum(self.player_board) == 0:
            self.ai_kalah+=sum(self.ai_board)
            self.ai_board = [0]*6
            return True
        elif sum(self.ai_board) == 0:
            self.player_kalah+=sum(self.player_board)
            self.player_board = [0]*6
            return True
        else:
            return False


    def check_is_end_player(self, kalah_new, first_pos):
        if self.player_kalah != kalah_new and self.ai_board[0] == first_pos:
            self.player_turn = True

        else:
            self.player_turn =  False

    def check_is_end_ai(self, kalah_new, first_pos):
        if self.ai_kalah != kalah_new and self.player_board[0] == first_pos:
            self.player_turn = False
        else:
            self.player_turn = True


    def make_turn(self, position):
        if self.player_turn== True:
            

            n = self.player_board[position]
            self.player_board[position]=0
            board = self.player_board[position+1:len(self.player_board)]+[self.player_kalah]+self.ai_board+self.player_board[0:position+1]
            for i in range(n):
                board[i] += 1

            player_board = board[-(position+1):]+board[:len(self.player_board)-(position+1)]
            player_kalah = board[len(self.player_board)-(position+1)]
            
            ai_board=board[len(self.player_board)-(position):len(self.player_board)-(position+7)]
            
            self.check_is_end_player(player_kalah, ai_board[0])
            print(self.player_turn)
            
            self.player_board = player_board
            self.player_kalah = player_kalah

            self.ai_board = ai_board
            self.check_is_end_game()
            print(self.ai_board," checked")
        else:
            n = self.ai_board[position]
            self.ai_board[position]=0
            board = self.ai_board[position+1:len(self.ai_board)]+[self.ai_kalah]+self.player_board+self.ai_board[0:position+1]
            for i in range(n):
                board[i] += 1

            ai_board = board[-(position+1):]+board[:len(self.ai_board)-(position+1)]
            ai_kalah = board[len(self.ai_board)-(position+1)]
            
            player_board=board[len(self.ai_board)-(position):len(self.ai_board)-(position+7)]
            
            self.check_is_end_ai(ai_kalah, player_board[0])

            self.ai_board = ai_board
            self.ai_kalah = ai_kalah

            self.player_board = player_board
            self.check_is_end_game()



""" k = Kalah()
k.player_turn = False
k.make_turn(4)
print(k.ai_board, k.player_board) """
# initializing the constructor 
""" pygame.init() 
  
# screen resolution 
res = (720,720) 
  
# opens up a window 
screen = pygame.display.set_mode(res) 
  
# white color 
color = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170) 
  
# dark shade of the button 
color_dark = (100,100,100) 
  
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Corbel',35) 
  
# rendering a text written in 
# this font 
text = smallfont.render('quit' , True , color) 
  
while True: 
      
    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            #if the mouse is clicked on the 
            # button the game is terminated 
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
                pygame.quit() 
                  
    # fills the screen with a color 
    screen.fill((60,25,60)) 
      
    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() 
      
    # if mouse is hovered on a button it 
    # changes to lighter shade 
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40: 
        pygame.draw.rect(screen,color_light,[width/2,height/2,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/2,height/2,140,40]) 
      
    # superimposing the text onto our button 
    screen.blit(text , (width/2+50,height/2)) 
      
    # updates the frames of the game 
    pygame.display.update()  """