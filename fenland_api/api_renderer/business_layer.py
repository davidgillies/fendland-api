from lxml import objectify


def data_prep(section, data):
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
