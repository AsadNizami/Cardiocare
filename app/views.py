from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import pickle as pk
import pandas as pd
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Test
from django.contrib.auth.decorators import login_required
from sklearn.preprocessing import StandardScaler
from .forms import TestForm
from .utility import join_mail, test_report
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
    test_report(request)
    cls = pk.load(open('app/templates/app/KNN_', 'rb'))
    Scalar = pk.load(open('app/templates/app/Scalar_', 'rb'))
    column_name = ['age', 'sex', 'cp', 'trestbps', 'chol', 'restecg',
                   'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    lst = list()
    for i in column_name:
        lst.append(request.POST[i])
    # print(lst)
    dic = {column_name[i]: lst[i] for i in range(len(lst))}
    # test_df = {
    #     'age': 57, 'sex': 1, 'cp': 1,
    #     'trestbps': 130, 'chol': 236, 'restecg': 0,
    #     'thalach': 174, 'exang': 0, 'oldpeak': 0,
    #     'slope': 1, 'ca': 1, 'thal': 2
    # }
    df = pd.DataFrame(dic, index=[0])

    columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    df[columns_to_scale] = Scalar.transform(df[columns_to_scale])
    print(df)
    ans = cls.predict(df)

    print(ans)
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

def render_pdf_view(request, pk):
    # date1 = datetime.datetime(date)
    # print(pk)
    hist = get_readable_data(Test.objects.get(pk=pk))
    patient = request.user

    template_path = 'app/user_printer.html'
    context = {'myvar': 'this is your template context', 'hist': hist, 'patient': patient}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'  # attachment; to download
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def get_readable_data(obj_raw):
    thal_dic = {0: 'Normal', 1: 'Fixed Defect', 2: 'Revesable Defect'}
    cp_dic = {0: 'None', 1: 'Low', 2: 'Medium', 3: 'High'}
    obj_raw.sex = 'Male' if obj_raw.sex == 1 else "Female"
    obj_raw.exang = 'Yes' if obj_raw.exang != 0 else 'No'
    obj_raw.thal = thal_dic[obj_raw.thal]
    obj_raw.result = 'High' if obj_raw.result == 'High' else 'Low'
    obj_raw.cp = cp_dic[obj_raw.cp]
    obj_raw.restecg = 'Normal' if obj_raw.restecg == 0 else 'Abnormal'

    return obj_raw
