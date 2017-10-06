class MathDojo(object):
    def __init__(self):
        self.value = 0
        
    def add(self, *num):
        for i in num:
            if type(i) == list:
                for j in i:
                    self.value += j
            elif type(i) == tuple:
                for j in i:
                    self.value += j
            else:
                self.value += i
        return self

    def subtract(self, *num):
        for i in num:
            if type(i) == list:
                for j in i:
                    self.value -= j
            elif type(i) == tuple:
                for j in i:
                    self.value -= j
            else:
                self.value -= i
        return self


md = MathDojo()
md.add(2).add(2,5).subtract(3,2)
print md.value

md.value = 0

md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3])
print md.value

md.value = 0

md.add([1], 3,4).add((3,5,7,8), [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3])
print md.value