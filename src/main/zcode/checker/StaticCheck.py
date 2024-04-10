from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
NumOfLoop = 0
class NoneType: pass

class FunctionType:
    def __init__(self,param,haveBody,returnType):
        self.param = param
        self.haveBody = haveBody
        self.returnType = returnType
class Symbol:
    def __init__(self, name, mtype):
        self.name = name
        self.mtype = mtype
class CannotInferType: pass
class HelpingTools:
    def checkRedeclared(name,o):
        for item in o[0]:
            if item.name == name and type(item.mtype) is not FunctionType:
                return True
        return False
    def inferType(name,Type,o,checkFunction=False):
        #print(name,Type)
        if type(name) is not str:
            name=name.name
        for scope in o:
            for item in scope:
                if item.name == name :
                    #print('item name: ',item.name)
                    #print('item type: ',item.mtype)
                    if checkFunction and type(item.mtype) is FunctionType or not checkFunction and type(item.mtype) is not FunctionType:
                        if type(item.mtype) is ArrayType and type(Type) is ArrayType:
                            #print('infer arrayType')
                            item.mtype.eleType = Type.eleType
                            item.mtype.size += Type.size
                        elif type(item.mtype) is FunctionType:
                            item.mtype.returnType = Type
                        else: 
                            #print('infer type: ',Type)
                            item.mtype = Type
                        return True  ## infer type successfully
        return False ## cannot infer type
    def getSubArrayType(name1,name2):    ## name1 va name2 la 2 ArrayType, name1 hoac name2 la nonetype, 
        result=[]                       ## func tra ve false neu 2 kieu khong tuong duong, tra ve kieu array de mot mang co the suy ra mang con lai
        #print('hehe')
        if type(name1.eleType) is NoneType and type(name2.eleType) is NoneType: 
            if len(name1.size) > len(name2.size): 
                for i in range(0,len(name2.size)):
                    if name1.size[i] != name2.size[i]:
                        return False
                for i in range(len(name2.size),len(name1.size)):
                    result+=[float(name1.size[i])]
            else:
                for i in range(0,len(name1.size)):
                    if name1.size[i] != name2.size[i]:
                        return False
                for i in range(len(name1.size),len(name2.size)):
                    result+=[float(name2.size[i])]
            if len(result) == 0: return NoneType()
            #print('result: ',result)
            return ArrayType(result,name1.eleType)
        elif type(name1.eleType) is NoneType and type(name2.eleType) is not NoneType:
            if len(name1.size) > len(name2.size):
                return False
            for i in range(0,len(name1.size)):
                    if name1.size[i] != name2.size[i]:
                        return False
            for i in range(len(name1.size),len(name2.size)):
                result+=[float(name2.size[i])]
            if len(result) == 0: return name2.eleType
            return ArrayType(result,name2.eleType)
        elif type(name1.eleType) is not NoneType and type(name2.eleType) is NoneType:
            if len(name1.size) < len(name2.size):
                return False
            for i in range(0,len(name2.size)):
                    if name1.size[i] != name2.size[i]:
                        return False
            for i in range(len(name2.size),len(name1.size)):
                result+=[float(name1.size[i])]
            if len(result) == 0: return name1.eleType
            return ArrayType(result,name1.eleType)
    def checkPriTypeEquivalent(type1,type2):  ## check 2 kieu du lieu co tuong duong nhau hay khong (gom primitive type va ArrayType, khong bao gom noneType)
        if type(type1) != type(type2): return False
        if type(type1) == ArrayType:
            if type1.size != type2.size or not HelpingTools.checkPriTypeEquivalent(type1.eleType ,type2.eleType):
                return False
        return True
    
    def getArrayType(item,dimension,names,o,canUpdate):  ## dimension la mang chua kich thuoc cua cac chieu cua mang, names gom cac NoneType Id, canUpdate cho phep cap nhat kich thuoc cua mang hay khong
        if type(item) is ArrayLiteral:
            #print(item)
            (firstEleTyp,firstEleDimension) = HelpingTools.getArrayType(item.value[0],dimension,names,o,canUpdate) 
            #print(firstEleTyp,firstEleDimension)
            #print(item.value[0],names)
            for i in range(1,len(item.value)):
                nameIth=[]
                (typEle,dimensionEle) = HelpingTools.getArrayType(item.value[i],dimension,nameIth,o,False) #ngoai phan tu dau tien ra, cac phan tu con lai ko duoc cap nhat dimesion cua mang
                #print(item[i],nameIth)
                if dimensionEle != firstEleDimension:   ## check kich thuoc giua cac phan tu cua mang
                    return (NoneType(),0)   ## return to raise error
                else:
                    if type(firstEleTyp) is NoneType and type(typEle) is not NoneType: 
                        for i in names:
                            HelpingTools.inferType(i,typEle,o)
                        firstEleTyp=typEle
                    elif type(firstEleTyp) is not NoneType and type(typEle) is NoneType:
                        if dimensionEle==0:
                            HelpingTools.inferType(item.value[i].name,firstEleTyp,o)
                        else:
                            for i in nameIth:
                                HelpingTools.inferType(i,firstEleTyp,o)
                    elif type(firstEleTyp) is not NoneType and type(typEle) is not NoneType:
                        if not HelpingTools.checkPriTypeEquivalent(firstEleTyp,typEle):
                            return (NoneType(),0)      ## return to raise error
                    else:  ## neu ca hai la NoneType thi lay ten Id de cap nhat kieu du lieu sau nay
                        for i in nameIth:
                            if i not in names:
                                names+=[i]
            #print(names)
            #print(firstEleDimension)
            if firstEleDimension!=0 and canUpdate: ## neu cac phan tu la array va co the cap nhat chieu cho mang
                dimension+=[float(firstEleDimension)]
                #print('dimension: ',dimension)
            return (firstEleTyp,len(item.value))      
        ## neu item ko phai la list thi tra ve tuple (kieu du lieu cua item,0)
        elif type(item) is Id:
            names+= [item.name]
            return (StaticChecker(item).visit(item,o),0)
        else: 
            return (StaticChecker(item).visit(item,o),0)
        
    def GetArrayType(item,names,o):  ## dimension la mang chua kich thuoc cua cac chieu cua mang, names gom cac NoneType Id, canUpdate cho phep cap nhat kich thuoc cua mang hay khong
        if type(item) is ArrayLiteral:
            #print(item)
            firstEleTyp= HelpingTools.GetArrayType(item.value[0],names,o) ## lay kieu du lieu cua phan tu dau tien cua mang
            #print(firstEleTyp)
            #print(item.value[0],names)
            for i in range(1,len(item.value)):
                nameIth=[]
                typEle = HelpingTools.GetArrayType(item.value[i],nameIth,o) #lay kieu du lieu cac phan tu con lai cua mang
                #print(item[i],nameIth)
                #print(typEle)
                #print(names)
                #print(type(firstEleTyp),type(typEle))
                if type(firstEleTyp) is NoneType  and type(typEle) is not NoneType: ## neu kieu du lieu cua phan tu dau tien la NoneType thì tất cả các phần tử đầu tiên đến trước phần tử hiện tại đều là NoneType
                    #print('go in here!!!')
                    #print('names: ',names)
                    for i in names:         ## names là list chứa các biến có kiểu dữ liệu là NoneType hoặc ArrayType có eleType là NoneType tư phần tử đầu tiên đến trước phần tử hiện tại
                        HelpingTools.inferType(i,typEle,o)              ## cập nhật kiểu cho tất cả các phần tử đầu tiên đến trước phần tử hiện tại
                    firstEleTyp=typEle  
                    if type(typEle) is ArrayType and type(typEle.eleType) is NoneType:    ## neu kieu du lieu cua phan tu hien tai la ArrayType va eleType la NoneType thi thêm vào names để cập nhật kiểu sau này
                        #print('firstEleTyp: ',firstEleTyp)
                        for i in nameIth:    ## co the sai neu co function trong array
                            if i not in names:
                                names+=[i]
                elif type(firstEleTyp) is not NoneType and type(typEle) is NoneType:    
                    for i in nameIth:       ## nameIth là list chứa các biến có kiểu dữ liệu là NoneType hoặc ArrayType có eleType là NoneType ở phần tử hiện tại
                        HelpingTools.inferType(i,firstEleTyp,o)
                    if type(firstEleTyp) is ArrayType and type(firstEleTyp.eleType) is NoneType:
                        for i in nameIth:    ## co the sai neu co function trong array
                            if i not in names:
                                names+=[i]
                        
                elif type(firstEleTyp) is not NoneType and type(typEle) is not NoneType:    ## neu ca 2 kieu du lieu khong phai la NoneType
                    if type(firstEleTyp) is ArrayType and type(typEle) is ArrayType: ## nếu cả 2 là ArrayType!!!
                        #print('both are ArrayType!!!')
                        #print(firstEleTyp,typEle)
                        if type(firstEleTyp.eleType) is not NoneType and type(typEle.eleType) is not NoneType: ## Nếu cả 2 đều có eleType khác NoneType
                            if not HelpingTools.checkPriTypeEquivalent(firstEleTyp,typEle):
                                return False
                        temp = HelpingTools.getSubArrayType(firstEleTyp,typEle) ## kiểm tra xem 2 kiểu array type (elementType một trong hai phải là NoneType) có tương đương nhau không
                        #print('temp: ',temp)
                        if temp is False: return False
                        if type(temp) is not NoneType:
                            if len(firstEleTyp.size) < len(typEle.size) or type(firstEleTyp.eleType) is NoneType : ## nếu hai array tương đương thì chắc chắn array có len dài hơn phải được suy ra từ array còn lại
                                #print('go here!!!')                    ## Hoặc array có eleType không phải là Nonetype phải được suy ra từ array còn lại (TH hai len bằng nhau)
                                firstEleTyp=typEle
                                for i in names:
                                    HelpingTools.inferType(i,temp,o)
                            else:
                                for i in nameIth:
                                    HelpingTools.inferType(i,temp,o)
                        if type(typEle) is ArrayType and type(typEle.eleType) is NoneType:    ## neu kieu du lieu cua phan tu hien tai la ArrayType va eleType la NoneType thi thêm vào names để cập nhật kiểu sau này
                            for i in nameIth:    ## co the sai neu co function trong array
                                if i not in names:
                                    names+=[i] 
                    elif not HelpingTools.checkPriTypeEquivalent(firstEleTyp,typEle): ## nếu cả 2 không phải đồng thời là ArrayType thì kiểm tra xem chúng có tương đương nhau không
                        return False
                else:  ## neu ca hai la NoneType thi lay ten Id de cap nhat kieu du lieu sau nay
                    for i in nameIth:    ## co the sai neu co function trong array
                        if i not in names:
                            names+=[i]
            #print(names)
            if type(firstEleTyp) is ArrayType:
                return ArrayType([float(len(item.value))]+firstEleTyp.size,firstEleTyp.eleType) ## 
            #print('hehe')
            return ArrayType([float(len(item.value))],firstEleTyp)   
        ## neu item ko phai la list thi tra ve tuple (kieu du lieu cua item,0)
        else: 
            getType= StaticChecker(item).visit(item,o)
            if type(getType) is NoneType :  ## gap Id voi kieu du lieu chua xac dinh
                names+=[item.name]
            return getType
    def customVisitId(name,o,isFunction=False):
        for scope in o:
            for i in scope:
                if i.name == name:
                    if isFunction and type(i.mtype) is FunctionType:
                        return i.mtype
                    if not isFunction and type(i.mtype) is not FunctionType:
                        return i.mtype
        if isFunction:
            raise Undeclared(Function(),name)
        else: raise Undeclared(Identifier(),name)
                    
        
    def printO(o):
        for scope in o:
            for item in scope:
                print(item.name,item.mtype)
            print('-------------------')
