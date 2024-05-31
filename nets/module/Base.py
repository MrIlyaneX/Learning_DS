class Base:
    def __init__(self):
        raise NotImplementedError()

    def forward(self):
        pass

    def backward(self):
        raise NotImplementedError()
