from vsg import parser


class procedure_keyword(parser.keyword):
    '''
    unique_id = interface_procedure_specification : procedure_keyword
    '''

    def __init__(self, sString):
        super().__init__(sString)


class parameter_keyword(parser.identifier):
    '''
    unique_id = interface_procedure_specification : parameter_keyword
    '''

    def __init__(self, sString):
        super().__init__(sString)


class designator(parser.designator):
    '''
    unique_id = interface_procedure_specification : designator
    '''

    def __init__(self, sString):
        super().__init__(sString)


class open_parenthesis(parser.open_parenthesis):
    '''
    unique_id = interface_procedure_specification : open_parenthesis
    '''

    def __init__(self, sString='('):
        super().__init__()


class close_parenthesis(parser.close_parenthesis):
    '''
    unique_id = interface_procedure_specification : close_parenthesis
    '''

    def __init__(self, sString=')'):
        super().__init__()
