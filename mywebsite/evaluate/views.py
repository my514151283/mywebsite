from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Example, Evaluation
from django.http import JsonResponse


def get_evaluation(user, example):
    context = dict()
    context['example_id'] = example.id
    context['post'] = example.post
    context['response'] = example.response
    context['result'] = example.result
    context['num'] = len(Example.objects.all())
    if Evaluation.objects.filter(user=user, example=example).exists():
        evaluation = Evaluation.objects.get(user=user, example=example)
        context['content'] = evaluation.content
        context['grammar'] = evaluation.grammar
        context['affect'] = evaluation.affect
    return context


@login_required
def turn_to_evaluate(request):
    """ 跳转页面 """
    user = request.user
    example = Example.objects.first()
    context = get_evaluation(user, example)
    return render(request, 'evaluate/evaluate.html', context)


def submit(request):
    """ 提交评分 """
    if request.method == 'POST':
        user = request.user
        example = Example.objects.get(id=request.POST.get('example_id'))
        content = request.POST.get('content')
        grammar = request.POST.get('grammar')
        affect = request.POST.get('affect')
        if Evaluation.objects.filter(user=user, example=example).exists():
            evaluation = Evaluation.objects.get(user=user, example=example)
            evaluation.content = content
            evaluation.grammar = grammar
            evaluation.affect = affect
        else:
            evaluation = Evaluation(user=user, example=example, content=content, grammar=grammar, affect=affect)
        evaluation.save()
        rest = len(Example.objects.all()) - len(Evaluation.objects.filter(user=user).all())
        return JsonResponse({'status': 'ok', 'msg': '提交成功！', 'rest': rest})
    return render(request, 'index/index.html')


def turn_to_last(request):
    if request.method == 'POST':
        user = request.user
        example = Example.objects.get(id=request.POST.get('example_id'))
        content = request.POST.get('content')
        grammar = request.POST.get('grammar')
        affect = request.POST.get('affect')
        if Evaluation.objects.filter(user=user, example=example).exists():
            evaluation = Evaluation.objects.get(user=user, example=example)
            evaluation.content = content
            evaluation.grammar = grammar
            evaluation.affect = affect
        else:
            evaluation = Evaluation(user=user, example=example, content=content, grammar=grammar, affect=affect)
        evaluation.save()
        example = Example.objects.last()
        context = get_evaluation(user, example)
        return render(request, 'evaluate/evaluate.html', context)


def turn_to_first(request):
    if request.method == 'POST':
        user = request.user
        example = Example.objects.get(id=request.POST.get('example_id'))
        content = request.POST.get('content')
        grammar = request.POST.get('grammar')
        affect = request.POST.get('affect')
        if Evaluation.objects.filter(user=user, example=example).exists():
            evaluation = Evaluation.objects.get(user=user, example=example)
            evaluation.content = content
            evaluation.grammar = grammar
            evaluation.affect = affect
        else:
            evaluation = Evaluation(user=user, example=example, content=content, grammar=grammar, affect=affect)
        evaluation.save()
        example = Example.objects.first()
        context = get_evaluation(user, example)
        return render(request, 'evaluate/evaluate.html', context)


def turn_to_pre(request):
    if request.method == 'POST':
        user = request.user
        example = Example.objects.get(id=request.POST.get('example_id'))
        content = request.POST.get('content')
        grammar = request.POST.get('grammar')
        affect = request.POST.get('affect')
        if Evaluation.objects.filter(user=user, example=example).exists():
            evaluation = Evaluation.objects.get(user=user, example=example)
            evaluation.content = content
            evaluation.grammar = grammar
            evaluation.affect = affect
        else:
            evaluation = Evaluation(user=user, example=example, content=content, grammar=grammar, affect=affect)
        evaluation.save()
        example = Example.objects.get(id=(int(request.POST.get('example_id')) - 1))
        context = get_evaluation(user, example)
        return render(request, 'evaluate/evaluate.html', context)


def turn_to_next(request):
    if request.method == 'POST':
        user = request.user
        example = Example.objects.get(id=request.POST.get('example_id'))
        content = request.POST.get('content')
        grammar = request.POST.get('grammar')
        affect = request.POST.get('affect')
        if Evaluation.objects.filter(user=user, example=example).exists():
            evaluation = Evaluation.objects.get(user=user, example=example)
            evaluation.content = content
            evaluation.grammar = grammar
            evaluation.affect = affect
        else:
            evaluation = Evaluation(user=user, example=example, content=content, grammar=grammar, affect=affect)
        evaluation.save()
        example = Example.objects.get(id=(int(request.POST.get('example_id')) + 1))
        context = get_evaluation(user, example)
        return render(request, 'evaluate/evaluate.html', context)
