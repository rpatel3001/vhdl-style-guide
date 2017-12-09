
from vsg import rule

import re


class rule_012(rule.rule):
    '''
    Port rule 012 checks for default assignments in port declarations.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'port'
        self.identifier = '012'
        self.solution = 'Remove default assignment in port declaration'
        self.phase = 1
        self.fixable = False  # Allow user to fix the default assignments

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isPortDeclaration:
                if re.match('^.*:=', oLine.line):
                    self.add_violation(iLineNumber)
