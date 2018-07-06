评测工具使用方法：

	工具名: evaluation.python，用于计算结果的MAP/ACC@1值，python版本为3.0以上

	命令: 'python evaluation.py QApairFile scoreFile outputFile'

	参数解释:
		QApairFile: 问答对文件
		scoreFile: 分数文件
		outputFile: 评测结果输出文件

	其中分数文件格式如下:
		0.2343556
		0.3434554
		0.5634232
		0.2324467
		0.1283477
		1.2384834
		0.4754545

	每行仅包含一个分数，表示问题和候选句之间的相关度。这些分数将会被评测工具用来对问题的候选句进行排序。
	请小心确认：问答对文件的行与分数文件的行保持对应，且他们的行数应相同。


