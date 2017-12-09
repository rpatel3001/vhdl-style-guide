
from vsg import rule
from vsg import fix

import re


class rule_014(rule.rule):
    '''
    Process rule 014 checks for a single space between the ) and "is" keyword.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'process'
        self.identifier = '014'
        self.solution = 'Ensure only a single space exists between the ) and "is" keyword.'
        self.phase = 2

    def analyze(self, oFile):
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isSensitivityListEnd:
                if re.match('^.*\)\s*is', oLine.lineLower):
                    if not re.match('^.*\)\sis', oLine.lineLower):
                        self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations:
            fix.enforce_one_space_before_word(self, oFile.lines[iLineNumber], 'is')
