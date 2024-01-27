class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        arr = []
        flag= 0
        counter = 0
        for i in range(0,numRows):
            arr.append("")
        temp = ""
        if numRows < 2:
            return s
        else:
            for z in range(0,len(s)):
                if flag == 0:
                    arr[counter]+=s[z]
                    counter+=1
                    
                else:
                    arr[counter]+=s[z]
                    counter=counter-1 
                if counter ==numRows-1:
                    flag=1
                if counter == 0:
                    flag=0
        for f in arr:
            temp+=f
        return temp
sol = Solution()
print(sol.convert('PAYPALISHIRRETAALPHABET',3))
