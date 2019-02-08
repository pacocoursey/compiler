class Token:
    """
    A single token.

    Attributes:
        content: stores additional information if number/identifier/string
        rep: string representation of this token
    """

    def __init__(self, kind, content="", rep=""):
        self.kind = kind
        self.content = content if content else str(self.kind)
        self.rep = rep

    def __repr__(self):
        return self.content

    def __str__(self):
        return self.rep if self.rep else self.content


class TokenType:
    """
    A known token type (return, int, sizeof, etc...)

    Attributes:
        rep: The representation of this token in text, if it exists (i.e. 'int')
        type: The list to add this TokenType to (i.e. 'symbols')
    """

    def __init__(self, rep="", type=[]):
        self.rep = rep
        type.append(self)

        # Sort the list of this TokenType
        # NOTE: This is because we want to match longest matching tokens first.
        type.sort(key=lambda t: -len(t.rep))

    def __str__(self):
        return self.rep


# Have to avoid the following Python keywords...
# False     class       finally     is          return
# None      continue    for         lambda      try
# True      def         from        nonlocal    while
# and       del         global      not         with
# as        elif        if          or          yield
# assert    else        import      pass
# break     except      in          raise

symbols = []
keywords = []

# ========
# Variable
# ========

identifier = TokenType()
number = TokenType()
string = TokenType()
character = TokenType()
filename = TokenType()

# =======
# Symbols
# =======

# Blocks
openParen = TokenType("(", symbols)
closeParen = TokenType(")", symbols)
openCurly = TokenType("{", symbols)
closeCurly = TokenType("}", symbols)
openSquare = TokenType("[", symbols)
closeSquare = TokenType("]", symbols)

# Unary operations
ampersand = TokenType("&", symbols)
pipe = TokenType("|", symbols)
xor = TokenType("^", symbols)
complement = TokenType("~", symbols)

# Equality
lt = TokenType("<", symbols)
gt = TokenType(">", symbols)
ltoe = TokenType("<=", symbols)
gtoe = TokenType(">=", symbols)
doubleEquals = TokenType("==", symbols)
notEquals = TokenType("!=", symbols)

# Assignment
equals = TokenType("=", symbols)
plusEquals = TokenType("+=", symbols)
minusEquals = TokenType("-=", symbols)
starEquals = TokenType("*=", symbols)
slashEquals = TokenType("/=", symbols)
plusPlus = TokenType("++", symbols)
minusMinus = TokenType("--", symbols)

# Strings
doubleQuote = TokenType('"', symbols)
singleQuote = TokenType("'", symbols)

# Misc
comma = TokenType(",", symbols)
period = TokenType(".", symbols)
semicolon = TokenType(";", symbols)
backSlash = TokenType("\\", symbols)
arrow = TokenType("->", symbols)
pound = TokenType("#", symbols)


# =========
# Operators
# =========

# Sum operations
plus = TokenType("+", symbols)
minus = TokenType("-", symbols)

# Multiplication operations
star = TokenType("*", symbols)
slash = TokenType("/", symbols)
mod = TokenType("%", symbols)

# Boolean operations
boolAnd = TokenType("&&", symbols)
boolOr = TokenType("||", symbols)
boolNot = TokenType("!", symbols)
leftShift = TokenType("<<", symbols)
rightShift = TokenType(">>", symbols)

# ========
# Keywords
# ========

# Numbers

int = TokenType("int", keywords)
long = TokenType("int", keywords)
double = TokenType("int", keywords)
char = TokenType("char", keywords)
short = TokenType("short", keywords)
signed = TokenType("signed", keywords)
unsigned = TokenType("unsigned", keywords)
float = TokenType("float", keywords)

# Data types

struct = TokenType("struct", keywords)
enum = TokenType("enum", keywords)
union = TokenType("union", keywords)
record = TokenType("record", keywords)

# Flow control

ifKeyword = TokenType("if", keywords)
elseKeyword = TokenType("else", keywords)
whileKeyword = TokenType("while", keywords)
forKeyword = TokenType("for", keywords)
breakKeyword = TokenType("break", keywords)
continueKeyword = TokenType("continue", keywords)
returnKeyword = TokenType("return", keywords)

# Boolean

true = TokenType("true", keywords)
false = TokenType("false", keywords)

# Misc

static = TokenType("static", keywords)
sizeof = TokenType("sizeof", keywords)
typedef = TokenType("typedef", keywords)
const = TokenType("const", keywords)
extern = TokenType("extern", keywords)
auto = TokenType("auto", keywords)
