import os
class DataSource():

    def read_data(self) -> str:
        pass

    def write_data(self, data: str) -> None:
        pass
    
class FileDataSource(DataSource):
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def read_data(self) -> str:
        with open(self.filename, "r") as file:
            return file.read()
    def write_data(self, data: str) -> None:
        with open(self.filename, "w") as file:
            file.write(data)

class DataSourceDecorator(DataSource):
    def __init__(self, source: DataSource) -> None:
        self.source = source

    def read_data(self) -> str:
        return self.source.read_data()

    def write_data(self, data: str) -> None:
        return self.source.write_data(data)
    
class EncryptionDecorator(DataSourceDecorator):
    def decrypt(self, data: str) -> str:
        return data
    
    def encrypt(self, data: str) -> str:
        return data
    
    def read_data(self) -> str:
        data = self.source.read_data()
        return self.decrypt(data)
        
    def write_data(self, data: str) -> None:
        return self.source.write_data(self.encrypt(data))

class CompressionDecorator(DataSourceDecorator):
    def compress(self, data: str) -> str:
        return data
    
    def decompress(self, data: str) -> str:
        return data

    def read_data(self) -> str:
        data = self.source.read_data()
        return self.decompress(data)
    
    def write_data(self, data: str) -> None:
        return self.source.write_data(self.compress(data))
    

if __name__ == "__main__":
    data_source = FileDataSource("data.txt")
    data_source = EncryptionDecorator(data_source)
    data_source.write_data("Hello, world!")
    print(data_source.read_data())

    # delete data.txt
    os.remove("data.txt")