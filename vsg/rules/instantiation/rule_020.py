
from vsg.rules.instantiation import instantiation_rule

import copy


class rule_020(instantiation_rule):
    '''
    Instantiation rule 020 checks for a port assignment on the same line as the port map keywords.
    '''

    def __init__(self):
        instantiation_rule.__init__(self)
        self.identifier = '020'
        self.solution = 'Move port assignment to it\'s own line.'
        self.phase = 1

    def analyze(self, oFile):
        lFailureLines = []
        for iLineNumber, oLine in enumerate(oFile.lines):
            if oLine.isInstantiationPortAssignment and oLine.isInstantiationPortKeyword:
                self.add_violation(iLineNumber)

    def _fix_violations(self, oFile):
        for iLineNumber in self.violations[::-1]:
            oFile.lines.insert(iLineNumber + 1, copy.deepcopy(oFile.lines[iLineNumber]))
            oLine = oFile.lines[iLineNumber]
            oLine.update_line(oLine.line.split('(')[0] + ' (')
            oLine.isInstantiationPortAssignment = False
            oLine = oFile.lines[iLineNumber + 1]
            oLine.update_line('  ' + oLine.line.split('(')[1])
            oLine.isInstantiationPortKeyword = False
