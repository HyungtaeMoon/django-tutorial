from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import loader

from .models import Question


def index(request):
    # DB에 있는 Question중, 가장 최근에 발행(pub_date)된 순서대로 최대 5개에 해당하는 Queryset을
    # latest_question_list변수에 할당
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    # # Django의 TEMPLATES설정에 정의된 방법으로
    # # 주어진 인자('polls/index.html')에 해당하는 템플릿 파일을 가지는 Template인스턴스를 생성
    # template = loader.get_template('polls/index.html')
    #
    # # Template인스턴스의 render()함수를 실행, 인수로 context와 request를 전달
    # # 결과로 렌더링 된 HTML문자열이 리턴됨
    # html = template.render(context, request)
    #
    # # 결과 HTML문자열을 사용해 생성한 HttpResponse객체를 리턴
    # return HttpResponse(html)

    return render(request, 'polls/index.html', context)

def custom_get_object_or_404(model, **kwargs):
    def custom_get_object_or_404(model, **kwargs):
        print(kwargs)
        try:
            return model.objects.get(**kwargs)
        except model.DoesNotExist:
            raise Http404()

    # 1번째 인자로 특정 Model Class를 받음
    # 최소 1개 이상의 키워드인자를 받아서, 받은 인자들을 사용해서 주어진 Model Class의 get()메서드를 실행
    # 존재하면 해당 인스턴스를 리턴
    # 없으면 raise Http404를 실행 (메시지는 임의로 지정)


def detail(request, question_id):
    # try-except 구문 없이
    # polls/detail.html에 해당하는 Question 인스턴스를 전달해서
    # HTML에서는 해당 Question의 question_text를 출력
    # question = Question.objects.get(id=question_id)
    # context = {
    #     'question':question,
    # }
    # return render(request, 'polls/detail.html', context)
    #

    try:
        question = Question.objects.get(id=question_id, pub_date__isnull=False)
    except Question.DoesNotExist:
        raise Http404('Question does not exist')


    # question = custom_get_object_or_404(Question, id=question_id, pub_date__is_null=False)
    custom_get_object_or_404(Question, id=1, pub_date_isnull=True)

    context = {
        'question': question,
    }

    return render(request, 'polls/detail.html', context)

    # 과제하기
    # return HttpResponse("You're looking at question %s."% question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s."% question_id)