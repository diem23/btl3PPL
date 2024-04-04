grammar ZCode;
@lexer::header {
2111056
from lexererr import *
}
options {
	language=Python3;
}
program: newline_list decl_list newline_list EOF ;
decl_list: decl decl_list | decl;
decl: func_decl | var_decl_full;
var_decl_full: var_decl nonnull_newline;
func_decl: FUNC IDENTIFIER LB parameter_list RB (newline_list function_body)? nonnull_newline;
function_body: block_stmt | return_stmt;

statement_list: nonnull_statement | ;
nonnull_statement: statement_full nonnull_statement | statement_full;
statement_full: stmt nonnull_newline;

elif_list: elif_stmt elif_list | ;
elif_stmt: nonnull_newline ELIF (LB expression1 RB)  newline_list all_stmt ;
stmt: var_decl
	| (arr_ele|IDENTIFIER) ASS expression1
	| block_stmt
	| return_stmt
	| IF (LB expression1 RB ) newline_list all_stmt elif_list (nonnull_newline ELSE newline_list all_stmt)?   // cau lenh if
	| FOR IDENTIFIER UNTIL expression1 BY expression1 newline_list all_stmt  // cau lenh FOR
	| BREAK 
	| CONT
	| IDENTIFIER LB argurment_list RB;
all_stmt: block_stmt | return_stmt | stmt;
block_stmt: BEGIN nonnull_newline statement_list END ;                       // statement_list có thể null
return_stmt: RETURN ((LB expression1 RB)| expression1)?;
parameter_list: nonnull_parameter| ;
nonnull_parameter: parameter COMMA nonnull_parameter | parameter;
parameter: pri_type (IDENTIFIER|arr_type);
var_decl: varkey_decl | dykey_decl | prikey_decl;
varkey_decl: VAR IDENTIFIER ASS expression1; 					// sau phep gan chi duoc co IDENTIFIER
dykey_decl: DYNAMIC IDENTIFIER (ASS expression1)?;				// sau phep gan chi duoc co IDENTIFIER
prikey_decl: pri_type (arr_type| IDENTIFIER) (ASS expression1)?;
pri_type: BOOL| NUMBER|STRING_DEF;
arr_type: IDENTIFIER LBRACE numlit_list RBRACE;
numlit_list: NUMBER_LIT COMMA numlit_list | NUMBER_LIT;
arr_value: (LBRACE index_operators RBRACE) ;                  // các thành phần của một mảng , có thể rỗng


expression1: expression2 CON expression2 | expression2;
expression2: expression3 ( DIF 
				|  BGOE 
				|  SMOE 
				|  BG 
				|  SM 
				|  EQUAL_NUM 
				|  EQUAL_STR) expression3
				| expression3 ;
expression3: expression3 (OR|AND) expression4 | expression4;
expression4: expression4 (MINUS|ADD) expression5 | expression5;
expression5: expression5 (DIV|MUL|MOD) expression6 | expression6;
expression6: NOT expression6 | expression7 ; 								// toán tử một ngôi 'not'
expression7: MINUS expression7 | expression8;								// toán tử một ngôi dấu '-'
expression8: acc_arr | expression9 ;        // phép toán truy cập mảng
expression9: LB expression1 RB | expression10;
expression10: function_call | IDENTIFIER | NUMBER_LIT | BOOL_LIT | STR_LIT | arr_value;
	   

// truy cap mang
acc_arr: arr_ele|arr_expr;
arr_ele: IDENTIFIER LBRACE index_operators RBRACE;
arr_expr:function_call LBRACE index_operators RBRACE;

// index operator
index_operators: expression1 
				| expression1 (COMMA index_operators);

// lời gọi hàm
function_call: IDENTIFIER LB argurment_list RB;
argurment_list: nonnull_argurment | ;
nonnull_argurment: argurment COMMA nonnull_argurment | argurment;
argurment: IDENTIFIER
        |expression1;
