class Automaton:
    def __init__(self):
        self.sign = 1
        self.res = 0
        self.state = "start"
        self.table = {
            "start": ["start", "sign", "is_number", "end"],
            "sign": ["end", "end", "is_number", "end"],
            "is_number": ["end", "end", "is_number", "end"],
            "end": ["end", "end", "end", "end"]
        }
        self.INT_MAX = 2 ** 31 - 1
        self.INT_MIN = -2 ** 31

    def get_status(self, c):
        if c == " ":
            return 0
        elif c == "-" or c == "+":
            return 1
        elif c.isdigit():
            return 2
        return 3

    def process(self, c):
        self.state = self.table[self.state][self.get_status(c)]
        if self.state == "is_number":
            self.res = int(c) + self.res * 10
            self.res = min(self.res, self.INT_MAX) if self.sign == 1 else min(self.res, -self.INT_MIN)
        elif self.state == "sign":
            self.sign = 1 if c == "+" else -1
        # 其余情况不做处理

    def get_res(self):
        return self.sign * self.res


class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.process(c)
        return automaton.get_res()


if __name__ == '__main__':
    A = Solution()
    print(A.myAtoi("122w3"))
    print(A.myAtoi("4193 with words"))
    print(A.myAtoi("00000-42a1234"))
