
def get_question_group(section, question_group):
    for qg in section.questionGroup:
        if qg.attrib['position'] == question_group:
            return qg


def get_question(question_group, question):
    for q in question_group.question:
        if q.attrib['position'] == question:
            return q
