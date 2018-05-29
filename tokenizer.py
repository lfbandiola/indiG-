import sys
import ply.lex as lex
from ply.lex import TOKEN

# List of tokens
tokens = (
            'NUMBER',
            'NAME',
            'ID',
            'NUM_CONST',
            'OPERATOR',
            'EXPR',
            'VAR',
            'COND',
            'PLUS',
            'MINUS',
            'TIMES',
            'DIVIDE',
            'MOD',
            'LPAREN',
            'RPAREN',
            'LBRACE',
            'RBRACE',
            'SEMICOLON',
            'COMMA',
            'ASSIGN',
            'AND',
            'OR',
            'NOT',
            'LESS',
            'GREATER'
        )

# Regular expression rules for simple tokens
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_SEMICOLON = r';'
t_COMMA = r','
t_ASSIGN = r'='
t_AND = r'&'
t_OR = r'\|'
t_NOT = r'!'
t_LESS = r'<'
t_GREATER = r'>'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

# Ignore whitespaces
t_ignore  = ' \t'

# RegExp for comments: No return value. Token discarded.
def t_COMMENT(t):
    r'\#.*'
    pass

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Match the first quotes for strings
def t_STRING(t):
    r'[\"\']'
    t.lexer.begin('str')
    t.lexer.str_start = t.lexer.lexpos
    t.lexer.str_marker = t.value

def t_STRING_END(t):
    r'[\"\']'

    if t.lexer.str_marker == t.value:
        t.type = 'STRING'
        t.value = t.lexer.lexdata[t.lexer.str_start:t.lexer.lexpos - 1]
        t.lexer.begin('INITIAL')
        return t

# Error handling rule
def t_error(t):
    print("Illegal character: '%s' \n\tLine number: %d" % (t.value[0], t.lineno))
    t.lexer.skip(1)

# Defining a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Build the lexer
lexer = lex.lex()

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE')
    )

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
# from calclex import tokens

names = {}

def p_statement_assign(t):
    'statement : NAME ASSIGN expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]
    print('add')
    print(p[0])
    print(p[1])
    print(p[3])

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]
    print('minus')

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]
    print('times')

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]
    print('divide')

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Syntax error")


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
while True:
    tok = lexer.token()
    if not tok: 
        break
    print(tok)

# while True:
#     try:
#         s = input('calc >')
#     except EOFError: break
parser.parse(data)