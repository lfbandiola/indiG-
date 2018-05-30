import sys
import ply.lex as lex
from ply.lex import TOKEN

# ----------------------------------------------------------------------------------- LEXICAL ANALYZER
# List of tokens
reserved = {
    'print': 'PRINT',
    'if':    'IF',
    'else':  'ELSE',
    'true':  'TRUE',
    'false': 'FALSE',
}

tokens = (
            'NUMBER',
            'VAR',
            'RESERVED',
    # arithmetic
            'PLUS',
            'MINUS',
            'TIMES',
            'DIVIDE',

            'LPAREN',
            'RPAREN',
            'ASSIGN',
        )

tokens = list(reserved.values()) + list(tokens)

# Regular expression rules for simple tokens
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_ASSIGN = r'='
t_VAR    = r'[a-z][a-zA-Z0-9_]*'

# Ignore whitespaces
t_ignore  = ' \t'

def t_RESERVED(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for reserved words
    t.type = reserved.get(t.value.lower(), 'VAR')
    return t

# RegExp for comments: No return value. Token discarded.
def t_COMMENT(t):
    r'\#.*'
    pass

# Values for arithmetic: Integer only
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Defining a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character: '%s' \n\tLine number: %d" % (t.value[0], t.lineno))
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

<<<<<<< HEAD
# ---------------------------------------------end of lexer-------------------------------------------------------------

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE')
    )

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
# from calclex import tokens
names = { }
=======
# ---------------------------------------------------------------------- GRAMMAR / BNF
import ply.yacc as yacc

# left asscociativity to fix the ambiguity of the operators with equal precedence
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE')
)
>>>>>>> 235a9d6046a3a1b67ed438d0093a1694e0649a09

variables = {}
def p_statement_assign(t):
<<<<<<< HEAD
    'statement : NAME ASSIGN expression'
    names[t[1]] = t[3]
    print("Result: ", names[t[1]])
=======
    'statement : VAR ASSIGN expression'
    variables[t[1]] = t[3]
    print(t[3])
>>>>>>> 235a9d6046a3a1b67ed438d0093a1694e0649a09

def p_statement_expr(t):
    'statement : expression'

def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]
<<<<<<< HEAD
    print("Result: ", p[0])
=======
>>>>>>> 235a9d6046a3a1b67ed438d0093a1694e0649a09

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]
<<<<<<< HEAD
    print("Result: ", p[0])
=======
    print(p[0])
>>>>>>> 235a9d6046a3a1b67ed438d0093a1694e0649a09

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]
<<<<<<< HEAD
    print("Result: ", p[0])
=======
    print(p[0])
>>>>>>> 235a9d6046a3a1b67ed438d0093a1694e0649a09

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_print_var(p):
    'print_stmt : PRINT LPAREN VAR RPAREN'
    print("HELLO")

def p_print_expr(p):
    'print_stmt : PRINT LPAREN expression RPAREN'
    print(p[2])

def p_error(p):
    print("Syntax error!\t Line Number: ", p)


# ---------------------------------------------------------------------- MAIN
parser = yacc.yacc()

# getting the file input from cmd
try:
    file_input = sys.argv[1];
    pass
except Exception as e:
    print("Missing file input!")
    print("Try this: python main.py <filename>")
    sys.exit()

# Open the input file.
f = open(file_input, 'r')
data = f.read()
f.close()

# Build the lexer
lexer.input(data)
print("TOKENS:")
while True:
    tok = lexer.token()
    if not tok: 
        break
    print("\t",end="")
    # print(tok)
    print(tok.type, ": ", tok.value)

print("\nEVALUATION:")

# while True:
#     try:
#         s = input('calc >')
#     except EOFError: break
parser.parse(data)


# ---------------------------------------------------------------------------
# NOTES:
# LexToken(%s,%r,%d,%d)' % (self.type, self.value, self.lineno, self.lexpos)
#    token()          -  Get the next token
#    lineno           -  Current line number
#    lexpos           -  Current position in the input string
# -----------------------------------------------------------------------------