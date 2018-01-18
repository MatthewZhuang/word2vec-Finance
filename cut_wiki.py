# -*- coding:utf-8 -*-
"""
 @description:
        
 @Time       : 18/1/4 下午11:19
 @Author     : guomianzhuang
"""
import os
import logging
import jieba
import sys


if __name__ == '__main__':
    program = os.path.basename("wiki")
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    # if len(sys.argv) < 3:
    #     print(globals()['__doc__'] % locals())
    #     sys.exit(1)
    # inp, outp = sys.argv[1:3]
    inp = "/Users/Matthew/Documents/workspace/NER-Master-zhuang/word2vec/wiki.zh.text.jian"
    outp = "/Users/Matthew/Documents/workspace/NER-Master-zhuang/word2vec/wiki.zh.text.jian.seg"
    i = 0

    with open(outp, mode='w') as f_o:
        with open(inp, mode='r') as f_r:
            for line in f_r.readlines():
                seg_list = jieba.cut(line.replace("\n", ""))
                content = " ".join(seg_list) + "\n"
                f_o.write(content)
                i += 1
                if i % 10000 == 0:
                    logger.info('Saved ' + str(i) + ' articles')
    logger.info('Finished ' + str(i) + ' articles')