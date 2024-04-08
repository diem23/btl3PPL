import unittest
from TestUtils import TestChecker

from AST import *
from main.zcode.utils.AST import *


class CheckerSuite(unittest.TestCase):
    #invalid_arrayliteral
#     def test_001(self):
#         input = """var a <- [[1,2],[1,2,3]]
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 401))
#     def test_002(self):
#         input = """
#         string b
#         var a <- [[1,2,4],[1,2,3],[b,b,b]]
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(4.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(b), Id(b), Id(b)))"
#         self.assertTrue(TestChecker.test(input, expect, 402))
#     def test_003(self):
#         input = """var a <- [[1,2,3],[1,2,3],[1,2,3,4],[1,2,3]]
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 403))
#     def test_004(self):
#         input = """
#         dynamic t
#         var a <- [[1,2],[1,t],[1,2,3]]
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), Id(t)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
#         self.assertTrue(TestChecker.test(input, expect, 404))
#     def test_005(self):
#         input = """
#         dynamic ans
#         dynamic temp <- "abc"
#         var a <- [[1,2],[1,ans],[temp,ans]]
#         """
#         expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), Id(ans)), ArrayLit(Id(temp), Id(ans)))"
#         self.assertTrue(TestChecker.test(input, expect, 405))
#     def test_006(self):
#         input = """
#         dynamic ans
#         number a[3.0,4.0] <- [[ans,ans,ans,ans],[1,2,ans,4],[1,2,3,4]]
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 406))
#     def test_007(self):
#         input = """number a[2,3] <- [[2,3],[2,3]]
#         """
#         expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(2.0), NumLit(3.0))))"
#         self.assertTrue(TestChecker.test(input, expect, 407))
#     def test_008(self):
#         input = """
#         dynamic t
#         dynamic b
#         dynamic c
#         dynamic d
#         dynamic e
#         dynamic f
#         number a[2,3] <- [[b,t,d],[c,e,f]]
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 408))
#     def test_009(self):
#         input = """
#         dynamic t
#         dynamic b
#         dynamic c
#         dynamic d
#         dynamic e
#         dynamic f
#         number a[2.0,3.0,2.0] <- [[[b,c],[d,d],[t,f]],[[e,e],[e,t],[f,d]]]
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 409))
#     def test_010(self):
#         input = """
#         dynamic t
#         dynamic b
#         dynamic c
#         dynamic d
#         dynamic e
#         dynamic f
#         number a[2.0,3.0,2.0] <- [[[1,c],[3,d],[t,f]],[[b,9],[e,t],[2,d]]]
#         """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 410))
#     def test011(self):
#         input = """
#     dynamic a
#     dynamic b
#     dynamic c
#     number arr[1, 2,2] <- [[a, b]]
#     ## number c[2, 2] <- arr
# """
#         expect = "No Entry Point"
#         self.assertTrue(TestChecker.test(input, expect, 411))
#     def test012(self):
#         input = """
# dynamic a
#     dynamic b
#     dynamic c
#     dynamic d
#     var e <- 1
#     var x <- [a, [b], [[c]], [[[d, e]]] ]
#     ##c <- [-10, 2 / 3 % 0.75]
#     ##b <- [c]
#     ##a <- [b]
# """
#         expect = "No Entry Point"
        
