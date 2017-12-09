
from vsg import rule
from vsg import fix

import re


class rule_003(rule.rule):
    '''Generic rule 003 checks spacing between "generic" keyword and the open parenthesis.'''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'generic'
        self.identifier = '003'
        self.solution = 'Change spacing between "generic" and "(" to one space.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isGenericKeyword:
                if not re.match('^\s*\S+\s\(', oLine.line):
                    self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_after_word(self, oFile.lines[iLineNumber], 'generic')
