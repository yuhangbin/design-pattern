
class Target:

    def request(self):
        return "Target: The default target's behavior."
    
class Adaptee:

    def special_request(self):
        return ".eetpadA eht fo roivaheb laicepS"
    
class Adapter(Target, Adaptee):

    def request(self):
        # This line does a few things:
        # 1. Calls special_request() from the Adaptee class to get the reversed string
        # 2. Uses [::-1] to reverse the string back to normal readable text
        # 3. Wraps it in an f-string with a label showing it was translated
        # This adapts the "weird" Adaptee interface into something the client expects
        return f"Adapter: (TRANSLATED) {self.special_request()[::-1]}"
    
def client_code(target: "Target") -> None:
    print(target.request())

if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. See, I don't understand it:")
    print(adaptee.special_request())
    print("\n")

    adapter = Adapter()
    print("Client: The Adapter works! See, I'm getting the Adaptee's weird translated text:")
    client_code(adapter)
    print("\n")