class HelloWorld:
    def __init__(self, message="Hello, World!"):
        self.message = message

    def display_message(self):
        print(self.message)


# Example usage
if __name__ == "__main__":
    hello = HelloWorld()  # Create an instance with the default message
    hello.display_message()  # Display the message

    custom_hello = HelloWorld("Hi there, Pythonista!")  # Create an instance with a custom message
    custom_hello.display_message()  # Display the custom message