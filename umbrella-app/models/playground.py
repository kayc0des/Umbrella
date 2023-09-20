# playground file

fruits = ['apple', 'avocado', 'banana', 'cherry']

for fruit in fruits:
    print(fruit)

fruitList = [fruit for fruit in fruits if 'a' in fruit]
print(fruitList)

myDict = {'name':'John', 'age':40, 'gender':'male'}

for key, value in myDict.items():
    print(f"{key} = {value}")

# *args and **kwargs
# write a function to multiply two numbers

def multiply(num1, num2):
    return num1 * num2

print(multiply(10, 9))

def multiplyFunc(*args):
    result = 1
    if args:
        for arg in args:
            result = result * arg
        return result
    else:
        result = 0
        return result

print(multiplyFunc(3, 4, 5))


class User():

    def __init__(self, **kwargs):
        self.id = 89
        allowed_keys = {'name', 'email', 'username', 'location'} # Using a set because sets hold unique values which cannot be repeated
        if kwargs:
            #self.__dict__.update(kwargs)
            self.__dict__.update((key, value) for key, value in kwargs.items() if key in allowed_keys)
            
            #for key, value in kwargs.items():
            #    setattr(self, key, value)


user1 = User(name = 'Foo', lastName = 'Bar')
print(user1.name)
print(user1.__dict__)
