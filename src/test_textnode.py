import unittest
from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is NOT a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2) 

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "https://boot.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertEqual(node, node2)

    def test_eq_url_false(self):
        node = TextNode("This is a text node", "bold", "https://shoe.dev")
        node2 = TextNode("This is a text node", "bold", "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode('This is a text node', 'bold', 'https://boot.dev')
        expected = "TextNode(This is a text node, bold, https://boot.dev)"
        self.assertEqual(expected, repr(node))
   

if __name__ == "__main__":
    unittest.main()
