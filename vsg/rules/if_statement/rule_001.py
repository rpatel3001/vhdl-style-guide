
from vsg.rules import indent_rule


class rule_001(indent_rule):
    '''
    If rule 001 checks the indent of the "if" keyword.
    '''

    def __init__(self):
        indent_rule.__init__(self, 'if', '001', 'isIfKeyword')

#    def analyze(self, oFile):
#        for iLineNumber, oLine in enumerate(oFile.lines):
#            if oLine.isIfKeyword or oLine.isElseIfKeyword or oLine.isEndIfKeyword or oLine.isElseKeyword:
#                check.indent(self, oLine, iLineNumber)
