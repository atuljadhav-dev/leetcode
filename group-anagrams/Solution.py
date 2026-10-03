class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        def anagram(s1, s2):
            if len(s1)!=len(s2):
                return False
            req={}
            for ch in s1:
                req[ch]=req.get(ch, 0)+1
            required=len(req)
            form={}
            formed=0
            for ch in s2:
                if ch not in req:
                    return False
                form[ch]=form.get(ch, 0)+1
                if form[ch]==req[ch]:
                    formed+=1
            if formed==required:
                return True
            else:
                return False
        group=[]
        create=True
        for s in strs:
            if len(group)>0:
                for g in group:
                    if anagram (g[0],s):
                        g.append(s)
                        create=False
            if create:
                group.append([s])
            else:
                create=True
        return group