class Example:
    def __init__(self):
        print("Example instance.")

    def __del__(self):
        print("Destor called, Example deleted")

obj = Example()
del obj
