# Abstract Class to
class VirtualizedInstanceInterface:
    __mime_type = 'virtualized_instance/interface'
    __description = None

    def __init__(self):
        print(f'Hi')

    def getMimeType(self) -> str:
        return self.__mime_type

    def getDescription(self) -> str:
        return self.__description


