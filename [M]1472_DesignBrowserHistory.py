class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.tracking = [homepage]
        self.cache = [homepage]
        

    def visit(self, url: str) -> None:
        self.tracking.append(url)
        self.cache = copy.deepcopy(self.tracking)
        return self.tracking[-1]


    def back(self, steps: int) -> str:
        if len(self.tracking) - steps < 1:
            steps = len(self.tracking) - 1
        if steps == 0:
            return self.tracking[-1]
        self.tracking = self.tracking[:-steps]
        return self.tracking[-1]
        

    def forward(self, steps: int) -> str:
        diff = len(self.cache) - len(self.tracking)
        if steps > diff:
            steps = diff
        print(steps, self.tracking, self.cache)
        self.tracking = self.cache[:len(self.tracking) + steps]
        return self.tracking[-1]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)