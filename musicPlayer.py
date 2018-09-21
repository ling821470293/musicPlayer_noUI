#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import pygame

def welcome():
    print("""
        ***********************
        *  欢迎来到酷我播放器 *
        *                     *
        ***********************
        """)
def choice():
    print("""
    进入功能区
    ***********************
    * 1.上一曲     2.下一曲*
    * 3.暂停       4.播放  *
    * 5.音量调大 6.音量调小*
    *     7.退出           *
    ************************
    """)

# 播放音乐
def play(pp):
    if pp == 'play':
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.pause()

# 暂停
def pause():
        pygame.mixer.music.pause()

# 取消暂停
def qxpause():
    pygame.mixer.music.unpause()


# 音量调节
def up_vol(v):
    if v >= 1:
        v = 1
        print('音量已经最大了')
    else:
        v += 0.2
    pygame.mixer.music.set_volume(v)
    return v

def down_vol(v):
    if v <= 0.1:
        v = 0.1
        print('音量已经最小了')
    else:
        v -= 0.2
    pygame.mixer.music.set_volume(v)
    return v

# 上一曲
def shangmusic(i):
    if i <= 0:
        print('当前已经是第一首歌了，没有上一曲')
    else:
        i -= 1
        path = r'music/' + song[i]
        pygame.mixer.music.load(path)
    return i

# 下一曲
def xiamusic(i):
    if i >= len(song)-1:
        print('当前已经是最后一歌了，没有下一曲')
    else:
        i += 1
        path = r'music/' + song[i]
        pygame.mixer.music.load(path)
    return i

# 文件夹路径
def addr(fp):
    for root, dirs, files in os.walk(fp):
        for fn in files:
           filelist.append(fn)
    return filelist

# 初始化音频
pygame.mixer.init()
# 初始化当前歌曲序列
i = 0
# 初始化音量
v = 0.5
pau = 'pause'
# 音乐文件夹路径
fp = r'music/'
# 初始化空文件列表
filelist = []
# song = ['dang.mp3','feima.wav','qingchen.mp3']
song = addr(fp)
path = fp + song[i]
pygame.mixer.music.load(path)
welcome()
while True:
    choice()
    n = input('请输入要选择的功能（1-7）：')
    if n == '1':
        print('上一曲')
        i = shangmusic(i)
        play('play')
    if n == '2':
        print('下一曲')
        i = xiamusic(i)
        play('play')
    # 播放
    if n == '4':
        print('播放')
        play('play')
    # 暂停和取消暂停
    if n == '3':
        if pau == 'pause':
            print('暂停')
            pause()
            pau = 'unpause'
            continue
        if pau == 'unpause':
            print('取消暂停')
            qxpause()
            pau = 'pause'
            continue
    # 调节音量
    if n == '5':
        print('音量调高')
        v = up_vol(v)
    if n == '6':
        print('音量调低')
        v = down_vol(v)
    # 退出
    if n == '7':
        print('退出')
        break
