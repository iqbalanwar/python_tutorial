# Classes and Objects Lesson

class Duck:
    # class variables are called properties
    sound = 'Quaaack'
    walking = 'Walks like a duck'

    # functions are called methods
    # first argument in methods is always self
    # self is python's version of 'this'
    # it references the object itself
    def quack(self):
        # print('Quaaack!')
        print(self.sound)
    
    def walk(self):
        # print('Walks like a duck.')
        print(self.walking)

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()