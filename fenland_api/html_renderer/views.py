from django.views.generic import View
from api_renderer.views import fenland_app
from django.shortcuts import render
from helpers import get_question_group, get_question


class HTMLView(View):
    def get(self, request, section=None, question_group=None,
            question=None):
        # test using this data in a template
        section = fenland_app.get_section(section)
        if question_group is None:
            result = {'section': section}
            return render(request, 'html_renderer/base.html', result)
        question_group = get_question_group(section, question_group)
        if question is None:
            result = {'questionGroup': question_group}
            return render(request, 'html_renderer/question_group.html', result)
        question = get_question(question_group, question)
        result = {'question': question}
        return render(request, 'html_renderer/question.html', result)
