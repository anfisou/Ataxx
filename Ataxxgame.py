from hashlib import new
from string import printable
from textwrap import fill
import pygame
import numpy as np
import sys
from pygame.locals import *
import random
import math

# define rgb codes of the used colors
white = (255,255,255)
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)
yellow = (255,255,0)
purple = (128,0,128)
lblue = (173,216,230)
orange = (255,165,0)


def select_mode(): #escolhe entre human vs human, human vs AI e AI vs AI com um clique nessa opção
    pygame.draw.rect(screen,lblue,(0,0,600,650))
    label= myfont.render("Choose game mode",1,purple)
    screen.blit(label,(150,10))
    pygame.draw.rect(screen,yellow,(0,50,600,200))
    pygame.draw.rect(screen,green,(0,250,600,200))
    pygame.draw.rect(screen,orange,(0,450,600,200))
    label= myfont.render("Human vs Human",1,purple)
    screen.blit(label,(171,150))
    label= myfont.render("Human vs AI",1,purple)
    screen.blit(label,(195,350))
    label= myfont.render("AI vs AI",1,purple)
    screen.blit(label,(231,550))
    pygame.display.update()
    a = 1
    while a > 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] <50:
                    a = 1
                else:
                    posy = event.pos[1]
                    line = (posy-50)//200 
                    a = -1
                    mode = line +1 
                    pygame.draw.rect(screen,black,(0,0,600,650))
                    return mode



def difficulty(mode):     #dependendo do modo de jogo escolhido, escolhe a dificuldade dos AI envolvidos
    if mode == 1:
        return 0,0
    
    elif mode == 2:
        pygame.draw.rect(screen,black,(0,0,600,650))
        pygame.draw.rect(screen,lblue,(0,0,600,650))
        label= myfont.render("Choose difficulty",1,purple)
        screen.blit(label,(150,10))
        pygame.draw.rect(screen,green,(0,50,600,200))
        pygame.draw.rect(screen,yellow,(0,250,600,200))
        pygame.draw.rect(screen,red,(0,450,600,200))
        label= myfont.render("Easy",1,black)
        screen.blit(label,(265,150))
        label= myfont.render("Medium",1,black)
        screen.blit(label,(242,350))
        label= myfont.render("Hard",1,black)
        screen.blit(label,(265,550))
        pygame.display.update()
        a = 1
        while a > 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[1] <50:
                        a = 1
                    else:
                        posy = event.pos[1]
                        line = (posy-50)//200 
                        a = -1
                        difficulty = line +1 
                        pygame.draw.rect(screen,black,(0,0,600,650))
                        return difficulty,0
    elif mode == 3:
        pygame.draw.rect(screen,black,(0,0,600,650))
        pygame.draw.rect(screen,blue,(0,0,600,650))
        label= myfont.render("Choose skill player 1",1,white)
        screen.blit(label,(110,10))
        pygame.draw.rect(screen,green,(0,50,600,200))
        pygame.draw.rect(screen,yellow,(0,250,600,200))
        pygame.draw.rect(screen,red,(0,450,600,200))
        label= myfont.render("Easy",1,black)
        screen.blit(label,(265,150))
        label= myfont.render("Medium",1,black)
        screen.blit(label,(242,350))
        label= myfont.render("Hard",1,black)
        screen.blit(label,(265,550))
        pygame.display.update()
        a = 1
        while a > 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[1] <50:
                        a = 1
                    else:
                        posy = event.pos[1]
                        line = (posy-50)//200 
                        a = -1
                        difficulty1 = line +1 
                        pygame.draw.rect(screen,black,(0,0,600,650))
                pygame.draw.rect(screen,black,(0,0,600,650))
        pygame.draw.rect(screen,red,(0,0,600,650))
        label= myfont.render("Choose skill player 2",1,white)
        screen.blit(label,(110,10))
        pygame.draw.rect(screen,green,(0,50,600,200))
        pygame.draw.rect(screen,yellow,(0,250,600,200))
        pygame.draw.rect(screen,red,(0,450,600,200))
        label= myfont.render("Easy",1,black)
        screen.blit(label,(265,150))
        label= myfont.render("Medium",1,black)
        screen.blit(label,(242,350))
        label= myfont.render("Hard",1,black)
        screen.blit(label,(265,550))
        pygame.display.update()
        a = 1
        while a > 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[1] <50:
                        a = 1
                    else:
                        posy = event.pos[1]
                        line = (posy-50)//200 
                        a = -1
                        difficulty2 = line +1 
                        pygame.draw.rect(screen,black,(0,0,600,650))
        return difficulty1,difficulty2

