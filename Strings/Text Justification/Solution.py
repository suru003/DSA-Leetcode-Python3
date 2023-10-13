'''
Link: https://leetcode.com/problems/text-justification/
Time Complexity: O(n)
Space Complexity: O(n)
'''
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer = []
        # Dummy val
        words.append("*" * 101)

        def getLine(parts, length):
            n = len(parts)
            if not n: return

            totalSpaces = maxWidth - length
            tabs = 0

            # n - 1 for not considering last word of the line
            if n - 1:
                tabs = totalSpaces // (n - 1)

            remained = totalSpaces - (tabs * (n - 1))

            temp = ""
            for index in range(n - 1):
                temp += parts[index] + " " * tabs
                if remained:
                    temp += " "
                    remained -= 1

            # last word as is
            temp += parts[-1]

            return temp + (" " * (maxWidth - len(temp)))

        used, lengths = 0, 0
        for i in range(len(words)):
            if lengths + len(words[i]) + used > maxWidth:
                line = getLine(words[i - used: i], lengths)
                if line: answer.append(line)

                used, lengths = 0, 0

            used += 1
            lengths += len(words[i])

        # last line
        lastLine = answer[-1]
        temp = lastLine.split(" ")
        lastLine = ""
        for word in temp:
            if word:
                lastLine += word + " "

        lastLine = lastLine.strip()
        answer[-1] = lastLine + " " * (maxWidth - len(lastLine))

        return answer
