import ply.yacc as yacc
from lexer import ArithLexer

tokens = ArithLexer.tokens

# Definição da gramática
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : assignment ";"
                 | write_statement ";"
                 | function_definition ";"'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : var "=" expression
                  | var "?" "=" expression
                  | var "!" "=" expression
                  | var "=" lista'''
    if len(p) == 4:
        p[0] = ('assign', p[1], p[3])
    else:
        p[0] = ('special_assign', p[1], p[2], p[4])

def p_write_statement(p):
    '''write_statement : escrever "(" expression ")"
                       | escrever "(" string ")"
                       | escrever "(" lista ")"'''
    p[0] = ('write', p[3])


def p_expression(p):
    '''expression : expression "+" term
                  | expression "-" term
                  | expression concat expression
                  | term'''
    if len(p) == 4:
        if p[2] == '<>':
            p[0] = ('concat', p[1], p[3])
        else:
            p[0] = ('binop', p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term "*" factor
            | term "/" factor
            | factor'''
    if len(p) == 4:
        p[0] = ('binop', p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : num
              | var
              | lista
              | string
              | "(" expression ")"'''
    if len(p) == 2:
        if isinstance(p[1], str):
            if p[1].startswith('"') and p[1].endswith('"'):
                p[0] = ('str', p[1][1:-1])
            elif p[1].startswith('[') and p[1].endswith(']'):
                p[0] = ('lista', eval(p[1]))
            else:
                p[0] = ('var', p[1])
        else:
            p[0] = ('num', p[1])
    else:
        p[0] = p[2]

def p_list(p):
    '''list : "[" elements "]"'''
    p[0] = p[2]

def p_elements(p):
    '''elements : elements "," expression
                | expression'''
    if len(p) > 2:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]
#FUNCAO soma(a,b),: a+b ;
def p_function_definition(p):
    '''function_definition : funcao var "(" parameter_list ")" ":" statement_list fim'''
    p[0] = ('func_def', p[2], p[4], p[7])

def p_parameter_list(p):
    '''parameter_list : parameter_list "," var
                      | var'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_error(p):
    print(f"Syntax error at '{p.value}'")

parser = yacc.yacc()

# Função de parsing
def parse(input_string):
    lexer = ArithLexer()
    lexer.build()
    return parser.parse(input_string, lexer=lexer.lexer)
