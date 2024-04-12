import unittest
from TestUtils import TestChecker

from AST import *
from main.zcode.utils.AST import *


class CheckerSuite(unittest.TestCase):
    #invalid_arrayliteral
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
        expect="No Function Definition: a"
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
    def test041(self):
        input="""
        func main(number a, number b)
        begin
            dynamic d
            dynamic c
            bool e <- (d...c == c ) and (a > b) or (a < b)
        end
        func main()
        """
        expect="Type Mismatch In Expression: BinaryOp(..., Id(d), BinaryOp(==, Id(c), Id(c)))"
        self.assertTrue(TestChecker.test(input,expect,441))
    def test042(self):
        input="""
        func main()
        begin
            number a <- 1
            number b <- 2
            bool c <- a > b
            bool d <- a < b
            bool e <- a == b
            bool f <- a != b
            bool g <- a >= b
            bool h <- a <= b
        end
        """
        expect="Type Mismatch In Expression: BinaryOp(==, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input,expect,442))
    def test043(self):
        input="""
        func test(number a, number b)
        begin
            dynamic c <- a + b > a - b and ((c ... "tam biet e nhe") == "hehe")
        end
        """
        expect="Type Mismatch In Expression: BinaryOp(and, BinaryOp(-, Id(a), Id(b)), BinaryOp(==, BinaryOp(..., Id(c), StringLit(tam biet e nhe)), StringLit(hehe)))"
        self.assertTrue(TestChecker.test(input,expect,443))
    def test044(self):
        input="""
        func hehe()
        func test(number a, number b)
        begin
            number t[2,3]<- hehe()
        end
        func hehe()
        begin
        number a [2,4]
        return a 
        end
        """
        expect="Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input,expect,444))
    def test045(self):
        input="""
        func test(number a, number b)
        begin
            dynamic c <- a + b > a - b and ((c ... "tam biet e nhe") == "hehe")
        end
        """
        expect="Type Mismatch In Expression: BinaryOp(and, BinaryOp(-, Id(a), Id(b)), BinaryOp(==, BinaryOp(..., Id(c), StringLit(tam biet e nhe)), StringLit(hehe)))"
        self.assertTrue(TestChecker.test(input,expect,445))
    ###test break,cont: 10
    ####test if,for,CallStmt: 10
    ####test CallExpr,ArrayCell:10
    ####complex test: 10
    
    
    #### My testcase is above
    def test0(self): # no entry point
        input = """number a
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 100))

    def test1(self): # no entry point
        input = """
            func main()
            return 1
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 101))

    def test2(self): # no entry point
        input = """
            func main(string a)
            return
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 102))

    def test3(self): # no entry point
        input = """
            func main()
            func f(string ba, number g)
            return 0
            func main()
            begin
            return "abc"
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 103))

    def test4(self): # no entry point
        input = """
            func f(string ba, number g)
            begin
            number main
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 104))

    def test5(self): # no entry point
        input = """
            func main(string ba, number g)
            begin
            number a <- 1
            return 7
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 105))

    def test6(self): # no entry point
        input = """
            number a <- 1
            number b <- 2
            number c <- 3
            func calc()
            begin
            end
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 106))

    def test7(self): # no entry point
        input = """
            func mainn() return
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 107))

    def test8(self): # no entry point
        input = """
            string a
            bool b
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 108))

    def test9(self): # entry point
        input = """
            func main()
            func abc() return 1
            func main()
            begin
            number a
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 109))

    def test10(self): # entry point
        input = """
            func main()
            return
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 110))

    def test11(self): # redeclared variable
        input = """
            func main()
            begin
            number a
            number a
            end
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 111))

    def test12(self): # redeclared function
        input = """
            func main()
            return
            func abc12() return 1
            func abc12() return "abc"
        """
        expect = "Redeclared Function: abc12"
        self.assertTrue(TestChecker.test(input, expect, 112))

    def test13(self): # redeclared parameter
        input = """
            func main()
            return
            func abc(string aaa, bool aaa)
        """
        expect = "No Function Definition: abc"
        self.assertTrue(TestChecker.test(input, expect, 113))

    def test14(self): # redeclared variable (different scope)
        input = """
            bool ayu
            func main()
            begin
            string ayu
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 114))

    def test15(self): # redeclared variable (different scope)
        input = """
            bool a
            func main()
            begin
            string a
                begin
                number a
                end
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 115))

    def test16(self): # redeclared function (definition for function)
        input = """
            func iiiii(number x)
            func main() return
            func iiiii(number y) return y
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 116))

    def test17(self): # redeclared function
        input = """
            func f17(number x)
            func main() return
            func f17(string y) return y
        """
        expect = "Redeclared Function: f17"
        self.assertTrue(TestChecker.test(input, expect, 117))

    def test18(self): # redeclared parameter
        input = """
            func main() return
            func f(string gh, string gh)
        """
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 118))

    def test19(self): # redeclared function
        input = """
            func main() return
            func f(string gh) return 0
            func f(string gh)
        """
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 119))

    def test20(self): # redeclared parameter
        input = """
            func main() return
            func f(string gh, string gh)
            func f(string gh, string a) return gh
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 120))

    def test21(self): # redeclared built-in function
        input = """
            func main() return
            func readNumber() return 123
        """
        expect = "Redeclared Function: readNumber"
        self.assertTrue(TestChecker.test(input, expect, 121))

    def test22(self): # undeclared identifier
        input = """
            func main() return
            func f() return a
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 122))

    def test23(self): # undeclared identifier
        input = """
            func main() return
            func f() return a
            number a
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 123))

    def test24(self): # undeclared identifier
        input = """
            func main()
            begin
            number a
            end
            func f() return a
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 124))

    def test25(self): # declared identifier
        input = """
            string a
            func main()
            begin
            number a
            end
            func f() return a
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 125))

    def test26(self): # declared identifier
        input = """
            func main() return
            func f(bool a) return a
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 126))

    def test27(self): # undeclared function
        input = """
            func main() return
            func f(bool a27)
            begin
            a27 <- foo27()
            end
        """
        expect = "Undeclared Function: foo27"
        self.assertTrue(TestChecker.test(input, expect, 127))

    def test28(self): # undeclared identifier
        input = """
            func main() return
            func f()
            begin
            a <- 123
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 128))

    def test29(self): # undeclared identifier
        input = """
            func main()
            begin
            number a <- 123 + b * 100 / 78
            end
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 129))

    def test30(self): # undeclared identifier
        input = """
            func main()
            begin
            number a
            for b until b > 10 by 1
            a <- b
            end
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 130))

    def test31(self): # undeclared identifier
        input = """
            func main()
            begin
            if (abc % 5 == 0) abc <- 5
            end
        """
        expect = "Undeclared Identifier: abc"
        self.assertTrue(TestChecker.test(input, expect, 131))

    def test32(self): # declared function (IO)
        input = """
            func main()
            begin
            number t1 <- readNumber()
            bool t2 <- readBool()
            string t3 <- readString()
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 132))

    def test33(self): # declared function
        input = """
            func a33()
            func main()
            begin
            a33()
            end
            func a33() return
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 133))

    def test34(self): # undeclared function
        input = """
            func main()
            begin
            a34()
            end
            func a34()
            func a34() return
        """
        expect = "Undeclared Function: a34"
        self.assertTrue(TestChecker.test(input, expect, 134))

    def test35(self): # redeclared function
        input = """
            func abcc() return
            func main()
            begin
            abcc()
            end
            func abcc()
            func abcc() return
        """
        expect = "Redeclared Function: abcc"
        self.assertTrue(TestChecker.test(input, expect, 135))

    def test36(self): # undeclared identifier
        input = """
            func main()
            begin
            a <- 1
            number a
            end
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 136))

    def test37(self): # type mismatch in expression
        input = """
            func main()
            begin
            number a
            number b <- a[0]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 137))

    def test38(self): # type mismatch in expression
        input = """
            func main()
            begin
            number a[2]
            number b <- a["hi"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [StringLit(hi)])"
        self.assertTrue(TestChecker.test(input, expect, 138))

    def test39(self): # type mismatch in expression
        input = """
            func main()
            begin
            string a[2]
            string b <- a[1, 2, 3, "hi"]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0), StringLit(hi)])"
        self.assertTrue(TestChecker.test(input, expect, 139))

    def test40(self): # undeclared function
        input = """
            func main()
            begin
            abc()
            end
            func abc() return
        """
        expect = "Undeclared Function: abc"
        self.assertTrue(TestChecker.test(input, expect, 140))

    def test41(self): # type mismatch in expression
        input = """
            func main()
            begin
            bool a[2]
            bool b <- a[true, false]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a), [BooleanLit(True), BooleanLit(False)])"
        self.assertTrue(TestChecker.test(input, expect, 141))

    def test42(self): # type mismatch in expression
        input = """
            func main()
            begin
            number b <- 1 + "hi"
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(1.0), StringLit(hi))"
        self.assertTrue(TestChecker.test(input, expect, 142))

    def test43(self): # undeclared identifier (note)
        input = """
            func main()
            begin
            number b <- b + 1
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 143))

    def test44(self): # type mismatch in expression
        input = """
            func main()
            begin
            number b <- true + "hi"
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, BooleanLit(True), StringLit(hi))"
        self.assertTrue(TestChecker.test(input, expect, 144))

    def test45(self): # type mismatch in expression
        input = """
            func main()
            begin
            string a
            number b <- (a + 1) = 5
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(a), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 145))

    def test46(self): # type mismatch in expression
        input = """
            func main()
            begin
            var a <- "abc" ... "aa"
            dynamic b <- a == false
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(==, Id(a), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 146))

    def test47(self): # type mismatch in expression
        input = """
            func calc47(number a, number b) return a = b
            func main()
            begin
            var a <- calc47(1, 4) * 2
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(*, CallExpr(Id(calc47), [NumLit(1.0), NumLit(4.0)]), NumLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 147))

    def test48(self): # type mismatch in expression
        input = """
            func calc(number a, number b) return a + b
            func main()
            begin
            var a <- calc(1, 4) * 2
            a <- a and a
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, Id(a), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 148))

    def test49(self): # type mismatch in expression
        input = """
            func calc49(number a49, number b49) return [a49, b49]
            func main()
            begin
            var arr49 <- calc49(1, 4)
            var b <- arr49[0]
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 149))

    def test50(self): # type mismatch in statement (note)
        input = """
            func main()
            begin
            number a50[2, 3] <- [[1, 2, 3], [4, 5, 6]]
            number b <- a50[0]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b), NumberType, None, ArrayCell(Id(a50), [NumLit(0.0)]))"
        self.assertTrue(TestChecker.test(input, expect, 150))

    def test51(self): # type mismatch in expression (note2)
        input = """
            func f() return
            func main()
            begin
            number a51 <- f()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 151))

    def test52(self): # type mismatch in statement (note)
        input = """
            func main()
            begin
            number a[2, 2, 2] <- [[[1, 2], [3, 4]], [[4, 5], [6, 7]]]
            number b <- a[0, 1, 1]
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 152))

    def test53(self): # type mismatch in expression
        input = """
            func main()
            begin
            var a <- -true
            end
        """
        expect = "Type Mismatch In Expression: UnaryOp(-, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 153))

    def test54(self): # type mismatch in expression
        input = """
            func main()
            begin
            var a <- not true
            var b <- not 1
            end
        """
        expect = "Type Mismatch In Expression: UnaryOp(not, NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 154))

    def test55(self): # undeclared identifier
        input = """
            func f() return 1
            func main()
            begin
            number a <- f
            end
        """
        expect = "Undeclared Identifier: f"
        self.assertTrue(TestChecker.test(input, expect, 155))

    def test56(self): # redeclared variable
        input = """
            func f()
            string f
            func main() return
            func f() return
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 156))

    def test57(self): # type mismatch in expression
        input = """
            func f() return "abcd"
            func main()
            begin
            number a <- f()[0]
            end
        """
        expect = "Type Mismatch In Expression: ArrayCell(CallExpr(Id(f), []), [NumLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 157))

    def test58(self): # type mismatch in expression
        input = """
            func f() return [1, 2]
            func main()
            begin
            number a <- f() + 1
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, CallExpr(Id(f), []), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 158))

        input = """
            func f() return "ahu"
            func main()
            begin
            string a <- f() ... "aaa"
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 159))

        input = """
            func f60(number x)
            begin
            if (x % 2 = 0)
            return true
            else
            return false
            end
            func main()
            begin
            var a60 <- not f60(readNumber())
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 160))

    def test59(self): # type mismatch in expression
        input = """
            func f() return [1, 2]
            func main()
            begin
            number a <- f() + 1
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, CallExpr(Id(f), []), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 161))

    def test60(self): # type mismatch in statement (note)
        input = """
            func main()
            begin
            number a[2, 3] <- [[1, 2, 3], [4, 5, 6]]
            number b[3] <- a[0]
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 162))

    def test61(self): # type mismatch in expression
        input = """
            func f61(string x61)
            begin
            if (x61 == "a") return x61 ... "a"
            elif (x61 == "b") return x61 ... "b"
            else return x61
            end
            func main()
            begin
            var a <- f61("a") == "ab"
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 163))

    def test62(self): # type cannot be inferred
        input = """
            func f62()
            begin
            dynamic a62
            return a62
            end
            func main()
            begin
            var a <- f62()
            end
        """
        expect = "Type Cannot Be Inferred: Return(Id(a62))"
        self.assertTrue(TestChecker.test(input, expect, 164))

    def test63(self): # type cannot be inferred
        input = """
            func main()
            begin
            dynamic x
            var a63 <- x
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a63), None, var, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 165))

    def test64(self): # type mismatch in expression
        input = """
            func f(number a, number b) return a + b
            func main()
            begin
            dynamic x <- f(1)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 166))

    def test65(self): # type mismatch in statement
        input = """
            func f(number a, number b) return
            func main()
            begin
            f(1)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [NumLit(1.0)])"
        self.assertTrue(TestChecker.test(input, expect, 167))

    def test66(self): # type cannot be inferred
        input = """
            func main()
            begin
            dynamic x
            dynamic y <- x
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(y), None, dynamic, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 168))

    def test67(self): # type cannot be inferred
        input = """
            func f()
            func main()
            begin
            dynamic x <- f()
            end
            func f() return 1
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, dynamic, CallExpr(Id(f), []))"
        self.assertTrue(TestChecker.test(input, expect, 169))

    def test68(self): # initialize implicit keywords with array expr
        input = """
            func main()
            begin
            var a <- [1,2,3,4]
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 170))

    def test69(self): # type mismatch in statement
        input = """
            func main()
            begin
            number x
            if (x) x <- 0
            end
        """
        expect = "Type Mismatch In Statement: If((Id(x), AssignStmt(Id(x), NumLit(0.0))), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 171))

    def test70(self): # type mismatch in statement
        input = """
            func main()
            begin
            number x
            if (x > 0) x <- 0
            elif (x - 9) x <- 0
            end
        """
        expect = "Type Mismatch In Statement: If((BinaryOp(>, Id(x), NumLit(0.0)), AssignStmt(Id(x), NumLit(0.0))), [(BinaryOp(-, Id(x), NumLit(9.0)), AssignStmt(Id(x), NumLit(0.0)))], None)"
        self.assertTrue(TestChecker.test(input, expect, 172))

    def test71(self): # type mismatch in statement
        input = """
            func f(number x)
            begin
            if (x > 5) return x % 2
            elif (x <= 5) return x - 1
            end
            func main()
            begin
            number x
            if (f(2)) x <- 0
            end
        """
        expect = "Type Mismatch In Statement: If((CallExpr(Id(f), [NumLit(2.0)]), AssignStmt(Id(x), NumLit(0.0))), [], None)"
        self.assertTrue(TestChecker.test(input, expect, 173))

    def test72(self): # type mismatch in statement
        input = """
            func main()
            begin
            number x
            for x until x by 1 x <- 0
            end
        """
        expect = "Type Mismatch In Statement: For(Id(x), Id(x), NumLit(1.0), AssignStmt(Id(x), NumLit(0.0)))"
        self.assertTrue(TestChecker.test(input, expect, 174))

        input = """
            func main()
            begin
            string x
            for x until x == "a" by 1 x <- 0
            end
        """
        expect = "Type Mismatch In Statement: For(Id(x), BinaryOp(==, Id(x), StringLit(a)), NumLit(1.0), AssignStmt(Id(x), NumLit(0.0)))"
        self.assertTrue(TestChecker.test(input, expect, 175))

        input = """
            func main()
            begin
            string x
            number y
            for y until x == "a" by x
            x <- 0
            end
        """
        expect = "Type Mismatch In Statement: For(Id(y), BinaryOp(==, Id(x), StringLit(a)), Id(x), AssignStmt(Id(x), NumLit(0.0)))"
        self.assertTrue(TestChecker.test(input, expect, 176))

    def test73(self): # type mismatch in expression (note2)
        input = """
            func f() return
            func main()
            begin
            number x <- f()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 177))

    def test74(self): # type mismatch in statement
        input = """
            func f() return "abc"
            func main()
            begin
            number x <- f()
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x), NumberType, None, CallExpr(Id(f), []))"
        self.assertTrue(TestChecker.test(input, expect, 178))

    def test75(self): # type mismatch in statement
        input = """
            func main()
            begin
            number y
            number x[1, 2] <- y
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x), ArrayType([1.0, 2.0], NumberType), None, Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 179))

    def test76(self): # type mismatch in statement
        input = """
            func main()
            begin
            number y[2, 2]
            number x[1, 2] <- y
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x), ArrayType([1.0, 2.0], NumberType), None, Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 180))

    def test77(self): # type mismatch in statement
        input = """
            func main()
            begin
            dynamic a
            number x[2] <- [a, 1]
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 181))

    def test78(self): # type mismatch in statement
        input = """
            func main()
            begin
            number x[2] <- [1]
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(x), ArrayType([2.0], NumberType), None, ArrayLit(NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 182))

    def test79(self): # type mismatch in statement (note)
        input = """
            func f() return 1
            func main()
            begin
            f()
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [])"
        self.assertTrue(TestChecker.test(input, expect, 183))

    def test80(self): # type mismatch in statement
        input = """
            func f(number x) return
            func main()
            begin
            f(1, 2)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [NumLit(1.0), NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 184))

    def test81(self): # type mismatch in statement
        input = """
            func f(number x) return
            func main()
            begin
            f(true)
            end
        """
        expect = "Type Mismatch In Statement: CallStmt(Id(f), [BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input, expect, 185))

    def test82(self): # type mismatch in statement
        input = """
            func f(number x) return
            func main()
            begin
            dynamic x
            f(x)
            x <- x + 1
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 186))

    def test83(self): # type mismatch in expression (note2)
        input = """
            func f(number x) return x
            func main()
            begin
            number x <- f(1, 2) * 8
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [NumLit(1.0), NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 187))

        input = """
            func f(number x) return x
            func main()
            begin
            number x <- f("abc") + 1
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [StringLit(abc)])"
        self.assertTrue(TestChecker.test(input, expect, 188))

    def test84(self): # type cannot be inferred
        input = """
            func main()
            begin
            dynamic c
            c <- c
            end
        """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(c), Id(c))"
        self.assertTrue(TestChecker.test(input, expect, 189))

    def test85(self): # type mismatch in expression
        input = """
            func main()
            begin
            number temp[3] <- [1, 2, true]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(1.0), NumLit(2.0), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 190))

    def test86(self): # type mismatch in statement
        input = """
            func f(number a, string b, bool c)
            begin
            if (a > 5) return [a + 1, a % 2]
            elif (a % 5 = 0) return [a, a - 1]
            else return [a * 6, a / 6]
            end
            func main()
            begin
            number temp[3] <- f(1, "a", true)
            end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(temp), ArrayType([3.0], NumberType), None, CallExpr(Id(f), [NumLit(1.0), StringLit(a), BooleanLit(True)]))"
        self.assertTrue(TestChecker.test(input, expect, 191))

    def test87(self): # type mismatch in statement
        input = """
            func f(number a)
            func main()
            begin
            number temp <- f(1)
            end
            func f(number a) return "abc"
        """
        expect = "Type Mismatch In Statement: Return(StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 192))

    def test88(self): # type mismatch in statement
        input = """
            func f(number a)
            begin
            if (a > 5) return a
            elif (a < 5) return "a"
            end
            func main()
            begin
            number temp <- f(1)
            end
        """
        expect = "Type Mismatch In Statement: Return(StringLit(a))"
        self.assertTrue(TestChecker.test(input, expect, 193))

    def test89(self): # type mismatch in statement (note)
        input = """
            func f89(number a)
            func main()
            begin
            f89(1)
            end
            func f89(number a) return a
        """
        expect = "Type Mismatch In Statement: Return(Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 194))

    def test90(self): # type mismatch in expression (note2)
        input = """
            func f(number a) return a
            func f2(string a) return a
            func main()
            begin
            dynamic a
            a <- f(1)
            a <- f("a")
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [StringLit(a)])"
        self.assertTrue(TestChecker.test(input, expect, 195))

    def test91(self): # type mismatch in expression
        input = """
            func main()
            begin
            var a <- 1 + 1 * 1 / 1 = "1"
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(=, BinaryOp(+, NumLit(1.0), BinaryOp(/, BinaryOp(*, NumLit(1.0), NumLit(1.0)), NumLit(1.0))), StringLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 196))

    def test92(self): # no definition for a function
        input = """
            func f()
            func main() return
        """
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 197))

    def test93(self): # break/continue not in loop
        input = """
            func main()
            begin
            continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 198))

    def test94(self): # break/continue not in loop
        input = """
            func main()
            begin
            break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 199))

    def test95(self): # break/continue not in loop
        input = """
            func main()
            begin
            number a
            if (a > 5) continue
            end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 200))

        input = """
            func main()
            begin
            number a
            if (a > 5)
                begin
                    begin
                    break
                    end
                end
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 201))

        input = """
            func main()
            begin
            number a
            for a until a > 10 by 5
            begin
                if (a > 5)
                    begin
                        begin
                        break
                        end
                    end
                end
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 202))

    def test96(self): # break/continue not in loop
        input = """
            func main()
            begin
            number a
            for a until a > 5 by 5
            continue
            break
            end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 203))

    def test97(self): # break/continue not in loop
        input = """
            func main()
            begin
            number a
            for a until a > 5 by 5
            if (a % 2 = 0) continue
            elif (a > 1) break
            else continue
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 204))

    def test98(self): # break/continue not in loop
        input = """
            func main()
            begin
            number a
            for a until a > 5 by 5
            if (a % 2 = 0)
                if (a > 2)
                    a <- a + 1
                elif (a > 3)
                    a <- a - 2
            elif (a % 3 = 1)
                continue
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 205))

    def test99(self): # break/continue not in loop
        input = """
            func main()
            begin
            number a
            for a until a > 5 by 5
            begin
                for a until a > 5 by 5
                begin
                continue
                end
                break
            end
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 206))

    def test100(self): # break/continue not in loop
        input = """
            func main()
            begin
            number a
            for a until a > 5 by 5
            begin
                for a until a > 5 by 5
                begin
                    for a until a > 5 by 5
                    begin
                        for a until a > 5 by 5
                        begin
                        continue
                        end
                        begin
                            break
                        end
                    end
                break
                end
                break
            end
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 207))

    def test101(self): # undeclared identifier
        input = """
            func f() return 1
            func main()
            begin
            number a <- f
            end
        """
        expect = "Undeclared Identifier: f"
        self.assertTrue(TestChecker.test(input, expect, 208))

    def test102(self): # undeclared function
        input = """
            func main()
            begin
            number f
            number a <- f()
            end
        """
        expect = "Undeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 209))

    def test103(self): # undeclared function
        input = """
            number a
            func main()
            begin
            string a
            a <- "abc"
            end
            func f() return a + 1
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 210))

    def test104(self): # redeclared
        input = """
            func f() return 1
            number f <- 1
            func main()
            begin
            number a <- f + f()
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 211))

    def test105(self): # no definition for a function
        input = """
            func main()
        """
        expect = "No Function Definition: main"
        self.assertTrue(TestChecker.test(input, expect, 212))

    def test106(self): # type cannot be inferred (note)
        input = """
            func main()
            begin
            var b <- b
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, var, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 213))

        input = """
            func main()
            begin
            dynamic b <- b
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(b), None, dynamic, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 214))

    def test107(self): # type mismatch in statement
        input = """
            func main()
            begin
            dynamic x107
            x107 <- (x107 = 1) or ("abc" == "abc")
            ##bool a107 <- x107
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x107), BinaryOp(or, BinaryOp(=, Id(x107), NumLit(1.0)), BinaryOp(==, StringLit(abc), StringLit(abc))))"
        self.assertTrue(TestChecker.test(input, expect, 215))
    
    def test108(self): # type mismatch in expression
        input = """
            func main()
            begin
            dynamic x
            var y <- (x = 1) or (x + 1)
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(or, BinaryOp(=, Id(x), NumLit(1.0)), BinaryOp(+, Id(x), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 216))

    def test109(self): # type mismatch in statement (note)
        input = """
            func f()
            func main()
            begin
            number x <- f()
            end
            func f() begin
            end
        """
        expect = "Type Mismatch In Statement: Block([])"
        self.assertTrue(TestChecker.test(input, expect, 217))

    def test110(self): # type mismatch in statement (note)
        input = """
            func a()
            func main()
            begin
            string a <- a()
            end
            
            func a()
            begin
            string b 
            end
        """
        expect = "Type Mismatch In Statement: Block([VarDecl(Id(b), StringType, None, None)])"
        self.assertTrue(TestChecker.test(input, expect, 218))

    def test111(self): # type mismatch in statement (note)
        input = """
            func main()
            begin
            number a 
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 219))

    def test112(self): # type mismatch in statement
        input = """
            func foo(number i)
            begin
                if (i = 1) return 2
                else
                begin
                    dynamic x
                    return x
                end
            end
            func main()
            begin
                bool b <- foo(2)
            end
        """
        expect = "Type Cannot Be Inferred: Return(Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 220))

    def test113(self): # type mismatch in expression
        input = """
            func foo()
            begin
                dynamic x113
                for x113 until x113 > 5 by 1
                continue
                x113 <- x113 and x113
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(and, Id(x113), Id(x113))"
        self.assertTrue(TestChecker.test(input, expect, 221))

    def test114(self): # type mismatch in statement + expression
        input = """
            func foo()
            begin
                dynamic x
                number a
                if (x) a <- 1
                x <- 1
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 222))

        input = """
            func foo()
            begin
                dynamic x
                number a
                if (x) a <- 1
                elif (x + 1 > 2) a <- 2
            end
            func main() return
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), NumLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 223))

    def test115(self): # type mismatch in statement
        input = """
            func foo()
            begin
                dynamic x
                dynamic a
                for a until x by a continue
                x <- a
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x), Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 224))

        input = """
            func main()
            begin
                dynamic x
                for x until true by 1
                begin
                x <- x + 1
                end
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 225))

    def test116(self): # type mismatch in statement
        input = """
            dynamic a
            dynamic b
            dynamic c
            func main()
            begin
            var c <- a * b = 5
            for a until c by c break
            end
        """
        expect = "Type Mismatch In Statement: For(Id(a), Id(c), Id(c), Break)"
        self.assertTrue(TestChecker.test(input, expect, 226))

    def test117(self): #
        input = """
            dynamic a
            dynamic b117
            dynamic c
            func foo117()
            begin
                var c <- a = 5
                if (c)
                begin
                    begin
                        begin
                        b117 <- b117 + 1
                        end
                    end
                end
                return b117
            end
            func main() return
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 227))

    def test118(self): # type mismatch in statement
        input = """
            func f()
            begin
                if (1 < 2)
                begin
                end
                elif (1 < 2)
                begin
                    return 1
                end
                elif (1 < 2)
                begin
                end
                else
                begin
                    return "abc"
                end
                return 2
            end
            func main() return
        """
        expect = "Type Mismatch In Statement: Return(StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 228))

    def test119(self): # type mismatch in expression (note2)
        input = """
            dynamic a
            dynamic b
            dynamic c
            func f(number b)
            begin
                dynamic c
                c <- not c
                a <- c and (-b = 6)
                return c
            end
            func main()
            begin
            c <- f(a)
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(f), [Id(a)])"
        self.assertTrue(TestChecker.test(input, expect, 229))

    def test120(self): # type cannot be inferred
        input = """
            dynamic a
            dynamic b
            dynamic c
            func f(number b)
            begin
                dynamic c
                c <- not c
                a <- c and (-b = 6)
                return c
            end
            func main()
            begin
            dynamic d <- b
            end
        """
        expect = "Type Cannot Be Inferred: VarDecl(Id(d), None, dynamic, Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 230))

    def test121(self): #
        input = """
            func main()
            begin
            var x <- readNumber()
            writeNumber(x)
            var y <- readBool()
            writeBool(y)
            y <- x = 4
            string z <- readString()
            writeString(z)
            z <- z ... "a"
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 231))

    def test122(self): # type mismatch in statement
        input = """
            func b122()
            func a122()
            begin
            return 1
            return b122()
            end
            func b122() return true
            func main() return
        """
        expect = "Type Cannot Be Inferred: Return(CallExpr(Id(b122), []))"
        self.assertTrue(TestChecker.test(input, expect, 232))

    def test123(self): # type cannot be inferred
        input = """
            func a()
            begin
            dynamic x
            return x
            return 1
            end
            func main() return
        """
        expect = "Type Cannot Be Inferred: Return(Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 233))

    def test124(self): #
        input = """
            dynamic z
            func a()
            begin
                dynamic x
                dynamic y
                return 1
                return x
                return y
                if (x > 5)
                begin
                    begin
                        return x + y
                    end
                end
                for x until x > y by 1
                begin
                    return z
                end
            end
            func main()
            begin
            z <- z + 1
            end
        """
        expect = "Type Cannot Be Inferred: Return(Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 234))

    def test125(self): # type mismatch in expression (note2)
        input = """
            func a()
            begin
            end
            func main()
            begin
            number a <- a()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(a), [])"
        self.assertTrue(TestChecker.test(input, expect, 235))

    def test126(self): # type mismatch in statement
        input = """
            func a()
            func main()
            begin
            dynamic a <- a() = 5
            var b <- (a() + 1 > 6) or (a and true)
            end
            func a() return false
        """
        expect = "Type Mismatch In Statement: Return(BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 236))

    def test127(self): # type mismatch in statement (note)
        input = """
            func main()
            begin 
                dynamic a127
                dynamic b
                dynamic c127
                number x127[3,3] <- [a127,b,c127]
                a127 <- [1,2,3]
                b <- [4,5,6]
                c127 <- [7,8,9]
                writeNumber(a127[0] + b[0] + c127[0])
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 237))

    def test128(self): #
        input = """
            func main()
            begin 
                number a[2,2,2] <- [[[1,2], [2,3]], [["abc",5], [6,7]]]
            end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(2.0), NumLit(3.0))), ArrayLit(ArrayLit(StringLit(abc), NumLit(5.0)), ArrayLit(NumLit(6.0), NumLit(7.0))))"
        self.assertTrue(TestChecker.test(input, expect, 238))

    def test129(self): #
        input = """
            func main()
            begin 
                dynamic a
                a <- [1,2,3]
                dynamic b
                b <- [1,2]
                bool c <- a = b
            end
        """
        expect = "Type Mismatch In Expression: BinaryOp(=, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 239))

    def test130(self): # type mismatch in expression
        input = """
        func foo()
            begin
            end

        func main()
            begin
                dynamic x <- foo()
            end
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [])"
        self.assertTrue(TestChecker.test(input, expect, 240))

    def test131(self): # type mismatch in expression
        input = """
        func f(number a)
        begin
            number a
        end
        func main() return
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 241))

    def test132(self): # redeclared function (note)
        input = """
        func f(string a)
        func f(number a)
        begin
        end
        """
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 242))

    def test133(self): # redeclared parameter
        input = """
        func f(string a, string a)
        begin
        end
        """
        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 243))

    def test134(self): # debug test
        input = """
        func f134(number a, string b)
        func f134(number a, string b)
        begin
        end
        func main() return
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 244))

    def test135(self): #
        """ Array Literals: RHS in Assign Statement """
        input = """
        func foo(number x[4])
        func main()
            begin
                dynamic x
                number arr135[2,3,4] 
                arr135 <- [foo(x),[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]
            end
        func createArr(number n)
            begin
                return [[n + n % n, n - n, -n, n * n],[n + 12.5, n % n - n, n, n],[n + - n, - n - - n, n, n]]
            end
        func foo(number n[4])
            return createArr(n[0])
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 245))

    def test136(self): # type mismatch in expression (note)
        input = """
        func main()
        begin
            dynamic x
            dynamic y
            number a136[2,2,2,2]
            a136 <- [[[[1,2], [3,4]], [[1,2], [3,4]]], [x, y]]
            ##a136 <- [[[[1,2], [3,4]], [[1,2], [3,4]]], [[[1,2], [3,4]], [[1,2], [3,4]]]]
        end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 246))

    def test137(self): # type mismatch in expression (note)
        input = """
        func main()
        begin
            dynamic x
            dynamic y
            number a[2,2,2,2]
            a <- [[[[1,2], [3,4]], [[1,2], [3,4]]], [x, y]]
            x <- [[5,6], [7,8]]
        end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 247))

    def test138(self): # type mismatch in expression (note)
        input = """
        func main()
        begin
            dynamic x
            dynamic y
            number a138[2,2,2,2]
            a138 <- [[[[1,2], [3,4]], [[1,2], [3,4]]], [x]]
        end
        """
        expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0))), ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(3.0), NumLit(4.0)))), ArrayLit(Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 248))

    def test139(self): # type mismatch in statement (note)
        input = """
        func f()
        begin
            dynamic x
            dynamic y
            number a[2,2,2,2]
            return a
            return [[[[1,2], [3,4]], [[1,2], [3,4]]], [x, y]]
            x <- [[5,6], [7,8]]
        end
        func main() return
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 249))

    def test140(self): # type mismatch in expression (note)
        input = """
        func f(number a[2,2,2,2])
        begin
            return 1
        end
        func main()
        begin
            dynamic x
            dynamic y
            number a <- f([[[[1,2], [3,4]], [[1,2], [3,4]]], [x, y]])
            x <- [[5,6], [7,8]]
            y <- x
        end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 250))

    def test141(self): # type mismatch in statement (note)
        input = """
        func f(number a[2,2,2,2])
        begin
        end
        func main()
        begin
            dynamic x
            dynamic y
            f([    [ [[1,2], [3,4]] , [[1,2], [3,4]] ]  ,    [x, y]  ] )
            x <- [[5,6], [7,8]]
            y <- x
        end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 251))

    def test142(self):
        input = """number a[2] <- [1]
        func main() 
        begin
        end
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2.0], NumberType), None, ArrayLit(NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 252))
    
    
    
    
    
    
    