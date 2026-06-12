class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        stack = []

        for day , temp in enumerate(temperatures):


            while stack and temp > temperatures[stack[-1]]:
                past_day = stack.pop()

                result[past_day]= day - past_day

            stack.append(day)


        return result

