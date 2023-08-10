'''
This script demonstartes creation of objects using abstract factory pattern
there will be no difference in the object creation but they are being called within the factory method
'''
from typing import Type

class Language:
    def greet(self, name : str) -> str:
        raise NotImplementedError

class English(Language):
    def __init__(self):
        pass

    def greet(self,name):
        return 'Hello ' + name + ' ! How are you Doing?'


class German(Language):
    def __init__(self):
        pass

    def greet(self,name):
        return 'Hallo ' + name + ' ! Wie Gehts?'

class LanguageStore:
    def __init__(self, language_factory: Type[Language]):
        self.language = language_factory

    def get_language(self):
        lang = self.language()
        return lang


def main():
    try:
        lang_code = eval(input("Enter your langugae : "))
        name = input("Enter your Name : ")


        lang_store = LanguageStore(lang_code)
        language = lang_store.get_language()
        print(language.greet(name))
    except NameError:
        print('Language Translation not available, Try English or German!')
    except Exception as e:
        print(e)




if __name__ == "__main__" :
    main()