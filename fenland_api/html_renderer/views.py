import json
from django.views.generic import View
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from api_renderer.views import fenland_app
from api_renderer import local_settings
if local_settings.CUSTOM is True:
    from api_renderer.custom_logic import CustomDataPrep as DataPrep
else:
    from api_renderer.cam_apps import DataPrep
#from famhist_new.models import FamHistQuestionnaire
from questionnaire.models import Results


class HTMLView(View):
    def get(self, request, section=None, question_group=None, question=None):
        result = {}
        if section is None:
            return HttpResponseNotFound('Page Not Found')
        section_obj = fenland_app.get_section(section)
        if request.GET:
            id_variable_value = request.GET['id']
            result['id_variable_value'] = id_variable_value
            data = fenland_app.get_data(section, 'id', id_variable_value)
            section_obj = DataPrep(section_obj, data)
            section_obj = section_obj.data_prep()
        else:
            data = {}
            data['id'] = None
        if question_group is None:
            result['section'] = section_obj
            result['data_id'] = data['id']
            return render(request, 'html_renderer/base2.html', result)
        question_group = section_obj.get_question_group(question_group)
        if question is None:
            result['question_group'] = question_group
            return render(request, 'html_renderer/question_group.html', result)
        question = question_group.get_question(question)
        result['question'] = question
        return render(request, 'html_renderer/question.html', result)

    def post(self, request, section=None, question_group=None, question=None):
        result = {}
        if section is None:
            return HttpResponseNotFound('Page Not Found')
        section_obj = fenland_app.get_section(section)
        myDict = dict(request.POST.iterlists())
        for k in myDict.keys():
            myDict[k] = myDict[k][0]
        if 'search' in myDict.keys():
            result['search_results'] = fenland_app.search(myDict['search'], section)
            data = {}
        else:
            myDict = json.dumps(myDict)
            data = fenland_app.update_data(section, 'id_variable',
                                           request.POST['id'], myDict)
            result['data_id'] = data['id']
        section_obj = DataPrep(section_obj, data)
        section_obj = section_obj.data_prep()
        result['section'] = section_obj
        return render(request, 'html_renderer/base2.html', result)


class TestView(View):
    def get(self, request, section=None, question_group=None,
            question=None):
        result = {}
        if section is None:
            return HttpResponseNotFound('Page Not Found')
        section_obj = fenland_app.get_section(section)
        if request.GET:
            id_variable_value = request.GET['id']
            data = fenland_app.get_data(section, 'id', id_variable_value)
            section_obj = DataPrep(section_obj, data)
            section_obj = section_obj.data_prep()
        if question_group is None:
            result['section'] = section_obj
            return render(request, 'html_renderer/fenland_template.html',
                          result)
        question_group = section_obj.get_question_group(section, question_group)
        if question is None:
            result['questionGroup'] = question_group
            return render(request, 'html_renderer/question_group.html', result)
        question = question_group.get_question(question_group, question)
        result['question'] = question
        return render(request, 'html_renderer/question.html', result)


class AltTestView(View):
    def get(self, request, section=None, question_group=None,
            question=None):
        result = {}
        if section is None:
            return HttpResponseNotFound('Page Not Found')
        section_obj = fenland_app.get_section(section)
        if request.GET:
            id_variable_value = request.GET['id']
            #data = fenland_app.get_data(section, 'id', id_variable_value)
            #section_obj = DataPrep(section_obj, data)
            #section_obj = section_obj.data_prep()
            q_data = Results.objects.filter(user_id=id_variable_value).filter(questionnaire_id='FamHist')
            data={}
            for q in q_data:
                data[q.var_name] = q.var_value
        if question_group is None:
            result['section'] = section_obj
            result['data'] = data
            return render(request, 'html_renderer/alt_fenland_template.html',
                          result)
        question_group = section_obj.get_question_group(section, question_group)
        if question is None:
            result['questionGroup'] = question_group
            return render(request, 'html_renderer/question_group.html', result)
        question = question_group.get_question(question_group, question)
        result['question'] = question
        return render(request, 'html_renderer/question.html', result)
        

class TestAreaView(View):
    def post(self, request):
        myDict = dict(request.POST.iterlists())
        for k in myDict.keys():
            myDict[k] = myDict[k][0]
            print "Key: %s,\n\tValue: %s" % (k, myDict[k])
        return HttpResponse(myDict)


class AltHTMLView(View):
    def get(self, request, section=None, question_group=None, question=None):
        result = {}
        if section is None:
            return HttpResponseNotFound('Page Not Found')
        section_obj = fenland_app.get_section(section)
        if request.GET:
            id_variable_value = request.GET['id']
            result['id_variable_value'] = id_variable_value
            # data = fenland_app.get_data(section, 'id', id_variable_value)
            # section_obj = DataPrep(section_obj, data)
            # section_obj = section_obj.data_prep()
            # data = FamHistQuestionnaire.objects.get(pk=id_variable_value)
            q_data = Results.objects.filter(user_id=id_variable_value).filter(questionnaire_id=section_obj.app_object.id)
            data={}
            for q in q_data:
                data[q.var_name] = q.var_value
        else:
            data = {}
            data['id'] = None
        if question_group is None:
            result['section'] = section_obj
            # result['data_id'] = data.id
            result['data'] = data
            return render(request, 'html_renderer/alt_base2.html', result)
        question_group = section_obj.get_question_group(question_group)
        if question is None:
            result['question_group'] = question_group
            return render(request, 'html_renderer/alt_question_group.html', result)
        question = question_group.get_question(question)
        result['question'] = question
        return render(request, 'html_renderer/alt_question.html', result)

    def post(self, request, section=None, question_group=None, question=None):
        result = {}
        if section is None:
            return HttpResponseNotFound('Page Not Found')
        section_obj = fenland_app.get_section(section)
        myDict = dict(request.POST.iterlists())
        id_variable_value = request.GET['id']
        for k in myDict.keys():
            myDict[k] = myDict[k][0]
        if 'search' in myDict.keys():
            result['search_results'] = fenland_app.search(myDict['search'], section)
            data = {}
        else:
            # myDict = json.dumps(myDict)
            #data = fenland_app.update_data(section, 'id_variable',
            #                               request.POST['id'], myDict)
            q_data = Results.objects.filter(user_id=id_variable_value).filter(questionnaire_id=section_obj.app_object.id)
            for q in q_data:
                if q.var_name in myDict.keys():
                    q.var_value = myDict[q.var_name]
                    q.save()
            data={}
            for q in q_data:
                data[q.var_name] = q.var_value
            result['data'] = data
            result['section'] = section_obj
            return render(request, 'html_renderer/alt_base2.html', result)
            # result['data_id'] = data['id']
        # section_obj = DataPrep(section_obj, data)
        # section_obj = section_obj.data_prep()
        result['section'] = section_obj
        return render(request, 'html_renderer/alt_base2.html', result)
