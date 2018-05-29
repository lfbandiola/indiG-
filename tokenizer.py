import sys
import ply.lex as lex
from ply.lex import TOKEN

# List of reserved words
# reserved = {
#     'print': 'PRINT',
#     'int': 'INT',
#     'float': 'FLOAT',
#     'bool': 'BOOLEAN',
#     'str': 'STRING',
#     'if': 'IF',
#     'elif': 'ELIF',
#     'else': 'ELSE',
#     'null': 'NULL',
#     'true': 'TRUE',
#     'false': 'FALSE',
# }

# # List of arithmetic operators
# arithmetic_op = {
#     '+': 'PLUS',
#     '-': 'MINUS',
#     '*': 'TIMES',
#     '/': 'DIVIDE',
#     '%': 'MOD',
# }

# # List of boolean operators
# boolean_op = {
#     '<': 'LESS',
#     '>': 'GREATER',
#     '>=': 'GREATER_EQ',
#     '<=': 'LESS_EQ',
#     '==': 'EQUAL',
#     '!=': 'NOT_EQ',
# }

# # List of bitwise operators
# bitwise_op = {
#     '&': 'AND',
#     '|': 'OR',
#     '!': 'NOT',
# }

# # List of special characters
# special_chars = {
#     '=': 'ASSIGN', 
#     '(': 'LPAREN',
#     ')': 'RPAREN',
#     '{': 'LBRACE',
#     '}': 'RBRACE',
#     ',': 'COMMA',
#     ';': 'SEMICOLON',
# }

# List of tokens
# edit Leica
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

# tokens = list(tokens)+ list(reserved.values())+ list(special_chars.values())+ list(arithmetic_op.values()) + list(boolean_op.values()) + list(bitwise_op.values())

# Regular expression rules for simple tokens
#edit Leica
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

# RegExp rules for alphanumerics
# def t_ID(t):
#     r'[a-zA-Z_][a-zA-Z_0-9]*'
#     # Check for reserved words
#     t.type = reserved.get(t.value.lower(), 'ID')
#     return t
 
 # RegExp for number constants
# r_NUMBER =  r'0 | [1-9]\d* | [0-9]+\.\d+'
# @TOKEN(r_NUMBER)
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

# @TOKEN(arithmetic_op)
# def t_ARITHMETIC_OP(t):
#     t.type = arithmetic_op.get(t.value, 'OPERATOR')
#     return t


# @TOKEN(boolean_op)
# def t_BOOLEAN_OP(t):
#     t.type = boolean_op.get(t.value, 'OPERATOR')
#     return t

# @TOKEN(bitwise_op)
# def t_BITWISE_OP(t):
#     t.type = bitwise_op.get(t.value, 'OPERATOR')
#     return t

# @TOKEN(special_chars)
# def t_SPECIAL_CHARS(t):
#     t.type = special_chars.get(t.value, 'SPECIAL')
#     return t

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

# # data = '3+1-5'
# # wala pa sya gtake sang float

# # Give the lexer some input

# while True:
#    try:
#         s = input('calc > ')

#         while True:
#             lexer.input(s)
#             tok = lexer.token();
#             print (tok)
#             break 
#    except EOFError:
#        break
#     # if not s: continue
   
#    # result = parser.parse(s)
#    # print (result)

# # Tokenizer
# # while True:
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE')
    )

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
# from calclex import tokens

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