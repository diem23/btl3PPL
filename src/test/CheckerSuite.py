import unittest
from TestUtils import TestChecker

from AST import *
from main.zcode.utils.AST import *


class CheckerSuite(unittest.TestCase):
    ##invalid_arrayliteral
    def test_001(self):
        input = """var a <- [[1,2],[1,2,3]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 401))
    def test_002(self):
        input = """
        string b
        var a <- [[1,2,4],[1,2,3],[b,b,b]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(4.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(b), Id(b), Id(b)))"
        self.assertTrue(TestChecker.test(input, expect, 402))
    def test_003(self):
        input = """var a <- [[1,2,3],[1,2,3],[1,2,3,4],[1,2,3]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 403))
    def test_004(self):
        input = """
        dynamic t
        var a <- [[1,2],[1,t],[1,2,3]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), Id(t)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
        self.assertTrue(TestChecker.test(input, expect, 404))
    def test_005(self):
        input = """
        dynamic ans
        dynamic temp <- "abc"
        var a <- [[1,2],[1,ans],[temp,ans]]
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), Id(ans)), ArrayLit(Id(temp), Id(ans)))"
        self.assertTrue(TestChecker.test(input, expect, 405))
    def test_006(self):
        input = """
        dynamic ans
        number a[3.0,4.0] <- [[ans,ans,ans,ans],[1,2,ans,4],[1,2,3,4]]
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 406))
    def test_007(self):
        input = """number a[2,3] <- [[2,3],[2,3]]
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(2.0), NumLit(3.0))))"
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test_008(self):
        input = """
        dynamic t
        dynamic b
        dynamic c
        dynamic d
        dynamic e
        dynamic f
        number a[2,3] <- [[b,t,d],[c,e,f]]
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 408))
    def test_009(self):
        input = """
        dynamic t
        dynamic b
        dynamic c
        dynamic d
        dynamic e
        dynamic f
        number a[2.0,3.0,2.0] <- [[[b,c],[d,d],[t,f]],[[e,e],[e,t],[f,d]]]
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 409))
    def test_010(self):
        input = """
        dynamic t
        dynamic b
        dynamic c
        dynamic d
        dynamic e
        dynamic f
        number a[2.0,3.0,2.0] <- [[[1,c],[3,d],[t,f]],[[b,9],[e,t],[2,d]]]
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 410))
    def test011(self):
        input = """
    dynamic a
    dynamic b
    dynamic c
    number arr[1, 2,2] <- [[a, b]]
    ## number c[2, 2] <- arr
"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 411))
    def test012(self):
        input = """
dynamic a
    dynamic b
    dynamic c
    dynamic d
    var e <- 1
    var x <- [a, [b], [[c]], [[[d, e]]] ]
    ##c <- [-10, 2 / 3 % 0.75]
    ##b <- [c]
    ##a <- [b]
"""
        expect = "No Entry Point"
        
        self.assertTrue(TestChecker.test(input, expect, 412))
    def test013(self):
        input = """
dynamic a
    dynamic b
    dynamic c
    dynamic d
    dynamic e
    var x <- [a, [b], [[c]], [[[d, e]]] ]
    ##c <- [-10, 2 / 3 % 0.75]
    ##b <- [c]
    ##a <- [b]
