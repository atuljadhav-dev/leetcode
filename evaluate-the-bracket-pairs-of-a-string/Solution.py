class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledge = dict(knowledge)
        result = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == "(":
                j = s.find(")", i + 1)#add i+1 for start search from 
                if j != -1:#if there is no closing parenthesis
                    key = s[i + 1 : j]
                    result.append(knowledge.get(key, "?"))
                    i = j + 1
                else:
                    result.append(s[i:])
                    break
            else:
                result.append(s[i])
                i += 1

        return "".join(result)
