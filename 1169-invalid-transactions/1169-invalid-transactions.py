class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        index=set()
        for i in range(len(transactions)):
            name,time,amount,city=transactions[i].split(",")
            if int(amount)>1000:
                index.add(i)
            for j in range(len(transactions)):
                if i==j:
                    continue
                name2,time2,amount2,city2=transactions[j].split(",")
                if name==name2 and city!=city2 and abs(int(time)-int(time2))<=60:
                    index.add(i)
                    break

        return [transactions[i] for i in index] 
        # transactions=sorted(transactions)
        # #print(transactions)
        # res=[]
        # stack=[]
        # for word in transactions:
        #     name,time,amount,city=list(map(str,word.split(",")))
        #     if int(amount)>1000:
        #         res.append(",".join([name,time,amount,city]))
        #     else:
        #         if stack and stack[-1][0]==name:
        #             if stack[-1][-1]!=city and abs(int(time)-int(stack[-1][1]))<60:
        #                 res.append(",".join(stack[-1]))
        #                 stack.pop()
        #                 res.append(",".join([name,time,amount,city]))
        #     stack.append([name,time,amount,city])

        # print(stack)
        # return res


