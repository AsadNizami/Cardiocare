from django.shortcuts import render
from django.http import HttpResponse
import pickle as pk
import pandas as pd
from django.contrib.auth.decorators import login_required
from sklearn.preprocessing import StandardScaler

@login_required()
def test(request):
    return render(request, 'test.html')

def landing_view(request):
    return render(request, 'home.html')

def result(request):
    cls = pk.load(open('templates/KNN_', 'rb'))
    column_name = ['age', 'sex', 'cp', 'trestbps', 'chol', 'restecg',
                   'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    lst = list()
    for i in column_name:
        lst.append(request.GET[i])

    # print(lst)
    dic = {column_name[i]: lst[i] for i in range(len(lst))}
    df = pd.DataFrame(dic, index=[0])
    standardScalar = StandardScaler()
    # print(df)
    columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    df[columns_to_scale] = standardScalar.fit_transform(df[columns_to_scale])
    ans = cls.predict(df)
    # print(ans)
    return render(request, 'result.html', context={'ans': ans[0]})
