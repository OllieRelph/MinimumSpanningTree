#New program
import pygame
import sys
import math
import numpy

window_height = 1000
window_width = 1000
colour_black = (0,0,0)
colour_white = (255,255,255)
colour_red = (255,0,0)
colour_green = (0,255,0)
colour_teal = (0,255,255)
colour_purple = (255,0,255)
block_size = 25
clicked_pos = []
quit_clicked = False
go_clicked = False
pos_array  = []
paths_calculated = False
coord1 = ()
coord2 = ()



'''
start_pos = (1,1)
end_pos = ((int(window_height/block_size)-2) , (int((window_height/block_size)*0.8)))
'''

def main():
    global go_clicked
    path_list = []
    pygame.init()
    window = pygame.display.set_mode((window_height,window_width))
    window.fill(colour_white)
    pygame.display.set_caption('Minimum Spanning Tree')
    font = pygame.font.Font('freesansbold.ttf',75)
    
    #Creeate text  for go button
    text_go = font.render('GO', True, colour_black)
    textRect_go = text_go.get_rect()
    textRect_go.center = ((window_width*0.25), (window_height*0.95))

    #Create text   for exit bubtton
    text_quit = font.render('QUIT', True, colour_black)
    textRect_quit = text_quit.get_rect()
    textRect_quit.center = ((window_width*0.75), (window_height*0.95))

    while True:
        draw(window,path_list)
        pygame.display.flip
        window.blit(text_go,textRect_go)
        window.blit(text_quit,textRect_quit)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN :
                
                pos = pygame.mouse.get_pos()
                if (pos[1] > window_height * 0.9):
                    if (pos[0] > window_width /2):
                        quit_clicked = True
                        print("Quit Confirmed")
                        pygame.quit()
                        sys.exit()
                    else:
                        go_clicked = True
                        
                if not go_clicked:
                    block_coord_x = (int(pos[0]/block_size))
                    block_coord_y = (int(pos[1]/block_size))
                    if ((block_coord_x,block_coord_y)) not  in clicked_pos:
                        clicked_pos.append((block_coord_x,block_coord_y))
                        
                if go_clicked == True:
                    
                    path_list = MST()
                    #convert path list back to coords
                    for x in range(0,len(path_list)):
                        node1 = path_list[x][0]
                        node2 = path_list[x][1]
                        
                        path_list[x] = [clicked_pos[node1],clicked_pos[node2]]
                new_list = []
                for sublist in path_list:
                    for item in sublist:
                        new_list.append(item)
                path_list = new_list
                draw(window,new_list)        
                
                
        pygame.display.flip      
        pygame.display.update()
        
            
def list_paths(clicked_pos):
    for x in range(0,len(clicked_pos)):
        pos_array.append([0]*len(clicked_pos))
    
    for x in range(0,len(clicked_pos)):
        for y in range(0,len(clicked_pos)):
            if x == y:
                pos_array[x][y] = 10000
            else:
                pos_array[x][y] = math.sqrt(float((((clicked_pos[x][0] - clicked_pos[y][0]) * (clicked_pos[x][0] - clicked_pos[y][0])) 
                + ((clicked_pos[x][1] - clicked_pos[y][1]) * (clicked_pos[x][1] - clicked_pos[y][1])))))
    connected_nodes = [0]
    path_list = []
    current_min = 10000
    while len(connected_nodes) != len(clicked_pos):
        #find smallest path among connected nodes
        for node in connected_nodes:
            if min(pos_array[node]) < current_min:
                current_min = min(pos_array[node])
                
        
        for node in connected_nodes:
            if min(pos_array[node]) == current_min and (node, pos_array[node].index(current_min)) not in path_list:
                path_list.append([node, pos_array[node].index(current_min)])
                if pos_array[node].index(current_min) not in connected_nodes:
                    connected_nodes.append(pos_array[node].index(current_min))
                pos_array[node][pos_array[node].index(current_min)] = 10000
        current_min = 10000
        
    
    return path_list         
            
    
def MST():
    if len(clicked_pos) == 0:
        print("Invalid Entry")
        sys.exit()
    
    path_list = list_paths(clicked_pos)
    
    return path_list
    '''
    for item in path_list:
        global coord1 
        coord1 = (clicked_pos[item[0]][0],clicked_pos[item[0]][1])
        global coord2 
        coord2 = (clicked_pos[item[1]][0],clicked_pos[item[1]][1])
        global paths_calculated 
        paths_calculated = True
        pygame.draw.line(window, colour_green, coord1, coord2)
        pygame.draw.lines(window, colour_green, False, path_list, 25)
        pygame.display.flip
       ''' 


def draw(window, path_list):
    
        
    for x in range(int(window_width/block_size)):
        for y in range(int(window_height/block_size)):
            
            if (x,y) in clicked_pos:
                rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
                if go_clicked == False:
                    pygame.draw.rect(window, colour_red, rect, 0)
                elif go_clicked == True: 
                    pygame.draw.rect(window, colour_black, rect, 0)
                    
            
            elif (y > (window_height/block_size)*0.9) and (x < (window_width/block_size)*0.5):
                rect = pygame.Rect(0,window_height*0.9, window_width/2, window_height*0.1)
                pygame.draw.rect(window, colour_teal, rect, 0)
                
            elif (y > (window_height/block_size)*0.9) and (x > (window_width/block_size)*0.5):
                rect = pygame.Rect(window_width/2 ,window_height*0.9, window_width/2, window_height*0.1)
                pygame.draw.rect(window, colour_purple, rect, 0)

                
            else: 
                print(path_list)
                
                #pygame.draw.lines(window, colour_green,False, path_list,25)
                #pygame.draw.lines(window,colour_green,False,[(100,150),(250,150)],25)
                #pygame.draw.line(window,colour_green,new_list[0],new_list[1],25)
                rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
                pygame.draw.rect(window, colour_black, rect, 1)
                
                
                
    

    
            
main()