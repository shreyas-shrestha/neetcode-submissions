class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: #if length 0 or 1 just return the length
            return len(s)
        last_seen = {} # array to store when last seen
        longest = 1 #longest streak
        current_streak = 1 #current streak
        L = 0 #left pointer
        R = 1 #right pointer
        while s[R] == s[L]: #finding starting points of r and l (when not the same)
            R+=1
            if R >= len(s):
                return longest # if r is len(s) or somehow greater, then the entire s is the same letter and the longest is just 1 character
        L = R-1 #wherever repeats stop-1 is left
        last_seen[s[L]] = L #left added to when last seen 
        while R < len(s):
            if s[R] not in last_seen or last_seen[s[R]] < L: #either we have not seen this char or we saw it outside of our window
                last_seen[s[R]] = R #update when we saw
                current_streak+=1 #update our current streak
                if current_streak > longest: #possibly update our longest streak
                    longest = current_streak
                R+=1 #right pointer to next
            else:
                previous_L = L #store value of previous L index
                L = last_seen[s[R]] + 1 #new L index
                L_jump = L - previous_L #how much we jumped in our left pointer
                last_seen[s[R]] = R #update when we last saw this val
                current_streak = current_streak - L_jump + 1 #the streak is the streak minus the jump plus 1 cause we did see one more character
                R+=1 #r to the next
        return longest #return longest


            
                
            




        