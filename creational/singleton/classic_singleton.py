'''
# Singleton classic pattern
simply use the static method for creating the getInstance method which has the ability to return the shared resource. 
We also make use of the so-called Virtual private Constructor to raise the exception against it although it is not much required.
'''
class Singleton:
 
    __shared_instance = None
 
    @staticmethod
    def getInstance():
        """Static Access Method"""
        if Singleton.__shared_instance == None:
            Singleton()
        return Singleton.__shared_instance
 
    def __init__(self):
        """virtual private constructor"""
        if Singleton.__shared_instance != None:
            raise Exception("This class is a singleton class !")
        else:
            Singleton.__shared_instance = self
 
 
# main method
if __name__ == "__main__":
 
    # create object of Singleton Class
    obj = Singleton()
    print(obj)
 
    # pick the instance of the class
    obj2 = Singleton.getInstance()
    print(obj2)

    # create object of Singleton Class will throw error
    #obj3 = Singleton()
    #print(obj3)

    # pick the instance of the class
    obj4 = Singleton.getInstance()
    print(obj4)