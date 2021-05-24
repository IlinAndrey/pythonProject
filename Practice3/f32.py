class C32:
    def __init__(self):
        self.state = 'A'

    def rush(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'D':
            self.state = 'E'
            return 4
        if self.state == 'E':
            self.state = 'B'
            return 7
        if self.state == 'G':
            self.state = 'G'
            return 9
        return None

    def trash(self):
        if self.state == 'B':
            self.state = 'B'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'D'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 6
        if self.state == 'F':
            self.state = 'G'
            return 8
        return None