def escolhe_board():            #escolhe um dos boards do ecrã com um clique
    pygame.draw.rect(screen,lblue,(0,0,600,50))
    label= myfont.render("Choose your board",1,purple)
    screen.blit(label,(150,10))
    b1 = pygame.image.load('b1.png')
    b1 = pygame.transform.scale(b1,(197,197))
    b2 = pygame.image.load('b2.png')
    b2 = pygame.transform.scale(b2,(197,197))
    b3 = pygame.image.load('b3.png')
    b3 = pygame.transform.scale(b3,(197,197))
    b4 = pygame.image.load('b4.png')
    b4 = pygame.transform.scale(b4,(197,197))
    b5 = pygame.image.load('b5.png')
    b5 = pygame.transform.scale(b5,(197,197))
    b6 = pygame.image.load('b6.png')
    b6 = pygame.transform.scale(b6,(197,197))
    b7 = pygame.image.load('b7.png')
    b7 = pygame.transform.scale(b7,(197,197))
    b8 = pygame.image.load('b8.png')
    b8 = pygame.transform.scale(b8,(197,197))
    b9 = pygame.image.load('b9.png')
    b9 = pygame.transform.scale(b9,(197,197))
    screen.blit(b1,(0,50))
    screen.blit(b2,(200,50))
    screen.blit(b3,(400,50))
    screen.blit(b4,(0,250))
    screen.blit(b5,(200,250))
    screen.blit(b6,(400,250))
    screen.blit(b7,(0,450))
    screen.blit(b8,(200,450))
    screen.blit(b9,(400,450))
    pygame.draw.rect(screen,green,(197,50,3,600))
    pygame.draw.rect(screen,green,(397,50,3,600))
    pygame.draw.rect(screen,green,(0,247,600,3))
    pygame.draw.rect(screen,green,(0,447,600,3))
    pygame.display.update()
    a = 1
    while a > 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[1] <50:
                    a = 1
                else:
                    posx = event.pos[0]
                    posy = event.pos[1]
                    col = posx//200
                    lin = (posy-50)//200
                    a = -1
                    r = 3*lin + col +1
                    return r



def carateristicas(nboard):     #para cada um dos boards predefinidos, retorna as caraterísticas associadas ao mesmo
    if nboard==1:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[1,0,0,0,0,0,2],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[2,0,0,0,0,0,1]])
    elif nboard==2:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[3,1,0,0,0,0,3],[0,3,0,0,0,3,2],[0,0,3,0,3,0,0],[0,0,0,3,0,0,0],[0,0,3,0,3,0,0],[2,3,0,0,0,3,0],[3,0,0,0,0,1,3]])
    elif nboard ==3:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[3,1,0,0,0,0,3],[0,0,0,0,3,0,2],[0,3,3,0,3,0,0],[0,0,0,0,0,0,0],[0,0,3,0,3,3,0],[2,0,3,0,0,0,0],[3,0,0,0,0,1,3]])
    elif nboard == 4:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[1,0,0,0,0,0,2],[0,3,3,0,3,3,0],[0,3,0,0,0,3,0],[0,0,0,0,0,0,0],[0,3,0,0,0,3,0],[0,3,3,0,3,3,0],[2,0,0,0,0,0,1]])
    elif nboard ==5:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[1,3,0,0,0,3,2],[0,3,0,0,0,3,0],[0,0,0,0,0,0,0],[0,0,0,3,0,0,0],[0,0,0,0,0,0,0],[0,3,0,0,0,3,0],[2,3,0,0,0,3,1]])
    elif nboard ==6:
        line,col = 10,10
        squaresize = 600/10
        board = np.array([[1,0,3,0,2,1,0,3,0,2],[0,0,3,0,0,0,0,3,0,0],[0,0,3,3,3,3,3,3,0,0],[0,0,3,0,0,0,0,3,0,0],[2,0,3,0,1,2,0,3,0,1],[1,0,3,0,2,1,0,3,0,2],[0,0,3,0,0,0,0,3,0,0],[0,0,3,3,3,3,3,3,0,0],[0,0,3,0,0,0,0,3,0,0],[2,0,3,0,1,2,0,3,0,1]])
    elif nboard == 7:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[1,0,0,3,0,0,2],[0,0,3,0,3,0,0],[0,3,0,0,0,3,0],[0,0,3,0,3,0,0],[0,3,0,0,0,3,0],[0,0,3,0,3,0,0],[2,0,0,3,0,0,1]])
    elif nboard == 8:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[1,0,0,0,0,0,2],[0,0,0,0,0,0,0],[3,3,0,0,0,3,3],[0,0,0,0,0,0,0],[3,3,0,0,0,3,3],[0,0,0,0,0,0,0],[2,0,0,0,0,0,1]])
    elif nboard == 9:
        line,col = 7,7
        squaresize = 600//7
        board = np.array([[1,0,3,3,3,0,2],[0,0,0,0,0,0,0],[0,0,3,3,3,0,0],[0,0,0,0,0,0,0],[0,0,3,3,3,0,0],[0,0,0,0,0,0,0],[2,0,3,3,3,0,1]])
    return line,col,squaresize,board



