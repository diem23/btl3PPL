from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
class NoneType: pass
class Symbol:
    def __init__(self, name, mtype, isFunc = False, params = []):
        self.name = name
        self.mtype = mtype
        self.isFunc = isFunc
        self.params = params
class HelpingTools:
    def checkRedeclared(name,o):
        for item in o[0]:
            if item.name == name:
                return True
        return False
    def inferType(name,Type,o):
        for scope in o:
            for item in scope:
                if item.name == name:
                    #print('item name: ',item.name)
                    #print('item type: ',item.mtype)
                    if type(item.mtype) is ArrayType and type(Type) is ArrayType:
                        #print('infer arrayType')
                        item.mtype.eleType = Type.eleType
                        item.mtype.size += Type.size
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
    # def getArrayType(item,o):
    #     dimension=[]
    #     while type(item) is list:
    #         flag=HelpingTools.getArrayType(item[0],o)
    #         if  not flag: return False
    #         for i in range(1,len(item)):
    #             element = HelpingTools.getArrayType(item[i],o)
    #             if not element: return False
    #             if type(element.eleType) is NoneType:
    #                 if type(flag.eleType) is not NoneType: 
    #                     HelpingTools.inferType(item[i].name,flag.eleType,o)
    #             elif type(flag.eleType) is NoneType:
    #                 i = 1
    #                 HelpingTools.inferType(item[0].name,element.eleType,o)
    #                 flag.eleType = element.eleType
    #                 flag.size = element.size
    #             elif element.size != flag.size or not HelpingTools.checkPriTypeEquivalent(element.eleType,flag.eleType):
    #                 return False
    #         dimension.append(float(len(item)))
    #         item=item[0]
    #     print(type(item))
    #     print (type(item) is Id, type(item) is ArrayLiteral)
    #     return ArrayType(dimension,StaticChecker(item).visit(item,o))
    
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
                if type(firstEleTyp) is NoneType and type(typEle) is not NoneType: ## neu kieu du lieu cua phan tu dau tien la NoneType thì tất cả các phần tử đầu tiên đến trước phần tử hiện tại đều là NoneType
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
        o[0]+=[Symbol('readNumber',NumberType(),True)]
        o[0]+=[Symbol('writeNumber',VoidType(),True,[NumberType()])]
        o[0]+=[Symbol('readBool',BoolType(),True,)]
        o[0]+=[Symbol('writeBool',VoidType(),True,[BoolType()])]
        o[0]+=[Symbol('readString',StringType(),True,)]
        o[0]+=[Symbol('writeString',VoidType(),True,[StringType()])]
        for i in ctx.decl:
            if isinstance(i,VarDecl):
                if HelpingTools.checkRedeclared(i.name.name,o):
                    raise Redeclared(i.name.name,"Variable")
            elif isinstance(i,FuncDecl):
                if HelpingTools.checkRedeclared(i.name.name,o):
                    raise Redeclared(i.name.name,"Function")
            self.visit(i, o)
        flagEntry= False
        HelpingTools.printO(o)
        for item in o[len(o)-1]:
            if item.isFunc and item.name == 'main':
                flagEntry = True
                break
        if not flagEntry:
            raise NoEntryPoint()
    def visitVarDecl(self,ctx:VarDecl,o:object): 
        if type(ctx.varInit) != type(None):
            if type(ctx.varInit) is ArrayLiteral:
                (rhs,names)=self.visit(ctx.varInit,o)
                #print(rhs,names)
            else: 
                rhs=self.visit(ctx.varInit,o)
            if type(rhs) is NoneType and type(ctx.varType) == type(None):   ## both are NoneType
                raise TypeCannotBeInferred(ctx.name.name)
            elif type(rhs) is NoneType and type(ctx.varType) == type(None): ## rhs is NoneType
                HelpingTools.inferType(ctx.varInit.name,ctx.value,o)
                o[0]+=[Symbol(ctx.name.name,ctx.varType)]
            elif type(rhs) is not NoneType and type(ctx.varType) == type(None): ## ctx.varType is NoneType
                o[0]+=[Symbol(ctx.name.name,rhs)]
            else:                                                               ## both are not NoneType
                if type(rhs) != type(ctx.varType):                              ## type mismatch
                    #print(type(rhs)is not NoneType,type(ctx.varType) == type(None))
                    raise TypeMismatchInStatement(ctx)
                if type(rhs) == ArrayType and type(ctx.varType) == ArrayType:   ## check array type

                    if type(rhs.eleType) is not NoneType and not HelpingTools.checkPriTypeEquivalent(rhs,ctx.varType): 
                        raise TypeMismatchInStatement(ctx)
                    temp = HelpingTools.getSubArrayType(ctx.varType,rhs)
                    if temp is False:
                        raise TypeMismatchInStatement(ctx)
                    for i in names:
                            HelpingTools.inferType(i,ctx.varType.eleType,o)
                    
                    
                o[0]+=[Symbol(ctx.name.name,ctx.varType)]
        else:   ## no initialization
            if type(ctx.varType) == type(None):
                o[0]+= [Symbol(ctx.name.name,NoneType())]
            else: o[0]+=[Symbol(ctx.name.name,ctx.varType)]
    def BinOp(self,ctx,o):
        #print(ctx)
        left = self.visit(ctx.left,o)
        right = self.visit(ctx.right,o)
        if ctx.op in ['+','-','*','/','%']:
            if type(right) is not NoneType and type(right) is not NoneType:
                if not (type(right) is NumberType and type(left) is NumberType):
                    raise TypeMismatchInExpression(ctx)
            if type(left) is NoneType:
                HelpingTools.inferType(ctx.left.name,NumberType(),o)
                left = NumberType()
            if type(right) is NoneType:
                HelpingTools.inferType(ctx.right.name,NumberType(),o)
                right = NumberType()
            return NumberType()
        elif ctx.op in ['and','or']:
            if type(right) is not NoneType and type(right) is not NoneType:
                if not (type(right) is BoolType and type(left) is BoolType):
                    raise TypeMismatchInExpression(ctx)
            if type(left) is NoneType:
                HelpingTools.inferType(ctx.left.name,BoolType(),o)
                left = BoolType()
            if type(right) is NoneType:
                HelpingTools.inferType(ctx.right.name,BoolType(),o)
                right = BoolType()
            return BoolType()
        elif ctx.op in ['...']:
            if type(right) is not NoneType and type(right) is not NoneType:
                if not (type(right) is StringType and type(left) is StringType):
                    raise TypeMismatchInExpression(ctx)
            if type(left) is NoneType:
                HelpingTools.inferType(ctx.left.name,StringType(),o)
                left = StringType()
            if type(right) is NoneType:
                HelpingTools.inferType(ctx.right.name,StringType(),o)
                right = StringType()
            return StringType()
        elif ctx.op in['<','<=','>','>=','!=','=']:
            if type(right) is not NoneType and type(right) is not NoneType:
                if not (type(right) is NumberType and type(left) is NumberType):
                    raise TypeMismatchInExpression(ctx)
            if type(left) is NoneType:
                HelpingTools.inferType(ctx.left.name,NumberType(),o)
                left = NumberType()
            if type(right) is NoneType:
                HelpingTools.inferType(ctx.right.name,NumberType(),o)
                right = NumberType()
            return BoolType()
        elif ctx.op in['==']:
            if type(right) is not NoneType and type(right) is not NoneType:
                if not (type(right) is StringType and type(left) is StringType):
                    raise TypeMismatchInExpression(ctx)
            if type(left) is NoneType:
                HelpingTools.inferType(ctx.left.name,StringType(),o)
                left = StringType()
            if type(right) is NoneType:
                HelpingTools.inferType(ctx.right.name,StringType(),o)
                right = StringType()
            return BoolType()
        raise TypeMismatchInExpression(ctx)
    def visitId(self,ctx:Id,o:object):
        #print('visitId')
        for scope in o:
            for item in scope:
                if item.name == ctx.name:
                    #print(item.name,item.mtype)
                    return item.mtype
        
        raise Undeclared(Identifier(),ctx.name)    
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
        #print(type(result.eleType) is NoneType)
        #print(ctx)
        
        #print(typ,lenght)
        if result is False:
            raise TypeMismatchInExpression(ctx)
        return (result,names)