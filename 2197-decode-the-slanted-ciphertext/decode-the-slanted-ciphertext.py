class Solution:
    def decodeCiphertext(self, et: str, row: int) -> str:
        out=""
        cs=len(et)//row
        for i in range(cs):
            r,c=0,i
            while r<row and c<cs:
                out+=et[cs*r+c]
                r+=1
                c+=1
        return out.rstrip()

