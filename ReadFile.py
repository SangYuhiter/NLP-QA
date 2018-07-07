# -*- coding: utf-8 -*-


# QA结构
class TrainQA(object):
    def __init__(self):
        self.question = ''  # 存储问题字符串
        self.answer = []    # 存储答句序列
        self.flag = []      # 存储相应答句的得分

    # 打印QA
    def showQA(self):
        print('%s\n' % (self.question))
        for i in range(0, len(self.answer)):
            print("%s\t%s\n" % (self.answer[i], self.flag[i]))


TQA = []    # TQA结构，存储QA


# 预处理数据：读入数据，写入特定的数据结构，去除特殊字符，去除首尾空格
def preprocess_data():
    # 读取训练数据到列表list_training
    with open('training.data', 'r', encoding='UTF-8') as f_training:
        list_training = f_training.readlines()

    # 对每行数据处理
    for record in list_training:
        record = record.rstrip('\n')    # 去除换行符
        # 特殊字符集
        delete_str = ["、", "，", "。", "【", "】", "？", "：", "“", "”", "（", "）", "《", "》", "◆", "；"]
        for dstr in delete_str:
            record = record.replace(dstr, " ")  # 用空格替换
        data = record.split('\t')   # 以制表符进行切分
        # 每个QA
        QA = TrainQA()
        QA.question = data[0].rstrip()      # 去除字符串首尾空格
        QA.answer.append(data[1].rstrip())
        QA.flag.append(data[2].rstrip())
        # TQA为空--添加QA
        if len(TQA) == 0:
            TQA.append(QA)
            continue
        # TQA最后一个QA的question域与当前将输入的QA的question域相同--添加answer和对应的flag
        if TQA[len(TQA) - 1].question == QA.question:
            TQA[len(TQA) - 1].answer.append(data[1].rstrip())
            TQA[len(TQA) - 1].flag.append(data[2].rstrip())
        # 上一个QA输入结束--添加下一个QA
        else:
            TQA.append(QA)


# 将预处理完成的数据写入preprocess.data
def write_preprocess_data(TQA):
    with open('preprocess.data', 'w', encoding='UTF-8') as f_preprocess:
        for QA in TQA:
            for i in range(0, len(QA.answer)):
                f_preprocess.write("%s\t%s\t%s\n" % (QA.question, QA.answer[i], QA.flag[i]))


# 将preprocess.data的数据读出到特定的数据结构TQA
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


# 测试代码，输出每个QA，将预处理的结果写到preprocess.data,ctrl+/注释或撤销注释
# preprocess_data()
# TQA[0].showQA()
# write_preprocess_data(TQA)
