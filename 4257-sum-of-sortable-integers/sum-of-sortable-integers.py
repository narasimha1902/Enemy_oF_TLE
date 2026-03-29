class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        div=[]
        n=len(nums)
        for i in range(1,int(n**(0.5))+1):
            if n%i==0:
                div.append(i)
                if i!=n//i:
                    div.append(n//i)
        sn=sorted(nums)
        ans=0
        for k in div:
            ok=True
            for i in range(0,n,k):
                bs=nums[i:i+k]
                osb=sn[i:i+k]
                if sorted(bs)!=osb:
                    ok=False
                    break
                s1='*'.join(map(chr,bs))
                s2='*'.join(map(chr,sorted(bs)))
                s2=s2+"*"+s2
                if s1 not in s2:
                    ok=False
                    break
            if ok:
                ans+=k
        return ans
