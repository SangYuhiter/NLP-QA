# -*- coding: utf-8 -*-
class TrainQA(object):
    def __init__(self):
        self.question = ''
        self.answer = []
        self.flag = []

    def showQA(self):
        print('%s\n' % (self.question))
        for i in range(0, len(self.answer)):
            print("%s\t%s\n" % (self.answer[i], self.flag[i]))


# 读取训练数据到列表list_training
with open('training.data', 'r', encoding='UTF-8') as f_training:
    list_training = f_training.readlines()

TQA = []
#对每行数据处理
for record in list_training:
    record = record.rstrip('\n')
    delete_str = ["、", "，", "。", "【", "】", "？", "：", "“", "”", "（", "）", "《", "》", "◆"]
    for dstr in delete_str:
        record = record.replace(dstr, " ")
    data = record.split('\t')

    #每个QA
    QA = TrainQA()
    QA.question = data[0]
    QA.answer.append(data[1])
    QA.flag.append(data[2])
    if len(TQA) == 0:
        TQA.append(QA)
        continue
    if TQA[len(TQA) - 1].question == QA.question:
        TQA[len(TQA) - 1].answer.append(data[1])
        TQA[len(TQA) - 1].flag.append(data[2])
    else:
        TQA.append(QA)

with open('preprocess.data', 'w', encoding='UTF-8') as f_preprocess:
    for QA in TQA:
        f_preprocess.write("%s\n" % (QA.question))
        for i in range(0, len(QA.answer)):
            f_preprocess.write("%s\t%s\n" % (str(QA.answer[i]), str(QA.flag[i])))
        f_preprocess.write("\n")

TQA[0].showQA()