"""
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, var, ArrayLit(Id(a), ArrayLit(Id(b)), ArrayLit(ArrayLit(Id(c))), ArrayLit(ArrayLit(ArrayLit(Id(d), Id(e))))))"
        self.assertTrue(TestChecker.test(input, expect, 413)) 
    def test014(self):
        input = """
        func b()
        dynamic b
        number a[2,3]<- [[b(),b,b],[b,b,b()]]
        func b()
        return true
        """
        result="Type Mismatch In Statement: Return(BooleanLit(True))"
        self.assertTrue(TestChecker.test(input,result,414))
    def test015(self):
        input ="""
        func main()
        begin
        number a <- [a,a,a,a,a]
        end
        """
        expect="Type Mismatch In Statement: VarDecl(Id(a), NumberType, None, ArrayLit(Id(a), Id(a), Id(a), Id(a), Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,415))
    def test016(self):
        input ="""
        func a()
        number a
        func main()
        begin
            number a[5] <- [a(),2,3,4,5]
        end
        func a()
            return
    """
        expect="Type Mismatch In Statement: Return()"
        self.assertTrue(TestChecker.test(input,expect,416))
    def test017(self):
        input="""
        dynamic a
        var c <-[a,[a],[[a,a,a]]]
        """
        expect="Type Cannot Be Inferred: VarDecl(Id(c), None, var, ArrayLit(Id(a), ArrayLit(Id(a)), ArrayLit(ArrayLit(Id(a), Id(a), Id(a)))))"
        self.assertTrue(TestChecker.test(input,expect,417))
    def test018(self):
        input="""
        dynamic a
        dynamic b
        dynamic c
        dynamic d
        dynamic e
        dynamic f
        var g <-[a,[b],[[c,d,e]]]
        """
        expect="Type Cannot Be Inferred: VarDecl(Id(g), None, var, ArrayLit(Id(a), ArrayLit(Id(b)), ArrayLit(ArrayLit(Id(c), Id(d), Id(e)))))"
        self.assertTrue(TestChecker.test(input,expect,418))
    def test019(self):
        input="""
       
        
       
        number d
        var c <-[c,c,c,c,d]   ## visit bien truoc roi moi visit init value
        """
        expect="Type Mismatch In Statement: VarDecl(Id(c), None, var, ArrayLit(Id(c), Id(c), Id(c), Id(c), Id(d)))"
        self.assertTrue(TestChecker.test(input,expect,419))
    def test020(self):
        input="""
        dynamic a
        dynamic b
        dynamic c
        dynamic d
        dynamic e
        dynamic f
        string g[6,99,100,101] <-[a,b,c,d,e,f]
        """
        expect="No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,420))
    # test func_para
    def test021(self):
        input="""
        func a1(number a,number b, number c)
        func main()
        begin
            number a <- 1
            a1(1,2,3)
        end
        func a(number a,number b, number c)
        begin
            a<-a1(a,b,c)
            return "lo ve du"
        end
        """
        expect="Type Mismatch In Expression: CallExpr(Id(a1), [Id(a), Id(b), Id(c)])"
        self.assertTrue(TestChecker.test(input,expect,421))
        
    def test022(self):
        input="""
        func a(number a,number b, number b)
        func main()
        return 0
        """
        expect="Redeclared Parameter: b"
        self.assertTrue(TestChecker.test(input,expect,422))
    def test023(self):
        input="""
        func test()
        func main()
        begin
            number a[2,3]<- test()
        end
        func test()
        begin
            begin
                begin
                    begin
                        return 1
                    end
                end
            end
        end
        """
        expect="Type Mismatch In Statement: Return(NumLit(1.0))"
        self.assertTrue(TestChecker.test(input,expect,423))
    def test024(self):
        input="""
        func test(number a[2,3])

        func main()
        begin
            number a[2,3]<- test(test(a))
        end
        """
        expect="No Function Definition: test"
        self.assertTrue(TestChecker.test(input,expect,424))
    def test025(self):
        input="""
        func test(number a, string b)
        func main()
            begin
            dynamic a
            dynamic b
                a <-test(test(a,b),test(a,b))
            end
        
        """
        expect="Type Mismatch In Expression: CallExpr(Id(test), [CallExpr(Id(test), [Id(a), Id(b)]), CallExpr(Id(test), [Id(a), Id(b)])])"
        self.assertTrue(TestChecker.test(input,expect,425))
    def test026(self):
        input="""
        func hehe()
        func main()
        begin
            number a[2,3]
            a[hehe(),hehe()]<-hehe()
            a[hehe()]<-[hehe(),hehe(),hehe()]
            a[hehe()]<-[hehe(),hehe(),hehe(),hehe()]
        end
        """
        expect="Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [CallExpr(Id(hehe), [])]), ArrayLit(CallExpr(Id(hehe), []), CallExpr(Id(hehe), []), CallExpr(Id(hehe), []), CallExpr(Id(hehe), [])))"
        self.assertTrue(TestChecker.test(input,expect,426))
    def test027(self):
        input="""
        func hehe()
        func main()
        begin
            number a[2,3]
            a[hehe(),hehe()]<-hehe()
            a[hehe()]<-[hehe(),hehe(),hehe()]
            
        end
        func hehe()
        begin
            begin
            end
        end
        """
        expect="Type Mismatch In Statement: Block([Block([])])"
        self.assertTrue(TestChecker.test(input,expect,427))
    def test028(self):
        input="""
        func hehe(number a, number b)
        func main()
        begin
            number a[2,3]
            a[hehe(1,2),hehe(1,2)]<-hehe(1,2)
            a[hehe(1,2)]<-[hehe(1,2),hehe(1,2),hehe(1,2)]
            
        end
        func hehe1(number a, number b)
        func hehe(number hehe1,number hehe)
        begin
            hehe<-hehe1(hehe,hehe)
            hehe1<-hehe1(hehe1,hehe1(hehe1,hehe1))+hehe(hehe1,hehe1(hehe1,hehe))
        
        end
        """
        expect="Type Mismatch In Statement: Block([AssignStmt(Id(hehe), CallExpr(Id(hehe1), [Id(hehe), Id(hehe)])), AssignStmt(Id(hehe1), BinaryOp(+, CallExpr(Id(hehe1), [Id(hehe1), CallExpr(Id(hehe1), [Id(hehe1), Id(hehe1)])]), CallExpr(Id(hehe), [Id(hehe1), CallExpr(Id(hehe1), [Id(hehe1), Id(hehe)])])))])"
        self.assertTrue(TestChecker.test(input,expect,428))
    def test029(self):
        input="""
        func hehe()
        func hehe1()
        func main()
        begin
            number a[2,3]
            a[hehe(),hehe()]<-hehe()
            a[hehe()]<-[hehe(),hehe(),hehe()]
            
        end
        func hehe()
        begin
            return 1
        end
        """
        expect="No Function Definition: hehe1"
        self.assertTrue(TestChecker.test(input,expect,429))
    def test030(self):
        input="""
        func hehe()
        func hehe1()
        func main()
        begin
            number a[2,3]
            a[hehe(),hehe()]<-hehe()
            a[hehe()]<-[hehe(),hehe(),hehe()]
            
        end
        func hehe(number hehe1, string hehe, number hehe2)
        begin
            hehe<- hehe...hehe
            return hehe1
        end
        """
        expect="Redeclared Function: hehe"
        self.assertTrue(TestChecker.test(input,expect,430))
    # test func_decl:10
    def test031(self):
        input="""
        func hehe()
        func hehe1(number a, number b)
        func main()
        return 0
        func hehe1(number c, number d)
        begin
        end
        
        """
        expect="No Function Definition: hehe"
        self.assertTrue(TestChecker.test(input,expect,431))
    def test032(self):
        input="""
       
        func hehe1(number a, number b)
        begin
            number c[2,3]
            begin 
                number a <- 1
            end
            number a <- a
        end
        func main()
            return 0
        
        """
        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,432))
    def test033(self):
        input="""
        func hehe1(number a, number b, number c[1,2,3])
        begin
            dynamic t
            dynamic hehe1 <- [c,t]
            return hehe1
        end
        
        func main()
        begin
            dynamic a
            hehe1(1,1,a)
        end
        
        """
        expect="Type Mismatch In Statement: CallStmt(Id(hehe1), [NumLit(1.0), NumLit(1.0), Id(a)])"
        self.assertTrue(TestChecker.test(input,expect,433))
    def test034(self):
        input="""
        func hehe()
        func hehe(number a)
        func main()
        return 0
        """
        expect="Redeclared Function: hehe"
        self.assertTrue(TestChecker.test(input,expect,434))
    def test035(self):
        input="""
        func hehe(number a)
        func hehe1(number a)
        return true
        
        func main()
        return 3
        func hehe(number t)
        return t
        func hehe1(number t)
        return t
        """
        expect="Redeclared Function: hehe1"
        self.assertTrue(TestChecker.test(input,expect,435))
    def test036(self):
        input="""
        func test1()
        func test2()
        func test3()
        func test(number test1, string test2, bool test3)
        begin
            return (test1 > test1()) and (test2 == test2()) or (test3 and test3())
        end
        func main()
        begin
            return test(1,"abc",true)
        end

        """
        expect="No Function Definition: test1"
        self.assertTrue(TestChecker.test(input,expect,436))
    def test037(self):
        input="""
        func test()
        return true
        func main()
        begin
            string t[2,3]
            dynamic a <- t[test(),test()]
        end
        """
        expect="Type Mismatch In Expression: ArrayCell(Id(t), [CallExpr(Id(test), []), CallExpr(Id(test), [])])"
        self.assertTrue(TestChecker.test(input,expect,437))
    def test038(self):
        input="""
        func happy()
        return 2
        func happy()
        return 1
        func main()
        return 0
        """
        expect="Redeclared Function: happy"
        self.assertTrue(TestChecker.test(input,expect,438))
    def test039(self):
        input="""
        func happy(string a, string b)
        begin
            a <- "Vi ngay em dep nhat"
            b <- "La ngay anh mat em"
            return a ... b
        end
        func main()
        begin
            dynamic a <- "Hen em kiep sau"
            dynamic b <- "Kiep nay thoi tim den nhau"
            happy()
        end
        return 0
        """
        expect="Type Mismatch In Statement: CallStmt(Id(happy), [])"
        self.assertTrue(TestChecker.test(input,expect,439))
    def test040(self):
        input="""
        func happy()
        number a <- happy()
        func happy()
        return 1
        

        func main()
        begin
            string a <- "Tu nay duyen kiep bo lai phia sau, troi nhu muon khoc ngay minh mat nhau"
            a <- happy()
            
        end
        """
        expect="Type Mismatch In Statement: AssignStmt(Id(a), CallExpr(Id(happy), []))"
        self.assertTrue(TestChecker.test(input,expect,440))
    # test Expression: 20
    
    ####test break,cont: 10
    #####test if,for,CallStmt: 10
    #####test CallExpr,ArrayCell:10
    #####complex test: 10
    
    
    
    
    
    
    
    
    
    