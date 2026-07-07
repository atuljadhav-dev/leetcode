class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls=0
        cows=0
        coveredidx=[]
        ch={}
        for i in range(0, len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
                coveredidx.append(i)
                continue
            ch[i]=secret[i]
            
        for i in range(0, len(secret)):
            if i in coveredidx:
                continue
            keys = [k for k, v in ch.items() if v == guess[i]]
            if len(keys)>0:
                cows+=1
                ch.pop(keys[0])
        return str(bulls) +"A"+str(cows) +"B"