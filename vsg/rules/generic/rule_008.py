
from vsg import rule
from vsg import check
from vsg import fix


class rule_008(rule.rule):
    '''
    Generic rule 008 checks the indentation of closing parenthesis for generic maps.
    '''

    def __init__(self):
        rule.rule.__init__(self, 'generic', '008')
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isEndGenericMap and not oLine.isGenericDeclaration:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.indent(self, oFile.lines[iLineNumber])
