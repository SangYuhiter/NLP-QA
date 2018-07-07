import ReadFile
import DataStatistics
import math


# 获取N连字符串字频
def get_N_word_frequency(N):
    word_dict = DataStatistics.calculate_data_word_frequency(N)
    return word_dict


# N_gram_QA_frequency结构，存储句子相似度结果
class N_gram_QA_frequency(object):
    def __init__(self):
        self.question = 0   # 问题统计概率
        self.answer = []    # 答句统计概率
        self.flag = []      # 答句得分估计
        self.N = 0          # 标识N连


# 计算N-gram句子概率
def calculate_N_gram_sentence_frequency(sentence, N):
    sentence_frequency = 0
    for i in range(len(sentence) - N + 1):
        word_num = N
        word = ''
        j = i
        while word_num > 0:
            word += sentence[j]
            j += 1
            word_num -= 1
        # 计算公式log加
        sentence_frequency += math.log(word_dict[word]/word_frequency)
    return sentence_frequency


# 计算QA的问句答句频率
def calculate_QA_sentence_frequency(N):
    N_gram_TQA_frequency = []   # 存储所有QA的概率值
    for QA in TQA:
        QA_frequency = N_gram_QA_frequency()    # 新建数据结构N_gram_QA_frequency存储一个QA的概率值
        QA_frequency.question = calculate_N_gram_sentence_frequency(QA.question, N)     # 问句计算
        QA_answer_frequency = []
        for answer in QA.answer:
            QA_answer_frequency.append(calculate_N_gram_sentence_frequency(answer, N))  # 答句计算
        QA_frequency.answer = QA_answer_frequency
        QA_frequency.N = N
        N_gram_TQA_frequency.append(QA_frequency)
    return N_gram_TQA_frequency


# 计算问答句中最相似的句子：做差比较绝对值最小的，返回索引
def find_similarity_sentence(N_gram_QA_frequency):
    diff = []
    for answer_frequency in N_gram_QA_frequency.answer:
        diff.append(math.fabs(answer_frequency-N_gram_QA_frequency.question))
    return diff.index(min(diff))


# 打印QA的问答句频率
def write_QA_sentence_frequency(N,list):
    i = 0
    correctAnsNum = 0.0
    for QA in list:
        print("%d\t%s\n" % (i, TQA[i].question))
        index = find_similarity_sentence(QA)
        print("最相似的句子序号:%d\t频率：%f\t%s\t%s\n" % (index , QA.answer[index], TQA[i].answer[index], TQA[i].flag[index]))
        if TQA[i].flag[index] == '1':
            correctAnsNum += 1
        i += 1
    print("%d\t%f" % (N, correctAnsNum/i))


TQA = ReadFile.read_preprocess_data()   # 获取预处理数据结果
# 去除空格
for QA in TQA:
    QA.question = QA.question.replace(" ", "")
    for i in range(len(QA.answer)):
        QA.answer[i] = QA.answer[i].replace(" ", "")
# 输出N连的几种情况
for N in range(1, 2):
    word_dict = get_N_word_frequency(N)
    # 获取总字频
    word_frequency = DataStatistics.calculate_word_total_frequency(word_dict)
    # 计算并输出N连情况下的问答情况：问句答句是否正确及正确率
    write_QA_sentence_frequency(N, calculate_QA_sentence_frequency(N))



# DataStatistics.write_statistic_data(word_dict)
