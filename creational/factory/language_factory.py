'''
This script demonstrates creation of objects using factory pattern
'''
class English():
    def __init__(self):
        pass

    def greet(self,name):
        return 'Hello ' + name + ' ! How are you Doing?'


class German():
    def __init__(self):
        pass

    def greet(self,name):
        return 'Hallo ' + name + ' ! Wie Gehts?'


class LanguageFactory():

    def create_language(self,language):
        if language == 'German':
            return German()
        else:
            return English()




def main():
    language_factory = LanguageFactory()
    lang_code = input("Enter your langugae : ")
    name = input("Enter your Name : ")

    greeter = language_factory.create_language(lang_code)
    print(greeter.greet(name))



if __name__ == "__main__" :
    main()


    