class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast):
        self.ast=ast
        self.io=[]
    def check(self):
        self.visit(self.ast, self.io)
        return "successful"
    #program: newline_list decl_list newline_list EOF ;
    def visitProgram(self,ctx:Program,o:object):
        #print(self.ast)
        o=[[]]
        ## declare build-in functions
        o[0]+=[Symbol('readNumber',FunctionType([],True,NumberType()))]
        o[0]+=[Symbol('writeNumber',FunctionType([NumberType()],True,VoidType()))]
        o[0]+=[Symbol('readBool',FunctionType([],True,BoolType()))]
        o[0]+=[Symbol('writeBool',FunctionType([BoolType()],True,VoidType()))]
        o[0]+=[Symbol('readString',FunctionType([],True,StringType()))]
        o[0]+=[Symbol('writeString',FunctionType([StringType()],True,VoidType()))]
        for i in ctx.decl:
            if isinstance(i,VarDecl):
                if HelpingTools.checkRedeclared(i.name.name,o):
                    raise Redeclared("Variable",i.name.name)
            self.visit(i, o)
            #print('program',len(o[0]))
        for scope in o:
            for item in scope:
                if type(item.mtype) is FunctionType and item.mtype.haveBody == False:
                    raise NoDefinition(item.name)
        flagEntry= False
        #HelpingTools.printO(o)
        for item in o[len(o)-1]:
            if type(item.mtype) is FunctionType and item.name == 'main':
                flagEntry = True
                break
        if not flagEntry:
            raise NoEntryPoint()
    def visitVarDecl(self,ctx:VarDecl,o:object): 
        if HelpingTools.checkRedeclared(ctx.name.name,o):
                raise Redeclared("Variable",ctx.name.name)
        #print('Vardecl: ', ctx)
        if type(ctx.varType) == type(None):
                o[0]+= [Symbol(ctx.name.name,NoneType())]
        else: 
            o[0]+=[Symbol(ctx.name.name,ctx.varType)]
        if type(ctx.varInit) != type(None):
            names=False
            if type(ctx.varInit) is ArrayLiteral:
                (rhs,names)=self.visit(ctx.varInit,o)
                #print(rhs,names)
            else: 
                rhs=self.visit(ctx.varInit,o)
            lhs=self.visit(ctx.name,o)
            if type(rhs) is CannotInferType:
                raise TypeCannotBeInferred(ctx)
            elif type(rhs) is NoneType and type(lhs) is NoneType:   ## both are NoneType
                raise TypeCannotBeInferred(ctx)
            elif type(rhs) is NoneType and type(lhs) is not NoneType: ## rhs is NoneType
                if type(ctx.varInit) is CallExpr:
                    HelpingTools.inferType(ctx.varInit.name.name,ctx.varType,o,True)
                HelpingTools.inferType(ctx.varInit.name,ctx.varType,o)
            elif type(rhs) is not NoneType and type(lhs) is NoneType: ## ctx.varType is NoneType
                
                if type(rhs) is ArrayType and type(rhs.eleType) is NoneType:
                    raise TypeCannotBeInferred(ctx)
                HelpingTools.inferType(ctx.name.name,rhs,o)
            else:                                                               ## both are not NoneType
                if type(rhs) != type(lhs):                              ## type mismatch
                    #print(type(rhs)is not NoneType,type(ctx.varType) == type(None))
                    raise TypeMismatchInStatement(ctx)
                if type(rhs) == ArrayType and type(lhs) is ArrayType:   ## check array type

                    if type(rhs.eleType) is not NoneType and not HelpingTools.checkPriTypeEquivalent(rhs,lhs): 
                        raise TypeMismatchInStatement(ctx)
                    temp = HelpingTools.getSubArrayType(lhs,rhs)
                    if temp is False:
                        raise TypeMismatchInStatement(ctx)
                    if names != False:      ## Loại trừ TH vế phải trả về arrayType nhưng nó ko phải là arrayLiteral (kết quả trả về từ một func)
                        for i in names:
                                HelpingTools.inferType(i,lhs.eleType,o)
        #print('VarDecl')
        #HelpingTools.printO(o)
        return (VoidType(),ctx)
            
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        #print(ctx)
        param_list=[]
        env = [[]] + o
        
        for i in ctx.param:
            param_list+=[i.varType]
            if HelpingTools.checkRedeclared(i.name.name,env):
                raise Redeclared("Parameter",i.name.name)
            self.visit(i,env)
        noDeclaration = True
        ele=0                # check redeclare function
        for ele in range(0,len(o[0])):
            if o[0][ele].name == ctx.name.name and type(o[0][ele].mtype) is FunctionType:  ## phát hiện ra function có cùng tên
                #print(ctx.name.name,o[0][ele].mtype.param,o[0][ele].mtype.haveBody,o[0][ele].mtype.returnType)
                if o[0][ele].mtype.haveBody == False and o[0][ele].mtype.param == param_list:     ## kiểm tra xem có rơi vào TH only declaration không
                    #print('returnType infered: ',o[0][ele].mtype.returnType)
                    noDeclaration=False
                    break
                else:                                                                           ## nếu không thì raise redeclare
                    raise Redeclared("Function",ctx.name.name)
        #print(ctx.name.name,    noDeclaration)        
        if noDeclaration:   
            newFunc=[Symbol(ctx.name.name,FunctionType(param_list,False,NoneType()))]
            o[0]+=newFunc
        #print('FuncDecl')
        #print(len(o[0]))
        
        #print(len(o[0]))
        if type(ctx.body) is  type(None):  ## nếu func đã được khai báo và giờ được khai báo tiếp (không có body)
            if noDeclaration == False:
                raise Redeclared(ctx.name.name,"Function")
        else:  ## nếu func có body
            #env[1]+=newFunc                     ## thêm tên func vào scope trước đó của env
            if type(ctx.body) is Block:
                returnType=(VoidType(),ctx.body)
                for i in ctx.body.stmt:
            
                    stmt=self.visit(i,env)
            # print("hehe")
            # HelpingTools.printO(newScope)
            #print('stmt',stmt)
                    if type(stmt[1]) is  Return and type(returnType[1]) is not Return:
                        returnType=stmt
            else:
                returnType=self.visit(ctx.body,env)     ## kiểm tra kiểu trả về của func
            
                #print('function return type: ',returnType)
            #print(returnType)
            #HelpingTools.printO(env)
            if noDeclaration:
                newFunc[0].mtype.returnType=returnType[0]  ## cập nhật kiểu trả về của func
                newFunc[0].mtype.haveBody=True
                o[0]=o[0][:-1] + newFunc                ## xóa func có kiểu trả về NoneType ra khỏi o và thêm func có kiểu trả về đã cập nhật vào o
            else:
                #print(ctx.name.name,returnType[0],o[0][ele].mtype.returnType)
                if type(o[0][ele].mtype.returnType) is NoneType:
                    o[0][ele].mtype.returnType=returnType[0]
                elif type(returnType[0]) != type(o[0][ele].mtype.returnType):
                    raise TypeMismatchInStatement(returnType[1])
                o[0][ele].mtype.haveBody=True

    def visitAssign(self,ctx,o:object):
        #print(ctx)
        if type(ctx.rhs) is ArrayLiteral:
            (rhs,names)=self.visit(ctx.rhs,o)
        else:
            rhs = self.visit(ctx.rhs,o)
        #print('rhs: ',type(rhs))
        lhs = self.visit(ctx.lhs,o)
        if type(lhs) is CannotInferType or type(rhs) is CannotInferType:
            raise TypeCannotBeInferred(ctx)
        #print('lhs: ',type(lhs))
        if type(lhs) is VoidType:
            raise TypeMismatchInStatement(ctx)
        elif type(lhs) is NoneType and type(rhs) is NoneType:
            raise TypeCannotBeInferred(ctx)   
        elif type(lhs) is NoneType and type(rhs) is not NoneType:
            if type(rhs) is ArrayType and type(rhs.eleType) is NoneType:
                raise TypeCannotBeInferred(ctx)
            HelpingTools.inferType(ctx.lhs.name,rhs,o)
        elif type(lhs) is not NoneType and type(rhs) is  NoneType: ## bên trái không thể là arrayType([...],NoneType) vì nếu có thì trước đó đã raise typeCannotBeInferred
            HelpingTools.inferType(ctx.rhs.name,lhs,o)
        else:
            if type(rhs) == ArrayType and type(lhs) == ArrayType:   ## check array type
                #print('go here!!!')
                if type(rhs.eleType) is not NoneType and type(lhs.eleType) is not NoneType:
                    if not HelpingTools.checkPriTypeEquivalent(rhs,lhs): 
                        raise TypeMismatchInStatement(ctx)
                temp = HelpingTools.getSubArrayType(lhs,rhs)
                if temp is False:
                    raise TypeMismatchInStatement(ctx)
                for i in names:
                        HelpingTools.inferType(i,lhs,o)
            elif not HelpingTools.checkPriTypeEquivalent(rhs,lhs):
                raise TypeMismatchInStatement(ctx)
        return (VoidType(),ctx)
    def visitIf(self,ctx,o:object):
        returnType=(VoidType(),ctx)
        ifExpr=self.visit(ctx.expr,o)
        if type(ifExpr) is CannotInferType:
            raise TypeCannotBeInferred(ctx)
        elif type(ifExpr) is NoneType:
            HelpingTools.inferType(ifExpr.name,BoolType(),o)
        elif type(ifExpr) is not BoolType:
            raise TypeMismatchInStatement(ctx)
        themStmtType=self.visit(ctx.thenStmt,o)
        if type(themStmtType[1]) is Return and type(returnType[1]) is not Return:
            returnType=themStmtType
        for i in ctx.elifStmt:
            expr=self.visit(i[0],o)
            if type(expr) is CannotInferType:
                raise TypeCannotBeInferred(ctx)
            elif type(expr) is NoneType:
                HelpingTools.inferType(expr.name,BoolType(),o)
            elif type(expr) is not BoolType:
                raise TypeMismatchInStatement(ctx)
            stmtType=self.visit(i[1],o)
            if not HelpingTools.checkPriTypeEquivalent(stmtType[0],returnType[0]): 
                raise TypeMismatchInStatement(stmtType[1])
        return returnType
    def visitFor(self,ctx,o:object): 
        returnType = (VoidType(),ctx)
        Id=self.visit(ctx.name,o)
        if type(Id) is NoneType:
            HelpingTools.inferType(ctx.name.name,NumberType(),o)
            Id=NumberType()   
        elif type(Id) is not NumberType:
            raise TypeMismatchInStatement(ctx)
        conExpr=self.visit(ctx.condExpr,o)
        if type(conExpr) is CannotInferType:
            raise TypeCannotBeInferred(ctx)
        elif type(conExpr) is NoneType:
            HelpingTools.inferType(ctx.condExpr.name,BoolType(),o)
        elif type(conExpr) is not BoolType:
            raise TypeMismatchInStatement(ctx)
        updExpr=self.visit(ctx.updExpr,o)
        if type(updExpr) is CannotInferType:
            raise TypeCannotBeInferred(ctx)
        elif type(updExpr) is NoneType:
            HelpingTools.inferType(ctx.updExpr.name,NumberType(),o)
        elif type(updExpr) is not NumberType:
            raise TypeMismatchInStatement(ctx)
        global NumOfLoop
        NumOfLoop+=1
        stmt=self.visit(ctx.body,o)
        NumOfLoop-=1
        if type(stmt[1]) is Return and type(returnType[1]) is not Return:
            returnType=stmt
        return returnType
    def visitBreak(self,ctx,o:object): 
        if NumOfLoop==0:
            raise MustInLoop('break')
        return (VoidType(),ctx)
    def visitContinue(self,ctx,o:object):
        if NumOfLoop==0:
            raise MustInLoop('continue')
        return (VoidType(),ctx)
    def visitReturn(self,ctx,o:object):
        if type(ctx.expr) is not type(None):
            returnType=self.visit(ctx.expr,o)
            #print('return: ',returnType)
            if type(returnType) is CannotInferType:
                raise TypeCannotBeInferred(ctx)
            elif type(returnType) is NoneType:
                raise TypeCannotBeInferred(ctx)
            return (returnType,ctx)
        return (VoidType(),ctx)
    def visitCallStmt(self,ctx,o:object):
        Id = HelpingTools.customVisitId(ctx.name.name,o,True)
        #print('callstmt: ')
        #print(Id.param,Id.haveBody,Id.returnType)
        if type(Id.returnType) is NoneType:
            HelpingTools.inferType(ctx.name.name,VoidType(),o,True)
        elif type(Id.returnType) is not VoidType:
            #print('go here!!!')
            raise TypeMismatchInStatement(ctx)
        if len(ctx.args) != len(Id.param):
            raise TypeMismatchInStatement(ctx)
        for i in range(0,len(ctx.args)):
            arg = self.visit(ctx.args[i],o)
            if type(arg) is CannotInferType:
                raise TypeCannotBeInferred(ctx)
            elif type(arg) is NoneType:
                HelpingTools.inferType(ctx.args[i].name,Id.param[i],o)
            elif not HelpingTools.checkPriTypeEquivalent(arg,Id.param[i]):
                
                raise TypeMismatchInStatement(ctx)
        return (VoidType(),ctx)
    def visitBlock(self,ctx,o:object):
        #print('block')
        returnType=(VoidType(),ctx)
        newScope=[[]]+o
        #HelpingTools.printO(newScope)
        for i in ctx.stmt:
            
            stmt=self.visit(i,newScope)
            # print("hehe")
            # HelpingTools.printO(newScope)
            #print('stmt',stmt)
            if type(stmt[1]) is  Return and type(returnType[1]) is not Return:
                returnType=stmt
        
        #print('block')
        #HelpingTools.printO(newScope)
        #print(returnType)
        return returnType
    
    def visitBinaryOp(self,ctx,o):
        #print(ctx)
        #print('!!!!!!!!!!!!!!!!!!!!')
        #HelpingTools.printO(o)
        left = self.visit(ctx.left,o)
        right = self.visit(ctx.right,o)
        if type(left) is CannotInferType or type(right) is CannotInferType:
            return CannotInferType()
        #print('left: ',left)
        #print('right: ',type(right))
        if ctx.op in ['+','-','*','/','%']:   # operantype is numbertype, return type is numbertype
            if type(right) not in [NoneType,NumberType] or type(left) not in [NoneType,NumberType]:
                raise TypeMismatchInExpression(ctx)
            if type(left) is NoneType:
                if type(ctx.left) is CallExpr:
                    HelpingTools.inferType(ctx.left.name.name,NumberType(),o,True)
                else:
                    HelpingTools.inferType(ctx.left.name,NumberType(),o)
                #print('infer left')
                #HelpingTools.printO(o)
                left = NumberType()
            if type(right) is NoneType:
                if type(ctx.right) is CallExpr:
                    HelpingTools.inferType(ctx.right.name.name,NumberType(),o,True)
                else:
                    HelpingTools.inferType(ctx.right.name,NumberType(),o)
                right = NumberType()
            return NumberType()
        elif ctx.op in ['and','or']: ## operantype is booltype, return type is booltype
            if type(right) not in [NoneType,BoolType] or type(left) not in [NoneType,BoolType]:
                raise TypeMismatchInExpression(ctx)
            if type(left) is NoneType:
                if type(ctx.left) is CallExpr:
                    HelpingTools.inferType(ctx.left.name.name,NumberType(),o,True)
                else:
                    HelpingTools.inferType(ctx.left.name,BoolType(),o)
                left = BoolType()
            if type(right) is NoneType:
                if type(ctx.right) is CallExpr:
                    HelpingTools.inferType(ctx.right.name.name,NumberType(),o,True)
                else:
                    HelpingTools.inferType(ctx.right.name,BoolType(),o)
                right = BoolType()
            return BoolType()
        elif ctx.op in ['...']: ## operantype is stringtype, return type is stringtype
            if type(right) not in [NoneType,StringType] or type(left) not in [NoneType,StringType]:
                raise TypeMismatchInExpression(ctx)
            if type(left) is NoneType:
                if type(ctx.left) is CallExpr:
                    HelpingTools.inferType(ctx.left.name.name,StringType(),o,True)
                else:
                    HelpingTools.inferType(ctx.left.name,StringType(),o)
                left = StringType()
            if type(right) is NoneType:
                if type(ctx.right) is CallExpr:
                    HelpingTools.inferType(ctx.right.name.name,StringType(),o,True)
                else:
                    HelpingTools.inferType(ctx.right.name,StringType(),o)
                right = StringType()
            return StringType()
        elif ctx.op in['<','<=','>','>=','!=','=']: ## operantype is numbertype, return type is booltype
            if type(right) not in [NoneType,NumberType] or type(left) not in [NoneType,NumberType]:
                raise TypeMismatchInExpression(ctx)
            if type(left) is NoneType:
                if type(ctx.left) is CallExpr:
                    HelpingTools.inferType(ctx.left.name.name,NumberType(),o,True)
                else:
                    HelpingTools.inferType(ctx.left.name,NumberType(),o)
                left = NumberType()
            if type(right) is NoneType:
                if type(ctx.right) is CallExpr:
                    HelpingTools.inferType(ctx.right.name.name,NumberType(),o,True)
                else:
                    HelpingTools.inferType(ctx.right.name,NumberType(),o)
                right = NumberType()
            return BoolType()
        elif ctx.op in['==']:   ## operantype is numbertype or stringtype, return type is booltype
            if type(right) not in [NoneType,StringType] or type(left) not in [NoneType,StringType]:
                raise TypeMismatchInExpression(ctx)
            if type(left) is NoneType:
                if type(ctx.left) is CallExpr:
                    HelpingTools.inferType(ctx.left.name.name,NumberType(),o)
                else:
                    HelpingTools.inferType(ctx.left.name,StringType(),o)
                left = StringType()
            if type(right) is NoneType:
                if type(ctx.right) is CallExpr:
                    HelpingTools.inferType(ctx.right.name.name,NumberType(),o)
                else:
                    HelpingTools.inferType(ctx.right.name,StringType(),o)
                right = StringType()
            return BoolType()
        #HelpingTools.printO(o)
        raise TypeMismatchInExpression(ctx)
    def visitUnaryOp(self,ctx,o):
        operand = self.visit(ctx.operand,o)
        if type(operand) is CannotInferType:
            return CannotInferType()
        #print('Unaryop: ', operand)
        if ctx.op in ['-','+']:
            if type(operand) not in [NoneType,NumberType]:
                    raise TypeMismatchInExpression(ctx)
            else:
                if type(ctx.operand) is CallExpr:
                    HelpingTools.inferType(ctx.operand.name.name,NumberType(),o,True)
                else:
                    HelpingTools.inferType(ctx.operand.name,NumberType(),o)
                operand = NumberType()
            return NumberType()
        elif ctx.op in ['not']:
            
            if type(operand) not in [NoneType,BoolType]:
                raise TypeMismatchInExpression(ctx)
            else:
                if type(ctx.operand) is CallExpr:
                    HelpingTools.inferType(ctx.operand.name.name,NumberType(),o,True)
                else:
                    HelpingTools.inferType(ctx.operand.name,BoolType(),o)
                operand = BoolType()
            return BoolType()

    def visitId(self,ctx:Id,o:object):
        returnType= HelpingTools.customVisitId(ctx.name,o)
        return returnType   
    def visitArrayCell(self,ctx:ArrayCell,o:object):
        arr=self.visit(ctx.arr,o)
        if type(arr) is NoneType:       ## if arr is NoneType, can not infer type of arr
            return CannotInferType()  
        elif type(arr) is not ArrayType: ## if arr is not ArrayType, raise error
            raise TypeMismatchInExpression(ctx)
        for i in ctx.idx:
            idx=self.visit(i,o)
            if type(idx) is CannotInferType:
                return CannotInferType()
            elif type(idx) is NoneType:
                if type(i) is CallExpr:
                    HelpingTools.inferType(i.name.name,NumberType(),o,True)
                HelpingTools.inferType(i.name.name,NumberType(),o)
            elif type(idx) is not NumberType:
                raise TypeMismatchInExpression(ctx)
        if len(ctx.idx) > len(arr.size):   ## invalid subscript
            raise TypeMismatchInExpression(ctx)
        elif len(ctx.idx) < len(arr.size):      ## return type of array cell is ArrayType
            return ArrayType(arr.size[len(ctx.idx):],arr.eleType)
        return arr.eleType
    def visitCallExpr(self,ctx:CallExpr,o:object):
       # print('callExpr')
        #HelpingTools.printO(o)
        Id = HelpingTools.customVisitId(ctx.name.name,o,True)
        # for i in Id.param:
        #     print(type(i))
        if type(Id) is not FunctionType:
            raise TypeMismatchInExpression(ctx)
        if type(Id.returnType) is VoidType:
            raise TypeMismatchInExpression(ctx)
        if len(ctx.args) != len(Id.param):
            raise TypeMismatchInExpression(ctx)
        for i in range(0,len(ctx.args)):
            arg = self.visit(ctx.args[i],o)
            print (ctx.args[i])
            print(arg, Id.param[i])
            if type(arg) is CannotInferType:
                return CannotInferType()
            elif type(arg) is NoneType:
                if type(ctx.args[i]) is CallExpr:
                    #print('go here!!!')
                    HelpingTools.inferType(ctx.args[i].name.name,Id.param[i],o,True)
                HelpingTools.inferType(ctx.args[i].name,Id.param[i],o)
            elif not HelpingTools.checkPriTypeEquivalent(arg,Id.param[i]):
                #print('go here!!!')
                raise TypeMismatchInExpression(ctx)
        return Id.returnType
    def visitNumberLiteral(self,ctx:NumberLiteral,o:object):
        return NumberType()
    def visitBooleanLiteral(self,ctx:BooleanLiteral,o:object):
        return BoolType()
    def visitStringLiteral(self,ctx:StringLiteral,o:object):
        return StringType()
    def visitArrayLiteral(self,ctx:ArrayLiteral,o:object): 
        #print(ctx)
        #HelpingTools.printO(o)
        names=[]
        result= HelpingTools.GetArrayType(ctx,names,o) 
        #print('result: ',result)
        #print('result: ',result)
        #print(type(result.eleType) is NoneType)
        #print(ctx)
        
        #print(typ,lenght)
        if result is False:
            raise TypeMismatchInExpression(ctx)
        return (result,names)