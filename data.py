import pygame
import os
import sys
from dataclasses import dataclass

USER_FILEPATH = os.getcwd()

sys.path.insert(0, f'{USER_FILEPATH}\\module')

from button import Button

pygame.init()

# There should be full screen mode i guess
# Maybe the data shouldnt all be in this file, but make distribution is needed

# Getting the Resolution of User Computer
info = pygame.display.Info()
computer_width = info.current_w
computer_height = info.current_h

# Screen Size
screen_width = computer_width*(80/100)
screen_height = computer_height*(80/100)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Visual Novel')

IMAGE_DIR = f'{USER_FILEPATH}\\images'
FONT_DIR = f'{USER_FILEPATH}\\fonts'
SOUNDTRACK_DIR = f'{USER_FILEPATH}\\soundtracks'

def load_image(filename):
    return pygame.image.load(f'{IMAGE_DIR}\\{filename}')

def load_font(filename):
    return f'{FONT_DIR}\\{filename}'

def load_soundtrack(filename):
    return pygame.mixer.Sound(f'{SOUNDTRACK_DIR}\\{filename}')

# ------------------ CONFIRGURATION ------------------ #

running = True

# Button
rectBtt = load_image('rect.jfif')
settingsImg = load_image('settings.png')

# Settings
settings_scale = 0.06
settings_gap = 10
settings_x = screen_width - (settingsImg.get_width()*settings_scale)/2 - settings_gap
settings_y = (settingsImg.get_height()*settings_scale)/2 + settings_gap

def settings_button():
    return Button(image=settingsImg, scale=settings_scale,  pos=(settings_x, settings_y), 
        text_input=None, font='timesnewroman', font_size=None, base_color="White", hovering_color="Green")

SETTINGS_BUTTON = settings_button()

# Intro Section


# Background
BGscaleW = 1
BGscaleH = 1
BG_width = screen_width * BGscaleW
BG_height = screen_height * BGscaleH
BG_x = screen_width/2
BG_y = screen_height/2


# Message Box
gapb = 12
widthb = screen_width - gapb*2
heightb = screen_height/3.6
xb = gapb
yb = screen_height - heightb - gapb

# Gap for Characrer in MessageBox
gapc = int(heightb/12)

# Character
xc = xb
yc = yb + heightb/2

# Sprite Group
character_group = pygame.sprite.Group()
text_group = pygame.sprite.Group()
situation_group = pygame.sprite.Group()
background_group = pygame.sprite.Group()
choices_group = pygame.sprite.Group()
button_group = pygame.sprite.Group()

button_group.add(SETTINGS_BUTTON)

# Trigger for occuring once
trigger_cb = True
trigger_mopt = True
trigger_mc = True
trigger_intro = True
trigger_situation = True

# Whether should start the game or not
@dataclass
class Game:
    current: bool

start_game = Game(False)
end_game = Game(False)

# ------------------ DATA ------------------ #

# Font
general_font = load_font('mynerve.ttf')
print(general_font)

# Sound
clickSound = load_soundtrack('clickSound.mp3')

# Character
MinhHuy_name = 'Minh Huy'
MinhHuy_image = load_image('minhhuy.png')

BoMinhHuy_name = 'Bố Minh Huy'
BoMinhHuy_image = load_image('bominhhuy.png')

# Background
neutral_state = load_image('neutralBoard.jpg')
scold_state = load_image('scold_surprise.jpg')
surprise_state = load_image('scold_surprise.jpg')
introBG = load_image('grey.jfif')

# Situtation
vnBoard = load_image('vnboard.png')

# ---------- CONFIG SITUATION FOR PAGE ---------- #
siGap = 10 # the frame of the background orange board

SituationC1No1 = [
    {
        'image': vnBoard,
        'img_width': 800,
        'img_height': 600,
        'img_x': BG_x,
        'img_y': BG_y,
    }, 
    {
        'image': settingsImg,
        'img_width': 100,
        'img_height': 100,
        'img_x': 600,
        'img_y': 400,
    },
]

