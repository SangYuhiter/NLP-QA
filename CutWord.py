# -*- coding: utf-8 -*-
import ReadFile
import jieba
import jieba.posseg as psg # 分词词性
from collections import Counter


# 分词
def CutWord(TQA):
    # 去除空格
    for QA in TQA:
        QA.question = QA.question.replace(" ", "")
        for i in range(len(QA.answer)):
            QA.answer[i] = QA.answer[i].replace(" ", "")
    for QA in TQA:
        QA.question = ','.join(jieba.cut(QA.question))
        for i in range(len(QA.answer)):
            QA.answer[i] = ','.join(jieba.cut(QA.answer[i]))
    return TQA

if __name__ == "__main__":
    filename = 'develop.data'
    TQA = ReadFile.preprocess_data(filename)  # 获取预处理数据结果
    TQA = CutWord(TQA)
    for QA in TQA:
        print(QA.question)
        print("\n")
        for answer in QA.answer:
            print(answer)
            print("\n")
