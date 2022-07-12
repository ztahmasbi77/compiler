import sys 
import ast
import ply.yacc as yacc
import symtable

# Get the token map
from lexical_analyzer import tokens


global v
global n
count_meghdar = 1
count_sotun = 1

# translation-unit:

def p_quary (t):
    '''query : entekhab
             | ezafe
             | brooz
             | hazf
             '''
    pass

###############################################################################

#select
def p_entekhab1 (t):
    'entekhab : Entekhab v Az xl Jayi_ke Lparen CONDITION Rparen SEMI_COLON'
    print(";")
    pass

def p_entekhab2 (t):
    'entekhab : Entekhab Asterisk Az xl SEMI_COLON'
    print(";")
    pass

###############################################################################
    
#insert
def p_ezafe1 (t):
    'ezafe : Ezafe Be xl Arzesh_ha Meghdar SEMI_COLON'
    print(";")
    symtable.SymTab._error(count_meghdar,count_sotun)
    pass

def p_ezafe2 (t):
    'ezafe : Ezafe Be xl Sotun Arzesh_ha Meghdar SEMI_COLON'
    print(";")
    symtable.SymTab._error(count_meghdar,count_sotun)
    pass

###############################################################################

#update
def p_brooz (t):
    'brooz : Brooz xl Tanzim SO_ME Jayi_ke Lparen CONDITION Rparen SEMI_COLON'
    print(";")
    pass

###############################################################################

#delete
def p_hazf1(t):
    'hazf : Hazf Az xl SEMI_COLON'
    print(";")
    pass
def p_hazf2(t):
    'hazf : Hazf Az xl JAYI_KE Lparen CONDITION Rparen SEMI_COLON'
    print(";")
    pass

###############################################################################

def p_condition(t):
    '''CONDITION : CONDITION VA CONDITION
                 | CONDITION YA CONDITION
                 | NA CONDITION
                 | v RELOP n
                 '''
    pass


def p_xl(t):
    ' xl : Name'
    t[0]=t[1]
    symtable.SymTab.insert(t[0], 'STR_LITER')
    pass


def p_v(t):
    ' v : Name'
    global count_sotun
    count_sotun = count_sotun + 1
    t[0]=t[1]
    symtable.SymTab.insert(t[0], 'STR_LITER')
    pass


def p_n(t):
    ''' n : Name
          | Digits
          '''
    global count_meghdar
    count_meghdar = count_meghdar + 1
    t[0]=t[1]
    symtable.SymTab.insert(t[0], 'STR_LITER')
    pass

#(n) , (n,...,n)
def p_meghdar(t):
    ' Meghdar : Lparen _Meghdar  Rparen'
    pass

def p_Meghdar(t):
    ''' _Meghdar : n                          
                 | n Comma _Meghdar 
                 '''
    pass

#(v) , (v,...,v)
def p_sotun(t):
    ' Sotun : Lparen _Sotun  Rparen'
    pass

def p_Sotun(t):
    ''' _Sotun : v                          
               | v Comma _Sotun
               '''
    pass

#(v) = (n) 
def p_so_me(t):
    ''' SO_ME : Lparen v Rparen Assign Lparen n Rparen
              | SO_ME Comma SO_ME
              '''
    pass

def p_Name(t):
    ''' Name : Letter
             | Name Digit 
             | Name Digit Name
             '''
    pass

def p_letter(t):
    ''' Letter : ID
               | Letter ID
               '''
    t[0]=t[1]
    print(t[0], end=" ")
    pass

def p_digit(t):
    ' Digit : STR_LITER'
    t[0]=t[1]
    print(t[0], end=" ")
    pass

def p_digits(t):
    ''' Digits : Digit
               | Digit Digits
               '''
    pass
# < , > , =
def p_relop(t):
    ''' RELOP : LT
              | GT
              | ASSIGN
              '''
    t[0]=t[1]
    print(t[0], end=" ")
    pass
###############################################################################
def p_Entekhab(t):
    'Entekhab : ENTEKHAB'
    print("SELECT", end=" ")
    pass
def p_Arzesh_ha(t):
    'Arzesh_ha : ARZESH_HA'
    print("VALUES", end=" ")
    pass
def p_Ezafe(t):
    'Ezafe : EZAFE'
    print("INSERT", end=" ")
    pass
def p_Hazf(t):
    'Hazf : HAZF'
    print("DELETE", end=" ")
    pass
def p_Be(t):
    'Be : BE'
    print("INTO", end=" ")
    pass
def p_Az(t):
    'Az : AZ'
    print("FROM", end=" ")
    pass
def p_Brooz(t):
    'Brooz : BROOZ'
    print("UPDATE", end=" ")
    pass
def p_Tanzim(t):
    'Tanzim : TANZIM'
    print("SET", end=" ")
    pass
def p_Jayi_ke(t):
    'Jayi_ke : JAYI_KE'
    print("WHERE", end=" ")
    pass
def p_Lparen(t):
    'Lparen : LPAREN'
    print("(", end=" ")
    pass
def p_Rparen(t):
    'Rparen : RPAREN'
    print(")", end=" ")
    pass
def p_Asterisk(t):
    'Asterisk : ASTERISK'
    print("*", end=" ")
    pass
def p_Comma(t):
    'Comma : COMMA'
    print(",", end=" ")
    pass
def p_Assign(t):
    'Assign : ASSIGN'
    print("=", end=" ")
    pass




###############################################################################
precedence = (
    ('left', 'ASSIGN'),
    ('left', 'LT', 'GT'),
)
 
# error recovery       
def p_error(p):    
    if not p:
       print(end='\n')
       print("End of File!")
       return
    else:
        print(end='\n')
        print("error in line :", p.lineno , end='')
        print(", token:"+ p.value)
        
#     Read ahead looking for a closing ';'
    while True:
        tok = parser.token()      # Get the next token  
        if not tok or tok.type == 'SEMI_COLON': 
            break
    parser.restart()   
   

# AST
class MyVisitor(ast.NodeVisitor):
    def visit_Str(self, node):
        print('String Node: "' + node.s + '"')

class MyTransformer(ast.NodeTransformer):
    def visit_Str(self, node):
        return ast.Str('str: ' + node.s)
parsed = ast.parse("print('Hello World')")
parsed = ast.fix_missing_locations(parsed)
exec(compile(parsed, '<string>', 'exec'))
MyTransformer().visit(parsed)
MyVisitor().visit(parsed)
   

parser = yacc.yacc()
#parser.defaulted_states = {}

while True:
    try:
        s = input('input > ')
    except EOFError:
        break
    if not s: 
        continue
    result = parser.parse(s)
    print(result)
