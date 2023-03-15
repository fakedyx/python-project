import pygame
import time
import random
from pygame.sprite import Sprite
from pygame.sprite import Group
import math
from pygame import K_LEFT


def fire_music():
    pass
    # 设置开火音乐
    effect = pygame.mixer.Sound('fire.wav')
    pygame.mixer.Sound.play(effect)


class Boss(Sprite):
    def __init__(self, boss_img_name):
        super().__init__()
        # 加载BOSS图片
        self.image = pygame.image.load('' + boss_img_name + '.png').convert_alpha()
        # 转换BOSS大小
        # self.image = pygame.transform.scale(self.image, (1, 12))
        # 生成BOSS矩形框架
        self.rect = self.image.get_rect()
        self.blood = 10000
        self.temp=self.blood
        # boss左右移动的速度
        self.speed = 3.5
        self.live = 3
        self.bullet_img = pygame.image.load("bossbullet1.png").convert_alpha()
        self.bullet_img = pygame.transform.scale(self.bullet_img, (12, 12))
        if True:
            self.shot=True
        self.shoot_frequency=0


    def move(self):
        if self.rect.centerx >= 512:
            self.speed = -self.speed
        if self.rect.centerx <= 0:
            self.speed = -self.speed
        self.rect.centerx += self.speed

    def shoot(self):
        if self.shoot_frequency % 200 == 0:
            bullet = Boss_Bullet(self.bullet_img, self.rect.midbottom)
            bullet2=Boss_Bullet2(self.bullet_img, self.rect.midbottom)
            self.bullets.add(bullet)
            self.bullets2.add(bullet2)
        self.shoot_frequency += 1
        if self.shoot_frequency > 200:
            self.shoot_frequency = 0
        '''
        #time.clock()
        bullet = Boss_Bullet(self.bullet_img, self.rect.midbottom)
        #time.clock()
        #if time.clock()==5:
        self.bullets.add(bullet)
        '''

    def hit_box(self, scr):
        self.rect.centerx = boss.rect.centerx
        self.rect.centery = boss.rect.centery
        self.x = (80/self.temp) * (self.temp -self.blood)
        pygame.draw.rect(scr, (255, 0, 0), (self.rect.centerx - 42, self.rect.centery - 60, 80 - self.x, 5))



        # 删除子弹

    def moveBullet(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def drawBullets(self, scr):
        self.bullets.draw(scr)

    def moveBullet2(self):
        for bullet2 in self.bullets2:
            bullet2.move()
            if bullet2.rect.bottom < 0:
                self.bullets2.remove(bullet2)

    def drawBullets2(self, scr):
        self.bullets2.draw(scr)


class Boss_Bullet(pygame.sprite.Sprite):
    def __init__(self, init_pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("bossbullet1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        # 敌机子弹初始位置设置
        self.rect.midbottom = init_pos
        self.rect.centery += 36
        self.speed = 6
        self.x=1

    def move(self):
        self.rect.centery += self.speed*random.randint(0,1)
        self.rect.centerx +=self.speed*random.randint(-self.x,self.x)


        '''
        self.rect.top += self.speed
        self.rect.left += self.speed
        
        self.temp = math.sqrt((student_plane.rect.top - self.rect.top) ** 2 + (student_plane.rect.left - self.rect.left) ** 2)
        if self.temp != 0:
            self.rect.centery += self.speed
            self.rect.centerx += self.speed * ((student_plane.rect.left - self.rect.left) / self.temp)
        '''


class Boss_Bullet2(pygame.sprite.Sprite):
    def __init__(self, init_pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("pd-10.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        # 敌机子弹初始位置设置
        self.rect.midbottom = init_pos
        self.rect.centery += 36
        self.speed = 20
        self.x = 1

    def move(self):
        self.rect.centery += self.speed * random.randint(0, 1)
        self.rect.centerx += self.speed * random.randint(-self.x, self.x)

        '''
        self.rect.top += self.speed
        self.rect.left += self.speed

        self.temp = math.sqrt((student_plane.rect.top - self.rect.top) ** 2 + (student_plane.rect.left - self.rect.left) ** 2)
        if self.temp != 0:
            self.rect.centery += self.speed
            self.rect.centerx += self.speed * ((student_plane.rect.left - self.rect.left) / self.temp)
        '''

class Enemy(Sprite):
    def __init__(self, screen):
        # 必须设置继承精灵 不然在使用精灵函数时会报错
        super().__init__()
        # 获取屏幕对象
        self.screen = screen
        # 随机 生成5个编号
        alien_num = random.randint(1, 5)
        # 随机 加载五个飞机中的某个
        self.image = pygame.image.load('alien_' + str(alien_num) + '.png')
        # picture = pygame.transform.scale(picture, (1280, 720))
        self.image = pygame.transform.scale(self.image, (62, 62))
        # 获取飞机的 rect
        self.rect = self.image.get_rect()
        #飞机音乐

        self.score = 10
        # 加载子弹的图片
        self.bullet_img = pygame.image.load("alien_bullet.png").convert_alpha()
        self.bullet_img = pygame.transform.scale(self.bullet_img, (12, 12))
        self.boold=100

        # 飞机的移动速度
        self.speed = random.randint(20, 30)

        # 生成子弹精灵组合
        self.bullets = Group()
        # 敌机射击频率
        self.shoot_frequency = 0

        #爆炸
        self.isboom = True
        self.index = 0


    # 飞机出现
    def move(self):
        self.rect.top += 5

    # 发射子弹
    def shoot(self):
        if self.shoot_frequency % 200 == 0:
            bullet = Enemy_Bullet(self.bullet_img, self.rect.midbottom)
            self.bullets.add(bullet)
        self.shoot_frequency += 1
        if self.shoot_frequency > 200:
            self.shoot_frequency = 0

    # 删除子弹
    def moveBullet(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.centery < 0:
                self.bullets.remove(bullet)

    def drawBullets(self, scr):
        self.bullets.draw(scr)




class Enemy_Bullet(pygame.sprite.Sprite):
    def __init__(self, init_pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("alien_bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        # 敌机子弹初始位置设置
        self.rect.midbottom = init_pos
        self.rect.centery += 36
        self.speed = 8

    def move(self):
        self.rect.top += self.speed


class Friend(Sprite):
    def __init__(self, screen):
        # 必须设置继承精灵 不然在使用精灵函数时会报错
        super().__init__()
        # 获取屏幕对象
        self.screen = screen
        self.image = pygame.image.load('plane.png')
        # picture = pygame.transform.scale(picture, (1280, 720))
        self.image = pygame.transform.scale(self.image, (62, 62))
        # 获取飞机的 rect
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 获取屏幕正中x坐标
        self.rect.centerx = self.screen_rect.centerx
        # 获取屏幕底部y坐标
        self.rect.centery = self.screen_rect.bottom - self.rect.height
        # 设置飞机初始位置
        self.centerX = float(self.rect.centerx)
        self.centerY = float(self.rect.centery)

        # 加载子弹的图片
        self.bullet_img = pygame.image.load("alien_bullet.png").convert_alpha()
        self.bullet_img = pygame.transform.scale(self.bullet_img, (12, 12))

        # 飞机的移动速度
        self.speed = random.randint(20, 30)

        # 生成子弹精灵组合
        self.bullets = Group()
        # 敌机射击频率
        self.shoot_frequency = 0

    # 飞机出现
    def move(self):
        self.rect.top -= 5

        # 暂时不用射击
        # self.shoot()
        # self.moveBullet()

    # 发射子弹
    def shoot(self):
        if self.shoot_frequency % 200 == 0:
            bullet = Friend_Bullet(self.bullet_img, self.rect.midbottom)
            self.bullets.add(bullet)
        self.shoot_frequency += 1
        if self.shoot_frequency > 200:
            self.shoot_frequency = 0

    # 删除子弹
    def moveBullet(self):
        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def drawBullets(self, scr):
        self.bullets.draw(scr)



class Friend_Bullet(pygame.sprite.Sprite):
    def __init__(self, init_pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("alien_bullet.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 50))
        self.rect = self.image.get_rect()
        # 友机子弹初始位置设置
        self.rect.midbottom = init_pos
        self.rect.centery -= 36
        self.speed = 20

    def move(self):
        self.rect.top -= self.speed


class MyHero(Sprite):
    _rate = 100  # 每帧停留的毫秒数

    def __init__(self, screen,size=1):
        super().__init__()
        # 获取屏幕对象
        self.screen = screen
        # 获取整张图片
        self.image_big = pygame.image.load('hero.png').convert_alpha()

        # subsurface 形成大图的子表面框架
        # 获取飞机正面图片
        self.image = self.image_big.subsurface(pygame.Rect(120, 0, 318 - 240, 87))
        # 获取飞机正面矩形框架尺寸
        self.rect = self.image.get_rect()
        # 获取屏幕对象矩形
        self.screen_rect = screen.get_rect()
        # 获取屏幕正中x坐标
        self.rect.centerx = self.screen_rect.centerx
        # 获取屏幕底部y坐标
        self.rect.centery = self.screen_rect.bottom - self.rect.height
        # 设置飞机初始位置
        self.centerX = float(self.rect.centerx)
        self.centerY = float(self.rect.centery)
        # 飞机尾焰
        self.air = None
        # 设置飞机尾焰位置
        self.air_rect = pygame.Rect(self.centerX - 20, self.centerY + int((self.rect.height + 72) / 2) - 10 - 36, 40,
                                    72)
        self.var=0

        # 玩家所有发射子弹的集合
        self.bullets = Group()
        self.bullet_image = pygame.image.load('feidan.png').convert_alpha()

        self.bullets2 = Group()
        self.bullet_image2 = pygame.image.load('bullet4.png').convert_alpha()
        self.bullet_image2 = pygame.transform.scale(self.bullet_image2, (200, 200))

        self.bullets3 = Group()
        self.bullet_image3 = pygame.image.load('wsparticle_super02.png').convert_alpha()
        self.bullet_image3 = pygame.transform.scale(self.bullet_image3, (160, 160))

        self.bullets4 = Group()
        self.bullet_image4 = pygame.image.load('wsparticle_super01.png').convert_alpha()
        self.bullet_image4 = pygame.transform.scale(self.bullet_image4, (100, 2000))

        self.blood=5
        self.life=3



    # 子弹射击
    def shoot(self):
        # 产生一颗子弹实例
        bullet = Bullet(self.bullet_image, self.rect.midtop)
        # 在group子弹精灵集合中加入子弹
        self.bullets.add(bullet)

    def shoot2(self):
        bullet2 = Bullet2(self.bullet_image2, self.rect.midtop)
        # 在group子弹精灵集合中加入子弹
        self.bullets2.add(bullet2)

    def shoot3(self):
        bullet3 = Bullet3(self.bullet_image3, self.rect.midtop)
        # 在group子弹精灵集合中加入子弹
        self.bullets3.add(bullet3)

    def shoot4(self):
        bullet4 = Bullet4(self.bullet_image4, self.rect.midtop)
        # 在group子弹精灵集合中加入子弹
        self.bullets4.add(bullet4)

    # 子弹删除
    def moveBullet(self):
        # 逐个检查子弹精灵集合 到达屏幕顶端的子弹删除
        for bullet in self.bullets:
            bullet.move()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

    def moveBullet2(self):
        # 逐个检查子弹精灵集合 到达屏幕顶端的子弹删除
        for bullet2 in self.bullets2:
            bullet2.move()
            if bullet2.rect.bottom < 0:
                self.bullets2.remove(bullet2)

    def moveBullet3(self):
        # 逐个检查子弹精灵集合 到达屏幕顶端的子弹删除
        for bullet3 in self.bullets3:
            bullet3.move()

    def moveBullet4(self):
        # 逐个检查子弹精灵集合 到达屏幕顶端的子弹删除
        for bullet4 in self.bullets4:
            bullet4.move()

    # 子弹显示
    def drawBullets(self, scr):
        # 将精灵集合中的子弹绘制到屏幕上
        self.bullets.draw(scr)

    def drawBullets2(self, scr):
        # 将精灵集合中的子弹绘制到屏幕上
        self.bullets2.draw(scr)

    def drawBullets3(self, scr):
        # 将精灵集合中的子弹绘制到屏幕上
        self.bullets3.draw(scr)

    def drawBullets4(self, scr):
        # 将精灵集合中的子弹绘制到屏幕上
        self.bullets4.draw(scr)

    # 向上飞时，增加喷射火焰
    def set_air(self, case):
        if case == 'up':
            air = pygame.image.load('air.png').convert_alpha()
            img = air.subsurface(pygame.Rect(80, 0, 50, 87))
            self.air = img
        elif case == 'remove':
            self.air = None

    def hit_box(self,scr):
        self.rect.centerx = student_plane.rect.centerx
        self.rect.centery = student_plane.rect.centery
        self.x=(80/5)*(5-self.blood)
        pygame.draw.rect(scr, (255, 0, 0), (self.rect.centerx - 42, self.rect.centery -60 ,80-self.x,5))


    def set_image(self, case):
        if case=='left':
            rect = pygame.Rect(195,0,318-248,87)
            image = self.image_big.subsurface(rect)
        elif case =='right':
            rect = pygame.Rect(195,0,318-248,87)
            image = pygame.transform.flip(self.image_big.subsurface(rect), True, False)
        elif case == 'up' or case == 'down':
            rect = pygame.Rect(120, 0, 318 - 240, 87)
            image = self.image_big.subsurface(rect)
        self.image = image


class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = bullet_img.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 20

    def move(self):
        # self.rect.top -= self.speed
        self.temp = math.sqrt((enemy.rect.top - self.rect.top) ** 2 + (enemy.rect.left - self.rect.left) ** 2)
        if self.temp!=0:
           self.rect.centery += self.speed * ((enemy.rect.top - self.rect.top) / self.temp)
           self.rect.centerx += self.speed * ((enemy.rect.left - self.rect.left) / self.temp)



class Bullet2(pygame.sprite.Sprite):
    def __init__(self, bullet_img2, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img2
        self.rect = bullet_img2.get_rect()
        self.rect.midbottom = init_pos

        self.speed = 30

    def move(self):
        # self.rect.top -= self.speed
        self.rect.top -= self.speed


class Bullet3(pygame.sprite.Sprite):
    def __init__(self, bullet_img3, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img3
        self.rect = bullet_img3.get_rect()
        self.rect.midbottom = init_pos

    def move(self):
        # self.rect.top -= self.speed
        self.rect.centerx = student_plane.rect.centerx
        self.rect.centery = student_plane.rect.centery


class Bullet4(pygame.sprite.Sprite):
    def __init__(self, bullet_img4, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img4
        self.rect = bullet_img4.get_rect()
        self.rect.midbottom = init_pos

    def move(self):
        # self.rect.top -= self.speed
        self.rect.centerx = student_plane.rect.centerx
        self.rect.centery = student_plane.rect.centery



class Buff(Sprite):
    def __init__(self, screen):
        # 必须设置继承精灵 不然在使用精灵函数时会报错
        super().__init__()
        # 获取屏幕对象
        self.screen = screen
        self.buff_num = random.randint(15, 16)
        self.image = pygame.image.load(str(self.buff_num) + '.png')
        self.p1=pygame.image.load('15.png')
        self.p2 = pygame.image.load('16.png')
        # picture = pygame.transform.scale(picture, (1280, 720))
        self.image = pygame.transform.scale(self.image, (30, 30))
        # 获取飞机的 rect
        self.rect = self.image.get_rect()

        self.speed = random.randint(20, 30)

    def move(self):
        if self.rect.centerx >= 512:
            self.speed = -self.speed
        if self.rect.centerx <= 0:
            self.speed = -self.speed
        self.rect.centerx += self.speed
        self.rect.top += 8


# 爆炸精灵类
class Explode(pygame.sprite.Sprite):
    def __init__(self):
        self.frame_width = 0
        self.frame_height = 0
        self.rect = 0,0,0,0
        self.columns = 0
        self.last_frame = 1
        self.last_time = 0
        self.frame = 0
        self.first_frame = 0
        self.old_frame = 0
        self.visible=False

    def load(self, filename, row, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()   # 载入整张图片
        self.master_rect = self.master_image.get_rect()                   # 获取图片的rect值
        self.frame_width = self.master_rect.width//columns                # 计算单一帧的宽度
        self.frame_height = self.master_rect.height//row                  # 计算单一帧的高度
        #self.rect = , student_plane.rect.centery, self.frame_width, self.frame_height             # 更新rect
        self.columns = columns                                            # 存储列的值（用以后续计算）
        self.last_frame = row * columns - 1                               # 计算是有0开始的，需要 -1

    def set_pos(self,x,y):
        self.rect=(x,y,self.frame_width*2, self.frame_height*2)

    def update(self, screen):
        self.frame += 1                                                   # 帧序号 +1
        if self.frame > self.last_frame:
            self.frame = self.first_frame                                 # 循环播放
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width           # 计算 subsurface 的 x 坐标
            frame_y = (self.frame // self.columns) * self.frame_height         # 计算 subsurface 的 y 坐标
            #rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height) # 获取subsurface 的 rect
            rect = (frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)                    # 更新self.image
            self.old_frame = self.frame                            # 更新self.old_frame
        if self.visible==True:
            screen.blit(self.image, self.rect)
            self.visible=False



# 初始化pygame
pygame.init()
pygame.mixer.init()
pygame.mixer_music.load('1.mp3')  # 加载播放音乐
pygame.mixer.music.play(-1)  # -1 为循环播放
# 设置游戏主题
pygame.display.set_caption('AirCraft')
# 初始化屏幕大小
screen = pygame.display.set_mode((512, 768))
flag=True

# 设置游戏背景图片
# 游戏刚开始时的背景图
bg_img0 = pygame.image.load('start_bg0.jpg').convert()
# 加载游戏开始图标
myfont = pygame.font.SysFont('simhei', 60)
color = 255, 0, 0
textimg = myfont.render(u'雷霆战机', True, color)

#爆炸图片
explosion01_image = pygame.image.load('爆炸2.png').convert_alpha()
explosion01_rect = explosion01_image.get_rect()

start_img = pygame.image.load('start.png').convert_alpha()
start_rect = start_img.get_rect()
start_rect.centerx = 262
start_rect.centery = 455
#  游戏进行中的背景图
bg_img1 = pygame.image.load('map2.jpg').convert()
bg_img2 = bg_img1.copy()
# 游戏结束时的背景图
bg_img3 = pygame.image.load('map3.jpg').convert()
# 加载游戏结束图标
gameover_img = pygame.image.load('gameover.png').convert_alpha()
# 加载游戏成功图标
gamesuccess = pygame.image.load('success.png').convert_alpha()

# 加载重玩图标
restart_img = pygame.image.load('restart.png').convert_alpha()
restart_rect = restart_img.get_rect()
restart_rect.centerx = 249
restart_rect.centery = 420
# 背景图片初始位置
pos_y1 = -768
pos_y2 = 0

# 实例化BOSS
boss = Boss('boss_1')
bosses = Group()
bosses.add(boss)

# 生成我方飞机

student_plane = MyHero(screen)

student_plane1 = MyHero(screen)
student_plane1.image_big = pygame.image.load('p02-1.png').convert_alpha()
student_plane1.image = student_plane1.image_big.subsurface(pygame.Rect(120, 0, 318 - 240, 87))
student_plane1.rect.centerx = student_plane.rect.centerx - 132
student_plane1.rect.centery = student_plane.rect.centery + 70
student_plane1.centerX = float(student_plane1.rect.centerx)
student_plane1.centerY = float(student_plane1.rect.centery)
student_plane1.bullet_image2 = pygame.image.load('bullet2.png').convert_alpha()
student_plane1.bullet_image2 = pygame.transform.scale(student_plane1.bullet_image2, (50, 70))

student_plane2 = MyHero(screen)
student_plane2.image_big = pygame.image.load('p02-1.png').convert_alpha()
student_plane2.image = student_plane2.image_big.subsurface(pygame.Rect(120, 0, 318 - 240, 87))
student_plane2.rect.centerx = student_plane.rect.centerx + 137
student_plane2.rect.centery = student_plane.rect.centery + 70
student_plane2.centerX = float(student_plane2.rect.centerx)
student_plane2.centerY = float(student_plane2.rect.centery)
student_plane2.bullet_image2 = pygame.image.load('bullet3.png').convert_alpha()
student_plane2.bullet_image2 = pygame.transform.scale(student_plane2.bullet_image2, (30, 50))

# 生成敌方飞机
# 生成敌机group
enemies = Group()

# 生成敌机子弹
enemy_bullets = Group()
max_enemies = 9

# 敌机随机出现的节奏 下方randint参数 为43,55
ran1, ran2 = 30, 40
ran3,ran4=10,200
# 生成boss子弹
boss_bullets = Group()
boss_bullets2 = Group()
# 生成友军
max_friends = 2
friends = Group()
# 友军子弹
friend_bullets = Group()
#buff
buffs=Group()
max_buff=2

#爆炸
my_explode = Explode()
my_explode.load('爆炸2.png', 3, 5)
framerate = pygame.time.Clock()


# 生成计时频率变量
sec = 0
rec = 0
tec=0
# 生成分数
score = 0
# 设置系统字体
my_font = pygame.font.SysFont("simhei", 15)



game = 'wait'

i = 9
a1 = False
help = False
cop = False


while True:
    framerate.tick(120)

    if game == 'wait':

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


            if event.type == pygame.MOUSEBUTTONDOWN:

                if start_rect.collidepoint(event.pos):
                    student_plane.__init__(screen)
                    game = 'ing'

        screen.blit(bg_img0, (0, 0))
        screen.blit(textimg, (140, 100))
        screen.blit(start_img, start_rect)

        pygame.display.flip()
        time.sleep(0.05)

    elif game == 'ing':
        # 屏幕滚动
        screen.blit(bg_img1, (0, pos_y1))
        screen.blit(bg_img2, (0, pos_y2))
        # if fly==False:
        pos_y1 += 3
        pos_y2 += 3
        # elif fly==True:
        # pos_y1 += 5
        # pos_y2 += 5

        # 屏幕背景滚动完毕后重置位置
        if pos_y1 >= 0:
            pos_y1 = -768
        if pos_y2 >= 768:
            pos_y2 = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and len(student_plane.bullets) < 2:
                mouse_press = pygame.mouse.get_pressed()
                if mouse_press == (0, 0, 1):
                    fire_music()
                    # 产生一颗子弹实例
                    # 在group子弹精灵集合中加入子弹
                    student_plane.shoot()
                    if cop == True:
                        student_plane1.shoot()
                        student_plane2.shoot()


                elif mouse_press == (1, 0, 0) and len(student_plane.bullets2) < 3 and len(student_plane1.bullets2) < 3 and len(student_plane2.bullets2) < 3:
                    fire_music()
                    # 产生一颗子弹实例
                    # 在group子弹精灵集合中加入子弹ad
                    student_plane.shoot2()
                    # 将精灵集合中的子弹绘制到屏幕上
                    if cop == True:
                        student_plane1.shoot2()
                        student_plane2.shoot2()


                elif mouse_press == (0, 1, 0) and len(student_plane.bullets3) < 1:
                    student_plane.shoot3()
                    a1 = False
                    if cop == True:
                        student_plane1.shoot3()
                        student_plane2.shoot3()

            if event.type == pygame.KEYUP:
                # student_plane.set_image('down')
                student_plane.air = None
                if cop == True:
                    student_plane1.air = None
                    student_plane2.air = None

            # 发射子弹
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and len(student_plane.bullets4) < 1:  # 检查子弹集合的数量限制子弹最大数量
                    fire_music()
                    # 产生一颗子弹实例
                    # 在group子弹精灵集合中加入子弹
                    student_plane.shoot4()
                    if cop == True:
                        student_plane1.shoot4()
                        student_plane2.shoot4()

        # 将精灵集合中的子弹绘制到屏幕上
        student_plane.drawBullets(screen)
        # 逐个检查子弹精灵集合 到达屏幕顶端的子弹删除
        student_plane.moveBullet()

        student_plane.drawBullets2(screen)
        # 逐个检查子弹精灵集合 到达屏幕顶端的子弹删除
        student_plane.moveBullet2()

        student_plane.drawBullets3(screen)
        student_plane.moveBullet3()

        student_plane.drawBullets4(screen)
        student_plane.moveBullet4()

        if cop == True:
            # 将精灵集合中的子弹绘制到屏幕上
            student_plane1.drawBullets(screen)
            # 逐个检查子弹精灵集合 到达屏幕顶端的子弹删除
            student_plane1.moveBullet()

            student_plane1.drawBullets2(screen)
            # 逐个检查子弹精灵集合 到达屏幕顶端的子弹删除
            student_plane1.moveBullet2()

            student_plane1.drawBullets3(screen)
            student_plane1.moveBullet3()

            student_plane1.drawBullets4(screen)
            student_plane1.moveBullet4()

            # 将精灵集合中的子弹绘制到屏幕上
            student_plane2.drawBullets(screen)
            # 逐个检查子弹精灵集合 到达屏幕顶端的子弹删除
            student_plane2.moveBullet()

            student_plane2.drawBullets2(screen)
            # 逐个检查子弹精灵集合 到达屏幕顶端的子弹删除
            student_plane2.moveBullet2()

            student_plane2.drawBullets3(screen)
            student_plane2.moveBullet3()

            student_plane2.drawBullets4(screen)
            student_plane2.moveBullet4()

        student_plane.hit_box(screen)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            # 设置飞机状态图片
            student_plane.set_image('left')
            if student_plane.rect.centerx >= 40:
                student_plane.rect.centerx -= 10.5
            # fly = False

        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            # 设置飞机状态图片
            student_plane.set_image('right')
            if student_plane.rect.centerx <= 478:
                student_plane.rect.centerx += 10.5
        # fly = False

        elif keys[pygame.K_w] or keys[pygame.K_UP]:
            # 设置飞机状态图片
            student_plane.set_image('up')
            student_plane.set_air('up')
            # fly=True
            if cop == True:
                student_plane1.set_air('up')
                student_plane2.set_air('up')

            if student_plane.rect.centery >= 45:
                student_plane.rect.centery -= 10.5

        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            # 设置飞机状态图片
            student_plane.set_image('down')
            if student_plane.rect.centery <= 727:
                student_plane.rect.centery += 10.5
            # fly = False
        elif keys[pygame.K_h]:
            help = True
        elif keys[pygame.K_j]:
            cop = True
        elif keys[pygame.K_ESCAPE]:
            break
        elif keys[pygame.K_r]:
            game='success'

        # 显示飞机
        if cop == False:
            screen.blit(student_plane.image, student_plane.rect)
        if cop == True:


            student_plane1.rect.centerx = student_plane.rect.centerx - 132
            student_plane1.rect.centery = student_plane.rect.centery + 70


            student_plane2.rect.centerx = student_plane.rect.centerx + 137
            student_plane2.rect.centery = student_plane.rect.centery + 70


            student_plane.bullet_image2 = pygame.image.load('wsparticle_super01.png').convert_alpha()
            student_plane.bullet_image2 = pygame.transform.scale(student_plane.bullet_image2, (80, 150))
            screen.blit(student_plane.image, student_plane.rect)

            screen.blit(student_plane1.image, (student_plane.rect.centerx - 180, student_plane.rect.centery))
            if student_plane1.air != None:
                screen.blit(student_plane1.air,
                            (student_plane.rect.centerx - 140 - 30, student_plane.rect.centery + 75))
            screen.blit(student_plane2.image, (student_plane.rect.centerx + 100, student_plane.rect.centery))
            if student_plane2.air != None:
                screen.blit(student_plane.air, (student_plane.rect.centerx + 140 - 30, student_plane.rect.centery + 75))
        if student_plane.air != None:
            screen.blit(student_plane.air, (student_plane.rect.centerx - 30, student_plane.rect.centery + 33))

        # 友机 ---------------------------------------------------------------------------------------
        if help == True:
            rec += 1
            rhy2 = random.randint(ran1, ran2)

            if rec % rhy2 == 0 and len(friends) < max_friends or rec == 1:
                friend = Friend(screen)
                friend.rect.centerx = random.randint(0, 512)
                friend_bullet = Friend_Bullet((friend.rect.centerx, friend.rect.centery))

                friends.add(friend)
                friend_bullets.add(friend_bullet)

            friends.draw(screen)
            friend_bullets.draw(screen)




            for friend in friends:
                friend.move()
                if friend.rect.bottom < 0:
                    friends.remove(friend)
            for friend_bullet in friend_bullets:
                friend_bullet.move()

        #buff
        tec += 1

        rhy3 = random.randint(ran3, ran4)


        if tec % rhy3 == 0 and len(buffs) < max_buff or tec == 1:
            #
            buff = Buff(screen)
            buff.rect.centerx = random.randint(0, 512)
            buffs.add(buff)

        buffs.draw(screen)


        for buff in buffs:
            # 让每个对象移动起来
            buff.move()
            if buff.rect.top > 768:
                buffs.remove(buff)

        #敌机
        sec += 1
        # 随机控制生成敌机的节奏
        rhy = random.randint(ran1, ran2)


        if my_explode.visible == True:
            my_explode.set_pos(enemy.rect.centerx-70, enemy.rect.centery-50)
            my_explode.update(screen)
            

        if sec % rhy == 0 and len(enemies) < max_enemies or sec == 1:  # 设置敌机数量总数为9
            # 生成一只敌机
            enemy = Enemy(screen)
            enemy.rect.centerx = random.randint(0, 512)
            # 生成上述敌机的子弹
            enemy_bullet = Enemy_Bullet((enemy.rect.centerx, enemy.rect.centery))
            # 敌机group 和 敌机子弹group加载敌机和子弹
            enemies.add(enemy)
            enemy_bullets.add(enemy_bullet)


        # 敌机出现 和 敌机子弹出现
        enemies.draw(screen)
        enemy_bullets.draw(screen)
        # 迭代敌机集合
        for enemy in enemies:

            # 让每个对象移动起来
            enemy.move()
            # 敌机超出屏幕边界后 自动删除敌机
            collision_over1 = pygame.sprite.collide_rect(student_plane, enemy)


            if collision_over1:
                # 为了重启游戏时 防止有旧子弹和飞机存在
                enemies.remove(enemy)
                student_plane.blood-=1
                my_explode.visible = True

            if enemy.rect.bottom > 768:
                enemies.remove(enemy)
        for enemy_bullet in enemy_bullets:
            # 让每个对象移动起来
            enemy_bullet.move()

            collision_over2 = pygame.sprite.collide_rect(student_plane, enemy_bullet)
            if collision_over2:
                # 为了重启游戏时 防止有旧子弹和飞机存在
                enemy_bullets.remove(enemy_bullet)
                student_plane.blood-=1

            # 敌机子弹超出屏幕边界后 自动删除敌机
            if enemy_bullet.rect.bottom > 768:
                enemy_bullets.remove(enemy_bullet)

        for boss_bullet in boss_bullets:
            # 让每个对象移动起来
            boss_bullet.move()

        for boss_bullet2 in boss_bullets2:
                # 让每个对象移动起来
            boss_bullet2.move()

            collision_over3 = pygame.sprite.collide_rect(student_plane, boss_bullet)
            if collision_over3:
                # 为了重启游戏时 防止有旧子弹和飞机存在
                boss_bullets.remove(boss_bullet)
                student_plane.blood-=1
            # 敌机子弹超出屏幕边界后 自动删除敌机
            if boss_bullet.rect.bottom > 768 or boss_bullet.rect.left < 0 or boss_bullet.rect.right > 512:
                boss_bullets.remove(boss_bullet)

        boss.move()

        if student_plane.blood <= 0 and student_plane.life != 0:
            student_plane.blood = 5
            student_plane.life -= 1
        if student_plane.life <= 0:
            game = 'over'
            boss.blood=100000
            boss.live=3

        if score >= 100:
            # 小敌机出现的节奏
            ran1, ran2 = 15, 25

            screen.blit(boss.image, boss.rect)
            boss.move()
            life_text2 = my_font.render('Boss Life: ' + str(boss.live), True, (0, 255, 255))
            life_text3 = my_font.render('Boss Blood: ' + str(boss.blood), True, (0, 255, 255))
            screen.blit(life_text3, [10, 50])
            screen.blit(life_text2, [10, 30])

            for my_bullet2 in student_plane.bullets2:
                hit_boss = pygame.sprite.collide_rect(boss, my_bullet2)
                if hit_boss:
                    boss.blood -= 100
                    score += 10
                    student_plane.bullets2.remove(my_bullet2)

            for my_bullet4 in student_plane.bullets4:
                hit_boss4 = pygame.sprite.collide_rect(boss, my_bullet4)
                if hit_boss4:
                    boss.blood -= 10
                    score += 10


            for my_bullet2 in student_plane1.bullets2:
                hit_boss = pygame.sprite.collide_rect(boss, my_bullet2)
                if hit_boss:
                    boss.blood -= 100
                    score += 10


            for my_bullet4 in student_plane1.bullets4:
                hit_boss4 = pygame.sprite.collide_rect(boss, my_bullet4)
                if hit_boss4:
                    boss.blood -= 100
                    score += 10

            for my_bullet2 in student_plane2.bullets2:
                hit_boss = pygame.sprite.collide_rect(boss, my_bullet2)
                if hit_boss:
                    boss.blood -= 100
                    score += 10

                    # 生成上述敌机的子弹
            for my_bullet4 in student_plane2.bullets4:
                hit_boss4 = pygame.sprite.collide_rect(boss, my_bullet4)
                if hit_boss4:
                    boss.blood -= 100
                    score += 10


            for friend_bullet in friend_bullets:
                hit_boss5 = pygame.sprite.collide_rect(boss, friend_bullet)
                if hit_boss5:
                    boss.blood -= 100
                    score += 10


            boss_bullet = Boss_Bullet((boss.rect.centerx, boss.rect.centery))
            boss_bullets.add(boss_bullet)
            if boss.live==3:
                if boss.blood <= 0 and boss.live != 0:
                    boss.blood = 20000
                    max_enemies = 15
                    max_friends = 4
                    Boss_Bullet.x = 2
                    Boss_Bullet.speed = 8
                    boss.image = pygame.image.load('boss_2.png').convert_alpha()
                    boss.image = pygame.transform.scale(boss.image, (462, 300))
                    boss.live -= 1
            if boss.live==2:
                if boss.blood <= 0 and boss.live != 0:
                    boss.blood = 50000
                    max_enemies = 20
                    max_friends = 6
                    Boss_Bullet.x=3
                    Boss_Bullet.speed=10
                    boss.image = pygame.image.load('boss_5.png').convert_alpha()
                    boss.image = pygame.transform.scale(boss.image, (600, 467))
                    boss.live -= 1

            if boss.live==1:
                if boss.blood <= 0:
                    game = 'success'
                boss_bullet2 = Boss_Bullet2((boss.rect.centerx, boss.rect.centery))
                boss_bullets2.add(boss_bullet2)
            boss.hit_box(screen)

        boss_bullets.draw(screen)
        boss_bullets2.draw(screen)
        for boss_bullet in boss_bullets:
            boss_bullet.move()
        for boss_bullet2 in boss_bullets2:
            boss_bullet2.move()


        collisions = pygame.sprite.groupcollide(student_plane.bullets, enemies, True, True)
        if collisions:
            score += 10
            my_explode.visible=True
        collisions2 = pygame.sprite.groupcollide(student_plane.bullets2, enemies,True, True)
        if collisions2:
            score += 10
            my_explode.visible= True

        if i == 0:
            a1 = True
            i = 9

        collisionsx = pygame.sprite.groupcollide(student_plane.bullets2, enemy_bullets, True, True)
        if collisionsx:
            score += 10

        collisionsy = pygame.sprite.groupcollide(student_plane.bullets2, boss_bullets, True, True)
        if collisionsy:
            score += 10

        collisions3 = pygame.sprite.groupcollide(student_plane.bullets3, enemies, a1, True)
        if collisions3:
            score += 10
            i -= 1
            my_explode.visible = True
        collisions4 = pygame.sprite.groupcollide(student_plane.bullets3, enemy_bullets, a1, True)
        if collisions4:
            score += 10
            i -= 1
            my_explode.visible = True
        collisions5 = pygame.sprite.groupcollide(student_plane.bullets3, boss_bullets, a1, True)
        if collisions5:
            score += 10
            i -= 1

        collisions6 = pygame.sprite.groupcollide(student_plane.bullets4, enemies, False, True)
        if collisions6:
            score += 10
            my_explode.visible = True

        collisions7 = pygame.sprite.groupcollide(student_plane.bullets4, boss_bullets, False, True)
        if collisions7:
            score += 10

        collisions8 = pygame.sprite.groupcollide(student_plane.bullets4, enemy_bullets, False, True)
        if collisions8:
            score += 10

        collisions9 = pygame.sprite.groupcollide(friend_bullets, enemies, True, True)
        if collisions9:
            score += 10
            my_explode.visible = True
        collisions9x = pygame.sprite.groupcollide(friend_bullets, boss_bullets, True, True)
        if collisions9x:
            score += 10

        collisions10 = pygame.sprite.groupcollide(friends, enemies, True, True)
        if collisions10:
            score += 10
            my_explode.visible = True

        collisions11 = pygame.sprite.groupcollide(friends, boss_bullets, True, True)

        collisions12 = pygame.sprite.groupcollide(friends, bosses, True, False)

        collisions13 = pygame.sprite.groupcollide(friend_bullets, bosses, True, False)
        if collisions13:
            score += 10


        collisions14 = pygame.sprite.groupcollide(friends, enemy_bullets, True, True)

        collisions15 = pygame.sprite.groupcollide(student_plane1.bullets, enemies, True, True)
        if collisions15:
            score += 10
            my_explode.visible = True
        collisions16 = pygame.sprite.groupcollide(student_plane1.bullets2, enemies, False, True)
        if collisions16:
            score += 10
            my_explode.visible = True

        collisions17 = pygame.sprite.groupcollide(student_plane1.bullets3, enemies, a1, True)
        if collisions17:
            score += 10
            my_explode.visible = True

        collisions18 = pygame.sprite.groupcollide(student_plane1.bullets3, enemy_bullets, a1, True)
        if collisions18:
            score += 10
            my_explode.visible = True
        collisions19 = pygame.sprite.groupcollide(student_plane1.bullets3, boss_bullets, a1, True)
        if collisions19:
            score += 10
            my_explode.visible = True

        collisions20 = pygame.sprite.groupcollide(student_plane1.bullets4, enemies, False, True)
        if collisions20:
            score += 10
            my_explode.visible = True

        collisions21 = pygame.sprite.groupcollide(student_plane1.bullets2, boss_bullets, True, True)
        if collisions21:
            score += 10


        collisions22 = pygame.sprite.groupcollide(student_plane1.bullets4, enemy_bullets, False, True)
        if collisions22:
            score += 10

        collisions23 = pygame.sprite.groupcollide(student_plane2.bullets, enemies, True, True)
        if collisions23:
            score += 10
            my_explode.visible = True
        collisions24 = pygame.sprite.groupcollide(student_plane2.bullets2, enemies, False, True)
        if collisions24:
            score += 10
            my_explode.visible = True

        collisions25 = pygame.sprite.groupcollide(student_plane2.bullets3, enemies, a1, True)
        if collisions25:
            score += 10
            my_explode.visible = True

        collisions26 = pygame.sprite.groupcollide(student_plane2.bullets3, enemy_bullets, a1, True)
        if collisions26:
            score += 10
        collisions27 = pygame.sprite.groupcollide(student_plane2.bullets3, boss_bullets, a1, True)
        if collisions27:
            score += 10

        collisions28 = pygame.sprite.groupcollide(student_plane2.bullets4, enemies, False, True)
        if collisions28:
            score += 10
            my_explode.visible = True

        collisions29 = pygame.sprite.groupcollide(student_plane2.bullets2, boss_bullets, True, True)
        if collisions29:
            score += 10

        collisions30 = pygame.sprite.groupcollide(student_plane2.bullets4, enemy_bullets, False, True)
        if collisions30:
            score += 10

        collisions31 = pygame.sprite.collide_rect(student_plane, buff)
        if collisions31:
            if buff.buff_num==16:
               buffs.remove(buff)
               student_plane.blood=5
            if buff.buff_num==15:
                buffs.remove(buff)
                student_plane.var+=1
                if student_plane.var>=50:
                    student_plane.bullet_image2=pygame.image.load('bullet5.png').convert_alpha()
                    student_plane.bullet_image2=pygame.transform.scale(student_plane.bullet_image2, (200, 200))



        # 分数和奖励的显示-------------------------------------------------------------------------
        surface1 = my_font.render(u"当前得分：%s" % (score), True, [255, 0, 0])
        life_text = my_font.render('Your Life: ' + str(student_plane.life), True, (255, 0, 0))
       # life_text2 = my_font.render('Boss Life: ' + str(boss.live), True, (0, 255, 255))
        #life_text3 = my_font.render('Boss Blood: ' + str(boss.blood), True, (0, 255, 255))
        text1=my_font.render("普通子弹(左键)",True,(0,255,0))
        text2 = my_font.render("护盾(鼠标中键)", True, (0,255,0))
        text3 = my_font.render("追踪弹(右键)", True, (0,255,0))
        text4 = my_font.render("激光大招(空格)", True, (0,255,0))
        text5 = my_font.render("友军支援(h)", True, (0,255,0))
        text6 = my_font.render("分身术(j)", True, (0,255,0))
        text7 = my_font.render("退出(Esc)", True, (0, 255, 0))
        text8 = my_font.render("重玩(r)", True, (0, 255, 0))

        #screen.blit(life_text3, [10, 50])
        #screen.blit(life_text2, [10, 30])
        screen.blit(surface1, [10, 10])

       # screen.blit(life_text3, [10,50])
        screen.blit(text1, [0, 200])
        screen.blit(text2, [0, 240])
        screen.blit(text3, [0, 280])
        screen.blit(text4, [0, 320])
        screen.blit(text5, [0, 360])
        screen.blit(text6, [0, 400])
        screen.blit(text7, [0, 440])
        screen.blit(text8, [0, 480])
        screen.blit(life_text, [10, 520])

        # 更新画面
        pygame.display.flip()
        # 设置帧数和延迟
        time.sleep(0.05)

    # 游戏结束状态
    if game == 'over':
        score = 0
        boss.blood=10000
        # 最小游戏框架一个都不能省略
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # 检测鼠标是否按下 重新开始按钮
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 检测鼠标点击位置是否与重启rect重叠
                if restart_rect.collidepoint(event.pos):
                    student_plane.__init__(screen)
                    game = 'ing'

        # 游戏结束游戏画面暂停
        screen.blit(bg_img1, (0, pos_y1))
        screen.blit(bg_img2, (0, pos_y2))

        screen.blit(gameover_img, (163, 310))
        screen.blit(restart_img, restart_rect)

        pos_y1 += 0
        pos_y2 += 0
        pygame.display.flip()
        time.sleep(0.05)
        surface2 = my_font.render("Game Over", True, [255, 0, 0])
        screen.blit(surface1, [250, 350])
    if game == 'success':
        score = 0
        boss.blood = 10000
        boss.live=3
        # 最小游戏框架一个都不能省略
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # 检测鼠标是否按下 重新开始按钮
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 检测鼠标点击位置是否与重启rect重叠
                if restart_rect.collidepoint(event.pos):
                    student_plane.__init__(screen)
                    game = 'ing'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        # 游戏结束游戏画面暂停
        screen.blit(bg_img1, (0, pos_y1))
        screen.blit(bg_img2, (0, pos_y2))

        screen.blit(gamesuccess, (170, 220))
        screen.blit(restart_img, restart_rect)
        # 测试尾焰位置
        # screen.blit(img, (100, 100))
        pos_y1 += 0
        pos_y2 += 0
        pygame.display.flip()
        time.sleep(0.05)
