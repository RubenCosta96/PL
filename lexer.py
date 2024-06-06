import ply.lex as plex

class ArithLexer:
    tokens = (
        "num", "var", "escrever", "string", "entrada", "aleatorio", "concat", 
        "comment", "comment_multi", "funcao", "fim", "lista", "fold", "map"
    )
    literals = ['+', '-', '*', '(', ')', '=', ';', ',', ':', '[', ']']
    t_ignore = " \t"

    @classmethod
    def get_tokens(cls):
        return cls.tokens

    def __init__(self):
        self.lexer = None   
    
    def t_num(self, t):
        r'\d+'
        t.value = int(t.value)
        return t
    
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_string(self, t):
        r'"([^\\"]|\\.)*"'
        t.value = t.value[1:-1]  # Remove the quotes
        return t

    def t_escrever(self, t):
        r"[Ee][Ss][Cc]([Rr][Ee][Vv][Ee][Rr])?"
        return t
        
    def t_entrada(self, t):
        r'[Ee][Nn][Tt][Rr][Aa][Dd][Aa]'
        return t

    def t_aleatorio(self, t):
        r'[Aa][Ll][Ee][Aa][Tt][Oo][Rr][Ii][Oo]\(\d+\)'
        t.value = int(t.value.split('(')[1][:-1])
        return t
    
    def t_lista(self,t):
        r'\[\]'
        t.value = eval(t.value)
        return t

    def t_concat(self, t):
        r'<>'
        return t
    
    def t_funcao(self, t):
        r'[Ff][Uu][Nn][Cc][Aa][Oo]'
        return t

    def t_fim(self, t):
        r'[Ff][Ii][Mm]'
        return t

    def t_map(self, t):
        r'[Mm][Aa][Pp]'
        t.type = 'map'
        return t

    def t_fold(self, t):
        r'[Ff][Oo][Ll][Dd]'
        t.type = 'fold'
        return t

    def t_var(self, t):
        r'[a-z_][a-zA-Z_0-9]*[\?!]?'
        return t

    def t_COMMENT(self, t):
        r'--.*'
        pass
        
    def t_COMMENT_MULTI(self, t):
        r'\{.*?\}'
        pass

    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    def input(self, string):
        self.lexer.input(string)

    def token(self):
        token = self.lexer.token()
        return token if token is None else token.type 

    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)
