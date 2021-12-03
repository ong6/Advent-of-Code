# %%

def lengthOfLongestSubstring(s):
    repeat_check = []
    max_list = []
    curr_max = 0
    for key in s:
        print(max_list)
        if key not in repeat_check:
            repeat_check.append(key)
            curr_max += 1
        else:
            repeat_check = []
            repeat_check.append(key)
            max_list.append(curr_max)
            curr_max = 1
        
    max_list.append(curr_max)
    print(max(max_list))
        
input = "abcabcbb" #3
input2 = "bbbbb" #1
input3 = "pwwkew" #3
input4 = ""
input5 = " "
input6 = "dvdf"


# lengthOfLongestSubstring(input)
# lengthOfLongestSubstring(input2)
# lengthOfLongestSubstring(input3)
# lengthOfLongestSubstring(input4)
# lengthOfLongestSubstring(input5)
lengthOfLongestSubstring(input6)


# %%
