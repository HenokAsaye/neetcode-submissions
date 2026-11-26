class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        a = defaultdict(int)
        b = defaultdict(int)

        for i in range(len(s)):
            a[s[i]]+=1
            b[t[i]] +=1
        print(a)
        print(b)
        for i,j in a.items():
            if a[i] != b[i]:
                return False
        return True

        