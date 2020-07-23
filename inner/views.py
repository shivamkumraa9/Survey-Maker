from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from django.contrib import messages
from .models import User_survey,Question,Answer

def home(request):
    return render(request,"inner/home.html",{'surveys':User_survey.objects.all()[:20]})

@login_required()
def create_survey(request):
    if request.method =='POST':
        data=dict(request.POST)
        if request.user.is_authenticated:
            s=User_survey(auther=request.user,heading=data['heading'][0])
            s.save()
            for i in range(len(data['question1'])):
                q=Question(part=s,text=data['question1'][i])
                q.save()
                Answer(question=q,text=data['option1'][i]).save()
                Answer(question=q,text=data['option2'][i]).save()
                if data['option3'][i] !='':
                    Answer(question=q,text=data['option3'][i]).save()
                if data['option4'][i] !='':
                    Answer(question=q,text=data['option4'][i]).save()
            messages.success(request,"New Survey Created !!!")
            return redirect("/")
    return render(request,"inner/create_survey.html")

@login_required()
def profile(request):
    surveys=request.user.user_survey_set.all()
    return render(request,'inner/profile.html',{'surveys':surveys})


@login_required()
def survey_detail(request,pk):
    survey=get_object_or_404(User_survey,pk=pk)
    if survey.auther==request.user:
        return render(request,'inner/detail_survey.html',{'survey':survey})
    return HttpResponseNotFound()

@login_required()
def delete_survey(request,pk):
    survey=get_object_or_404(User_survey,pk=pk)
    if survey.auther==request.user:
        survey.delete()
        messages.success(request,"Survey Deleted")
        return redirect("inner:profile")
    return HttpResponseNotFound()

@login_required()
def fill_survey(request,pk):
    survey=get_object_or_404(User_survey,pk=pk)
    if survey.auther==request.user :
        messages.info(request,"Auther cannot fill the Survey")
        return redirect("inner:detail_survey",pk = survey.pk)
    if request.user in survey.fillers.users_filled.all():
        messages.info(request,"You Already Filled that survey")
        return redirect("/")
    if request.method == "POST":
        for i in survey.question_set.all():
            for j in i.answer_set.all():
                if j.text==request.POST[i.text]:
                    j.votes+=1
                    j.save()
        survey.total_filled+=1
        survey.fillers.users_filled.add(request.user)
        survey.save()
        messages.success(request,"Your Survey has Submitted")
        return redirect("/")
    else:
        return render(request,'inner/fill_survey.html',{'survey':survey})
