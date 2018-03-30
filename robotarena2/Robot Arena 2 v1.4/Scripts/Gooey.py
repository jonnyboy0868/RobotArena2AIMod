import plus

class Plain(object):
    def __init__(self, name, x, y, w, h):
        self.window = plus.addWindow(name, x, y, w, h)

        self.controls = {}

    def addText(self, name, x, y, w, h):
        text = plus.addText(self.window, x, y, w, h)
        self.controls[name] = text
        return text

    def get(self, name):
        return self.controls[name]
