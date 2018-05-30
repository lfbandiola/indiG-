
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEAND ASSIGN COMMA COND DIVIDE EXPR GREATER ID LBRACE LESS LPAREN MINUS MOD NAME NOT NUMBER NUM_CONST OPERATOR OR PLUS RBRACE RPAREN SEMICOLON TIMES VARstatement : NAME ASSIGN expressionstatement : expressionexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : NUMBERfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'NAME':([0,],[2,]),'NUMBER':([0,7,8,9,10,11,12,],[6,6,6,6,6,6,6,]),'LPAREN':([0,7,8,9,10,11,12,],[7,7,7,7,7,7,7,]),'$end':([1,3,4,5,6,14,15,16,17,18,19,],[0,-2,-5,-8,-9,-1,-3,-4,-6,-7,-10,]),'ASSIGN':([2,],[8,]),'PLUS':([3,4,5,6,13,14,15,16,17,18,19,],[9,-5,-8,-9,9,9,-3,-4,-6,-7,-10,]),'MINUS':([3,4,5,6,13,14,15,16,17,18,19,],[10,-5,-8,-9,10,10,-3,-4,-6,-7,-10,]),'RPAREN':([4,5,6,13,15,16,17,18,19,],[-5,-8,-9,19,-3,-4,-6,-7,-10,]),'TIMES':([4,5,6,15,16,17,18,19,],[11,-8,-9,11,11,-6,-7,-10,]),'DIVIDE':([4,5,6,15,16,17,18,19,],[12,-8,-9,12,12,-6,-7,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,7,8,],[3,13,14,]),'term':([0,7,8,9,10,],[4,4,4,15,16,]),'factor':([0,7,8,9,10,11,12,],[5,5,5,5,5,17,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> NAME ASSIGN expression','statement',3,'p_statement_assign','tokenizer.py',108),
  ('statement -> expression','statement',1,'p_statement_expr','tokenizer.py',112),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','tokenizer.py',116),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','tokenizer.py',124),
  ('expression -> term','expression',1,'p_expression_term','tokenizer.py',129),
  ('term -> term TIMES factor','term',3,'p_term_times','tokenizer.py',133),
  ('term -> term DIVIDE factor','term',3,'p_term_div','tokenizer.py',138),
  ('term -> factor','term',1,'p_term_factor','tokenizer.py',143),
  ('factor -> NUMBER','factor',1,'p_factor_num','tokenizer.py',147),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','tokenizer.py',151),
]
