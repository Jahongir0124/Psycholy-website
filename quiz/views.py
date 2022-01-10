from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from questions.models import Question,Answer
from results.models import Result
class QuizListView(ListView):
    model = Quiz
    template_name = 'main.html'

def quiz_view(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request,'quiz.html',{'obj':quiz})
def quiz_data_view(request,pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q):answers})
    return JsonResponse(
        {
            'data':questions,
            'time':quiz.time,
        }
    )

def save_quiz_view(request,pk):

    if request.is_ajax():
        questions = []
        data = request.POST
        data1 = dict(data.lists())
        data1.pop('csrfmiddlewaretoken')
        for k in data1.keys():
            question = Question.objects.get(text=k)
            questions.append(question)
        user = request.user
        user_data = user.first_name+" "+user.last_name
        quiz = Quiz.objects.get(pk=pk)
        score = 0
        multiplier = 100/quiz.number_of_questions
        results = []
        correct_answer = None
        for que in questions:
            a_selected = request.POST.get(que.text)
            if a_selected != "":
                question_answers = Answer.objects.filter(question=que)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score+=1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text
                results.append({str(que):{'correct_answer':correct_answer,'answered':a_selected}})
            else:
                results.append({str(que):'not answered'})
        score_ = score*multiplier
        Result.objects.create(quiz=quiz,user=user,score=score_)
        if score_>quiz.required_score_to_pass:
            return JsonResponse({'passed':True,'natija':score_,'results':results,'pol':user_data})
        else:
            return JsonResponse({'passed':False,'natija':score_,'results':results,'pol':user_data})

