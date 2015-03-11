from cam_apps import Question


def data_prep(section, data):
    for qg in section.section_objects:
        question_list = [q for q in qg.question_group_objects if isinstance(q, Question)]
        for q in question_list:
            if q.variable == 'surgery':
                q.var_value = data['surgery_id']
            elif q.variable == "diabetes":
                q.var_value = data['diabetes_diagnosed']
            else:
                q.var_value = data[q.variable]
    return section
