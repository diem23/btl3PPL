from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *
# from target.ZCodeParser import ZCodeParser
# from target.ZCodeVisitor import ZCodeVisitor
# from main.zcode.utils.AST import *


class ASTGeneration(ZCodeVisitor):
    #program: newline_list decl_list EOF ;
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decl_list()))
    #decl_list: decl decl_list | decl;
    def visitDecl_list(self, ctx: ZCodeParser.Decl_listContext):
        if (ctx.getChildCount()==1): return [self.visit(ctx.decl())]
        return [self.visit(ctx.decl())] + self.visit(ctx.decl_list())
    #decl: func_decl | var_decl_full;
    def visitDecl(self, ctx: ZCodeParser.DeclContext):
        if (ctx.func_decl()): return self.visit(ctx.func_decl())
        return self.visit(ctx.var_decl_full())
    # var_decl_full: var_decl nonnull_newline;
    def visitVar_decl_full(self, ctx: ZCodeParser.Var_decl_fullContext):
        return self.visit(ctx.var_decl())
    # func_decl: FUNC IDENTIFIER LB parameter_list RB (newline_list function_body)? nonnull_newline;
    def visitFunc_decl(self, ctx: ZCodeParser.Func_declContext):
        return FuncDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.parameter_list()), self.visit(ctx.function_body())) if (ctx.function_body()) else FuncDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.parameter_list()))
    # function_body: block_stmt | return_stmt;
    def visitFunction_body(self, ctx: ZCodeParser.Function_bodyContext):
        
        if (ctx.block_stmt()): 
            #print("hello")
            return self.visit(ctx.block_stmt())
        return self.visit(ctx.return_stmt())
    # statement_list: nonnull_statement | ;
    def visitStatement_list(self, ctx: ZCodeParser.Statement_listContext):
        if (ctx.getChildCount()==0): return []
        #print(ctx.nonnull_statement().getText())
        return self.visit(ctx.nonnull_statement())
    #nonnull_statement: statement_full nonnull_statement | statement_full;
    def visitNonnull_statement(self, ctx: ZCodeParser.Nonnull_statementContext):
        if (ctx.getChildCount()==1): return [self.visit(ctx.statement_full())]
        return [self.visit(ctx.statement_full())] + self.visit(ctx.nonnull_statement())
    # statement_full: stmt nonnull_newline;
    def visitStatement_full(self, ctx: ZCodeParser.Statement_fullContext):
        
        return self.visit(ctx.stmt())
    # elif_list: elif_stmt elif_list | ;
    def visitElif_list(self, ctx: ZCodeParser.Elif_listContext):
        if (ctx.getChildCount()==0): return []
        return [self.visit(ctx.elif_stmt())] + self.visit(ctx.elif_list())
    #elif_stmt: nonnull_newline ELIF (LB expression1 RB)  newline_list (block_stmt|return_stmt|stmt) ;
    def visitElif_stmt(self, ctx: ZCodeParser.Elif_stmtContext):
        return (self.visit(ctx.expression1()),self.visit(ctx.all_stmt()))
    # stmt: var_decl
	# | (arr_ele|IDENTIFIER) ASS expression1
	# | block_stmt
	# | return_stmt
	# | IF (LB expression1 RB ) newline_list (block_stmt|return_stmt|stmt) elif_list (nonnull_newline ELSE newline_list (block_stmt|return_stmt|stmt))?   // cau lenh if
	# | FOR IDENTIFIER UNTIL expression1 BY expression1 newline_list (block_stmt|return_stmt|stmt)  // cau lenh FOR
	# | BREAK 
	# | CONT
	# | function_call;
    def visitStmt(self, ctx: ZCodeParser.StmtContext):
        if (ctx.var_decl()): return self.visit(ctx.var_decl())
        elif (ctx.ASS()): 
            #print("rhs: ", ctx.IDENTIFIER().getText())
            
                # print("countChild: ", ctx.getText())
                # print("rhs: ", ctx.IDENTIFIER().getText())
                # print("ASS: ", ctx.ASS().getText())
                # print("lhs: ", ctx.expression1(0).getText())
            if (ctx.arr_ele()): return Assign(self.visit(ctx.arr_ele()), self.visit(ctx.expression1(0)))
            return Assign(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.expression1(0)))
        elif (ctx.block_stmt()): return self.visit(ctx.block_stmt())
        elif (ctx.return_stmt()): return self.visit(ctx.return_stmt())
        elif (ctx.IF()): 
            #print(ctx.expression1(0).getText())
            #print(ctx.all_stmt(0).getText())
            if (ctx.ELSE()): 
                #print(ctx.all_stmt(1).getText())
                #print("we have else!!")
                return If(self.visit(ctx.expression1(0)),self.visit(ctx.all_stmt(0)),self.visit(ctx.elif_list()),self.visit(ctx.all_stmt(1)))
            return If(self.visit(ctx.expression1(0)),self.visit(ctx.all_stmt(0)),self.visit(ctx.elif_list()))
        elif (ctx.FOR()):
            # print("for_stmt: ", ctx.getText())
            # print("name: ", ctx.IDENTIFIER().getText())
            # print("con: ", ctx.expression1(0).getText())
            # print("update: ", ctx.expression1(1).getText())
            # print("body: ", ctx.all_stmt(0).getText())
            return For(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.expression1(0)),self.visit(ctx.expression1(1)), self.visit(ctx.all_stmt(0)))
        elif (ctx.BREAK()): return Break()
        elif (ctx.CONT()): return Continue()
        return CallStmt(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.argurment_list()))
    # all_stmt: block_stmt | return_stmt | stmt;
    def visitAll_stmt(self, ctx: ZCodeParser.All_stmtContext):
        if (ctx.block_stmt()): return self.visit(ctx.block_stmt())
        elif (ctx.return_stmt()): return self.visit(ctx.return_stmt())
        return self.visit(ctx.stmt())
    # block_stmt: BEGIN nonnull_newline statement_list END ;                       // statement_list có thể null
    def visitBlock_stmt(self, ctx: ZCodeParser.Block_stmtContext):
        #print("Hi")
        return Block(self.visit(ctx.statement_list()))
    # return_stmt: RETURN ((LB expression1 RB)| expression1)?;
    def visitReturn_stmt(self, ctx: ZCodeParser.Return_stmtContext):
        if (ctx.getChildCount()>1): return Return(self.visit(ctx.expression1()))
        return Return()
    # parameter_list: nonnull_parameter| ;
    def visitParameter_list(self, ctx: ZCodeParser.Parameter_listContext):
        if (ctx.getChildCount()==0): return []
        return self.visit(ctx.nonnull_parameter())
    # nonnull_parameter: parameter COMMA nonnull_parameter | parameter;
    def visitNonnull_parameter(self, ctx: ZCodeParser.Nonnull_parameterContext):
        if (ctx.getChildCount()==1): return [self.visit(ctx.parameter())]
        return [self.visit(ctx.parameter())]+ self.visit(ctx.nonnull_parameter())
    # parameter: pri_type (IDENTIFIER|arr_type);
    def visitParameter(self, ctx: ZCodeParser.ParameterContext):
        if (ctx.arr_type()) :
            ARR = self.visit(ctx.arr_type())
            return VarDecl(ARR[0],ArrayType(ARR[1],self.visit(ctx.pri_type())))
        return VarDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.pri_type()))
    # var_decl: varkey_decl | dykey_decl | prikey_decl;
    def visitVar_decl(self, ctx: ZCodeParser.Var_declContext):
        if ctx.varkey_decl(): return self.visit(ctx.varkey_decl())
        if ctx.dykey_decl(): return self.visit(ctx.dykey_decl())
        return self.visit(ctx.prikey_decl())
    # varkey_decl: VAR IDENTIFIER ASS expression1;
    def visitVarkey_decl(self, ctx: ZCodeParser.Varkey_declContext):
        return VarDecl(Id(ctx.IDENTIFIER().getText()),None,ctx.VAR().getText(),self.visit(ctx.expression1()))
    # dykey_decl: DYNAMIC IDENTIFIER (ASS expression1)?;
    def visitDykey_decl(self,ctx: ZCodeParser.Dykey_declContext):
        if (ctx.expression1()): 
            #print("modifier: ",ctx.DYNAMIC().getText())
            return VarDecl(Id(ctx.IDENTIFIER().getText()),None,ctx.DYNAMIC().getText(), self.visit(ctx.expression1()))
        return VarDecl(Id(ctx.IDENTIFIER().getText()),None,ctx.DYNAMIC().getText())
    # prikey_decl: pri_type (arr_type| IDENTIFIER) (ASS expression1)?;
    def visitPrikey_decl(self,ctx: ZCodeParser.Prikey_declContext):
        EXP=None
        if (ctx.expression1()): EXP = self.visit(ctx.expression1())
        if (ctx.arr_type()) :
            ARR = self.visit(ctx.arr_type())
            return VarDecl(ARR[0],ArrayType(ARR[1],self.visit(ctx.pri_type())),None,EXP)
        return VarDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.pri_type()),None,EXP)
    # pri_type: BOOL| NUMBER|STRING_DEF;
    def visitPri_type(self, ctx:ZCodeParser.Pri_typeContext):
        if (ctx.BOOL()): return BoolType()
        if (ctx.NUMBER()): return NumberType()
        return StringType()
    # arr_type: IDENTIFIER LBRACE numlit_list RBRACE;
    def visitArr_type(self, ctx:ZCodeParser.Arr_typeContext):
        #print("dimension of arr: ", ctx.numlit_list().getText())
        return (Id(ctx.IDENTIFIER().getText()),self.visit(ctx.numlit_list()))
    # numlit_list: NUMBER_LIT COMMA numlit_list | NUMBER_LIT;
    def visitNumlit_list(self, ctx:ZCodeParser.Numlit_listContext):
        if (ctx.getChildCount()==1): return [float(ctx.NUMBER_LIT().getText())]
        return [float(ctx.NUMBER_LIT().getText())] + self.visit(ctx.numlit_list())
    # arr_value: (LBRACE index_operators RBRACE) ;  
    def visitArr_value(self, ctx:ZCodeParser.Arr_valueContext):
        return ArrayLiteral(self.visit(ctx.index_operators()))
    #expression1: expression2 CON expression2 | expression2;
    def visitExpression1(self, ctx:ZCodeParser.Expression1Context):
        if (ctx.getChildCount()==1): return self.visit(ctx.expression2(0))
        return BinaryOp(ctx.CON().getText(),self.visit(ctx.expression2(0)),self.visit(ctx.expression2(1)))
    # expression2: expression3 ( DIF 
	# 			|  BGOE 
	# 			|  SMOE 
	# 			|  BG 
	# 			|  SM 
	# 			|  EQUAL_NUM 
	# 			|  EQUAL_STR) expression3
	# 			| expression3 ;
    def visitExpression2(self, ctx:ZCodeParser.Expression2Context):
        if ctx.getChildCount()==1: return self.visit(ctx.expression3(0))
        elif ctx.DIF(): return BinaryOp(ctx.DIF().getText(),self.visit(ctx.expression3(0)),self.visit(ctx.expression3(1)))
        elif ctx.BGOE(): return BinaryOp(ctx.BGOE().getText(),self.visit(ctx.expression3(0)),self.visit(ctx.expression3(1)))
        elif ctx.BG(): return BinaryOp(ctx.BG().getText(),self.visit(ctx.expression3(0)),self.visit(ctx.expression3(1)))
        elif ctx.SM(): return BinaryOp(ctx.SM().getText(),self.visit(ctx.expression3(0)),self.visit(ctx.expression3(1)))
        elif ctx.EQUAL_NUM(): return BinaryOp(ctx.EQUAL_NUM().getText(),self.visit(ctx.expression3(0)),self.visit(ctx.expression3(1)))
        elif ctx.EQUAL_STR(): return BinaryOp(ctx.EQUAL_STR().getText(),self.visit(ctx.expression3(0)),self.visit(ctx.expression3(1)))
        return BinaryOp(ctx.SMOE().getText(),self.visit(ctx.expression3(0)),self.visit(ctx.expression3(1)))
    # expression3: expression3 (OR|AND) expression4 | expression4;
    def visitExpression3(self, ctx:ZCodeParser.Expression3Context):
        #print("exp: ",ctx.getText())
        if (ctx.getChildCount()==1): return self.visit(ctx.expression4())
        if (ctx.OR()): return BinaryOp(ctx.OR().getText(),self.visit(ctx.expression3()),self.visit(ctx.expression4()))
        return BinaryOp(ctx.AND().getText(),self.visit(ctx.expression3()),self.visit(ctx.expression4()))
    # expression4: expression4 (MINUS|ADD) expression5 | expression5;    
    def visitExpression4(self, ctx:ZCodeParser.Expression4Context):
        if (ctx.getChildCount()==1): return self.visit(ctx.expression5())
        if (ctx.MINUS()): return BinaryOp(ctx.MINUS().getText(),self.visit(ctx.expression4()),self.visit(ctx.expression5()))
        return BinaryOp(ctx.ADD().getText(),self.visit(ctx.expression4()),self.visit(ctx.expression5()))
    # expression5: expression5 (DIV|MUL|MOD) expression6 | expression6;
    def visitExpression5(self, ctx:ZCodeParser.Expression5Context):
        if (ctx.getChildCount()==1): return self.visit(ctx.expression6())
        if (ctx.DIV()): return BinaryOp(ctx.DIV().getText(),self.visit(ctx.expression5()),self.visit(ctx.expression6()))
        if (ctx.MUL()): return BinaryOp(ctx.MUL().getText(),self.visit(ctx.expression5()),self.visit(ctx.expression6()))
        return BinaryOp(ctx.MOD().getText(),self.visit(ctx.expression5()),self.visit(ctx.expression6()))
    # expression6: NOT expression6 | expression7 ; 
    def visitExpression6(self, ctx:ZCodeParser.Expression6Context):
        if (ctx.getChildCount()==1): return self.visit(ctx.expression7())
        return UnaryOp(ctx.NOT().getText(),self.visit(ctx.expression6()))
    # expression7: MINUS expression7 | expression8 ; 
    def visitExpression7(self, ctx:ZCodeParser.Expression7Context):
        if (ctx.getChildCount()==1): return self.visit(ctx.expression8())
        return UnaryOp(ctx.MINUS().getText(),self.visit(ctx.expression7()))
    # expression8: acc_arr | expression9 ;  
    def visitExpression8(self, ctx:ZCodeParser.Expression8Context):
        if (ctx.expression9()): return self.visit(ctx.expression9())
        return self.visit(ctx.acc_arr())
    # expression9: LB expression1 RB | expression10;
    def visitExpression9(self, ctx:ZCodeParser.Expression9Context):
        if (ctx.expression10()): return self.visit(ctx.expression10())
        return self.visit(ctx.expression1())
    # expression10: function_call | IDENTIFIER | NUMBER_LIT | BOOL_LIT | STR_LIT | arr_value;
    def visitExpression10(self, ctx:ZCodeParser.Expression10Context):
        if (ctx.function_call()): return self.visit(ctx.function_call())
        elif (ctx.IDENTIFIER()): return Id(ctx.IDENTIFIER().getText())
        elif (ctx.BOOL_LIT()): 
            flag = ctx.BOOL_LIT().getText()
            if flag == 'true':
                return BooleanLiteral(True)
            return BooleanLiteral(False)
        elif (ctx.NUMBER_LIT()): return NumberLiteral(float(ctx.NUMBER_LIT().getText()))
        elif (ctx.STR_LIT()): return StringLiteral(ctx.STR_LIT().getText())
        return self.visit(ctx.arr_value())
    # acc_arr: arr_ele|arr_expr;
    def visitAcc_arr(self, ctx:ZCodeParser.Acc_arrContext):
        if (ctx.arr_ele()): return self.visit(ctx.arr_ele())
        return self.visit(ctx.arr_expr())
    # arr_ele: IDENTIFIER LBRACE index_operators RBRACE;
    def visitArr_ele(self, ctx:ZCodeParser.Arr_eleContext):
        return ArrayCell(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.index_operators()))
    # arr_expr:function_call LBRACE index_operators RBRACE;
    def visitArr_expr(self, ctx:ZCodeParser.Arr_exprContext):
        return ArrayCell(self.visit(ctx.function_call()),self.visit(ctx.index_operators()))
    # index_operators: expression1 
	# 			| expression1 (COMMA index_operators);
    def visitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        if (ctx.getChildCount()==1): return [self.visit(ctx.expression1())]
        return [self.visit(ctx.expression1())] + self.visit(ctx.index_operators())
    # function_call: IDENTIFIER LB argurment_list RB;
    def visitFunction_call(self, ctx:ZCodeParser.Function_callContext):
        return CallExpr(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.argurment_list()))
    # argurment_list: nonnull_argurment | ;
    def visitArgurment_list(self, ctx:ZCodeParser.Argurment_listContext):
        if ctx.getChildCount() == 0: return []
        return self.visit(ctx.nonnull_argurment())
    # nonnull_argurment: argurment COMMA nonnull_argurment | argurment;
    def visitNonnull_argurment(self, ctx:ZCodeParser.Nonnull_argurmentContext):
        if (ctx.getChildCount()==1): return [self.visit(ctx.argurment())]
        return [self.visit(ctx.argurment())] + self.visit(ctx.nonnull_argurment())
    # argurment: IDENTIFIER
    #     |expression1;
    def visitArgurment(self, ctx:ZCodeParser.ArgurmentContext):
        if ctx.IDENTIFIER(): return Id(ctx.IDENTIFIER().getText())
        return self.visit(ctx.expression1())
#################### MY CODE IS ABOVE #####################

            
    
    
