# lexer.py
import sys
import ply.lex as lex

# Palavras reservadas
reserved = {
    'program'  : 'PROGRAM',
    'procedure': 'PROCEDURE',
    'function' : 'FUNCTION',
    'end'      : 'END',
    'var'      : 'VAR',
    'begin'    : 'BEGIN',
    'integer'  : 'iNTEGER',
    'boolean'  : 'BOOLEAN',
    'false'    : 'FALSE',
    'true'     : 'TRUE',
    'while'    : 'WHILE',
    'do'       : 'DO',
    'if'       : 'IF',
    'then'     : 'THEN',
    'else'     : 'ELSE',
    'read'     : 'READ',
    'write'    : 'WRITE',
    'and'      : 'AND',
    'or'       : 'OR',
    'not'      : 'NOT',
    'div'      : 'DIV',
}


# Tokens nomeados
tokens = (
    'NUM', # 0-9
    'ID', # nome de variáveis e de funções
    'DIFERENTE', # <>
    'MAIOR_IGUAL', # >=
    'MENOR_IGUAL', # <=
    'ATRIBUICAO', # :=
) + tuple(reserved.values())


# Tokens literais
literals = ['=', '+', '-', '*', '/', '(', ')', ':', ';', '<', '>', ',', '.']


# Regras simples

t_DIFERENTE = r'\<>'
t_MAIOR_IGUAL = r'\>='
t_MENOR_IGUAL = r'\<='
t_ATRIBUICAO = r'\:='


# Números inteiros e reais
def t_NUM(t):
    
    r'\d+'
    t.value = int(t.value)
    return t


# Identificadores válidos + palavras reservadas
def t_ID(t):
    
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')
    return t


# Espaços e tabulações
t_ignore = ' \t\r'


# Quebra de linha e contagem de linhas
def t_newline(t):
    
    r'\n+'
    t.lexer.lineno += len(t.value)
    
    
'''
# Comentários de linha (// até o fim da linha)
def t_COMMENT(t):
    r'//[^\n]*'
    pass
'''

'''
# Conta colunas de uma linha
def calcula_coluna(t, lexico):
    
    # coluna começando em 1
    line_start = getattr(lexico, 'line_start', 0) # getattr(obj, attr, default) é função nativa do Python
    # soma 1 para o valor de coluna começar em 1
    return t.lexpos - line_start + 1
'''

# Erros léxicos
def t_error(t):
    
    if t.value[0] == '_':
        print(f"ERRO LÉXICO na linha {t.lineno}: símbolo '_' não pode iniciar um identificador")
    else:
        print(f"ERRO LÉXICO na linha {t.lineno}: símbolo ilegal {t.value[0]!r}")
    t.lexer.skip(1)


# Instancia o lexer
def make_lexer():
    
    return lex.lex()
    

# Para testar o lexer sozinho: python3 lexer.py <exemplo.calc
if __name__ == '__main__':
    data = sys.stdin.read()
    lexer = make_lexer()
    lexer.input(data)
    for tok in lexer:
        print(f'< {tok.type} , {tok.value!r} > na linha: {tok.lineno}')