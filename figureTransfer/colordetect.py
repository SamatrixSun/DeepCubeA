# -*- coding:utf-8 -*-
import cv2
import numpy as np
import sys
from colordraw import *
import math
import json
import time
from multiprocessing import Pool

kernel_5 = np.ones((5,5),np.uint8)#5x5的卷积核
kernel_15 = np.ones((15,15),np.uint8)#15x15的卷积核
kernel_50 = np.ones((50,50),np.uint8)#50x50的卷积核
draw = np.zeros((4800,6400, 3), dtype="uint8")#创建一个高4800*宽6400画布

front=''
up=''
down=''
left=''
right=''
back=''

#处理图片
def colorMatch(name):
    #cube_rgb = picture
    cube_rgb = cv2.imread(name + '.jpg')
    cube_rgb = cv2.resize(cube_rgb,(300,300))
    cube_gray = cv2.cvtColor(cube_rgb, cv2.COLOR_BGR2GRAY)#颜色转换gray
    #cv2.imshow(name,deepcube_size)
    cube_hsv = cv2.cvtColor(cube_rgb,cv2.COLOR_BGR2HSV)#颜色转换hsv
    cube_gray = cv2.adaptiveThreshold(cube_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)#自适应滤波

    # 白色
    lower_white = np.array([0, 0, 201])
    upper_white = np.array([180, 50, 255])
    white_mask = cv2.inRange(cube_hsv, lower_white, upper_white)
    white_erosion = cv2.erode(white_mask, kernel_5, iterations = 1)
    white_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = white_erosion)
    #cv2.imshow(name,white_res)

    #红色
    lower_red = np.array([0,50,245])
    upper_red = np.array([10,255,255])
    red_mask0 = cv2.inRange(cube_hsv, lower_red, upper_red)
    lower_red = np.array([172, 135, 150])
    upper_red = np.array([179, 240, 255])
    red_mask1 = cv2.inRange(cube_hsv, lower_red, upper_red)
    red_mask = red_mask0 + red_mask1
    red_erosion = cv2.erode(red_mask, kernel_5, iterations = 1)
    red_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = red_erosion)
    #cv2.imshow(name,red_res)

    #橙色
    lower_orange = np.array([7, 51, 0])
    upper_orange = np.array([30, 255, 255])
    orange_mask = cv2.inRange(cube_hsv, lower_orange, upper_orange)
    orange_erosion = cv2.erode(orange_mask, kernel_5, iterations = 1)
    orange_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = orange_erosion)
    #cv2.imshow(name,orange_res)

    #黄色
    lower_yellow = np.array([31, 51, 0])
    upper_yellow = np.array([40, 255, 255])
    yellow_mask = cv2.inRange(cube_hsv, lower_yellow, upper_yellow)
    yellow_erosion = cv2.erode(yellow_mask, kernel_5, iterations = 1)
    yellow_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = yellow_erosion)
    #cv2.imshow(name,yellow_res)

    #绿色
    lower_green = np.array([45,51,0])
    upper_green = np.array([82,255,255])
    green_mask = cv2.inRange(cube_hsv, lower_green, upper_green)
    green_erosion = cv2.erode(green_mask, kernel_5, iterations = 1)
    green_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = green_erosion)
    #cv2.imshow(name,green_res)

    #蓝色
    lower_blue = np.array([90, 50, 150])
    upper_blue = np.array([120, 255, 255])
    blue_mask = cv2.inRange(cube_hsv, lower_blue, upper_blue)
    blue_erosion = cv2.erode(blue_mask, kernel_5, iterations = 1)
    blue_res = cv2.bitwise_and(cube_rgb, cube_rgb, mask = blue_erosion)
    #cv2.imshow(name,blue_res)

    #总掩膜
    mask = red_erosion + green_erosion + yellow_erosion + blue_erosion + orange_erosion + white_erosion
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_5)#开运算分割色块
    mask = cv2.erode(mask, kernel_5, iterations = 1)
    res = cv2.bitwise_and(cube_hsv, cube_hsv, mask = mask)
    #cv2.imshow(name,res)
    #cv2.waitKey(0)
       
    edges = cv2.Canny(mask,50,80,apertureSize=5)
    points = cv2.findNonZero(edges)
    
    #求得图像最大最小值点
    min = np.amin(points, axis=0)#求每列的最小值，axis 0为列,1为行
    max = np.amax(points, axis=0)#求每列的最大值，axis 0为列,1为行
    
    #求像素x、y最大最小值
    w, h = cube_gray.shape[::-1]#获取cube_gray大小(宽列数w*高行数h)
    x_max = max[0][0]
    y_max = max[0][1]
    x_min = min[0][0]
    y_min = min[0][1] 
    width = int(x_max - x_min)
    height = int(y_max - y_min)

    cube_rgb = cube_rgb[y_min:y_max, x_min:x_max]
    cube_rgb = cv2.resize(cube_rgb,(300,300))
    #cv2.imshow('1',cube_rgb)
    #cv2.waitKey(100000)

    #cube_hsv = cv2.cvtColor(cube_rgb,cv2.COLOR_BGR2HSV)#颜色转换hsv
    
    
    
    #确定区域颜色
    def getcolor(x1,y1,x2,y2):
        max_num = 0
        white_num = 0
        orange_num = 0
        blue_num = 0
        green_num = 0
        yellow_num = 0
        red_num = 0

        for i in range (y1,y2):
            for j in range (x1,x2):
                rgb = cube_rgb[i, j]
                if ((180<=rgb[0]<=255 ) and (180<=rgb[1]<=255) and(180<=rgb[2]<=255)):#白
                    white_num += 1
                    #return ('D')
                if ((0<=rgb[0]<=100) and (70<=rgb[1]<=225)and (200<=rgb[2] <=255)):#澄
                    orange_num += 1
                    #return ('B')
                if ((150<=rgb[0] <=255) and (0<=rgb[1]<=120) and (0<=rgb[2]<=120)):#蓝
                    blue_num += 1
                    #return ('L')
                if( (0<=rgb[0]<=150) and (150<=rgb[1]<=255) and (0<=rgb[2]<=150)):#绿
                    green_num += 1
                    #return ('R')
                if ((50<=rgb[0]<=150) and (200<=rgb[1]<=255) and(150<=rgb[2]<=255)):#黄
                    yellow_num += 1
                    #return ('U')
                if ( (0<=rgb[0]<=100)and(0<=rgb[1]<=70) and (150<=rgb[2]<=255)):#红
                    red_num += 1
                    #return ('F')

        if(white_num > max_num):max_num = white_num
        if(orange_num > max_num):max_num = orange_num
        if(blue_num > max_num):max_num = blue_num
        if(green_num > max_num):max_num = green_num
        if(yellow_num > max_num):max_num = yellow_num
        if(red_num > max_num):max_num = red_num

        if(white_num == max_num):return('D')
        elif(orange_num == max_num):return('B')
        elif(blue_num == max_num):return('L')
        elif(green_num == max_num):return('R')
        elif(yellow_num == max_num):return('U')
        elif(red_num == max_num):return('F')

    s=''
    s += getcolor(25,25,75,75)
    s += getcolor(125,25,175,75)
    s += getcolor(225,25,275,75)
    s += getcolor(25,125,75,175)
    s += getcolor(125,125,175,175)
    s += getcolor(225,125,275,175)
    s += getcolor(25,225,75,275)
    s += getcolor(125,225,175,275)
    s += getcolor(225,225,275,275)
    
    if(name == 'down'):
        global down
        down += s

    if(name == 'back'):
        global back
        back += s

    if(name == 'left'):
        global left
        left += s

    if(name == 'right'):
        global right
        right += s

    if(name == 'up'):
        global up
        up += s

    if(name == 'front'):
        global front
        front += s

