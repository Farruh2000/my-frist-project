class fibonacci():
    def __init__(self,step):
        self.start = 0
        self.total = 1
        self.step = step
        self.previous = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.previous >= self.step:
            raise StopIteration

        self.previous +=1
        fib=self.start

        temp=self.start
        self.start=self.total
        self.total=temp+self.total

        return fib


fib=fibonacci(15)
for i in fib:
    print(i)