#         self.assertTrue(TestChecker.test(input, expect, 412))
#     def test013(self):
#         input = """
# dynamic a
#     dynamic b
#     dynamic c
#     dynamic d
#     dynamic e
#     var x <- [a, [b], [[c]], [[[d, e]]] ]
#     ##c <- [-10, 2 / 3 % 0.75]
#     ##b <- [c]
#     ##a <- [b]
# """
#         expect = "Type Cannot Be Inferred: VarDecl(Id(x), None, var, ArrayLit(Id(a), ArrayLit(Id(b)), ArrayLit(ArrayLit(Id(c))), ArrayLit(ArrayLit(ArrayLit(Id(d), Id(e))))))"
#         self.assertTrue(TestChecker.test(input, expect, 413)) 
    
    
    
    
    
    
    
    
    
    
    def test_no_entry_point(self):
            input = """number a
            """
            expect = "No Entry Point"
            self.assertTrue(TestChecker.test(input, expect, 400))
    
    def test_no_entry_point_2(self):
        input = """func b() 
            begin
            end
        """
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_no_entry_point_3(self):
        input = """func main() 
            begin
                return 1
            end
        """
        expect = """['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"""
        self.assertTrue(TestChecker.test(input, expect, 402))
    
    def test_no_entry_point_4(self):
        input = """func main() 
            begin
                return
            end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    def test_no_entry_point_5(self):
        input = """func bkool()
            begin
                return true
            end
            ##test_var
        """
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 404))
        
    def test_invalid_param_1(self):
        input = """
        func inc(number a) return a+1
            """
        expect = """No Entry Point"""
        self.assertTrue(TestChecker.test(input, expect, 485))
        
    ## REDECLARED VARIABLES
    
    def test_redecl_var_1(self):
        input = """func main()
            begin
                number a
                string a
            end
            """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 405))
    
    def test_redecl_var_2(self):
        input = """func main()
            begin
                number a
                number b
                string c
                bool b
            end
            """
        expect = """Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input, expect, 406))
    
    def test_redecl_var_3(self):
        input = """ number a
            func main()
            begin
                string a
                return
            end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 407))
    
    def test_redecl_var_4(self):
        input = """ number a
            func main()
            begin
                number a
                begin
                    string a
                end
            end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 408))
    
    def test_redecl_var_5(self):
        input = """ number a
            number b
            func main()
            begin
                number a
            end
            number b
            """
        expect = """Redeclared Variable: b"""
        self.assertTrue(TestChecker.test(input, expect, 409))
        
    def test_redecl_func_4(self):
        input = """func main()
            begin
            end
            func foo (number a)
            begin
                bool a
            end
            """
        expect = """Redeclared Variable: a"""
        self.assertTrue(TestChecker.test(input, expect, 414))
        
    def test_redecl_func_5(self):
        input = """func main() 
            begin
            end
            func foo(number a) 
            begin
            end
            string a
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 415))
        
    ## BREAK/CONTINUE NOT IN LOOP
        
    def test_ifs_normal_preventDefault(self):
        input = """
        func f()
        begin
            var j <- 1
            for j until j > 11 by 1
            begin
            
            end
            break
        end
        
        func main()
        begin
            f()
        end
        """
        expect = "break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 410))
        
    def test_mil_1(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i < 10 by i
            begin
                continue
                break
            end
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 465))
    
    def test_mil_2(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i < 10 by i
            begin
                continue
            end
            break
        end
            """
        expect = """break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 466))
    
    def test_mil_3(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i < 10 by i
            begin
                break
            end
            continue
        end
            """
        expect = """continue Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 467))
    
    def test_mil_4(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i < 10 by i
            begin
                continue
                begin
                    break
                end
            end
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 468))
    
    def test_mil_5(self):
        input = """
        func main()
        begin
            number i <- 0
            for i until i < 10 by i + 1
            begin
                continue
            end
            begin
                break
            end
        end
            """
        expect = """break Not In Loop"""
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_476(self):
        input = """
            func f()
        begin
            var i <- 0
            for i until i > 10 by i
            begin
            
            end
            continue
        end
        func main()
        begin
            number x <- 2 + true
            writeNumber(x)
        end
            """
        expect = "continue Not In Loop"
        
        self.assertTrue(TestChecker.test(input, expect, 476))
        
    ## PASS ARRAY AS ARGUMENT
    
    def test_ifs_block_stmt(self):
        input = """
        func findMax(number x[10], number n)
        begin
            if (n = 1) return x[0]
            number k <- findMax(x, n - 1)
            if (k >= x[n]) return k
            return x[n]
        end
    
        func main() 
        begin
            dynamic x <- [3, 4, 8, 1, 2, 7, 9, 8, 5, 6]
            writeNumber(findMax(x, 10))
        end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 411))
        
    ## REDECLARED PARAMETERS
    
    def test_ifs_inherit_parent(self):
        input = """
        func foo (number n, string n) begin
        
        end 
        func main() begin
        
        end
        """
        expect = "Redeclared Parameter: n"
        self.assertTrue(TestChecker.test(input, expect, 412))
        
    def test_redecl_param_1(self):
        input = """func main() 
            begin
            end
            func foo (number a, string a)
            begin
            end
            """
        expect = """Redeclared Parameter: a"""
        self.assertTrue(TestChecker.test(input, expect, 416))
        
    def test_redecl_param_2(self):
        input = """func main() 
            begin
            end
            func foo (number foo) ## No error variable name can be same as func name
            begin
            end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 417))
    
    def test_redecl_param_3(self):
        input = """func main() 
            begin
            end
            func foo(number main)
            begin
            end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 418))
    
    def test_redecl_param_4(self):
        input = """func main()
            begin
            end
            func foo (number a)
            begin
            end
            func a (number foo)
            begin
            end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 419))


    def test_ifs_redecl_var(self):
        input = """
        func foo(number x) begin
            number a <- 7
        end
        func foo1(string x, bool x) begin
        
        end
        func main() begin
        
        end
        """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 497))    
    ## FOR MULTIPLE FUNCTIONS
   
    def test_redecl_func_3(self):
        input = """func main()
        begin
            number main
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 413))
    
    
    ## UNDECLARED IDENTIFIERS
    
    def test_undecl_var_1(self):
        input = """func main()
        begin
            a <- 2
            return
        end
            """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 420))
    
    def test_undecl_var_2(self):
        input = """number a
        func main()
        begin
            a <- 2
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 421))
    
    def test_undecl_var_3(self):
        input = """func main()
        begin
            var a <- 2
            var b <- a + 2
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 422))
    
    def test_undecl_var_4(self):
        input = """func main()
        begin
            begin
                number a
            end
            a <- 2
        end
            """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 423))
    
    def test_undecl_var_5(self):
        input = """
            func main() 
            begin 
            end
            func foo(number a)
            begin
                a <- 2
            end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 424))
        
    def test_478(self):
        input = """
        func main()
        begin
            dynamic x <- (x - 2) * (x + true)
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 478))
    
    def test_func_id(self):
        input = """
        func foo() return 1
        var a <- foo
        func main()
        begin
        end
            """
        expect = """Undeclared Identifier: foo"""
        self.assertTrue(TestChecker.test(input, expect, 494))
        
    def test_array_id(self):
        input = """
        func foo()
        begin
        end
        func main()
        begin
            a[0] <- 5
        end
            """
        expect = """Undeclared Identifier: a"""
        self.assertTrue(TestChecker.test(input, expect, 495)) 
            
    ## UNDECLARED FUNCTIONS
    
    def test_undecl_func_1(self):
        input = """
        func check()
        begin
        end
        func main()
        begin
            foo()
        end
            """
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 425))
    
    def test_undecl_func_2(self):
        input = """func main()
        begin
            number a
            a <- foo() + 5
        end
            """
        expect = """Undeclared Function: foo"""
        self.assertTrue(TestChecker.test(input, expect, 426))
        
    
    def test_func_pass(self):
        input = """
            func main()
            begin
                number arr <- 2
                main()
            end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 427))
        

    def test_undeclare_func(self):
        input = """
        func x() return
        func main()
        begin
            super()
        end
            """
        expect = """Undeclared Function: super"""
        self.assertTrue(TestChecker.test(input, expect, 492))


    def test_ifs_inherit_grandparent(self):
        input = """
        func foo(number a) begin
            writeNumber(a)
            number c <- 109
        end
        
        func main() begin
            foo(2018)
            goo(20, 1998)
        end
        
        func goo(number a, number b) begin            
            foo(3)
        end
         """
        expect = "Undeclared Function: goo"
        self.assertTrue(TestChecker.test(input, expect, 496))        
    ## TYPE MISMATCH STMT: ASSIGN-STMT
    
    def test_4001(self):
        input = """
            number a[3] <- [2,3,4]
            func main()
            begin
                a[3] <- "error here"
            end
            """
        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(3.0)]), StringLit(error here))"
        self.assertTrue(TestChecker.test(input, expect, 428))
        
    def test_ial_2(self):
        input = """
        number b1
        func main()
        begin
            bool a[5]
            bool b1 
            bool b2
            a <- [b1,b2]
        end
            """
        expect = """Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(Id(b1), Id(b2)))"""
        self.assertTrue(TestChecker.test(input, expect, 446))
        
    def test_ial_3(self):
        input = """
        string a[5]
        func main()
        begin
            number i1 <- 25
            number f2 <- 25.0
            a <- [i1,f2]
        end
            """
        expect = """Type Mismatch In Statement: AssignStmt(Id(a), ArrayLit(Id(i1), Id(f2)))"""
        self.assertTrue(TestChecker.test(input, expect, 447))
        
    def test_ial_5(self):
        input = """
        func main()
        begin
            number a[5]
            string s
            a[3] <- 2.5
            a[2] <- 5
            a[1] <- s
        end
            """
        expect = """Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a), [NumLit(1.0)]), Id(s))"""
        self.assertTrue(TestChecker.test(input, expect, 449))
        
    def test_tmms_asm_1(self):
        input = """
        func main()
        begin
            bool b
            number i
            dynamic v
            v <- v
        end
            """
        expect = """Type Cannot Be Inferred: AssignStmt(Id(v), Id(v))"""
        self.assertTrue(TestChecker.test(input, expect, 458))
        
    def test_471(self):
        input = """
            func main()
            begin
                dynamic c
                dynamic d
                d <- c
            end
            """
        expect = "Type Cannot Be Inferred: AssignStmt(Id(d), Id(c))"
        
        self.assertTrue(TestChecker.test(input, expect, 471))
        
    ## TYPE MISMATCH EXPRESSION: CALL-EXPR
        
    def test_4002(self):
        """Call function with the void type (wrong)"""
        
        input = """
            func foo(number x)
            begin
                return
            end
            
            func main()
            begin
                number x <- 2
                dynamic y
                y <- foo(x)
            end
            
            """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo), [Id(x)])"
        
        self.assertTrue(TestChecker.test(input, expect, 429))
        
    def test_tmme_c2_param_typ(self):
        """Pass wrong type as arguments"""
        
        input = """
        func foo(number a, number b)
        func main()
        begin
            number a <- 2
            string b <- "2.1"
            a <- foo(b,a) + 2
        end
        func foo(number a, number b)
        begin
            return a+b
        end
            """
        expect = """Type Mismatch In Expression: CallExpr(Id(foo), [Id(b), Id(a)])"""
        self.assertTrue(TestChecker.test(input, expect, 443))
        
    def test_tmme_c3_param_len(self):
        """Pass not enough parameters"""
        
        input = """
        func foo(number a, number b, number c)
        func main()
        begin
            number a <- 2
            number b <- 2.1
            a <- foo(a,b) + 2
        end
        func foo(number a, number b, number c)
        begin
            return a+b+c
        end
            """
        expect = """Type Mismatch In Expression: CallExpr(Id(foo), [Id(a), Id(b)])"""
        self.assertTrue(TestChecker.test(input, expect, 444))
        
    def test_tmms_func_2(self):
        input = """
        func foo(number a,number b,number c)
        begin
            return 0.0
        end
        
        func bar()
        begin
        end
        
        func main()
        begin
            number i
            number f
            f <- foo(i,f,f)+f ## infer: foo->number, a->number, b->number, c->number
            f <- foo(1,"2",3.0) ## invalid: param 2 mismatch
        end
            """
        expect = """Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0), StringLit(2), NumLit(3.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 461))
    
    ## TYPE MISMATCH EXPR: ARRAY-CELL
    
    def test_tmme_a1(self):
        input = """
        func main()
        begin
            number a[5]
            number b
            b <- a[5]
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test_tmme_a2(self):
        input = """
        func main()
        begin
            number a
            number b
            b <- a[5]
        end
            """
        expect = """Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(5.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 431))
    
    def test_tmme_a3(self):
        input = """
        func main()
        begin
            number a[5, 5]
            number b
            b <- a[1.0,"1"]
        end
            """
        expect = """Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), StringLit(1)])"""
        self.assertTrue(TestChecker.test(input, expect, 432))
    
    def test_array_asm(self):
        input = """
        func foo(number a) return "vankha"
        func main()
        begin
            number a[2,3]
            a[1,2,3] <- 1
        end
            """
        expect = """Type Mismatch In Expression: ArrayCell(Id(a), [NumLit(1.0), NumLit(2.0), NumLit(3.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 488))
        
           
    ## TYPE MISMATCH EXPR: BINARY-OP
    
    def test_tmme_b1_implicit(self):
        input = """
        func main()
        begin
            number a 
            string b
            ## a + b: Unknown a: number
            a <- a + b
        end
            """
        expect = """Type Mismatch In Expression: BinaryOp(+, Id(a), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 433))
    
    def test_tmme_b2_implicit(self):
        input = """
        func main()
        begin
            number a
            number b
            ## number -> number:OK
            b <- a
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 434))
    
    def test_tmme_b6_binary(self):
        input = """
        func main()
        begin
            dynamic a
            dynamic b
            a <- 1
            dynamic c
            c <- a + b
        end
            """
        expect = """['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"""
        self.assertTrue(TestChecker.test(input, expect, 438)) 
        
    def test_tmme_b7_binary(self):
        input = """
        func main()
        begin
            number a
            number b
            number c
            string d 
            string e 
            d <- d ... e ## valid
            b <- a % c ## valid
            a <- a == b ## invalid: a == b
        end
            """
        expect = """Type Mismatch In Expression: BinaryOp(==, Id(a), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 439))
    
    def test_tmme_b8_binary(self):
        input = """
        func main()
        begin
            number a
            bool b
            bool c
            b <- (b and c) or c ## valid
            b <- a and b ## invalid: a and b
        end
            """
        expect = """Type Mismatch In Expression: BinaryOp(and, Id(a), Id(b))"""
        self.assertTrue(TestChecker.test(input, expect, 440))
    
    def test_tmme_b9_binary(self):
        input = """
        func main()
        begin
            number a
            number b
            bool c
            bool d
            number e
            c <- b > e
            c <- e <= b
            d <- b == e ## invalid: b==e
        end
            """
        expect = "Type Mismatch In Expression: BinaryOp(==, Id(b), Id(e))"
        self.assertTrue(TestChecker.test(input, expect, 441))
        
    def test_472(self):
        input = """
        func main()
        begin
            dynamic x 
            x  <- (x - 2) * (x + true)
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, Id(x), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 472))    

    def test_477(self):
        input = """
        func main()
        begin
            number x <- 2 + true
            writeNumber(x)
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(+, NumLit(2.0), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 477))
        
    def test_479(self):
        input = """
        dynamic a
        func main()
        begin
            var i <- a ... 2.75
        end
        """
        expect = "Type Mismatch In Expression: BinaryOp(..., Id(a), NumLit(2.75))"
        self.assertTrue(TestChecker.test(input, expect, 479))
        
    ## TYPE CANNOT BE INFERRED: VARDECL
    
    def test_tmme_b3_implicit(self):
        input = """
        func main()
        begin
            number a <- 1
            number b <- a + 2
            string c <- 2.3
        end
            """
        expect = """Type Mismatch In Statement: VarDecl(Id(c), StringType, None, NumLit(2.3))"""
        self.assertTrue(TestChecker.test(input, expect, 435))
        
    def test_ifs_normal_super(self): # check again
    
        input = """
        dynamic x
        func main() 
        begin
            var y <- x[0, 0] + 1
            writeNumber(y)
        end
            """
        expect = "Type Cannot Be Inferred: VarDecl(Id(y), None, var, BinaryOp(+, ArrayCell(Id(x), [NumLit(0.0), NumLit(0.0)]), NumLit(1.0)))"
        self.assertTrue(TestChecker.test(input, expect, 470))
        
        
    def test_474(self):
        input = """
            dynamic y
            func main()
            begin
                var x <- 2
                if (true) 
                begin
                    var a <- y
                    if (true)
                    begin
                        x <- y
                    end
                end
            end
            """
        expect = "Type Cannot Be Inferred: VarDecl(Id(a), None, var, Id(y))"
        
        self.assertTrue(TestChecker.test(input, expect, 474))       


    def test_array_cell_nonatomic(self):
        input = """
        func main()
        begin
            number a[1,2,3]
            number x <- a[1]
        end
            """
        expect = """Type Mismatch In Statement: VarDecl(Id(x), NumberType, None, ArrayCell(Id(a), [NumLit(1.0)]))"""
        self.assertTrue(TestChecker.test(input, expect, 491))        
    ## TYPE MISMATCH EXPR: UNARY-OP
    
    def test_tmme_b4_unary(self):
        input = """
        func main()
        begin
            string a
            a <- -a
        end
            """
        expect = """Type Mismatch In Expression: UnaryOp(-, Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 436))
    
    def test_tmme_b5_unary(self):
        input = """
        func main()
        begin
            number a
            a <- not a
        end
            """
        expect = """Type Mismatch In Expression: UnaryOp(not, Id(a))"""
        self.assertTrue(TestChecker.test(input, expect, 437))
        
        
    #TYPE MISMATCH STMT: RETURN-STMT
    

    
    def test_invalid_param_2(self):
        input = """
            func inc(number a) 
            func main()
            begin
                string c <- "hello world" 
                var x <- inc(3)...c 
            end 
            func inc(number a) return a+1 
            """
        expect = """Type Mismatch In Statement: Return(BinaryOp(+, Id(a), NumLit(1.0)))"""
        self.assertTrue(TestChecker.test(input, expect, 486))
        
    def test_return_after(self):
        input = """
        func foo(string a, number b)
        begin
            if (b>0)
            begin
                return a ## -> string
            end
            return "a" ## -> string
            return 1 ## -> dont care
        end
        func main()
        begin
            writeString(foo("Hello",2))
        end
        
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 499))   
        
                 
    ## TYPE MISMATCH EXPRESSION: ARRAYLITERAL
    
    def test_ial_1(self):
        """Wrong type in array literal"""
        
        input = """
        func main()
        begin
            number a[5]
            a <- [1,"2.0"]
        end
            """
        expect = """Type Mismatch In Expression: ArrayLit(NumLit(1.0), StringLit(2.0))"""
        self.assertTrue(TestChecker.test(input, expect, 445))
    
    def test_ial_4(self):
        """Wrong type in array literal"""
        
        input = """
        func main()
        begin
            number a[5, 5]
            a <- [[1,2],[1,2,3],[1,2,"3"]]
        end
            """
        expect = """Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), StringLit(3)))"""
        self.assertTrue(TestChecker.test(input, expect, 448))
        
    def test_tmms_asm_2(self):
        input = """
        func main()
        begin
            bool b
            dynamic c
            number a[2, 3]
            a <- [[c, c, c], [c, c, c]]
        end
            """
        expect = """['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"""
        self.assertTrue(TestChecker.test(input, expect, 459))
        
    def test_475(self):
        input = """
            func main()
            begin
                number x[3] <- [2,3,"4"]
            end
            """
        expect = "Type Mismatch In Expression: ArrayLit(NumLit(2.0), NumLit(3.0), StringLit(4))"
        
        self.assertTrue(TestChecker.test(input, expect, 475))
        
    def test_array_as_param(self):
        input = """
        func foo1() return 2
        func foo2() return 3
        func main()
        begin
            number a[2] <- [ foo1(), foo2()]
            writeNumber(foo1())
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 490))              
    ## TYPE MISMATCH STMT: IF-STMT
        
    def test_tmms_condexpr_1(self):
        input = """
        func main()
        begin
            bool b
            number i
            if(b) 
            begin
            end
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test_tmms_condexpr_2(self):
        input = """
        func main()
        begin
            bool b
            number i
            if (b)
            begin
            end
            elif (i)
            begin 
            end
        end
            """
        expect = """Type Mismatch In Statement: If((Id(b), Block([])), [(Id(i), Block([]))], None)"""
        self.assertTrue(TestChecker.test(input, expect, 451))
    
    def test_tmms_condexpr_3(self):
        input = """
        func main()
        begin
            bool b1
            bool b2
            number i1
            number i2
            if(i1 = i2)
            begin
            end
            
            if(i1)
            begin
            end
            if(b1)
            begin
            end
        end
            """
        expect = """Type Mismatch In Statement: If((Id(i1), Block([])), [], None)"""
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test_tmms_condexpr_4(self):
        input = """
        func main()
        begin
            bool b1
            bool b2
            number i
            if (b1 and b2)
            begin
            end
            elif(b1 or b2)
            begin
            end
            elif (i)
            begin
            end
        end
            """
        expect = """Type Mismatch In Statement: If((BinaryOp(and, Id(b1), Id(b2)), Block([])), [(BinaryOp(or, Id(b1), Id(b2)), Block([])), (Id(i), Block([]))], None)"""
        self.assertTrue(TestChecker.test(input, expect, 453))
        
        
    ## TYPE MISMATCH STMT: FOR-STMT
    
    def test_tmms_forexpr_1(self):
        input = """
        func main()
        begin
            bool b
            var i <- 0
            for i until i<10 by i+1
            begin
            end
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test_tmms_forexpr_2(self):
        input = """
        func main()
        begin
            bool b <- true
            number i
            for b until i<10 by i*2
            begin
            end
        end
            """
        expect = """Type Mismatch In Statement: For(Id(b), BinaryOp(<, Id(i), NumLit(10.0)), BinaryOp(*, Id(i), NumLit(2.0)), Block([]))"""
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test_tmms_forexpr_3(self):
        input = """
        func main()
        begin
            bool b <- true
            dynamic i <- 0
            for i until i<10 by i<10
            begin
            end
        end
            """
        expect = """Type Mismatch In Statement: For(Id(i), BinaryOp(<, Id(i), NumLit(10.0)), BinaryOp(<, Id(i), NumLit(10.0)), Block([]))"""
        self.assertTrue(TestChecker.test(input, expect, 456))
    
    def test_tmms_forexpr_4(self):
        input = """
        func main()
        begin
            bool b
            number i
            for i until i+1 by i<10
            begin 
            end
        end
            """
        expect = """Type Mismatch In Statement: For(Id(i), BinaryOp(+, Id(i), NumLit(1.0)), BinaryOp(<, Id(i), NumLit(10.0)), Block([]))"""
        self.assertTrue(TestChecker.test(input, expect, 457))
        
    
    ## TYPE MISMTACH STMT: CALL-STMT
    
    def test_tmms_func_1(self):
        input = """
        func foo()
        begin
            return 0
        end
        func main()
        begin
            number i 
            number f
            f <- f+i
            foo() ## foo -> int (return - not auto anymore) != void (CallExpr) => INVALID !!
            f <- f+foo(i)
            i <- i+f
        end
            """
        expect = """Type Mismatch In Statement: CallStmt(Id(foo), [])"""
        self.assertTrue(TestChecker.test(input, expect, 460))
    
    def test_tmms_func_3(self):
        input = """
        func foo(number a,number b,number c)
        begin
            return 0.0 
        end
        func main()
        begin
            number i
            number f
            f <- foo(i,f,f)+f ## infer: foo->number, a->number, b->number, c->number
            f <- foo(1,2.0,3.0) 
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 462))
    
    def test_tmms_func_4(self):
        input = """
        func foo(number a,number b,number c, number d)
        begin
            return 0
        end
        func main()
        begin
            number i
            number f
            f <- f+i
            begin
                f <- foo(i,f,f,i) ## infer: foo->number,a->number,b->number,c->number
            end
            f <- foo(1,2.0,3.0,1)
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 463))
    
    # def test_tmms_func_5(self):
    #     input = """
    #     func foo(number a,number b,number c, number d)
    #     begin
    #         a <- 5
    #         return a ## foo->number
    #     end
    #     func main()
    #     begin
    #         var f <- foo(1,2,3,4) ## f->number
    #         f <- f + "wrong"
    #     end
    #         """
    #     expect = """Type Mismatch In Expression: BinaryOp(+, Id(f), StringLit(wrong))"""
    #     self.assertTrue(TestChecker.test(input, expect, 464))
        
    def test_infer_func_3(self):
        input = """
        func foo(number a, number b) return 1.2
        func main()
        begin
            foo(1,2) ## error here because foo returns number type, not void
            number a <- foo(1,2) + 1
        end
            """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0), NumLit(2.0)])"
        self.assertTrue(TestChecker.test(input, expect, 484))
        
        
    def test_out_param(self):
        input = """
        func foo(number x[2]) return
        func main()
        begin
            foo(1)
        end
            """
        expect = """Type Mismatch In Statement: CallStmt(Id(foo), [NumLit(1.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 489))
        
    ## INFER TYPE PARAMETER
        
    def test_473(self):
        input = """
            func foo(number x)
            begin
                return x
            end
        
            func main()
            begin
                dynamic x <-2 
                dynamic a
                var y <- 2
                x <- y + foo(a)
            end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        
        self.assertTrue(TestChecker.test(input, expect, 473))
    
    

    ## INFER VARDECL
    def test_var(self):
        input = """
        func main()
        begin
            var a <- 1
        end
            """
        expect = """['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"""
        self.assertTrue(TestChecker.test(input, expect, 480))
    
    def test_infer_var(self):
        input = """
        func main()
        begin
            var a <- 10
            var b <- "100"
            var c <- a < 10
            writeNumber(a)
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 481))
    
    def test_infer_func_1(self):
        
        input = """
        func foo(number a, number b) return 1.2
        func main()
        begin
            number a <- foo(1,2)
            writeNumber(foo(1,2))
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 482))
        
    def test_infer_func_2(self):
        input = """
        func foo(number a, number b) return 1.2
        func main()
        begin
            number a <- foo(1,2) + 1
            writeNumber(foo(1,2))
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 483))
    

    ## TYPE MISMATCH STMT: VARDECL
    def test_array_decl(self):
        input = """
        func foo(number a) return "vankha"
        func main()
        begin
            number a[3] <- [1,2]
        end
            """
        expect = """Type Mismatch In Statement: VarDecl(Id(a), ArrayType([3.0], NumberType), None, ArrayLit(NumLit(1.0), NumLit(2.0)))"""
        self.assertTrue(TestChecker.test(input, expect, 487)) 
        
    def test_nonatomic_cell_init(self):
        input = """
        func x() return
        func main()
        begin
            number a[2, 3]
            number b <- a[0, 0]
            dynamic c <- a[0]
        end
            """
        expect = """['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"""
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_coercion_array_intfloat(self):
        input = """
        func main()
        begin
            number a[4] <- [1,2,3,4]
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 498)) 

    #################### Check function redeclared/no definition ##########
    
    def test_no_definition(self):
        input = """
            func f(number a) return 1
            func f(number x)
            
            func main()
            begin
                number a <- f(2) + 1
            end
        """
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 500))
        
    def test_no_definition_2(self):
        input = """
            func f(number x)
            func f(number a) return 1
            
            func main()
            begin
                number a <- f(2) + 1
            end
        """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 501)) 
        
    def test_no_definition_3(self):
        input = """
            func f(number x)
            
            func main()
            begin
                number a <- f(2) + 1
            end
        """
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 502)) 
    
    def test_no_definition_4(self):
        input = """
            func f(number x)
            func f(number x)
            func f(number x)
            func f(number x) return 1
            
            func main()
            begin
                number a <- f(2) + 1
            end
        """
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 503)) 
    
    def test_no_definition_4(self):
        input = """
            func f(number x)
            func f(number x) return 1
            func f(number x)
            func f(number x)
            
            func main()
            begin
                number a <- f(2) + 1
            end
        """
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 504)) 
    
    
    def test_tmme_c1_void_CallExpr(self):
        """Return() in void function -> infer call expr"""
        input = """
        func foo()
        func main()
        begin
            number a <- 2
            a <- foo() + 2
        end
        func foo()
        begin
            return
        end
            """
        expect = """Type Mismatch In Statement: Return()"""
        self.assertTrue(TestChecker.test(input, expect, 442))    
    
    def test_redecl_var_6(self):
        input = """func main() 
            begin 
            end
            func c() 
            begin 
            end
            number c
            """
        expect = """['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"""
        self.assertTrue(TestChecker.test(input, expect, 505))
    
    def test_redecl_func_2(self):
        input = """func main() begin 
        end
            func c() begin 
            end
            func c() begin 
            end
            """
        expect = """Redeclared Function: c"""
        self.assertTrue(TestChecker.test(input, expect, 506))
        
    def test_infer_subscript(self):
        input = """
        func foo()
        func bar()
        func main()
        begin
            number a[3,4]
            a[foo(), 1+4] <- 222
            a[1,2] <- bar()
            writeNumber(foo())
            writeNumber(bar())
        end
        func foo() return 1
        func bar() return 2
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 507))
        
    def test_undecl_mismatch_param(self):
        input = """
        func foo()
        func main()
        begin
        end
        number a <- foo(1, 2)
        func foo() return 1
            """
        expect = """Type Mismatch In Expression: CallExpr(Id(foo), [NumLit(1.0), NumLit(2.0)])"""
        self.assertTrue(TestChecker.test(input, expect, 508))
        
    def test_undecl_func_3(self):
        """forward invocation"""
        input = """
        func foo()
        begin
            return 1
        end
        
        func check()
        begin
            return 2
        end
        
        func main()
        begin
            number a
            begin
                a <- foo() + 5
            end
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 509))
    
    def test_undecl_func_4(self):
        """backward invocation"""
        input = """
        func foo()
        func main()
        begin
            number a
            a <- foo() + 5
        end
        func foo()
        begin
           return 1
        end
            """
        expect = "['s', 'u', 'c', 'c', 'e', 's', 's', 'f', 'u', 'l']"
        self.assertTrue(TestChecker.test(input, expect, 510))
    
    def test_undecl_func_5(self):
        input = """
        func foo()
        func main()
        begin
            number a
            a <- foo() + 5
        end
        
        func foo()
        begin
            barrr()
            return 1
        end
        
        func bar()
        begin
            return 2
        end
            """
        expect = """Undeclared Function: barrr"""
        self.assertTrue(TestChecker.test(input, expect, 511))

    def test443(self): 
        input = """
number x
number y
func f()

func main()
    return
"""
        expect = "No Function Definition: f"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_param_array(self):
        input = """
        number x
        number y
        func f(number a[10], number x)
        func f(number a[5], number x)
            return x
        
        func main()
            return
        """
        expect = "Redeclared Function: f"
        self.assertTrue(TestChecker.test(input, expect, 512))