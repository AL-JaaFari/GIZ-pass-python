# VS code IDE
# According to Wikipedia 
# [“A palindrome is a word, number, phrase, or other sequences of characters 
# that reads the same backward as forward, such as madam, racecar.”]

#One way to solve is by :
# [1] creating all possible substrings
# [2] eliminate non-palindromic substring, 
# [3] find the maximum length among the remaining substring.
# for checking if a string is palindrome or not, compare the word with its reverse. 
#               If both are the same, >> the word is palindromic.

# index [0 1 2 3 4]
# str   [b a b a d]
# So:
# Define 2D matrix of order same as the length of string, Set the major diagonal elements as True, and otherwise with False

class Solution(object):
   def longestPalindrome(self, s):
      diagonal_elements = [[False for i in range(len(s))] for i in range(len(s))]
      for i in range(len(s)):
         diagonal_elements[i][i] = True
      max_length = 1
      start = 0
      for l in range(2,len(s)+1):
         for i in range(len(s)-l+1):
            end = i+l
            if l==2:
               if s[i] == s[end-1]:
                  diagonal_elements[i][end-1]=True
                  max_length = l
                  start = i
            else:
               if s[i] == s[end-1] and diagonal_elements[i+1][end-2]:
                  diagonal_elements[i][end-1]=True
                  max_length = l
                  start = i
      return s[start:start+max_length]
lps = Solution()

# TEST
print(lps.longestPalindrome("babad"))
print(lps.longestPalindrome("cbbd"))
print(lps.longestPalindrome("a"))
print(lps.longestPalindrome("ac"))