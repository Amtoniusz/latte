# Generated from Latte.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LatteParser import LatteParser
else:
    from LatteParser import LatteParser

from lib.EConstNode import EConstNode
from lib.EFunCallNode import EFunCallNode
from lib.ExpStmtNode import ExpStmtNode
from lib.ItemNodeMy import ItemNodeMy
from lib.DeclStmtNode import DeclStmtNode
from lib.EIdNode import EIdNode
from lib.ERelNode import ERelNode
from lib.EBinNode import EBinNode
from lib.AssStmtNode import AssStmtNode
from lib.BlockStmtNode import BlockStmtNode
from lib.WhileStmtNode import WhileStmtNode
from lib.RetStmtNode import RetStmtNode
from lib.TopdefNode import TopdefNode
from lib.ArgNode import ArgNode
from lib.CondStmtNode import CondStmtNode
from lib.EUnNode import EUnNode
from lib.EAndOrNode import EOrNode,EAndNode
from lib.IncDecStmtNode import IncDecStmtNode
from lib.IncDecStmtNode import IncDecStmtNode


# This class defines a complete generic visitor for a parse tree produced by LatteParser.
class LatteVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LatteParser#program.
    def visitProgram(self, ctx:LatteParser.ProgramContext):
        topDefs = []
        for i in range (ctx.getChildCount()):
            child = ctx.getChild(i)
            child_result = self.visit(child)
            topDefs.append(child_result)
        return topDefs


    # Visit a parse tree produced by LatteParser#topDef.
    def visitTopDef(self, ctx:LatteParser.TopDefContext):
        # print(f" type = {ctx.type_().getText()} name = {ctx.ID()}\n")
        t = ctx.type_().getText()
        name = ctx.ID().getText()
        args = []
        if ctx.arg() is not None:
            args = self.visit(ctx.arg())
        # for i in args:
        #     print(f"{i.type} {i.name} " );
        block = self.visit(ctx.block())
        line = (ctx.start.line,ctx.start.column)
        return TopdefNode(t, name, args, block, line)


    # Visit a parse tree produced by LatteParser#arg.
    def visitArg(self, ctx:LatteParser.ArgContext):
        args = []
        counter = 0
        t = ""
        name = ""
        if ctx.getChildCount() == 0:
            return []
        for i in range (ctx.getChildCount()):
            a = ctx.getChild(i)
            if i % 3 == 0:
                t = a.getText()
            if i % 3 == 1:
                name = a.getText()
                args.append(ArgNode(t, name))
        return args

    # Visit a parse tree produced by LatteParser#block.
    def visitBlock(self, ctx:LatteParser.BlockContext):
        stmts = []
        for i in range (1,ctx.getChildCount()-1):
            s =  ctx.getChild(i)
            # print(s.getText())
            stmt = self.visit(s)
            # stmt.text()
            stmts.append(stmt)
        line = (ctx.start.line,ctx.start.column)    
        return BlockStmtNode("Block",stmts, line)



    # Visit a parse tree produced by LatteParser#Empty.
    def visitEmpty(self, ctx:LatteParser.EmptyContext):
        return EmptyStmtNode("Empty")


    # Visit a parse tree produced by LatteParser#BlockStmt.
    def visitBlockStmt(self, ctx:LatteParser.BlockStmtContext):
        return self.visit(ctx.block())


    # Visit a parse tree produced by LatteParser#Decl.
    def visitDecl(self, ctx:LatteParser.DeclContext):
        t = ctx.type_().getText()
        items = []
        for i in range (1,ctx.getChildCount()):
            it =  ctx.getChild(i)
            if i % 2 == 1:
                item = self.visit(it)
                items.append(item)
        line = (ctx.start.line,ctx.start.column)          
        return DeclStmtNode("Decl",t,items, line)


    # Visit a parse tree produced by LatteParser#Ass.
    def visitAss(self, ctx:LatteParser.AssContext):
        name = ctx.ID().getText()
        expr = self.visit(ctx.expr())
        line = (ctx.start.line,ctx.start.column)  
        return AssStmtNode("Ass",name, expr, line)


    # Visit a parse tree produced by LatteParser#Incr.
    def visitIncr(self, ctx:LatteParser.IncrContext):
        name = ctx.ID().getText()
        line = (ctx.start.line,ctx.start.column)
        return IncDecStmtNode("Inc", name, line)


    # Visit a parse tree produced by LatteParser#Decr.
    def visitDecr(self, ctx:LatteParser.DecrContext):
        name = ctx.ID().getText()
        line = (ctx.start.line,ctx.start.column)
        return IncDecStmtNode("Dec", name, line)


    # Visit a parse tree produced by LatteParser#Ret.
    def visitRet(self, ctx:LatteParser.RetContext):
        expr = self.visit(ctx.expr())
        line = (ctx.start.line,ctx.start.column)
        return RetStmtNode("Ret", expr, line)


    # Visit a parse tree produced by LatteParser#VRet.
    def visitVRet(self, ctx:LatteParser.VRetContext):
        line = (ctx.start.line,ctx.start.column)
        return RetStmtNode("VRet",None , line)


    # Visit a parse tree produced by LatteParser#Cond.
    def visitCond(self, ctx:LatteParser.CondContext):
        expr = self.visit(ctx.expr())
        blockTrue = self.visit(ctx.sTrue)
        line = (ctx.start.line,ctx.start.column)
        return CondStmtNode ("Cond", expr, blockTrue, None,line)


    # Visit a parse tree produced by LatteParser#CondElse.
    def visitCondElse(self, ctx:LatteParser.CondElseContext):
        expr = self.visit(ctx.expr())
        blockTrue = self.visit(ctx.sTrue)
        blockFalse = self.visit(ctx.sFlase)
        line = (ctx.start.line,ctx.start.column)
        return CondStmtNode ("CondElse", expr, blockTrue, blockFalse, line)


    # Visit a parse tree produced by LatteParser#While.
    def visitWhile(self, ctx:LatteParser.WhileContext):
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        line = (ctx.start.line,ctx.start.column)
        return WhileStmtNode("While", expr, stmt, line)

    # Visit a parse tree produced by LatteParser#SExp.
    def visitSExp(self, ctx:LatteParser.SExpContext):
        expr = self.visit(ctx.expr())
        return ExpStmtNode("Exp", expr)

    
    # Visit a parse tree produced by LatteParser#Int.
    def visitInt(self, ctx:LatteParser.IntContext):
        return self.visitChildren(ctx) #DONE


    # Visit a parse tree produced by LatteParser#Str.
    def visitStr(self, ctx:LatteParser.StrContext):
        return self.visitChildren(ctx)#DONE


    # Visit a parse tree produced by LatteParser#Bool.
    def visitBool(self, ctx:LatteParser.BoolContext):
        return self.visitChildren(ctx)#DONE


    # Visit a parse tree produced by LatteParser#Void.
    def visitVoid(self, ctx:LatteParser.VoidContext):
        return self.visitChildren(ctx)#DONE


    # Visit a parse tree produced by LatteParser#item.
    def visitItem(self, ctx:LatteParser.ItemContext):
        line = (ctx.start.line,ctx.start.column)
        name = ctx.ID().getText()
        expr = None
        if ctx.expr() is not None:
            expr = self.visit(ctx.expr())   
        i = ItemNodeMy(name, expr, line)
        return i


    # Visit a parse tree produced by LatteParser#EId.
    def visitEId(self, ctx:LatteParser.EIdContext):
        name = ctx.ID().getText()
        line = (ctx.start.line,ctx.start.column)
        return EIdNode("EId", name, line)


    # Visit a parse tree produced by LatteParser#EFunCall.
    def visitEFunCall(self, ctx:LatteParser.EFunCallContext):
        name = ctx.ID().getText()
        exprs = []
        for i in range (2,ctx.getChildCount()-1):
            expr =  ctx.getChild(i)
            if i % 2 == 0:
                expr = self.visit(expr)
                exprs.append(expr)
        line = (ctx.start.line,ctx.start.column)        
        return EFunCallNode ("EFunCall", name, exprs, line)


    # Visit a parse tree produced by LatteParser#ERelOp.
    def visitERelOp(self, ctx:LatteParser.ERelOpContext):
        op = ctx.relOp().getText();
        exprL = self.visit(ctx.left)
        exprR = self.visit(ctx.right)
        line = (ctx.start.line,ctx.start.column)
        return ERelNode ("ERel", exprL, exprR, op, line)

    # Visit a parse tree produced by LatteParser#ETrue.
    def visitETrue(self, ctx:LatteParser.ETrueContext):
        return EConstNode("ETrue", "boolean", "true")


    # Visit a parse tree produced by LatteParser#EOr.
    def visitEOr(self, ctx:LatteParser.EOrContext):
        op = '||'
        exprL = self.visit(ctx.left)
        exprR = self.visit(ctx.right)
        line = (ctx.start.line,ctx.start.column)
        return EOrNode ("EOr", exprL, exprR, op, line)


    # Visit a parse tree produced by LatteParser#EInt.
    def visitEInt(self, ctx:LatteParser.EIntContext):
        i = ctx.INT().getText()
        return EConstNode("EInt", "int", i)


    # Visit a parse tree produced by LatteParser#EUnOp.
    def visitEUnOp(self, ctx:LatteParser.EUnOpContext):
        op = ctx.getChild(0).getText()
        expr = self.visit(ctx.expr())
        # print(f"OPERATOR EUNOP = {op}\n")
        line = (ctx.start.line,ctx.start.column)
        return EUnNode ("EUn", expr, op, line)


    # Visit a parse tree produced by LatteParser#EStr.
    def visitEStr(self, ctx:LatteParser.EStrContext):
        s = ctx.STR().getText()
        return EConstNode("EStr", "string", s)


    # Visit a parse tree produced by LatteParser#EMulOp.
    def visitEMulOp(self, ctx:LatteParser.EMulOpContext):
        op = ctx.mulOp().getText();
        exprL = self.visit(ctx.left)
        exprR = self.visit(ctx.right)
        line = (ctx.start.line,ctx.start.column)
        return EBinNode ("EMul", exprL, exprR, op, line)


    # Visit a parse tree produced by LatteParser#EAnd.
    def visitEAnd(self, ctx:LatteParser.EAndContext):
        op = "&&"
        exprL = self.visit(ctx.left)
        exprR = self.visit(ctx.right)
        line = (ctx.start.line,ctx.start.column)
        return EAndNode ("EAnd", exprL, exprR, op, line)



    # Visit a parse tree produced by LatteParser#EParen.
    def visitEParen(self, ctx:LatteParser.EParenContext):
        return self.visit(ctx.expr())


    # Visit a parse tree produced by LatteParser#EFalse.
    def visitEFalse(self, ctx:LatteParser.EFalseContext):
        return EConstNode("EFalse", "boolean", "false")


    # Visit a parse tree produced by LatteParser#EAddOp.
    def visitEAddOp(self, ctx:LatteParser.EAddOpContext):
        op = ctx.addOp().getText();
        exprL = self.visit(ctx.left)
        exprR = self.visit(ctx.right)
        line = (ctx.start.line,ctx.start.column)
        return EBinNode ("EAdd", exprL, exprR, op, line)


    # Visit a parse tree produced by LatteParser#addOp.
    def visitAddOp(self, ctx:LatteParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#mulOp.
    def visitMulOp(self, ctx:LatteParser.MulOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#relOp.
    def visitRelOp(self, ctx:LatteParser.RelOpContext):
        return self.visitChildren(ctx)



del LatteParser