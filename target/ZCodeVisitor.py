# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_list.
    def visitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_decl_full.
    def visitVar_decl_full(self, ctx:ZCodeParser.Var_decl_fullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_decl.
    def visitFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_body.
    def visitFunction_body(self, ctx:ZCodeParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement_list.
    def visitStatement_list(self, ctx:ZCodeParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nonnull_statement.
    def visitNonnull_statement(self, ctx:ZCodeParser.Nonnull_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#statement_full.
    def visitStatement_full(self, ctx:ZCodeParser.Statement_fullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_list.
    def visitElif_list(self, ctx:ZCodeParser.Elif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_stmt.
    def visitElif_stmt(self, ctx:ZCodeParser.Elif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#all_stmt.
    def visitAll_stmt(self, ctx:ZCodeParser.All_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_stmt.
    def visitBlock_stmt(self, ctx:ZCodeParser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_stmt.
    def visitReturn_stmt(self, ctx:ZCodeParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter_list.
    def visitParameter_list(self, ctx:ZCodeParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nonnull_parameter.
    def visitNonnull_parameter(self, ctx:ZCodeParser.Nonnull_parameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#parameter.
    def visitParameter(self, ctx:ZCodeParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_decl.
    def visitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#varkey_decl.
    def visitVarkey_decl(self, ctx:ZCodeParser.Varkey_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dykey_decl.
    def visitDykey_decl(self, ctx:ZCodeParser.Dykey_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#prikey_decl.
    def visitPrikey_decl(self, ctx:ZCodeParser.Prikey_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#pri_type.
    def visitPri_type(self, ctx:ZCodeParser.Pri_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_type.
    def visitArr_type(self, ctx:ZCodeParser.Arr_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#numlit_list.
    def visitNumlit_list(self, ctx:ZCodeParser.Numlit_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_value.
    def visitArr_value(self, ctx:ZCodeParser.Arr_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression1.
    def visitExpression1(self, ctx:ZCodeParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression2.
    def visitExpression2(self, ctx:ZCodeParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression3.
    def visitExpression3(self, ctx:ZCodeParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression4.
    def visitExpression4(self, ctx:ZCodeParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression5.
    def visitExpression5(self, ctx:ZCodeParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression6.
    def visitExpression6(self, ctx:ZCodeParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression7.
    def visitExpression7(self, ctx:ZCodeParser.Expression7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression8.
    def visitExpression8(self, ctx:ZCodeParser.Expression8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression9.
    def visitExpression9(self, ctx:ZCodeParser.Expression9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression10.
    def visitExpression10(self, ctx:ZCodeParser.Expression10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#acc_arr.
    def visitAcc_arr(self, ctx:ZCodeParser.Acc_arrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_ele.
    def visitArr_ele(self, ctx:ZCodeParser.Arr_eleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_expr.
    def visitArr_expr(self, ctx:ZCodeParser.Arr_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_operators.
    def visitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function_call.
    def visitFunction_call(self, ctx:ZCodeParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argurment_list.
    def visitArgurment_list(self, ctx:ZCodeParser.Argurment_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nonnull_argurment.
    def visitNonnull_argurment(self, ctx:ZCodeParser.Nonnull_argurmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#argurment.
    def visitArgurment(self, ctx:ZCodeParser.ArgurmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_list.
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nonnull_newline.
    def visitNonnull_newline(self, ctx:ZCodeParser.Nonnull_newlineContext):
        return self.visitChildren(ctx)



del ZCodeParser