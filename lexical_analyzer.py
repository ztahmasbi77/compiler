import sys
sys.path.insert(0, "../lib")

import ply.lex as lex
from ply.lex import TOKEN


# Keywords
keyword = (
    'ENTEKHAB', 'EZAFE', 'BE', 'ARZESH_HA', 'HAZF', 'BROOZ', 'AZ', 'JAYI_KE',
    'TANZIM', 'VA', 'YA', 'NA'
)



# String Literals
string_literals = ('STR_LITER',)

# Operators
operator = (
    # Arithmetic operators (*)
    'ASTERISK',

    # Comparison operators (<, >)
    'LT', 'GT',

    # Assignment operators (=)
    'ASSIGN',


    # Other operators (,)
    'COMMA',

)

# Punctuators
punctuator = (
    'LPAREN', 'RPAREN',            # (, )
    'SEMI_COLON',                  # ;
)

# Tokens
tokens = keyword + string_literals + operator + punctuator + (
    'ID',
    'SPS',
)

# Keywords
keyword_map = {
    'entekhab' : 'ENTEKHAB',
    'ezafe' : 'EZAFE',
    'be' : 'BE',
    'arzesh_ha' : 'ARZESH_HA',
    'hazf' : 'HAZF',
    'brooz' : 'BROOZ',
    'az' : 'AZ',
    'jayi_ke' : 'JAYI_KE',
    'tanzim' : 'TANZIM',
    'va' : 'VA',
    'ya' : 'YA',
    'na' : 'NA'
 }

# String Literals
def t_STR_LITER(t):
    r"""
        L?
        \"
        (
            (
                [^\"\\\n]
                | \\[\'\"\?\\abfnrtv]
                | \\[0-7]{1,3}
                | \\x[0-9a-fA-f]+
            )+
        )*
        \"
     """
    return t


# Arithmetic operators
t_ASTERISK = r'\*'

# Comparion operators
t_LT = r'<'
t_GT = r'>'


# Assignment operators
t_ASSIGN = r'='



# Other operators
t_COMMA = r','

# Punctuators

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMI_COLON = r';'





# Identifier
def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = keyword_map.get(t.value, 'ID')
    return t


# Newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


# Comments
def t_comment(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


# White Space
def t_SPS(t):
    r'\ '
    


# Error handling
def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)


lexical_analyzer = lex.lex()
if __name__ == "__main__":
    lex.runmain(lexical_analyzer)
