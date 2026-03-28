class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        lu={c:i for i,c in enumerate(s)}
        used=set()
        stack=[]
        for i,c in enumerate(s):
            if c not in used:
                while stack and c<stack[-1] and lu[stack[-1]]>i:
                    used.remove(stack.pop())
                stack.append(c)
                used.add(c)
        return "".join(stack) 