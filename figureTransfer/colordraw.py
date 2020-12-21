# -*- coding:utf-8 -*-
import cv2
import numpy as np
import sys
from numpy import *
#from colordetect1 import draw
draw = np.zeros((4800,6400, 3), dtype="uint8")#创建一个高4800*宽6400画布       
def drawcolor(get_str):#URFDLB 传入54个字符 
    #strcolor={'U':(0,255,255),'R':(0,255,0),'F':(0,0,255),'D':(255,255,255),'L':(255,191,0),'B':(0,128,255)}  
    #strcolor="URFDLB"  
    draw_str=[]
    #BGR:
    U=(0,255,255)
    R=(0,255,0)
    F=(0,0,255)
    D=(255,255,255)
    L=(255,191,0)
    B=(0,128,255) 
    for key in get_str:#遍历54个字符中每个字符，i为字符
        #def findstr(get_str):  
        #for get_str[i] in range(6):
        #for key in strcolor:
        if key=='U':
            draw_str.append(U)
        elif key=='R':
            draw_str.append(R)
        elif key=='F':
            draw_str.append(F)
        elif key=='D':
            draw_str.append(D)
        elif  key=='L':
            draw_str.append(L)
        elif  key=='B':
            draw_str.append(B)   
#上面    
    cv2.rectangle(draw, (1600, 1600-1500), (1600+500,1600-1000), draw_str[0],-1)
    cv2.rectangle(draw, (1600+500, 1600-1500), (1600+1000, 1600-1000), draw_str[1], -1)
    cv2.rectangle(draw, (1600+1000, 1600-1500), (1600+1500,1600-1000),draw_str[2], -1)
    cv2.rectangle(draw, (1600, 1600-1000), (1600+500, 1600-500), draw_str[3], -1)
    cv2.rectangle(draw, (1600+500, 1600-1000), (1600+1000, 1600-500),draw_str[4],-1)
    cv2.rectangle(draw, (1600+1000,1600-1000), (1600+1500, 1600-500),draw_str[5], -1)
    cv2.rectangle(draw, (1600,1600-500), (1600+500, 1600),draw_str[6], -1)
    cv2.rectangle(draw, (1600+500, 1600-500), (1600+1000,1600),draw_str[7], -1)
    cv2.rectangle(draw, (1600+1000,1600-500), (1600+1500, 1600),draw_str[8], -1)
    cv2.putText(draw, 'U', (1600+500+125, 1600-1000+400), cv2.FONT_HERSHEY_COMPLEX, 15, (0, 0, 0), 50)
#右面
    cv2.rectangle(draw, (3100, 1600), (3100+500,1600+500),draw_str[9],-1)
    # Color 2
    cv2.rectangle(draw, (3100+500, 1600), (3100+1000, 1600+500), draw_str[10], -1)
    # Color 3
    cv2.rectangle(draw, (3100+1000, 1600), (3100+1500,1600+500),draw_str[11], -1)
    # Color 4
    cv2.rectangle(draw, (3100, 1600+500), (3100+500, 1600+1000),draw_str[12], -1)
    # Color 5
    cv2.rectangle(draw, (3100+500, 1600+500), (3100+1000, 1600+1000),draw_str[13],-1)
    # Color 6
    cv2.rectangle(draw, (3100+1000,1600+500), (3100+1500, 1600+1000),draw_str[14], -1)
    # Color 7
    cv2.rectangle(draw, (3100, 1600+1000), (3100+500, 1600+1500), draw_str[15], -1)
    # Color 8
    cv2.rectangle(draw, (3100+500, 1600+1000), (3100+1000,1600+1500),draw_str[16], -1)
    # Color 9
    cv2.rectangle(draw, (3100+1000,1600+1000), (3100+1500, 1600+1500),draw_str[17], -1)
    cv2.putText(draw, 'R', (3100+500+125, 1600+500+400), cv2.FONT_HERSHEY_COMPLEX, 15, (0, 0, 0), 50) 
#前面
    cv2.rectangle(draw, (1600, 1600), (1600+500,1600+500), draw_str[18],-1)
    # Color 2
    cv2.rectangle(draw, (1600+500, 1600), (1600+1000, 1600+500), draw_str[19], -1)
    # Color 3
    cv2.rectangle(draw, (1600+1000, 1600), (1600+1500,1600+500), draw_str[20], -1)
    # Color 4
    cv2.rectangle(draw, (1600, 1600+500), (1600+500, 1600+1000), draw_str[21], -1)
    # Color 5
    cv2.rectangle(draw, (1600+500, 1600+500), (1600+1000, 1600+1000), draw_str[22],-1)
    # Color 6
    cv2.rectangle(draw, (1600+1000,1600+500), (1600+1500, 1600+1000), draw_str[23], -1) 
    # Color 7
    cv2.rectangle(draw, (1600, 1600+1000), (1600+500, 1600+1500),draw_str[24], -1)
    # Color 8
    cv2.rectangle(draw, (1600+500, 1600+1000), (1600+1000,1600+1500),draw_str[25], -1)
    # Color 9
    cv2.rectangle(draw, (1600+1000,1600+1000), (1600+1500, 1600+1500),draw_str[26], -1)
    cv2.putText(draw, 'F', (1600+500+125, 1600+500+400), cv2.FONT_HERSHEY_COMPLEX, 15, (0, 0, 0), 50)
