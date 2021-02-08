patterns = {}
messages = {}
class SetupStatement:
    def __init__(self, pattern, FriendlyName, name):
        self.pattern = pattern
        patterns[name] = pattern
        messages[name] = self.__class__
        self.FriendlyName = FriendlyName
        self.name = name
