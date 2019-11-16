# -*- coding: utf-8 -*-
import sys
if __name__ == "__main__":    
    #读取工作数量和小伙伴数量
    temp = sys.stdin.readline().strip().split()
    jobs = int(temp[0])
    fris = int(temp[1])
    diff = []
    dic = {}
    #读取工作难度和报酬，创建字典
    for i in range(jobs):
        temp = sys.stdin.readline().strip().split()
        diff.append(temp[0])
        dic[temp[0]] = temp[1]
    #读取小伙伴能力
    fri = sys.stdin.readline().strip().split()
    for i in range(fris):
        money = 0
        j = 0
        for j in range(jobs):
            #如果伙伴能力大于工作难度且所给报酬高于前者
            if (int(fri[i]) >= int(diff[j])) and (money < int(dic[diff[j]])):
                    money = int(dic[diff[j]])
            continue
        print(money)
                