from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        visited.add("0000")
        queue = ["0000"]

        def add(code, index):
            return code[:index] + str(((int(code[index]) + 1) % 10)) + code[index + 1:]

        def sub(code, index):
            return code[:index] + str(((int(code[index]) - 1) % 10)) + code[index + 1:]

        def bfs(step=0):
            while queue:
                for _ in range(len(queue)):
                    node = queue.pop(0)

                    if node == target:
                        return step
                    elif node in deadends:
                        continue

                    for index in range(4):

                        after_add = add(node, index)
                        if after_add not in visited:
                            visited.add(after_add)
                            queue.append(after_add)

                        after_sub = sub(node, index)
                        if after_sub not in visited:
                            visited.add(after_sub)
                            queue.append(after_sub)
                step += 1
            return -1

        return bfs(step=0)
