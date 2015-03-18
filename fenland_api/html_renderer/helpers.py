
def get_question_group(section, question_group):
    for qg in section.question_groups:
        if qg.position == question_group:
            return qg


def get_question(question_group, question):
    for q in question_group.question_group_objects:
        if q.position == question:
            return q
