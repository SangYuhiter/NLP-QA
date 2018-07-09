# -*- coding:UTF-8 -*-

import ReadFile


# 统计问句单字字频，使用字典结构，若键不存在则添加键，并将键值设为1，若存在，则键值加1
def calculate_question_word_frequency(TQA):
    word_dict = {}
    for QA in TQA:
        for word in QA.question:
            if word in word_dict.keys():
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return word_dict


# 统计答句单字字频，同统计问句单字字频
def calculate_answer_word_frequency(TQA):
    word_dict = {}
    for QA in TQA:
        for answer in QA.answer:
            for word in answer:
                if word in word_dict.keys():
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    return word_dict


# 统计文本字频:N:连续字数
def calculate_data_word_frequency(TQA, N):
    # 去除空格
    for QA in TQA:
        QA.question = QA.question.replace(" ", "")
        for i in range(len(QA.answer)):
            QA.answer[i] = QA.answer[i].replace(" ", "")
    # 利用字典结构存储键及键值
    word_dict = {}
    for QA in TQA:
        # 一个字符串可分为有限个N连字符子串，个数：len(str)-N+1
        # 例:'abcde',N=3  'abc'/'bcd'/'cde'
        for i in range(len(QA.question)-N+1):
            word_num = N
            word = ''
            j = i
            while word_num > 0:
                word += QA.question[j]  # 添加包括当前位置的N个字符串
                j += 1
                word_num -= 1
            # 判断键是否在字典中
            if word in word_dict.keys():
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        for answer in QA.answer:
            for i in range(len(answer) - N + 1):
                word_num = N
                word = ''
                j = i
                while word_num > 0:
                    word += answer[j]
                    j += 1
                    word_num -= 1
                if word in word_dict.keys():
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    return word_dict

# 统计文本词频:N:连续词数
def calculate_data_words_frequency(TQA, N):
    # 利用字典结构存储键及键值
    word_dict = {}
    for QA in TQA:
        question_words = QA.question.split(',')
        for i in range(len(question_words) - N + 1):
            word_num = N
            word = ''
            j = i
            while word_num > 0:
                word += ' '
                word += question_words[j]  # 添加包括当前位置的N个字符串
                j += 1
                word_num -= 1
            # 判断键是否在字典中
            if word in word_dict.keys():
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        for answer in QA.answer:
            answer_words = answer.split(',')
            for i in range(len(answer_words) - N + 1):
                word_num = N
                word = ''
                j = i
                while word_num > 0:
                    word += ' '
                    word += answer_words[j]
                    j += 1
                    word_num -= 1
                if word in word_dict.keys():
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
    return word_dict

# 统计总字频
def calculate_word_total_frequency(word_dict):
    word_frequency = 0
    # 循环计数
    for word in word_dict:
        word_frequency += word_dict[word]
    return word_frequency


# 打印排序后的N连字符及其频数
def write_statistic_data(word_dict):
    for data in sorted(word_dict.items(), key=lambda k: -k[1], reverse=True):
        print(data)


if __name__ == "__main__":
    filename = 'training.data'
    TQA = ReadFile.preprocess_data(filename)  # 获取预处理数据结果
    # 测试代码，输出字符统计结果，N代表N连字符,ctrl+/注释或撤销注释
    # write_statistic_data(calculate_question_word_frequency(TQA))
    # write_statistic_data(calculate_answer_word_frequency(TQA))
    write_statistic_data(calculate_data_word_frequency(TQA, 1))

