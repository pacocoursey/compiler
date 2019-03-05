"""
Classes that represent grammar rules for our Parse Tree.
"""


def parseToken(desc, content="", children=[]):
    """Parse a token into the relevant class."""

    if desc == "program":
        return Program(children)
    if desc == "functionDeclaration":
        return FunctionDeclaration(children)
    if desc == "returnStatement":
        return ReturnStatement(children)
    if desc == "typeSpecifier":
        return TypeSpecifier(content)
    if desc == "ID":
        return Identifier(content)
    if desc == "constNum":
        return ConstNum(content)
    if desc == "varDec":
        return varDec(children)
    if desc == "assignment":
        return assignment(children)

    return GeneralNode(content, children)


def printPrefix(level):
    """Print a prefix level deep for pretty printing."""

    for _ in range(level):
        print("  ", end=" ")
    print("| - ", end=" ")


class Node:
    """General parse tree node class"""

    def __init__(self):
        pass

    def __str__(self):
        return self.__class__.__name__

    def print(self, level=0):
        """
        General node print method.
        First, print the class name, then print all it's children.

        This method is overriden at lower level nodes like NUMCONST.
        """

        printPrefix(level)
        print(self.__class__.__name__)

        for child in self.children[0]:
            child.print(level + 1)


class Program(Node):
    """Program node."""

    def __init__(self, *children):
        self.children = children


class FunctionDeclaration(Node):
    """Function declaration node."""

    def __init__(self, *children):
        self.children = children


class TypeSpecifier(Node):
    """Type specifier node."""

    def __init__(self, value):
        self.value = value

    def print(self, level=0):
        printPrefix(level)
        print(f"{self.__class__.__name__}: {self.value}")


class ReturnStatement(Node):
    """Return statement node."""

    def __init__(self, *children):
        self.children = children

    def print(self, level=0):
        printPrefix(level)
        print(f"{self.__class__.__name__}")
        for child in self.children[0]:
            child.print(level + 1)


class ConstNum(Node):
    """Number constant node."""

    def __init__(self, value):
        self.value = value

    def print(self, level=0):
        printPrefix(level)
        print(f"{self.__class__.__name__}: {self.value}")


class Identifier(Node):
    """ID node."""

    def __init__(self, value):
        self.value = value

    def print(self, level=0):
        printPrefix(level)
        print(f"{self.__class__.__name__}: {self.value}")


class GeneralNode(Node):
    """General node (fallback)."""

    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

    def print(self, level=0):
        # if len(self.children) == 0:
        #    printPrefix(level)
        #    print(self.value)
        # else:
        for child in self.children:
            child.print(level)
