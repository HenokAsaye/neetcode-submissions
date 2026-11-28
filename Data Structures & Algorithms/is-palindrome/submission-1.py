class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = "".join(char for char in s if char.isalnum())
        i=0
        j=len(c)-1
        while i<j:
            if(c[j].lower() != c[i].lower()):
                print("j",c[j],"i",c[i])
                return False
            i+=1
            j-=1
        return True
        