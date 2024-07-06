# Generator


# def tub_son(a):
#     x = 2
#     while x < a:
#         total = True
#         i = 2
#         while i <=(x ** 0.5):
#             if x % i == 0:
#                 total = False
#                 break
#             i += 1
#         if total:
#             yield x
#         x += 1
#
#
# for tub in tub_son(int(input("Enter a number: "))):
#     print(tub, "tub son")


# Iterator

class Tub_son:
    def __init__(self, tub):
        self.tub = tub
        self.y = 2

    def __iter__(self):
        return self

    def __next__(self):
        while self.y < self.tub:
            son = True
            for i in range(2, int(self.y ** 0.5) + 1):
                if self.y % i == 0:
                    son = False
                    break
            if son:
                sone = self.y
                self.y += 1
                return sone
            self.y += 1
        raise StopIteration


for tub in Tub_son(int(input("Tub number: "))):
    print(tub, "tub son")