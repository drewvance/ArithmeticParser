from string_feeder import StringFeeder

class Parser():
    def __init__(self, string):
        self._string_feeder = StringFeeder(string)
        self._digits = ['0','1','2','3','4','5','6','7','8','9']
        self._operators = ['+','-','/','*',]

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        require_end_parenthesis = False
        if self._string_feeder.peek_next() == '(':
            require_end_parenthesis = True
            self._string_feeder.take_one()

        first_value = self.parse_value()
        
        operator = self.parse_operator()
        second_value = self.parse_value()

        if require_end_parenthesis:
            end_char = self._string_feeder.take_next()
            if end_char != ')':
                raise Exception('Unexpected Char: ' + end_char)

        return self.perform_operation(first_value, operator, second_value)

    

    def parse_value(self):
        if self._string_feeder.peek_next() == '(':
            return self.parse_expression()
        else:
            is_negative = False
            if self._string_feeder.peek_next() == '-':
                is_negative = True
                self._string_feeder.take_one()
            
            value = ""
            while self._string_feeder.peek_one() in self._digits:
                value += self._string_feeder.take_one()
            
            if is_negative:
                return int(value) * -1
            else: 
                return int(value)

    def parse_operator(self):
        char = self._string_feeder.take_next()
        if char in self._operators:
            return char
        else:
            raise Exception("Unexpected Char: " + char)

    def perform_operation(self, first_value, operator, second_value):
        if operator == "+":
            return first_value + second_value
        elif operator == "-":
            return first_value - second_value
        elif operator == "/":
            return first_value / second_value
        elif operator == "*":
            return first_value * second_value
        else:
            raise Exception("Unexpected Operator: " + operator)

    
