# Generated from Latte.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LatteParser import LatteParser
else:
    from LatteParser import LatteParser

from .LatteAst import *
# This class defines a complete generic visitor for a parse tree produced by LatteParser.

class LatteVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LatteParser#program.
    def visitProgram(self, ctx:LatteParser.ProgramContext):
        for i in range (ctx.getChildCount()):
            child = ctx.getChild(i)
            child_result = self.visit(child)

    # Visit a parse tree produced by LatteParser#topDef.
    def visitTopDef(self, ctx:LatteParser.TopDefContext):
        print(f" type = {ctx.type_().getText()} name = {ctx.ID()}\n")
        t = ctx.type_().getText()
        name = ctx.ID().getText()
        args = []
        if ctx.arg() is not None:
            args = self.visit(ctx.arg())
        for i in args:
            print(f"{i.type} {i.name} " );
        block = self.visit(ctx.block())
        return TopdefNode(t, name, args, block)


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
            print(s.getText())
            stmt = self.visit(s)
            stmt.text()
            stmts.append(stmt)
        return BlockStmtNode("Block",stmts)



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

        return DeclStmtNode("Decl",t,items)


    # Visit a parse tree produced by LatteParser#Ass.
    def visitAss(self, ctx:LatteParser.AssContext):
        name = ctx.ID().getText()
        #TODO
        expr = "EXPR"
        return AssStmtNode("Ass",name, expr)


    # Visit a parse tree produced by LatteParser#Incr.
    def visitIncr(self, ctx:LatteParser.IncrContext):
        name = ctx.ID().getText()
        return IncDecStmtNode("Inc", name)


    # Visit a parse tree produced by LatteParser#Decr.
    def visitDecr(self, ctx:LatteParser.DecrContext):
        name = ctx.ID().getText()
        return IncDecStmtNode("Dec", name)


    # Visit a parse tree produced by LatteParser#Ret.
    def visitRet(self, ctx:LatteParser.RetContext):
        return RetStmtNode("Ret")


    # Visit a parse tree produced by LatteParser#VRet.
    def visitVRet(self, ctx:LatteParser.VRetContext):
        # TODO
        expr = "EXPR"
        return RetStmtNode("Ret", expr)


    # Visit a parse tree produced by LatteParser#Cond.
    def visitCond(self, ctx:LatteParser.CondContext):
        #TODO
        expr = "EXPR"
        blockTrue = self.visit(ctx.sTrue)
        return CondStmtNode ("Cond", expr, blockTrue)


    # Visit a parse tree produced by LatteParser#CondElse.
    def visitCondElse(self, ctx:LatteParser.CondElseContext):
        #TODO
        expr = "EXPR"
        blockTrue = self.visit(ctx.sTrue)
        blockFalse = self.visit(ctx.sFlase)
        return CondStmtNode ("CondElse", expr, blockTrue, blockFalse)


    # Visit a parse tree produced by LatteParser#While.
    def visitWhile(self, ctx:LatteParser.WhileContext):
        #TODO
        expr = "EXPR"
        stmt = self.visit(ctx.stmt())
        return WhileStmtNode("While", expr, stmt)

    # Visit a parse tree produced by LatteParser#SExp.
    def visitSExp(self, ctx:LatteParser.SExpContext):
        # TODO
        expr = "EXPR"
        return ExpStmtNode("Exp", expr)

    # Visit a parse tree produced by LatteParser#Int.
    def visitInt(self, ctx:LatteParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#Str.
    def visitStr(self, ctx:LatteParser.StrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#Bool.
    def visitBool(self, ctx:LatteParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#Void.
    def visitVoid(self, ctx:LatteParser.VoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#item.
    def visitItem(self, ctx:LatteParser.ItemContext):
        name = ctx.ID().getText()
        # TODO
        expr = None
        if ctx.expr() is not None:
            expr = "EXPR"
        i = ItemNodeMy(name, expr)
        return i


    # Visit a parse tree produced by LatteParser#EId.
    def visitEId(self, ctx:LatteParser.EIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EFunCall.
    def visitEFunCall(self, ctx:LatteParser.EFunCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#ERelOp.
    def visitERelOp(self, ctx:LatteParser.ERelOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#ETrue.
    def visitETrue(self, ctx:LatteParser.ETrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EOr.
    def visitEOr(self, ctx:LatteParser.EOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EInt.
    def visitEInt(self, ctx:LatteParser.EIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EUnOp.
    def visitEUnOp(self, ctx:LatteParser.EUnOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EStr.
    def visitEStr(self, ctx:LatteParser.EStrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EMulOp.
    def visitEMulOp(self, ctx:LatteParser.EMulOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EAnd.
    def visitEAnd(self, ctx:LatteParser.EAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EParen.
    def visitEParen(self, ctx:LatteParser.EParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EFalse.
    def visitEFalse(self, ctx:LatteParser.EFalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LatteParser#EAddOp.
    def visitEAddOp(self, ctx:LatteParser.EAddOpContext):
        return self.visitChildren(ctx)


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