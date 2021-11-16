#   Encapsulation is implmeneted by creating a protected or private methor or property
class Protected:
    def __init__(self):
        #   Protected is prefixed with a single underscore
        self._protectedVar = 0
        #   Private is prefixed with a double underscore
        self.__privateVar = 12

    #   Private is harder to access but can still be done
    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private
              

obj = Protected()
print(obj._protectedVar)
#   Protected variables could still be modified
obj._protectedVar = 34
print(obj._protectedVar)

obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()

                 