// danh sách expression cách nhau bởi dấu phẩy  (trùng với index_operator ở trên)
//expression_list: expression1 COMMA expression_list | expression1;
// chuỗi xuống hàng
newline_list: nonnull_newline| ;
nonnull_newline: NEWLINE nonnull_newline | NEWLINE;
//fragment support
fragment TRUE: 'true';
fragment FALSE: 'false';
fragment DIGIT: [0-9];
fragment LETTER: [a-zA-Z];
fragment STRING: LETTER*;
fragment ESC: '\\' ('b'|'f'|'r'|'n'|'t'|'\''|'\\') ;
fragment ILLEGAL_ESC: '\\' ~('b'|'f'|'r'|'n'|'t'|'\''|'\\');
fragment INTEGER: DIGIT+;

fragment DECIMAL: DIGIT*;
fragment EXP: [e|E] ('+'|'-')? DIGIT+ ;

fragment ARR_DIM_EXPA: ',' DIGIT ;
fragment ARR_STR_EXPA: ',' LETTER+;
fragment ARR_NUM_EXPA: ',' NUMBER_LIT;
fragment ARR_BOOL_EXPA: ',' BOOL_LIT;


// program comment
CMT: '##' (~('\n'|'\f'|'\r'))*->skip;
// escape character
WS : ('\t'|' '|'\f'|'\b')+ -> skip ; // skip spaces, tabs, newlines
//BSP: '\b' ;					// backspace character
NEWLINE:'\r'| ('\r'? '\n') {
	if (len(self.text)==2):
		self.text = self.text[-1]
     };     // newline character
// FORMFEED: '\f'{
// 	print("formfeed:", len(self.text));
// };
// CARIAGE_RETURN: '\r'{
// 	print("carriage:", len(self.text));
// };
// keywords
NUMBER: 'number';
BOOL: 'bool';
STRING_DEF: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func' ;
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONT: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';  // BOOLEAN_LIT OPERANDS
AND: 'and';	// BOOLEAN_LIT OPERANDS
OR: 'or';	// BOOLEAN_LIT OPERANDS
LB: '(';
RB: ')';
LBRACE: '[';
RBRACE:	']';
COMMA:	',';

// operator
ADD: '+';	// NUMBER_LIT OPERANDS
MINUS: '-';	// NUMBER_LIT OPERANDS
MUL: '*';	// NUMBER_LIT OPERANDS
DIV: '/';	// NUMBER_LIT OPERANDS
MOD: '%';	// NUMBER_LIT OPERANDS
EQUAL_NUM: '=';	// equa // NUMBER_LIT OPERANDS
EQUAL_STR: '==';	//equa	// STR_LIT OPERANDS
ASS: '<-';	// assignment 
DIF: '!=';	// different // NUMBER_LIT OPERANDS
SM: '<';	// smaller	// NUMBER_LIT OPERANDS
SMOE: '<='; // smaller or equal	// NUMBER_LIT OPERANDS
BG: '>';	//	bigger	// NUMBER_LIT OPERANDS
BGOE: '>='; // bigger or equal	// NUMBER_LIT OPERANDS
CON: '...'; //concat two string // STR_LIT OPERANDS

// LITERALS
NUMBER_LIT: INTEGER| INTEGER ('.' DECIMAL?) EXP| INTEGER ('.' DECIMAL?) | INTEGER EXP;

BOOL_LIT: TRUE|FALSE;
STR_LIT: '"' (~["\f\n\r\\]| ESC  |'\'"' )* '"' {self.text = self.text[1:-1]};   // NHO SUA LAI STRING

// STR_LIT: '"' (~('"'|'//') | ESC | '\'"')* '"';

IDENTIFIER: ('_'|LETTER) (LETTER|DIGIT|'_')*;



UNCLOSE_STRING: '"' (~('"'|'\f'|'\r'|'\n'|'\\')  | '\'"'|ESC)* ('\f'|'\r'|'\n'|EOF) {
	decrease = ['\f','\r','\n']
	if (self.text[-1] in decrease): 
		raise UncloseString(self.text[1:-1])
	else:
		raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE: '"' (~('"'|'\f'|'\r'|'\n'|'\\')  | '\'"'|ESC)* ILLEGAL_ESC {
	raise IllegalEscape(self.text[1:])};

ERROR_CHAR: . {
	raise ErrorToken(self.text)};