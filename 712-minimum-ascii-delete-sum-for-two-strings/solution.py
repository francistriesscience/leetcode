class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        

        if m < n:
            return self.minimumDeleteSum(s2, s1)
            
        dp = [0] * (n + 1)
        
        for char1 in s1:
            prev_row_diag = 0 
            for j, char2 in enumerate(s2):
                temp = dp[j+1]
                
                if char1 == char2:
                    dp[j+1] = prev_row_diag + ord(char1)
                else:
                    dp[j+1] = max(dp[j+1], dp[j])
                    
                prev_row_diag = temp
        
        total_ascii = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        max_common_ascii = dp[n]
        
        return total_ascii - 2 * max_common_ascii
