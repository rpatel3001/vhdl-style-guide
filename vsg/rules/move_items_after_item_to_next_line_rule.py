
import copy

from vsg import rule
from vsg import parser
from vsg import utils


class move_items_after_item_to_next_line_rule(rule.rule):
    '''
    Splits the line at items and moves items after it to the next line.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    sObjectType : string
       The object to check the space after.

    Attributes
    ----------

    self.phase : integer = 2
       Sets the phase the rule will run in.

    self.solution : string = None
       Instructions on how to fix the violation.
    '''

    def __init__(self, name, identifier, trigger):
        rule.rule.__init__(self, name=name, identifier=identifier)
        self.phase = 1
        self.subphase = 1
        self.solution = None
        self.trigger = trigger

    def analyze(self, oFile):
        lContexts = oFile.get_context_declarations()
        for dContext in lContexts:
            bFound = False
            bBreak = False
            for iLine, oLine in enumerate(dContext['lines']):
                lObjects = oLine.get_objects()
                for iObject, oObject in enumerate(lObjects):
                    if bFound == True:
                        if not isinstance(oObject, parser.whitespace) and not isinstance(oObject, parser.comment):
                            dViolation = utils.create_violation_dict(dContext['metadata']['iStartLineNumber'] + iLine)
                            self.add_violation(dViolation)
                            bBreak = True
                            break
                    if isinstance(oObject, self.trigger):
                        bFound = True
                if bBreak:
                    break
                if bFound:
                    break


    def _fix_violations(self, oFile):
        for dViolation in self.violations[::-1]:
            oLine = utils.get_violating_line(oFile, dViolation)
            oNewLine = copy.deepcopy(oLine)
            lObjects = oLine.get_objects()
            iLineNumber = utils.get_violation_line_number(dViolation)
            for iObject, oObject in enumerate(lObjects):
                if isinstance(oObject, self.trigger):
                    lOldObjects = lObjects[:iObject + 1]
                    lNewObjects = lObjects[iObject + 1:]
                    oLine.update_objects(lOldObjects)
                    oNewLine.update_objects(lNewObjects)
                    oFile.insert_line(iLineNumber + 1, oNewLine)
                    break
