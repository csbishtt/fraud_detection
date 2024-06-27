from django.shortcuts import render
import pickle
import os

# pip show scikit-learn joblib
# python manage.py runserver

# Load the model
with open('static\classifier111.pkl','rb') as file:
    clf=pickle.load(file)


def index(request):
    return render(request,'index.html')

def features(request):
    return render(request,'features.html')

def about(request):
    return render(request,'about.html')

def prediction(request):
    if request.method=="POST":
        v1 = float(request.POST.get("v1"))
        v2 = float(request.POST.get("v2"))
        v3 = float(request.POST.get("v3"))
        v4 = float(request.POST.get("v4"))
        v5 = float(request.POST.get("v5"))
        v6 = float(request.POST.get("v6"))
        v7 = float(request.POST.get("v7"))
        v8 = float(request.POST.get("v8"))
        v9 = float(request.POST.get("v9"))
        v10 = float(request.POST.get("v10"))
        v11 = float(request.POST.get("v11"))
        v12 = float(request.POST.get("v12"))
        v13 = float(request.POST.get("v13"))
        v14 = float(request.POST.get("v14"))
        v15 = float(request.POST.get("v15"))
        v16 = float(request.POST.get("v16"))
        v17 = float(request.POST.get("v17"))
        v18 = float(request.POST.get("v18"))
        v19 = float(request.POST.get("v19"))
        v20 = float(request.POST.get("v20"))
        v21 = float(request.POST.get("v21"))
        v22 = float(request.POST.get("v22"))
        v23 = float(request.POST.get("v23"))
        v24 = float(request.POST.get("v24"))
        v25 = float(request.POST.get("v25"))
        v26 = float(request.POST.get("v26"))
        v27 = float(request.POST.get("v27"))
        v28 = float(request.POST.get("v28"))

        pred=clf.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,1]])
    
        if pred==0:
            send="No Fraud Detection"
        else:
            send="Fraud Detection"

        output={
            "output":send
        }

        return render(request,'prediction.html',output)
    else:
        return render(request,'prediction.html')

