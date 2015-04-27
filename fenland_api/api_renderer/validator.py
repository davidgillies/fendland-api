

class Validator(object):
    def __init__(self, questions, data):
        self.data = data
        self.questions = questions
        self.errors = {}

    def is_valid(self):
        valid = True
        for k in self.data:
            if k != 'id':
                for test in self.questions[k].tests:
                    result, error = self.do_test(test)(self.questions[k], self.data[k])
                    if result is False:
                        self.errors[k] = error
                        valid = False
        return valid

    def do_test(self, test):
        return {'CheckMaxLength': self.maxlength, 'IsAnswered': self.required,
                'type': self.test_type}[test]

    def get_type_test(self, the_type):
        return {'string': str, 'date': str, 'datetime': str}[the_type]

    def maxlength(self, question, answer):
        if len(answer) > int(question.maxlength):
            return (False, 'Your answer should be less than %s characters long' % question.maxlength)
        else:
            return (True, None)

    def required(self, question, answer):
        if question.required and not answer:
            return (False, 'Please give an answer')
        else:
            return (True, None)

    def test_type(self, question, answer):
        return (True, None)
