'''
This script demonstartes creation of objects using abstract factory pattern
there will be no difference in the object creation but they are being called within the factory method
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
    def __init__(self, language = 'English'):
        self.language = '{}()'.format(language)

    def greet(self,name):
        try:
            language_obj = eval(self.language)
            print(language_obj.greet(name))
        except NameError:
            print("Defaulting to Engligh!")
            print(English().greet(name))
        except Exception as e:
            print(e)


def main():
    
    lang_code = input("Enter your langugae : ")
    name = input("Enter your Name : ")

    language= LanguageFactory(lang_code)
    language.greet(name)



if __name__ == "__main__" :
    main()
