class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map_dict = {')':'(',']':'[','}':'{'}


        for ele in s:
            if ele in map_dict and stack:
                top_ele = stack.pop()

                if top_ele != map_dict[ele]:
                    return False
            else:
                stack.append(ele)

        return len(stack)==0