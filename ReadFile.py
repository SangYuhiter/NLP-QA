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

TQA = []
def preprocess_data():
    # 读取训练数据到列表list_training
    with open('training.data', 'r', encoding='UTF-8') as f_training:
        list_training = f_training.readlines()
    # 对每行数据处理
    for record in list_training:
        record = record.rstrip('\n')
        delete_str = ["、", "，", "。", "【", "】", "？", "：", "“", "”", "（", "）", "《", "》", "◆"]
        for dstr in delete_str:
            record = record.replace(dstr, " ")
        data = record.split('\t')

        # 每个QA
        QA = TrainQA()
        QA.question = data[0].rstrip()
        QA.answer.append(data[1].rstrip())
        QA.flag.append(data[2].rstrip())
        if len(TQA) == 0:
            TQA.append(QA)
            continue
        if TQA[len(TQA) - 1].question == QA.question:
            TQA[len(TQA) - 1].answer.append(data[1].rstrip())
            TQA[len(TQA) - 1].flag.append(data[2].rstrip())
        else:
            TQA.append(QA)


def write_preprocess_data(TQA):
    with open('preprocess.data', 'w', encoding='UTF-8') as f_preprocess:
        for QA in TQA:
            for i in range(0, len(QA.answer)):
                f_preprocess.write("%s\t%s\t%s\n" % (QA.question, QA.answer[i], QA.flag[i]))


def read_preprocess_data():
    with open('preprocess.data', 'r', encoding='UTF-8') as f_preprocess:
        list_preprocess = f_preprocess.readlines()
    for record in list_preprocess:
        record = record.rstrip('\n')
        data = record.split('\t')
        # 每个QA
        QA = TrainQA()
        QA.question = data[0].rstrip()
        QA.answer.append(data[1].rstrip())
        QA.flag.append(data[2].rstrip())
        if len(TQA) == 0:
            TQA.append(QA)
            continue
        if TQA[len(TQA) - 1].question == QA.question:
            TQA[len(TQA) - 1].answer.append(data[1].rstrip())
            TQA[len(TQA) - 1].flag.append(data[2].rstrip())
        else:
            TQA.append(QA)
    return TQA


# for test
preprocess_data()
TQA[0].showQA()
write_preprocess_data(TQA)


