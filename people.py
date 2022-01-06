import pygame
import sys
from pygame.locals import *
import random

# 初始化pygame
pygame.init()
# 设置帧率（屏幕每秒刷新的次数）
FPS = 60
# 获得pygame的时钟
fpsClock = pygame.time.Clock()
# 设置窗口大小
screen = pygame.display.set_mode((500, 400), 0, 32)
# 设置标题
pygame.display.set_caption('People game')
# 加载图片
img = pygame.image.load("imgs/one.png", )
img = pygame.transform.scale(img, (15, 20), )
img2 = pygame.image.load("imgs/two.png", )
img2 = pygame.transform.scale(img2, (15, 20), )
img3 = pygame.image.load("imgs/san.png", )
img3 = pygame.transform.scale(img3, (15, 20), )
img4 = pygame.image.load("imgs/si.png", )
img4 = pygame.transform.scale(img4, (15, 20), )
# 把图片对象封装到字典中
tuzidianyou = {0: img, 10: img2, 20: img3, 30: img4}
imgzuo = pygame.image.load("imgs/onezuo.png", )
imgzuo = pygame.transform.scale(imgzuo, (15, 20), )
img2zuo = pygame.image.load("imgs/twozuo.png", )
img2zuo = pygame.transform.scale(img2zuo, (15, 20), )
img3zuo = pygame.image.load("imgs/sanzuo.png", )
img3zuo = pygame.transform.scale(img3zuo, (15, 20), )
img4zuo = pygame.image.load("imgs/sizuo.png", )
img4zuo = pygame.transform.scale(img4zuo, (15, 20), )
tuzidianzuo = {0: imgzuo, 10: img2zuo, 20: img3zuo, 30: img4zuo}
# 初始化图片的位置
imgx = 10
imgy = 30
zhi = 0
# 初始化图片的移动方向
direction = 'right'
# 定义随机金钱图标出现位置
img1x = random.randint(15, 465)
img1y = random.randint(30, 365)
# 导入字体并设置字体大小
imgg = pygame.font.Font("Font/COOPBL.TTF", 20)
ziti = pygame.font.Font("Font/COOPBL.TTF", 50)
# 使用字体编辑游戏结束语句
wenzi = ziti.render('Game Over', True, (0, 0, 0))
tishi = imgg.render("Press R restart", True, (0, 0, 0))
# 定义结束语大字在中心位置
wenziwei = wenzi.get_rect()
wenziwei.center = (250, 200)
# 这个变量用于判断人物是否死亡
number = 1
# 这个变量用于人物图片之间切换实现跑动效果
jishu = 0
# 定义默认小人奔跑方向为右
tuzidian = tuzidianyou
while True:
    # 因为每10帧切换一次图片，判断显示完第四张图片后切换为第一张
    if jishu == 40:
        jishu = 0
    # 因为字典的键为0，10，20，30 所以判断jishu变量为这个值时传入字典
    if jishu == 0 or jishu % 10 == 0:
        img = tuzidian[jishu]
    # 每次循环jishu变量值+1
    jishu += 1
    # 定义背景颜色为白色
    screen.fill((255, 255, 255))
    # 导入钱袋图标以及大小
    img1 = pygame.image.load("imgs/钱钱.png")
    img1 = pygame.transform.scale(img1, (20, 20))
    # 通过绝对值函数判断小人是否拿到了钱
    if abs(imgx-img1x) < 15 and abs(imgy-img1y) < 25:
        # 重新生成图标位置
        img1x = random.randint(15, 465)
        img1y = random.randint(30, 365)
        # 拿到了钱之后经验值+20
        zhi += 20
        # 拿到钱之后页面刷新速度增加
        FPS += 15
    # 绘制钱图标在屏幕上
    screen.blit(img1, (img1x, img1y), )
    # 定义经验值文字和显示位置
    experience = imgg.render('experience: {}'.format(zhi), True, (0, 0, 0), )
    screen.blit(experience, (10, 0), )
    # 定义边框
    pygame.draw.line(screen, (0, 0, 0), (10, 25), (490, 25), 2, )
    pygame.draw.line(screen, (0, 0, 0), (10, 390), (490, 390), 2, )
    pygame.draw.line(screen, (0, 0, 0), (10, 25), (10, 390), 2, )
    pygame.draw.line(screen, (0, 0, 0), (490, 25), (490, 390), 2, )
    # 判断移动的方向，并对相应的坐标做加减d
    if number == 1:
        if direction == "right":
            imgx += 1
            tuzidian = tuzidianyou
            # 判断是否碰撞边缘
            if imgx == 475:
                number = 0
        elif direction == 'down':
            imgy += 1
            if imgy == 365:
                number = 0
        elif direction == 'left':
            imgx -= 1
            tuzidian = tuzidianzuo
            if imgx == 12:
                number = 0
        elif direction == 'up':
            imgy -= 1
            if imgy == 25:
                number = 0
        # 该方法将用于图片绘制到相应的坐标中
        screen.blit(img, (imgx, imgy), )
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == ord('d'):
                    direction = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    direction = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    direction = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    direction = 'down'
    else:
        # 人物死亡后绘制结束语
        screen.blit(wenzi, wenziwei, )
        screen.blit(tishi, (170, 230))
    # 刷新屏幕
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            # 判断输入r键之后所有复原，重新开始
            if event.key == ord('r'):
                imgx = 10
                imgy = 30
                direction = 'right'
                img1x = random.randint(15, 465)
                img1y = random.randint(30, 365)
                FPS = 60
                zhi = 0
                number = 1
    # 设置pygame时钟的间隔时间
    fpsClock.tick(FPS)
