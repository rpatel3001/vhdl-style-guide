
from vsg import rule
from vsg import check
from vsg import fix


class rule_001(rule.rule):
    '''Generate rule 001 checks for spaces at the beginning of the line.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'generate'
        self.identifier = '001'
        self.solution = 'Ensure proper indentation.'
        self.phase = 4

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenerateKeyword or oLine.isGenerateBegin or oLine.isGenerateEnd:
                check.indent(self, oLine, iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.indent(self, oFile.lines[iLineNumber])
