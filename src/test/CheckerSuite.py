import unittest
from TestUtils import TestChecker

#from AST import *
from main.zcode.utils.AST import *


class CheckerSuite(unittest.TestCase):
    #invalid_arrayliteral
    # def test_001(self):
    #     input = """var a <- [[1,2],[1,2,3]]
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
    #     self.assertTrue(TestChecker.test(input, expect, 401))
    # def test_002(self):
    #     input = """
    #     string b
    #     var a <- [[1,2,4],[1,2,3],[b,b,b]]
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(4.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(Id(b), Id(b), Id(b)))"
    #     self.assertTrue(TestChecker.test(input, expect, 402))
    # def test_003(self):
    #     input = """var a <- [[1,2,3],[1,2,3],[1,2,3,4],[1,2,3]]
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0), NumLit(4.0)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
    #     self.assertTrue(TestChecker.test(input, expect, 403))
    # def test_004(self):
    #     input = """
    #     dynamic t
    #     var a <- [[1,2],[1,t],[1,2,3]]
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), Id(t)), ArrayLit(NumLit(1.0), NumLit(2.0), NumLit(3.0)))"
    #     self.assertTrue(TestChecker.test(input, expect, 404))
    # def test_005(self):
    #     input = """
    #     dynamic ans
    #     dynamic temp <- "abc"
    #     var a <- [[1,2],[1,ans],[temp,ans]]
    #     """
    #     expect = "Type Mismatch In Expression: ArrayLit(ArrayLit(NumLit(1.0), NumLit(2.0)), ArrayLit(NumLit(1.0), Id(ans)), ArrayLit(Id(temp), Id(ans)))"
    #     self.assertTrue(TestChecker.test(input, expect, 405))
    # def test_006(self):
    #     input = """
    #     dynamic ans
    #     number a[3.0,4.0] <- [[ans,ans,ans,ans],[1,2,ans,4],[1,2,3,4]]
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 406))
    # def test_007(self):
    #     input = """number a[2,3] <- [[2,3],[2,3]]
    #     """
    #     expect = "Type Mismatch In Statement: VarDecl(Id(a), ArrayType([2.0, 3.0], NumberType), None, ArrayLit(ArrayLit(NumLit(2.0), NumLit(3.0)), ArrayLit(NumLit(2.0), NumLit(3.0))))"
    #     self.assertTrue(TestChecker.test(input, expect, 407))
    # def test_008(self):
    #     input = """
    #     dynamic t
    #     dynamic b
    #     dynamic c
    #     dynamic d
    #     dynamic e
    #     dynamic f
    #     number a[2,3] <- [[b,t,d],[c,e,f]]
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 408))
    # def test_009(self):
    #     input = """
    #     dynamic t
    #     dynamic b
    #     dynamic c
    #     dynamic d
    #     dynamic e
    #     dynamic f
    #     number a[2.0,3.0,2.0] <- [[[b,c],[d,d],[t,f]],[[e,e],[e,t],[f,d]]]
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 409))
    # def test_010(self):
    #     input = """
    #     dynamic t
    #     dynamic b
    #     dynamic c
    #     dynamic d
    #     dynamic e
    #     dynamic f
    #     number a[2.0,3.0,2.0] <- [[[1,c],[3,d],[t,f]],[[b,9],[e,t],[2,d]]]
    #     """
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input, expect, 410))
#     def test455(self):
#         input = """
#     dynamic a
#     dynamic b
#     dynamic c
#     number arr[1, 2,2] <- [[a, b]]
#     ## number c[2, 2] <- arr
# """
#         expect = "Type Mismatch In Statement: VarDecl(Id(arr), ArrayType([2.0, 2.0], NumberType), None, ArrayLit(ArrayLit(Id(a), Id(b))))"
#         self.assertTrue(TestChecker.test(input, expect, 455))
    def test485(self):
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
        
        self.assertTrue(TestChecker.test(input, expect, 485))