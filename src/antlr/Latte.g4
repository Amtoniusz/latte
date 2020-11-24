grammar Latte;

program
    : topDef+
    ;

topDef
    : type_ ID '(' arg? ')' block
    ;

arg
    : type_ ID ( ',' type_ ID )*
    ;

block
    : '{' stmt* '}'
    ;

stmt
    : ';'                                                   # Empty
    | block                                                 # BlockStmt
    | type_ item ( ',' item )* ';'                          # Decl
    | ID '=' expr ';'                                       # Ass
    | ID '++' ';'                                           # Incr
    | ID '--' ';'                                           # Decr
    | 'return' expr ';'                                     # Ret
    | 'return' ';'                                          # VRet
    | 'if' '(' cond=expr ')' sTrue=stmt                     # Cond
    | 'if' '(' cond=expr ')' sTrue=stmt 'else' sFlase=stmt  # CondElse
    | 'while' '(' cond=expr ')' stmt                        # While
    | expr ';'                                              # SExp
    ;

type_
    : 'int'     # Int
    | 'string'  # Str
    | 'boolean' # Bool
    | 'void'    # Void
    ;

item
    : ID
    | ID '=' expr
    ;

expr
    : op=('-'|'!') expr                                    # EUnOp
    | left=expr op=mulOp right=expr                        # EMulOp
    | left=expr op=addOp right=expr                        # EAddOp
    | left=expr op=relOp right=expr                        # ERelOp
    | <assoc=right> left=expr op='&&' right=expr           # EAnd
    | <assoc=right> left=expr op='||' right=expr           # EOr
    | ID                                                   # EId
    | INT                                                  # EInt
    | 'true'                                               # ETrue
    | 'false'                                              # EFalse
    | ID '(' ( expr ( ',' expr )* )? ')'                   # EFunCall
    | STR                                                  # EStr
    | '(' expr ')'                                         # EParen
    ;

addOp
    : '+'
    | '-'
    ;

mulOp
    : '*'
    | '/'
    | '%'
    ;

relOp
    : '<'
    | '<='
    | '>'
    | '>='
    | '=='
    | '!='
    ;

COMMENT : ('#' ~[\r\n]* | '//' ~[\r\n]*) -> channel(HIDDEN);
MULTICOMMENT : '/*' .*? '*/' -> channel(HIDDEN);

fragment Letter  : Capital | Small ;
fragment Capital : [A-Z\u00C0-\u00D6\u00D8-\u00DE] ;
fragment Small   : [a-z\u00DF-\u00F6\u00F8-\u00FF] ;
fragment Digit : [0-9] ;

INT : Digit+ ;
fragment ID_First : Letter | '_';
ID : ID_First (ID_First | Digit)* ;

WS : (' ' | '\r' | '\t' | '\n')+ ->  skip;

STR
    :   '"' StringCharacters? '"'
    ;
fragment StringCharacters
    :   StringCharacter+
    ;
fragment
StringCharacter
    :   ~["\\]
    |   '\\' [tnr"\\]
    ;
