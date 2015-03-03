from lxml import objectify


def get_question_group(section, question_group):
    for qg in section.questionGroup:
        if qg.attrib['position'] == question_group:
            return qg

def get_question(question_group, question):
    for q in question_group.question:
        if q.attrib['position'] == question:
            return q

def data_prep(section, data):
    print data
    for qg in section.questionGroup:
        for q in qg.question:
            var_value = objectify.Element('{http://www.mrc-epid.cam.ac.uk/schema/common/epi}var_value')
            if q.variable.varName == 'surgery':
                var_value.value = data['surgery_id']
            elif q.variable.varName == "diabetes":
                var_value.value = data['diabetes_diagnosed']
            else:
                var_value.value = data[q.variable.varName]
            q.variable.append(var_value)
    return section
