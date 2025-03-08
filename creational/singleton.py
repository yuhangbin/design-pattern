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
    

# Two more classes using SingletonMeta
class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, connection_string):
        self.connection_string = connection_string
        
    def __str__(self):
        return f"Database connected to: {self.connection_string}"


class Logger(metaclass=SingletonMeta):
    def __init__(self, log_level):
        self.log_level = log_level
        self.logs = []
        
    def log(self, message):
        self.logs.append(message)
        
    def __str__(self):
        return f"Logger with level: {self.log_level}"


if __name__ == "__main__":
    # Testing original Singleton
    s1 = Singleton("Hello")
    s2 = Singleton("World")
    print("Original Singleton Test:")
    print(f"s1: {s1}")  # Will print "Hello"
    print(f"s2: {s2}")  # Will also print "Hello"
    print(f"s1 is s2: {s1 is s2}")  # Will print True
    
    # Testing DatabaseConnection singleton
    db1 = DatabaseConnection("mysql://localhost:3306")
    db2 = DatabaseConnection("postgres://localhost:5432")  # This connection string will be ignored
    print("\nDatabase Connection Test:")
    print(f"db1: {db1}")  # Will show mysql connection
    print(f"db2: {db2}")  # Will also show mysql connection
    print(f"db1 is db2: {db1 is db2}")  # Will print True
    
    # Testing Logger singleton
    logger1 = Logger("DEBUG")
    logger2 = Logger("INFO")  # This log level will be ignored
    logger1.log("First message")
    logger2.log("Second message")  # Will be added to the same logger instance
    print("\nLogger Test:")
    print(f"logger1: {logger1}")  # Will show DEBUG level
    print(f"logger2: {logger2}")  # Will also show DEBUG level
    print(f"logger1 is logger2: {logger1 is logger2}")  # Will print True
    print(f"Combined logs: {logger1.logs}")  # Will show both messages