#下面
    cv2.rectangle(draw, (1600, 1600+1500), (1600+500,1600+2000),draw_str[27],-1)
    # Color 2
    cv2.rectangle(draw, (1600+500, 1600+1500), (1600+1000, 1600+2000), draw_str[28], -1)
    # Color 3
    cv2.rectangle(draw, (1600+1000, 1600+1500), (1600+1500,1600+2000), draw_str[29], -1)
    # Color 4
    cv2.rectangle(draw, (1600, 1600+2000), (1600+500, 1600+2500),draw_str[30], -1)
    # Color 5
    cv2.rectangle(draw, (1600+500, 1600+2000), (1600+1000, 1600+2500), draw_str[31],-1)
    # Color 6
    cv2.rectangle(draw, (1600+1000,1600+2000), (1600+1500, 1600+2500),draw_str[32], -1)
    # Color 7
    cv2.rectangle(draw, (1600, 1600+2500), (1600+500, 1600+3000), draw_str[33], -1)
    # Color 8
    cv2.rectangle(draw, (1600+500, 1600+2500), (1600+1000, 1600+3000),draw_str[34], -1)
    # Color 9
    cv2.rectangle(draw, (1600+1000,1600+2500), (1600+1500,  1600+3000), draw_str[35], -1)
    cv2.putText(draw, 'D', (1600+500+125, 1600+2000+400), cv2.FONT_HERSHEY_COMPLEX, 15, (0, 0, 0), 50)  
#左面
    cv2.rectangle(draw, (1600-1500, 1600), (1600-1000,1600+500), draw_str[36],-1)
    # Color 2
    cv2.rectangle(draw, (1600-1000, 1600), (1600-500, 1600+500), draw_str[37], -1)
    # Color 3
    cv2.rectangle(draw, (1600-500, 1600), (1600,1600+500), draw_str[38], -1)
    # Color 4
    cv2.rectangle(draw, (1600-1500, 1600+500), (1600-1000, 1600+1000), draw_str[39], -1)
    # Color 5
    cv2.rectangle(draw, (1600-1000, 1600+500), (1600-500, 1600+1000), draw_str[40],-1)
    # Color 6
    cv2.rectangle(draw, (1600-500,1600+500), (1600, 1600+1000), draw_str[41], -1)
    # Color 7
    cv2.rectangle(draw, (1600-1500, 1600+1000), (1600-1000, 1600+1500), draw_str[42], -1)
    # Color 8
    cv2.rectangle(draw, (1600-1000, 1600+1000), (1600-500,1600+1500), draw_str[43], -1)
    # Color 9
    cv2.rectangle(draw, (1600-500,1600+1000), (1600, 1600+1500), draw_str[44], -1)
    cv2.putText(draw, 'L', (1600-1000+125, 1600+500+400), cv2.FONT_HERSHEY_COMPLEX, 15, (0, 0, 0), 50)    
#后面
    cv2.rectangle(draw, (4600, 1600), (4600+500,1600+500),  draw_str[45],-1)
    # Color 2
    cv2.rectangle(draw, (4600+500, 1600), (4600+1000, 1600+500), draw_str[46], -1)
    # Color 3
    cv2.rectangle(draw, (4600+1000, 1600), (4600+1500,1600+500),  draw_str[47], -1)
    # Color 4
    cv2.rectangle(draw, (4600, 1600+500), (4600+500, 1600+1000), draw_str[48], -1)
    # Color 5
    cv2.rectangle(draw, (4600+500, 1600+500), (4600+1000, 1600+1000),  draw_str[49],-1)
    # Color 6
    cv2.rectangle(draw, (4600+1000,1600+500), (4600+1500, 1600+1000),  draw_str[50], -1)
    # Color 7
    cv2.rectangle(draw, (4600, 1600+1000), (4600+500, 1600+1500),  draw_str[51], -1)
    # Color 8
    cv2.rectangle(draw, (4600+500, 1600+1000), (4600+1000,1600+1500),  draw_str[52], -1)
    # Color 9
    cv2.rectangle(draw, (4600+1000,1600+1000), (4600+1500, 1600+1500), draw_str[53], -1)
    cv2.putText(draw, 'B', (4600+500+125, 1600+500+400), cv2.FONT_HERSHEY_COMPLEX, 15, (0, 0, 0), 50)    
    sum1=0
    sum2=0
    for i in range(13):
    	cv2.line(draw, (1600-1500+sum1,1600-1500), (1600-1500+sum1,1600+3000),(0,0,0),50)   
    	sum1=sum1+500  
    for i in range(10):
    	cv2.line(draw, (1600-1500,1600-1000+sum2), (1600+4500,1600-1000+sum2),(0,0,0),50)   
    	sum2=sum2+500  
     
    cv2.namedWindow('draw',cv2.WINDOW_NORMAL )
    cv2.imshow('draw',draw)

