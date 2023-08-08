'''
This script demonstrates creation of objects manually without any pattern
'''
class English():
    def __init__(self, name):
        self.name = name

    def greet(self):
        return 'Hello ' + self.name + ' ! How are you Doing?'


class German():
    def __init__(self, name):
        self.name = name

    def greet(self):
        return 'Hallo ' + self.name + ' ! Wie Gehts?'


class Language():
    def __init__(self):
        pass 



def main():
    language = Language()
    lang_code = input("Enter your langugae : ")
    name = input("Enter your Name : ")

    if lang_code == "English":
        english = English(name)
        print(english.greet())
    elif lang_code == "German":
        german = German(name)
        print(german.greet())
    else:
        print("Language can be English and German!")



if __name__ == "__main__" :
    main()


    