class Pen:
    def write(self):
        print("Writing")

class Highlighter:
    def highlight(self):
        print("Highlighting")

class Marker(Pen, Highlighter):
    pass
marker = Marker()
marker.write()
marker.highlight()