class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        #index of prefix and suffix
        prefix = 0
        suffix = n-1
        while prefix < suffix:
            if s[prefix] != s[suffix]:
                break
            while prefix < suffix and s[prefix] == s[prefix+1]:
                prefix += 1
            while prefix < suffix and s[suffix] == s[suffix-1]:
                suffix -= 1
            #the current suffix and prefix matched, so we delete them
            #if same position all can be deleted
            if prefix == suffix: return 0
            #still character exist
            #check for suffix and prefix
            prefix += 1
            suffix -= 1
        #length of remaining word
        return suffix-prefix+1