def get_the_num(str1):
    #p = [2,5,8,1,4,7,0,3,6,33,30,27,34,31,28,35,32,29,45,46,47,48,49,50,51,52,53,18,21,24,19,22,25,20,23,26,17,16,15,14,13,12,11,10,9,36,37,38,39,40,41,42,43,44]
    p = [33,30,27,34,31,28,35,32,29,2,5,8,1,4,7,0,3,6,53,52,51,50,49,48,47,46,45,26,25,24,23,22,21,20,19,18,36,37,38,39,40,41,42,43,44,17,16,15,14,13,12,11,10,9]
    str2 = [0 for i in range(54)]
    for i in range(0,54):
        str2[i] = str1[p[i]]
    return str2

if __name__ == '__main__':

        front=''
        up=''
        down=''
        left=''
        right=''
        back=''
        side=['up','right','front','down','left','back']
        
        for i in range (0,6):
            colorMatch(side[i])

        print("front:" + front)
        print("up:" + up)
        print("down:" + down)
        print("right:" + right)
        print("left:" + left)
        print("back:" + back)

        while(1):
            get_str = up + right + front + down + left + back
            print('当前颜色:'+ get_str)
            drawcolor(get_str)
            cv2.waitKey(10000)
            read = input('请核对并修正：（如没有问题，输入ok；如有问题，输入problem\n')
            if read == 'ok':
                break
            elif read == 'problem':
                read1 = input('请输入有问题的面（F、B、R、L、U、D）\n')
                read2 = input('请输入该面的颜色字符串（红为F，蓝为L，绿为R，黄为U，白为D，橙为B）\n')
                if(read1 == 'F'): front = read2
                if(read1 == 'B'): back = read2
                if(read1 == 'R'): right = read2
                if(read1 == 'L'): left = read2
                if(read1 == 'U'): up = read2
                if(read1 == 'D'): down = read2
            else:
                print('请输入正确的回应')

        get_str = up + right + front + down + left + back
        print('当前颜色:'+ get_str)

        num_str = up + right + front + down + left + back
        num_str = get_the_num(get_str)
        
        print('颜色序号:')
        for item in num_str:
            if(item=='D'):print('0',end=' ')
            elif(item=='U'):print('1',end=' ')
            elif(item=='B'):print('2',end=' ')
            elif(item=='F'):print('3',end=' ')
            elif(item=='L'):print('4',end=' ')
            elif(item=='R'):print('5',end=' ')

        #drawcolor(get_str)
        #cv2.waitKey(0)
	