def draw_board(board):         #recebe uma matriz representativa do board e tranforma-a numa imagem 
    a = 0
    v = 0
    for l in range(line):
        for c in range(col):
            if board[l,c] != 3:     #pinta o quadrado de branco, se o quadrado for jogável e dependendo do que lá tiver, pinta(ou não) um círculo dessa cor. 
                pygame.draw.rect(screen,white,(c * squaresize,(l) * squaresize+50,squaresize-1,squaresize-1))
                if board[l,c] == 1:
                    pygame.draw.circle(screen,blue,(int(c * squaresize + squaresize/2),int((l) * squaresize+ 50 + squaresize/2)),squaresize/2-10)
                    a += 1
                if board[l,c] == 2:
                    pygame.draw.circle(screen,red,(int(c * squaresize + squaresize/2),int((l) * squaresize +50 + squaresize/2)),squaresize/2-10)
                    v +=1
    a = str(a)
    v = str(v)
    # cria os contadores de peças
    pygame.draw.rect(screen,lblue,(0,0,130,50))
    pygame.draw.rect(screen,lblue,(500,0,100,50))
    label1 = myfont.render(a,1,blue)
    screen.blit(label1,(10,15))
    label2 = myfont.render(v,1,red)
    screen.blit(label2,(550,15))
    pygame.draw.circle(screen,blue,(60,30),12)
    pygame.draw.circle(screen,red,(530,30),12)
    pygame.display.update()


def jogada(board,player,line,col):          # recebe cliques até que estes formem uma jogada válida
    b = 1   
    while b > 0:  # recebe um par de cliques que definem uma jogada e aceita-a se for válida
        a = 1
        while a > 0:    # recebe o primeiro clique e aceita-o se for uma peça do player
            for l in range(line):
                for c in range(col):
                    if board[l,c] == 0:
                        pygame.draw.rect(screen,white,(c * squaresize,(l) * squaresize+50,squaresize-1,squaresize-1))
                        pygame.display.update()
            x1,y1 = seleciona_peca()
            if board[x1-1,y1-1] == player:
                a = -1
        c = 0
        for i in range(x1-2,x1+3):
            for k in range(y1-2,y1+3):
                if valid_move(board,x1,y1,i,k,line,col,player):
                    pygame.draw.rect(screen,green,((k-1) * squaresize + squaresize/5,(i-1) * squaresize + squaresize/5+50 ,3*squaresize/5,3*squaresize/5))
                    pygame.draw.rect(screen,white,((k-1) * squaresize + squaresize/4,(i-1) * squaresize + squaresize/4 +50 ,squaresize/2,squaresize/2))
                    pygame.draw.rect(screen,white,((k-1) * squaresize + 4*squaresize/10,(i-1) * squaresize+50,squaresize/5,squaresize-1))
                    pygame.draw.rect(screen,white,((k-1) * squaresize,(i-1) * squaresize+ 4*squaresize/10 +50,squaresize-1,squaresize/5))
                    pygame.display.update()               
                    c = 1
        if c == 1:      # se a peça selecionada pode ser movida
            x2,y2 = seleciona_peca()
            if valid_move(board,x1,y1,x2,y2,line,col,player):
                b = -1
    return x1,y1,x2,y2


