import re

f = open('MiniLang.code', 'r')
program = f.read()

# Define regular expressions
RE_Keywords = r"\b(if|else|print|true|false)\b"
RE_DataType = r"\b(int|bool|char|string|double)\b"
RE_Comments = r"//.*?$"
RE_Operators = r"[\+\-\*/=]|==|!="
RE_Numbers = r"\b\d+\b"
RE_Boolean = r"\btrue\b|\bfalse\b"
RE_Identifiers = r"\b[a-zA-Z][a-zA-Z0-9]*\b"


# Combine all regular expressions into a single pattern
input_program_tokens = re.findall(r'//.*?$|/\*.*?\*/|\b\w+\b|[^\w\s]', program, re.MULTILINE|re.DOTALL)


# Tokenized Program output
print(input_program_tokens)


# To Categorize The Tokens
for token in input_program_tokens:
    if re.match(RE_Keywords, token):
        print(token, "-> Keyword")
    elif re.match(RE_DataType, token):
        print(token, "-> DataType")
    elif re.match(RE_Comments, token):
        print(token, "-> Comment")
    elif re.match(RE_Operators, token):
        print(token, "-> Operator")
    elif re.match(RE_Numbers, token):
        print(token, "-> Integer Literal")
    elif re.match(RE_Boolean, token):
        print(token, "-> Boolean Literal")
    elif re.match(RE_Identifiers, token):
        print(token, "-> Identifier")
    else:
        print(token, "-> Unknown Value")
