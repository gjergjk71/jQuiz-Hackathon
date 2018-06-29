from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.contrib.auth.hashers import make_password
from .models import *
from django.contrib.auth.decorators import login_required

def redirectToHome(request):
	return redirect("/home")

def home(request):
	quizzes = Quiz.objects.all()
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		user = authenticate(username=username,password=password)
		if user is not None:
			return login(request)
		else:
			context = {"invalid":True,"registered":False,"quizzes":quizzes}
			return render(request,"home.html",context)
	elif request.method == "GET":
		context = {"invalid":False,"registered":False,"quizzes":quizzes}
		return render(request,"home.html",context)

def signup(request):
    if request.method == 'POST':
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password')
        User.objects.create_user(username=username,password=raw_password)
        context = {"registered":True}
        return render(request,'home.html',context)
    else:
    	return redirect("/home")
    context = {"registered":False}
    return render(request, 'home.html',context)

@login_required
def quiz(request,ID):
	quiz = Quiz.objects.get(pk=ID)
	questions = Question.objects.filter(quiz=quiz)
	questions_answers = {}
	for question in questions:
		answers = Answer.objects.filter(question=question)
		questions_answers[question] = answers
	context = {"quiz":quiz,"questions_answers":questions_answers}
	return render(request,"kuiz.html",context)
@login_required
def result(request,ID):
	if request.method == "POST":
		quiz = Quiz.objects.get(pk=ID)
		questions = Question.objects.filter(quiz=quiz)
		answers = request.POST.getlist("answerList[]")
		correct_answers = 0 
		questions_answers = {}
		for question in questions:
			answers_list = []
			for answer in Answer.objects.filter(question=question):
				answers_list.append(answer.correct)
				
			questions_answers[question] = answers_list

		for answer in answers:
			try:
				if Answer.objects.get(pk=int(answer)).correct == "1":
					correct_answers +=1
			except:
				pass
		"""
			for question in questions:
			for answer in answers:
				try:
					if Answer.objects.get(pk=int(answer)).correct == "1":
						correct_answers +=1
				except:
					pass
					"""
		context = {"quiz":quiz,"answers":len(answers),"correct_answers":correct_answers,
						"questions_answers":questions_answers}
		return render(request,"result.html",context)
	else:
		return redirect("/quiz/{}".format(ID))