nums = [1,2,3,4,5,6]

#
# for num in nums:
#     print(num)


print(dir(nums))

# i_nums = nums.__iter__()

i_nums = iter(nums)
print(i_nums)

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration as e:
        print(e.__repr__())
        break



class MyAppRange:
    def __init__(self, start , end ):
        self.value = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return current


nums = MyAppRange(0,14)

print(nums)

for rec in nums:
    print(rec)

def MyAppCustrange(start, end):
    current = start
    while current < end:
        yield current
        current += 1


nums = MyAppCustrange(0,19)

print(nums)

for rec in nums:
    print(rec)


def fiba(number):
    result = []
    a = 0
    b =1
    count = 0
    while count < number:
        print(a)
        temp = a +  b
        a = b
        b = temp
        count += 1

def fiba_gen(number):
    a = 0
    b = 1
    count = 0
    while count <  number :
        yield a
        temp = a + b
        a = b
        b = temp
        count += 1

print("*" * 100 )
outer_rsults = fiba(10)
print(outer_rsults)
print("*" * 100 )
outer_rsults_2 = fiba_gen(10)
for rec in outer_rsults_2:
    print(rec)



class myAppFiba:
    def __init__(self, number):
        self.number = number
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.number:
            raise StopIteration
        return_value = self.a
        temp = self.a + self.b
        self.a = self.b
        self.b = temp
        self.count += 1
        return return_value

print("*" * 100 )
myAppFiba_1 = myAppFiba(10)
for rec in myAppFiba_1:
    print(rec)

print("*" * 100)