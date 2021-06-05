class Solution:
    def solve(self, votes):
        dic = {}
        for i in range(len(votes)):
            for j in range(1,len(votes[i])):
                if votes[i][j] not in dic:
                    dic[votes[i][j]] = 1
                else:
                    dic[votes[i][j]] += 1
        flag = any(v > 1 for v in iter(dic.values()))
        if flag == True:
            return True
        else:
            return False