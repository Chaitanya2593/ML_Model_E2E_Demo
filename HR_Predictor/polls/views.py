from django.shortcuts import render, get_object_or_404
from polls.models import dl_model
from .form import FillForm, RawFillForm, modelFillForm
from polls.predictor import  Predictor
from django.conf import settings
import os
import shutil
import pandas as pd
import json
root_path = settings.UPLOAD_ROOT + r'\\'

def index(request):
    latest_dl_models = dl_model.objects.all()
    context = {"latest_dl_models": latest_dl_models}
    return render(request, 'polls/index.html', context)

def form(request):

    output_html = ""
    output_html_ns = ""
    form = modelFillForm(request.POST or None, request.FILES or None)
#     form_2 = RawFillForm(request.POST or None)
    if form.is_valid():
        initial_obj = form.save(commit=False)
        initial_obj.save()

        file_path = root_path + request.FILES['file_upload'].name
        
        output_html, output_html_ns = define_model(file_path)
#         form_2 = modelFillForm()

        context = {'outputfile': output_html, 'outputfile_ns': output_html_ns, 
                   'Input_filename':request.FILES['file_upload'].name,
                   }
        clear_files(file_path)
        
        return render(request, 'polls/output.html', context)
    else:
        print("Form is going to invalid " + str(form.is_valid()))
#         form = RawFillForm()
        form_2 = modelFillForm()

    context = {'form': form, }
    return render(request, 'polls/form.html', context)

def define_model(file_path):
    print(file_path)
    predictor = Predictor()
    # return predictor.invokeBatchExecutionService(file_path)
    return predictor.predict_function(file_path)

def remov_decimal(attribute):
    attribute= str(attribute).replace("Decimal", '')
    attribute= attribute.replace("(", '')
    return attribute.replace(")", '')

def clear_files(file_path):


    # file_path = os.path.join(root_path, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
        print(file_path)
    except Exception as e:
        print(e)