# ---------- CONFIG PAGE FOR CHAPTER ---------- #
# những config này chỉ đơn giản là những thông tin phải nhập vào để generate một cái trang thôi
SconfigC1STP1 = {
    'character_image': None, 
    'character_name': None, 
    'character_messages': ['*Minh Huy đang ngồi trên bàn học và nghĩ về Học kỳ 1 vừa qua*'], 
    'text_speed': 5,
    'background': neutral_state,
    'situation': SituationC1No1,
    'next': 'single-C1-ST-P2' 
}

SconfigC1STP2 = {
    'character_image': MinhHuy_image, 
    'character_name': MinhHuy_name, 
    'character_messages': ['Thế là qua 1 Học Kỳ dài đã qua rồi. Haizzz...'], 
    'text_speed': 16,
    'background': neutral_state,
    'situation': None,
    'next': 'single-C1-ST-P3'
}

SconfigC1STP3 = {
    'character_image': None, 
    'character_name': None, 
    'character_messages': ['*Bố của Minh Huy mở cửa bước vào*'], 
    'text_speed': 16,
    'background': neutral_state,
    'situation': None,
    'next': 'single-C1-ST-P4'
}

SconfigC1STP4 = {
    'character_image': BoMinhHuy_image, 
    'character_name': BoMinhHuy_name, 
    'character_messages': ['Mặt con gì mà đầy muộn phiền vậy?'], 
    'text_speed': 16,
    'background': neutral_state,
    'situation': None,
    'next': 'multiple-C1-ST-P5'
}

MconfigC1STP5 = {
    'character_image': BoMinhHuy_image, 
    'character_name': BoMinhHuy_name, 
    'character_messages': ['Con có muốn tâm sự với bố một chút không?'], 
    'text_speed': 16,
    'background': neutral_state,
    'choices': {'m1-opt1': 'Vâng con đang muốn chia sẻ vài điều với bố ạ', 
                'm1-opt2': 'Xin lỗi bố ,con đang bận học ạ. lần sau nhé bố'
                },
    'next': 'single-C1-M1-P1'
} 

SconfigC1_M1OPT1_P1 = {
    'character_image': BoMinhHuy_image, 
    'character_name': BoMinhHuy_name, 
    'character_messages': ['Thế bố con mình nói chuyện chút nhé. Bố đang khá vui vẻ nên bố cũng muốn cùng con giải quyết chuyện của con á.',
                            'Gần đây con có gặp khó khăn gì ở trường không?'], 
    'text_speed': 16,
    'background': neutral_state,
    'situation': None,
    'next': 'single-C1-M1-P2' 
}

SconfigC1_M1OPT1_P2 = {
    'character_image': MinhHuy_image, 
    'character_name': MinhHuy_name,
    'character_messages': ['Có một chút bố ạ. Bố đi họp phụ huynh cho con nên cũng biết đấy.',
                            'Hmm… Điểm làm việc nhóm của con khá thấp nên có phần ảnh hưởng đến kết quả HK1 ạ.'], 
    'text_speed': 16,
    'background': neutral_state,
    'situation': None,
    'next': 'end'
}

SconfigC1_M1OPT2_P1 = {
    'character_image': BoMinhHuy_image, 
    'character_name': BoMinhHuy_name, 
    'character_messages': ['Vậy à. Thế con cứ tiếp tục học. Bố không làm phiền con nữa nhé.',
                            'Khi đói thì xuống bếp có thức ăn bố nấu rồi đấy.'], 
    'text_speed': 16,
    'background': neutral_state,
    'situation': None,
    'next': 'single-C1-M1-P2' 
}

SconfigC1_M1OPT2_P2 = {
    'character_image': MinhHuy_image, 
    'character_name': MinhHuy_name,
    'character_messages': ['Vâng, con cảm ơn bố ạ'], 
    'text_speed': 16,
    'background': neutral_state,
    'situation': None,
    'next': 'end'
}

SconfigC1_END_P1 = {
    'character_image': MinhHuy_image, 
    'character_name': MinhHuy_name, 
    'character_messages': ['Sheesh, We are unlucky today'
                            'Painmon please walk this time.'], 
    'text_speed': 16,
    'background': neutral_state,
    'situation': vnBoard,
    'next': 'single-C1-E-P2'
}

