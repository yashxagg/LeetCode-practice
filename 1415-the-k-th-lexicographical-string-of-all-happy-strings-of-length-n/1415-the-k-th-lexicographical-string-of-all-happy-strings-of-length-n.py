class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.result = ""
        self.count = 0

        def backtrack(current_string):
            if self.count == k:
                return
            
            if len(current_string) == n:
                self.count += 1
                if self.count == k:
                    self.result = current_string
                return
            
            for char in ['a','b','c']:
                if not current_string or current_string[-1] != char:
                    backtrack(current_string + char)
        
        backtrack("")
        return self.result