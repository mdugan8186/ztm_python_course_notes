# ==== under the hood of generators ===

# how a for loop works under the hood
def special_for(iterable):
    # the iter function will allow us to use the next function
    iterator = iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator) * 2)
        except StopIteration:
            break


special_for([1, 2, 3])

# the object exists in the same memory space even though we're looping through it

# iter()
# The iter() function returns an iterator object
# iter(object, sentinel)
# object	Required. An iterable object
# sentinel	Optional. If the object is a callable object the iteration will stop when the returned value is the same as the sentinel


# how ranges work under the hood
class MyGen():
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 10)
for i in gen:
    print(i)
