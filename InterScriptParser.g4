parser grammar InterScriptParser;

options { tokenVocab=InterScriptLexer; }

program: statement* ;

statement: variableDeclaration
         | functionDeclaration
         | ifStatement
         | forStatement
         | returnStatement
         | expressionStatement ;

variableDeclaration: LET IDENTIFIER COLON type ASSIGN expression SEMICOLON ;

functionDeclaration: FUNCTION IDENTIFIER LPAREN parameterList RPAREN COLON type LBRACE statement* RBRACE ;

parameterList: parameter (COMMA parameter)* | ;
parameter: IDENTIFIER COLON type ;

ifStatement: IF LPAREN expression RPAREN LBRACE statement* RBRACE (ELSE LBRACE statement* RBRACE)? ;

forStatement: FOR LPAREN variableDeclaration expression SEMICOLON expression RPAREN LBRACE statement* RBRACE ;

returnStatement: RETURN expression SEMICOLON ;

expressionStatement: expression SEMICOLON ;

expression: primaryExpr (binaryOp primaryExpr)* ;

binaryOp: PLUS | MINUS | STAR | SLASH | GT | LT | EQ | NEQ ;

primaryExpr: IDENTIFIER
           | literal
           | functionCall
           | LPAREN expression RPAREN ;

functionCall: IDENTIFIER LPAREN argumentList RPAREN ;
argumentList: expression (COMMA expression)* | ;

literal: INT | STRING | TRUE | FALSE ;

type: IDENTIFIER ;
