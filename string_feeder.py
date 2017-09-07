
class StringFeeder():
    def __init__(self, string):
        self._string = string

    def take_one(self):
        if self._string == '':
            return None

        char = self._string[0]

        self._string = self._string[1:]
        return char

    def peek_one(self):
        if self._string == '':
            return None
        else:
            return self._string[0]

    def take_next(self):
        char = self.take_one()
        if char is None: 
            return None
        
        while char.strip() == '':
            char = self.take_one()
            if char is None: 
                return None
            
        return char

    def peek_next(self):
        if self._string == '':
            return None
        else:
            while self._string[0].strip() == '':
                self.take_one()

            return self._string[0]


    
    
    
