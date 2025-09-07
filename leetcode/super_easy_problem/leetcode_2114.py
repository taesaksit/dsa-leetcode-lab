from typing import List

class Solution:
    def mostWordsFoundByTae(self, sentences: List[str]) -> int:
        stack = []
        for i in sentences:
            stack.append(len(i.split(" ")))
       
        return  max(stack)
    
    def mostWordsFoundByOther(self, sentences: List[str]) -> int:
        ans = 0
        for i in sentences:
            size = len(i.split(" "))
            if size > ans:
                ans = size
        print(ans)
        return  size
        
sentences = ["w jrpihe zsyqn l dxchifbxlasaehj","nmmfrwyl jscqyxk a xfibiooix xolyqfdspkliyejsnksfewbjom","xnleojowaxwpyogyrayfgyuzhgtdzrsyococuqexggigtberizdzlyrdsfvryiynhg","krpwiazoulcixkkeyogizvicdkbrsiiuhizhkxdpssynfzuigvcbovm","rgmz rgztiup wqnvbucfqcyjivvoeedyxvjsmtqwpqpxmzdupfyfeewxegrlbjtsjkusyektigr","o lgsbechr lqcgfiat pkqdutzrq iveyv iqzgvyddyoqqmqerbmkxlbtmdtkinlk","hrvh efqvjilibdqxjlpmanmogiossjyxepotezo","qstd zui nbbohtuk","qsdrerdzjvhxjqchvuewevyzlkyydpeeblpc"]
sol = Solution()
sol.mostWordsFoundByOther(sentences)