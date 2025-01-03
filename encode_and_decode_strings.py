class Solution:

    # Time: O(M) where M is the sum of lengths of all strings
    # Space: O(1)
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    # Time: O(M)
    # Space: O(1)
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            # keep reading the number to understand the length of the next string, stop when we hit a pound sign
            while s[j] != "#":
                j += 1
            # length of the next string 
            length = int(s[i:j])
            # string starts from the character after the pound sign and has a size of 'length'
            res.append(s[j + 1 : j + 1 + length])
            # character next to the end of this string marks the beginning of the next encoded value
            i = j + 1 + length
        return res

# Note: We cannot simply use a pound sign because the input strings can have any ascii characters. If the string contains a pound sign itself, the decode method won't be able to understand the original string. Similarly, we cannot just prefix the strings with their lengths because the strings themselves can have numeric values too.
# Thus, we are using length to determine the size of the next string and then another delimiter pound so that we can ensure that we can decode any string irrespective of what they contain.
# Example: ['leet', 'coding', '45', '#abc'] will be encoded to '4#leet6#coding2#454##abc'
