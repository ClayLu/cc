#encoding=utf-8
import sys
sys.path.append("../")
import jieba

#fid = open('C:\Users\Lu\Desktop\eat.txt',  encoding='utf_8_sig' )
#jieba.load_userdict(fid)
#jieba.load_userdict("C:\Users\Lu\Desktop\eat.txt")
import jieba.posseg as pseg

test_sent = "喔，吃了阿堂鹹粥、安平豆花會哈哈哈!".decode('utf-8')
test_sent += "李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿".encode('utf-8')
words = jieba.cut(test_sent)
for w in words:
    print w

