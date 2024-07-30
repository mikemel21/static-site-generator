class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    '''return True if all properties of two TextNode objects are equal.'''
    def __eq__(self, otherNode):
        return self.text == otherNode.text and self.text_type == otherNode.text_type and self.url == otherNode.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def main():
    testNode = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(testNode)

if __name__ == "__main__":
    main()
