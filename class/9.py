class String:
    def get_String(self):
        s = input('please input your message :')
        return s

    def print_String(self):
        s = self.get_String()
        print(s.upper())


String().print_String()

