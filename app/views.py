from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import pickle as pk
import pandas as pd
from .models import Test
from django.contrib.auth.decorators import login_required
from sklearn.preprocessing import StandardScaler
from .forms import TestForm
import datetime

@login_required()
def test(request):
    form = TestForm(instance=request.user)
    context = {'form': form}
    return render(request, 'app/test1.html', context)

def landing_view(request):
    return render(request, 'app/home.html')

def result(request):
    if request.method == 'POST':
        ans = 'High' if get_result(request) == 1 else 'Low'
        form = TestForm(request.POST)
        if form.is_valid():
            test_ = form.save(commit=False)
            test_.user = request.user
            test_.date = datetime.datetime.now()

            test_.result = ans
            test_.save()
        else:
            messages.warning(request, f'Enter the form correctly')
            return redirect('test')

        return render(request, 'app/result.html', context={'ans': ans})
    else:
        return redirect('test')

def get_result(request):
    cls = pk.load(open('app/templates/app/KNN_', 'rb'))
    column_name = ['age', 'sex', 'cp', 'trestbps', 'chol', 'restecg',
                   'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    lst = list()
    for i in column_name:
        lst.append(request.POST[i])
    # print(lst)
    dic = {column_name[i]: lst[i] for i in range(len(lst))}
    df = pd.DataFrame(dic, index=[0])
    standardScalar = StandardScaler()
    # print(df)
    columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    df[columns_to_scale] = standardScalar.fit_transform(df[columns_to_scale])
    ans = cls.predict(df)
    return ans[0]

@login_required()
def history(request):
    hist = Test.objects.filter(user=request.user)
    if hist.exists():
        context = {'history': hist}
        return render(request, 'app/history.html', context)
    else:
        messages.warning(request, 'History is empty! Take a test now')
        return redirect('test')