SconfigC1_END_P2 = {
    'character_image': MinhHuy_image, 
    'character_name': MinhHuy_name, 
    'character_messages': ['Oh, Oh. That looks cool'
                            'Let go there.'], 
    'text_speed': 16,
    'background': neutral_state,
    'situation': vnBoard,
    'next': 'single-C1-E-P2'
}

# ------------------ CHAPTER ------------------ #
chapter1 = {
    'start': {
        "single-C1-ST-P1": SconfigC1STP1,
        "single-C1-ST-P2": SconfigC1STP2,
        "single-C1-ST-P3": SconfigC1STP3,
        "single-C1-ST-P4": SconfigC1STP4,
        "multiple-C1-ST-P5": MconfigC1STP5
    },
    'm1-opt1': {
        'single-C1-M1-P1': SconfigC1_M1OPT1_P1,
        'single-C1-M1-P2': SconfigC1_M1OPT1_P2,
    },
    'm1-opt2': {
        'single-C1-M1-P1': SconfigC1_M1OPT2_P1,
        'single-C1-M1-P2': SconfigC1_M1OPT2_P2,
    },
    'end': {
        "single-C1-E-P1": SconfigC1_END_P1,
        "single-C1-E-P2": SconfigC1_END_P2,
    }
}

chapters = [chapter1]

# ---------- CONFIG STATE ---------- #

# tạo ra một file user_state.txt để lưu trang mà người dùng đã đọc tới
if not os.path.exists("user_state.txt"):
    f = open("user_state.txt", "x")
    with open("user_state.txt", "w") as f:
        f.write("0 start single-C1-ST-P1")
        user_state = [0, 'start', 'single-C1-ST-P1']
else:
    with open("user_state.txt", "r") as f:
        user_state = f.read().split(' ')
        user_state[0] = int(user_state[0])

@dataclass
class State:
    chapter: any
    chapter_phrase: str
    page_state: str

# chapter: đại diện cho cái chương mà user hiện tại đang ở
# chapter_phrase: chỉ đơn giản những phần nhỏ được chia ra từ chương lớn, tại sao lại chia như v thì đơn giản là vì:
# -> trong này có option, khi mà chung ta không chia mà để cho trôi chảy một section lớn nhất duy nhất thì không thể nào, trừ khi chapter đó không có multiple choices thôi
# page_state: đó là trang mà user đang ở khi ở một phrase của một chapter nào đó
state = State(chapters[user_state[0]], user_state[1], user_state[2])

# Ví dụ ở phần CHAPTER trong data này thì chapter1 ở đây là thuộc tính chapter, start,..., end là phrase và single-C1-ST-P1 hay multiple-C1-ST-P5 là page


# LƯU Ý:
# page nào mà chỉ có cuộc hội thoại không thôi tức là không có multiple choices dính dáng gì tới hội thoại thì cái page_state đó luôn phải có chữ 'single-'
# nếu page đó có multiple choices thì ghi 'multiple-'

# mọi chapter đều phải có phrase start và end, vd như chapter 1: có phrase start và end
# ở phrase start và end thì cái page_state phải có ST (là cho start) và E (là cho end) ở giữa mỗi từ page_state (vd: single-C1-ST-P1, single-C1-E-P1)

# phần 'next' là bắt buộc phải có vì nó giúp báo trước trang sau là gì
# - VD: bây giờ đang ở trang single-C1-ST-P1 thì mình bắt buộc phải nhập trang tiếp theo tức là single-C1-ST-P2 vào

# khi mà phrase tiếp theo là phrase 'end' thì hãy nhập 'next': 'end' cho trang cuối của phrase trước phrase 'end'
# còn mà hết chapter r thì page cuối cùng của chapter đó hãy nhập là 'end_chapter'
# khi mà đã hết cốt truyện thì hãy nhập 'end_game' vào page cuối cùng của code truyện đó

# ở đây character_image và situation có thể được ghi là None vì cs vài hội thoại trong cốt truyện chỉ miêu tả khoảng khắc ko cs lời nói nhân vật