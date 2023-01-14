
class Size:
    def __init__(self, width=144, height=144):
        # Initialize parameters
        self.width = width
        self.height = height

    def as_tuple(self):
        return (self.width, self.height)

