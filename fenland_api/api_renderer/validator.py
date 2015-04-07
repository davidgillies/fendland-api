class Validator(object):
    def __init__(self, rules, data):
        self.rules = rules
        self.data = data
        self.local_settings_mapping = {}
        self.errors = {}

    def is_valid(self):
        valid = True
        for data_item in self.data.keys():
            if data_item != 'id' and data_item in self.rules.keys():
                self.errors[data_item] = ''
                if 'CheckMaxLength' in self.rules[data_item].keys():
                    if int(self.rules[data_item]['CheckMaxLength']) < len(self.data[data_item]):
                        valid = False
                        self.errors[data_item] = 'Your answer should be less than %s characters long' % self.rules[data_item]['CheckMaxLength']
                if 'IsAnswered' in self.rules[data_item].keys():
                    if not self.data[data_item]:
                        valid = False
                        self.errors[data_item] = 'Please give an answer'
        return valid
        