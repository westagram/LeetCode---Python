class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # Create a stack
        # Continuously push and pop items in stack until it's empty
        # Return True if the stack is empty, else False

        stack = []
        while len(pushed) != 0 or len(popped) != 0:
            if len(stack) == 0:
                if len(pushed) == 0:
                    return False
                stack.append(pushed.pop(0))
                continue
            if popped[0] == stack[-1]:
                stack.pop(-1)
                popped.pop(0)
            else:
                if len(pushed) == 0:
                    return False
                stack.append(pushed.pop(0))
        return True
