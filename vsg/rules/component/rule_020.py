
from vsg import rule
from vsg import check
from vsg import fix
from vsg import line


class rule_020(rule.rule):
    '''
    Entity rule 020 ensures the alignment of comments in a component declaration.
    '''

    def __init__(self):
        rule.rule.__init__(self)
        self.name = 'component'
        self.identifier = '020'
        self.solution = 'Inconsistent alignment of comments in component instantiation.'
        self.phase = 6

    def analyze(self, oFile):
        lGroup = []
        fGroupFound = False
        iStartGroupIndex = None
        for iLineNumber, oLine in enumerate(oFile.lines):
            fGroupFound, iStartGroupIndex = search_for_group(fGroupFound, oLine, iStartGroupIndex, iLineNumber)
            if oLine.isComponentEnd:
                lGroup.append(oLine)
                fGroupFound = False
                check.keyword_alignment(self, iStartGroupIndex, '--', lGroup)
                lGroup = []
                iStartGroupIndex = None
            store_lines_for_group(fGroupFound, oLine, lGroup)

    def _fix_violations(self, oFile):
        fix.keyword_alignment(self, oFile)


def search_for_group(fGroupFound, oLine, iStartGroupIndex, iLineNumber):
    if not fGroupFound and oLine.insideComponent:
        return True, iLineNumber
    return fGroupFound, iStartGroupIndex


def store_lines_for_group(fGroupFound, oLine, lGroup):
    if fGroupFound:
        if oLine.hasComment and not oLine.isComment:
            lGroup.append(oLine)
        else:
            lGroup.append(line.line('Removed line'))
