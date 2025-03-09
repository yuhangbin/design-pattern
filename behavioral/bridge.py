
class Device:
    def __init__(self, name):
        self.name = name
        self.volume = 50
        self.channel = 1

    def set_volume(self, volume):
        self.volume = volume

    def set_channel(self, channel):
        self.channel = channel

    def get_volume(self):
        return self.volume

    def get_channel(self):
        return self.channel
    
    def __str__(self):
        return f"{self.name} (Volume: {self.volume}, Channel: {self.channel})"

class TV(Device):
    def __init__(self, name):
        super().__init__(name)

class Radio(Device):
    def __init__(self, name):
        super().__init__(name)

class Remote:
    def __init__(self, device: Device):
        self.device = device

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)
    
    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)
    
    def channel_up(self):
        self.device.set_channel(self.device.get_channel() + 1)
    
    def channel_down(self):
        self.device.set_channel(self.device.get_channel() - 1)
    
class AdvancedRemote(Remote):
    def mute(self):
        self.device.set_volume(0)

def client_code() -> None:
    tv = TV("TV")
    radio = Radio("Radio")

    print(tv)
    print("\n")
    print(radio)
    print("\n")

    remote = Remote(tv)
    remote.channel_up()
    remote.volume_up()
    print(tv)
    print("\n")
    remote = AdvancedRemote(radio)
    remote.mute()
    print(radio)
    print("\n")
if __name__ == "__main__":
    print("Client: Testing basic remote.\n")
    client_code()

    