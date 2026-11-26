class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans= []
        ansdict = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            ansdict[key].append(word)
        for i,j in ansdict.items():
            ans.append(ansdict[i])
        return ans
        
        



            

        
        

            

        