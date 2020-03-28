import re
def count(wordlist):
    dic = {}
    max = 0
    for s in wordlist:
        if len(s) > max:
            max = len(s)
        if s not in dic:
            dic[s] = 1
        else:
            dic[s] += 1
    return dic, max

def sort_d(dic):
    sorted_dic = sorted(dic.items(),key=lambda x: x[0])
    sorted_dic = sorted(sorted_dic, key=lambda x: x[1], reverse=True)
    return sorted_dic

def wordcount(filepath):
    with open(filepath) as f:
        wordlist = f.read().split()

    dic, max = count(wordlist)
    sorted_dic = sort_d(dic)
    for i in sorted_dic:
        print("%s %s" % ((i[0] + ":").ljust(max + 1), "*" * i[1]))
