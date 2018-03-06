# -*- coding: utf-8 -*-
import codecs
import pickle
import threading

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def create_word_file():
    fin = codecs.open('lagou_job.txt', mode='r', encoding='utf-8')
    print '正在进行分词'

    # 第一次运行程序时将分好的词存入文件
    text = ''
    with open('lagou_job.txt') as fin:
        for line in fin.readlines():
            line = line.strip('\n')
            text += ' '.join(jieba.cut(line))
            text += ' '
    fout = open('text.txt', 'wb')
    pickle.dump(text, fout)
    fout.close()
    print '分词结束'


class JieBaWordThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        # 设置锁
        jieba_word_threadLock.acquire()
        create_word_file()
        # 释放锁
        jieba_word_threadLock.release()


class StopWordThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        # 设置锁
        stop_word_threadLock.acquire()
        create_stop_word_list()
        # 释放锁
        stop_word_threadLock.release()


jieba_word_threadLock = threading.Lock()
stop_word_threadLock = threading.Lock()
stop_word = []


def create_stop_word_list():
    with open('stopwords') as fin:
        for line in fin.readlines():
            line = line.strip('\n')
            stop_word.append(line)


import os

def word_count():
    word_lst = []
    key_list = []

    for line in open('lagou_job.txt',):  # 1.txt是需要分词统计的文档

        item = line.strip('\n').split('\t')  # 制表格切分
        tags = jieba.cut(item[0])  # jieba分词
        for t in tags:
            word_lst.append(t)

    word_dict = {}
    with open("wordCount.txt", 'w') as wf2:  # 打开文件

        for item in word_lst:
            if item not in word_dict:  # 统计数量
                word_dict[item] = 1
            else:
                word_dict[item] += 1

        orderList = list(word_dict.values())
        orderList.sort(reverse=True)
        # print orderList
        for i in range(len(orderList)):
            for key in word_dict:
                if word_dict[key] == orderList[i]:
                    print key + ' ' + str(word_dict[key])
                    wf2.write(key + ' ' + str(word_dict[key]) + '\n')  # 写入txt文档
                    key_list.append(key)
                    word_dict[key] = 0



def word_cloud():
    thread = StopWordThread(1, "Thread-Stop-Word")
    thread.start()
    thread.join(20)
    # 直接从文件读取数据
    fr = open('text.txt', 'rb')
    text = pickle.load(fr)
    backgroud_Image = plt.imread('python_creater.jpg')
    wc = WordCloud(background_color='white',  # 设置背景颜色
                   mask=backgroud_Image,  # 设置背景图片
                   max_words=2000,  # 设置最大现实的字数
                   stopwords=STOPWORDS,  # 设置停用词
                   font_path='C:/Users/Windows/Fonts/FZSTK.TTF',  # 设置字体格式，如不设置显示不了中文
                   max_font_size=50,  # 设置字体最大值
                   random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
                   )
    wc.generate(text)
    image_colors = ImageColorGenerator(backgroud_Image)
    wc.recolor(color_func=image_colors)
    plt.imshow(wc)
    plt.axis('off')
    plt.show()
    print('completed')
    save_file_name = os.path.join(os.path.dirname(__file__), 'job_des.png')
    wc.to_file(save_file_name)


if __name__ == '__main__':
    word_count()
    if os.path.exists(os.path.join(os.path.dirname(__file__), 'text.txt')) is not True:
        thread = JieBaWordThread(1, "Thread-JieBa-Word")
        thread.start()
        thread.join(120)



