
# Singleton class
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
    

class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
    

if __name__ == "__main__":
    s1 = Singleton("Hello")
    s2 = Singleton("World")
    if s1 == s2:
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