def seleciona_peca():       #tranforma um clique na sua posição respetiva no board
    a = 1
    while a > 0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                x1 = int((posy-50)//squaresize +1)
                y1 = int(posx//squaresize + 1)
                a = -1
    return(x1,y1)


def valid_move(board,x1,y1,x2,y2,line,col,player):              #verifica se a jogada é válida
    if x1<1 or x1>line or y1<1 or y1>col or x2<1 or x2>line or y2<1 or y2>col:   # se a posição pertence ao board
        return False
    if board[x1-1,y1-1] != player:   # se a peça é do player
        return False
    if board[x2-1,y2-1] != 0:   # se o quadrado para onde vamos mover a peça está livre
        return False
    if x2==x1 and y2==y1:    # se a jogada não mexe a peça
        return False
    if abs(x2-x1)>2 or abs(y2-y1)>2:   # se a jogada mexe a peça mais do que aquilo que pode
        return False
    if abs(x2-x1) + abs(y2-y1) == 3:
        return False
    return True


def move(board,x1,y1,x2,y2,line,col,player):            #executa a jogada desejada se for válida        
    if valid_move(board,x1,y1,x2,y2,line,col,player):                                 
        if abs(x2-x1)>1 or abs(y2-y1)>1:            # se a jogada for de expansão
            board[x1-1,y1-1] = 0
            board[x2-1,y2-1] = player
        else:                                       # se a jogada for de salto
            board[x2-1,y2-1] = player
    return board



def capture(board,x2,y2,line,col,player):             #depois de uma jogada, verifica se captura peças do adversário
    for k in range (x2-2,x2+1):
        if k >= 0 and k <= line-1:
            for l in range(y2-2,y2+1):
                if l >= 0 and l <= col-1:
                    if board[k,l] == 3-player:
                        board[k,l] = player
    return board

def available_moves(board,player,line,col):             #verifica se o jogador tem jogadas válidas
    for i in range(1,line+1):
        for j in range(1,col+1):
            if board[i-1,j-1]==int(player):
                for k in range(i-2,i+3):
                    for l in range(j-2,j+3):
                        if valid_move(board,i,j,k,l,line,col,player):
                            return True
    return False


    

def fill_board(board,line,col,player,actual_board):  # preenche os espaços livres com peças do player
    if actual_board:
        pygame.draw.rect(screen,lblue,(0,0,600,50))
        if player == 1:
            label1 = myfont.render("Player 2 has no valid moves",1,black)
            label = myfont.render("Player 1's turn",1,blue)
        else:
            label1 = myfont.render("Player 1 has no valid moves",1,black)
            label = myfont.render("Player 2's turn",1,red)
        screen.blit(label1,(65,10))
        pygame.display.update()
        pygame.time.wait(1500)
        pygame.draw.rect(screen,lblue,(0,0,600,50))
        screen.blit(label,(165,10))
        pygame.display.update()
    for l in range(line):
        for c in range(col):
            if board[l,c] == 0:
                board[l,c] = player
                if actual_board:
                    draw_board(board)
                    pygame.time.wait(250)
    return board

def count_pieces(board,line,col):  # conta o número de peças no tabuleiro
    contador = 0
    for l in range(line):
        for c in range(col):
            if board[l,c] == 1 or board[l,c] == 2:
                contador += 1
    return contador

def force_game_over(board,line,col):  #determina um vencedor mesmo que o estado não seja final, escolhendo o player com mais peças
    a = 0
    v = 0
    for l in range(line):
        for c in range(col):
            if board[l,c] == 1:
                a += 1
            if board[l,c] == 2:
                v += 1
    if a > v:
        return 1
    if a < v:
        return 2
    if a == v:
        return 0

def game_over(board,line,col,actual_board):              #verifica se o jogo terminou, e nesse caso retorna o vencedor
    winner = -1
    if not available_moves(board,1,line,col) and available_moves(board,2,line,col):#condição de vitória do player 1
        board = fill_board(board,line,col,2,actual_board)
        winner = force_game_over(board,line,col)
    elif not available_moves(board,2,line,col) and available_moves(board,1,line,col):#condição de vitória do player 2
        board = fill_board(board,line,col,1,actual_board)
        winner = force_game_over(board,line,col)
    elif not available_moves(board,1,line,col) and not available_moves(board,2,line,col):  # condição de empate
        c1 = 0
        c2 = 0
        for i in range(line):
            for j in range(col):
                if board[i,j] == 1:
                    c1 += 1
                elif board[i,j] == 2:
                    c2 += 1
        if c1 == c2:
            winner = 0
        elif c1 > c2:
            winner = 1
        else:
            winner = 2
    return winner


def heuristic(board,line,col,player):       # avalia o estado do jogo para o jogador
    otherplayer = 3 - player
    points = 0   # diferença entre o número de peças do player e do adversário
    if game_over(board,line,col,False) == player:         # se ganhou o jogo
        return 500
    elif game_over(board,line,col,False) == otherplayer:  # se perdeu o jogo
        return -500
    elif game_over(board,line,col,False) == 0:            # se empatou o jogo
        return 0
    for l in range(line):
        for c in range(col):
            if board[l,c] == player:
                points += 1
            elif board[l,c] == otherplayer:
                points -= 1
            
    return points


def every_move(board,line,col,player):   # retorna todos as jogadas disponiveis para o jogador
    moves = []
    for l in range(1,line+1):
            for c in range(1,col+1):
                if board[l-1,c-1] == player:
                    for i in range(l-2,l+3):
                        for k in range(c-2,c+3):                                
                            if valid_move(board,l,c,i,k,line,col,player):
                                moves.append([l,c,i,k])
    return moves

def random_move(board,line,col,player):     #retorna uma jogada random das jogadas disponíveis
    moves = every_move(board,line,col,player)
    r = random.randint(0,len(moves)-1)
    jogada = moves[r]
    return jogada

def best_move(board,line,col,player):   # implementação do algoritmo greedy, em que de todos as jogadas possíveis, retorna a que tem melhor avaliação após a sua execução
    
    moves = every_move(board,line,col,player)
    b_move = moves[random.randint(0,len(moves)-1)]  # para que o AI seja menos previsivel
    tempboard = board.copy()
    max_score = heuristic(move(tempboard,b_move[0],b_move[1],b_move[2],b_move[3],line,col,player),line,col,player) 
    for possivel_jogada in range(len(moves)):
        tempboard = board.copy()
        x1,y1,x2,y2 = moves[possivel_jogada][0],moves[possivel_jogada][1],moves[possivel_jogada][2],moves[possivel_jogada][3]
        tempboard = move(tempboard,x1,y1,x2,y2,line,col,player)
        tempboard = capture(tempboard,x2,y2,line,col,player)
        if heuristic(tempboard,line,col,player) > max_score:
            b_move = moves[possivel_jogada]
            max_score = heuristic(tempboard,line,col,player)
    return b_move


def minimax(board,depth,alpha,beta,maximizingplayer,player):  #implementação do algoritmo minimax com alpha-beta cuts, em que retorna a jogada que garante uma melhor posição num espaco de "depth" jogadas
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
        if event.type == pygame.QUIT:
            sys.exit()
    if (player == 2 and maximizingplayer) or (player == 1 and not maximizingplayer): # se é o player 2 a jogar
        valid_moves = every_move(board,line,col,2)
    else:                                                                            # se é o player 1 a jogar
        valid_moves = every_move(board,line,col,1)
    if depth == 0 or game_over(board,line,col,False) != -1:
        if game_over(board,line,col,False) != -1:
            if game_over(board,line,col,False) == player:         # se ganhamos o jogo
                return (None,10000000)
            elif game_over(board,line,col,False) == 3-player:     # se perdermos o jogo
                return (None,-10000000)
            else:                                           # se empatamos o jogo
                return (None,0)
        else:                                                # se atingimos a profundidade desejada
            return (None,heuristic(board,line,col,player))
    if maximizingplayer:      # se é o "max" a jogar
        value = -math.inf
        for jogada in valid_moves:
            board_copy = board.copy()
            x1,y1,x2,y2 = jogada[0],jogada[1],jogada[2],jogada[3]
            board_copy = move(board_copy,x1,y1,x2,y2,line,col,player)
            board_copy = capture(board_copy,jogada[2],jogada[3],line,col,player)
            new_value = minimax(board_copy,depth-1,alpha,beta,False,player)[1]      # até obtermos um estado final ou a depth desejada
            if new_value > value:               # se obtermos uma jogada "melhor"
                value = new_value
                mov = jogada
            if value >= beta:    # se for impossível obtermos uma jogada "melhor"
                break
            alpha = max(alpha,value)
        return mov,value
    else:                     # se é o "min" a jogar
        value = math.inf
        for jogada in valid_moves:
            board_copy = board.copy()
            x1,y1,x2,y2 = jogada[0],jogada[1],jogada[2],jogada[3]
            board_copy = move(board_copy,x1,y1,x2,y2,line,col,3-player)
            board_copy = capture(board_copy,jogada[2],jogada[3],line,col,3-player)
            new_value = minimax(board_copy,depth-1,alpha,beta,True,player)[1]   # até obtermos um estado final ou a depth desejada
            if new_value < value:   # se obtermos uma jogada "melhor"
                value = new_value
                mov = jogada
            if value <= alpha:      # se for impossível obtermos uma jogada "melhor"
                break
            beta = min(beta,value)
        return mov,value
    




def main_game(board,line,col,mode,difficulty1,difficulty2): #corre o jogo até terminar,baseado no modo de jogo, do board escolhido e (eventualmente) a dificuldade dos AI
    winner = game_over(board,line,col,True)
    player = int(random.randint(1,2))       # define o primeiro jogador aleatoriamente
    vezes = 0                               # numero de peças no tabuleiro atual
    lnpieces = 0                            # numero de peças no tabuleiro antes da última jogada
    if mode == 1:
        while winner == -1:   #loop do jogo
            pygame.draw.rect(screen,lblue,(0,0,600,50))
            if player == 1:
                label = myfont.render("Player 1's turn",1,blue)
            elif player == 2:
                label = myfont.render("Player 2's turn",1,red) 
            screen.blit(label,(165,10))
            draw_board(board)
            pygame.display.update()
            x1,y1,x2,y2 = jogada(board,player,line,col)                             
            board = move(board,x1,y1,x2,y2,line,col,player)
            board = capture(board,x2,y2,line,col,player)   
            draw_board(board)
            pygame.display.update()
            winner = game_over(board,line,col,True)            
            player = 3 - player 
            npieces = count_pieces(board,line,col)
            if npieces == lnpieces:
                vezes += 1
            else:
                vezes = 0
            lnpieces = npieces
            if vezes >= 30:        #prevenção de loops
                winner = force_game_over(board,line,col)
        pygame.draw.rect(screen,lblue,(0,0,600,50))
    elif mode == 2:
        while winner == -1:   #loop do jogo
            pygame.draw.rect(screen,lblue,(0,0,600,50))
            if player == 1:
                label = myfont.render("Player 1's turn",1,blue)
                screen.blit(label,(165,10))
                draw_board(board)       
                pygame.display.update()
                x1,y1,x2,y2 = jogada(board,player,line,col)                             
                board = move(board,x1,y1,x2,y2,line,col,player)
                board = capture(board,x2,y2,line,col,player)
                draw_board(board)
                pygame.display.update()
            elif player == 2:
                label = myfont.render("AI's turn",1,red)
                screen.blit(label,(250,10))
                draw_board(board)
                pygame.display.update()
                if difficulty1 == 1:
                        jogad= random_move(board,line,col,player) 
                        pygame.time.wait(500)
                elif difficulty1 == 2:
                        jogad= best_move(board,line,col,player) 
                        pygame.time.wait(500)
                elif difficulty1 == 3:
                    if nboard == 6:
                        jogad= minimax(board,2,-math.inf,math.inf,True,player)[0]
                    else:
                        jogad= minimax(board,3,-math.inf,math.inf,True,player)[0]
                # jogada definida dependendo da dificuldade do AI
                x1,y1,x2,y2 = jogad[0],jogad[1],jogad[2],jogad[3]
                board = move(board,x1,y1,x2,y2,line,col,player)
                board = capture(board,x2,y2,line,col,player)
                pygame.display.update()   
            npieces = count_pieces(board,line,col)
            if npieces == lnpieces:
                vezes += 1
            else:
                vezes = 0
            lnpieces = npieces 
            if vezes >= 30:   #prevenção de loops
                winner = force_game_over(board,line,col)           
            draw_board(board)
            pygame.display.update()
            winner = game_over(board,line,col,True)
            player = 3 - player 
        pygame.draw.rect(screen,lblue,(0,0,600,50))
    elif mode == 3:
        while winner == -1:
            pygame.draw.rect(screen,lblue,(0,0,600,50))
            if player == 1:
                label = myfont.render("Player 1's turn",1,blue)
                screen.blit(label,(165,10))
                draw_board(board)       
                pygame.display.update()
                if difficulty1 == 1:
                        jogad= random_move(board,line,col,player) 
                elif difficulty1 == 2:
                        jogad= best_move(board,line,col,player) 
                elif difficulty1 == 3:
                    if nboard == 6 or nboard == 1:
                        jogad= minimax(board,2,-math.inf,math.inf,True,player)[0]
                    else:
                        jogad= minimax(board,3,-math.inf,math.inf,True,player)[0] 
                x1,y1,x2,y2 = jogad[0],jogad[1],jogad[2],jogad[3]
                board = move(board,x1,y1,x2,y2,line,col,player)
                board = capture(board,x2,y2,line,col,player)
                pygame.display.update()
            elif player == 2:
                label = myfont.render("Player 2's turn",1,red)
                screen.blit(label,(165,10))
                draw_board(board)
                pygame.display.update()
                if difficulty2 == 1:
                        jogad= random_move(board,line,col,player) 
                elif difficulty2 == 2:
                        jogad= best_move(board,line,col,player) 
                elif difficulty2 == 3:
                    if nboard == 6 or nboard == 1:
                        jogad= minimax(board,2,-math.inf,math.inf,True,player)[0]
                    else:
                        jogad= minimax(board,3,-math.inf,math.inf,True,player)[0] 
                x1,y1,x2,y2 = jogad[0],jogad[1],jogad[2],jogad[3]
                board = move(board,x1,y1,x2,y2,line,col,player)
                board = capture(board,x2,y2,line,col,player)
                pygame.display.update()   
            draw_board(board)
            pygame.display.update()
            winner = game_over(board,line,col,True)
            player = 3 - player 
            pygame.time.wait(500)
            
            npieces = count_pieces(board,line,col)
            if npieces == lnpieces:
                vezes += 1
            else:
                vezes = 0
            lnpieces = npieces
            if vezes >= 30:
                winner = force_game_over(board,line,col)
        pygame.draw.rect(screen,lblue,(0,0,600,50))
    # depois de o jogo ter acabado, verifica quem ganhou
    if winner == 0:
        label = myfont.render("Draw",1,green)
        screen.blit(label,(260,10))
    elif winner == 1:
        label = myfont.render("Player 1 won!",1,blue)
        screen.blit(label,(165,10))
    elif winner == 2:
        label = myfont.render("Player 2 won!",1,red)
        screen.blit(label,(165,10))
    a = 0
    v = 0
    for l in range(line):
        for c in range(col):
            if board[l,c] == 1:
                a +=1
            elif board[l,c] == 2:
                v += 1
    a = str(a)
    v = str(v)
    label1 = myfont.render(a,1,blue)
    screen.blit(label1,(10,15))
    label2 = myfont.render(v,1,red)
    screen.blit(label2,(550,15))
    pygame.draw.circle(screen,blue,(60,30),12)
    pygame.draw.circle(screen,red,(530,30),12)
    pygame.display.update()
    pygame.time.wait(5000)


                  

pygame.init()
size = (600,650)
screen = pygame.display.set_mode(size)  # cria a janela do jogo
myfont = pygame.font.SysFont("monospace", 30)  # define o tipo de letra
mode = select_mode()  #escolhe o modo de jogo
difficulty1,difficulty2 = difficulty(mode)# escolhe a dificuldade
nboard = escolhe_board()  #escolhe o tabuleiro
line,col,squaresize,board = carateristicas(nboard)
pygame.draw.rect(screen,black,(0,0,600,700))
main_game(board,line,col,mode,difficulty1,difficulty2)  #corre o jogo