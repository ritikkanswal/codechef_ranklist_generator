from django.shortcuts import render
from codechef.models import Student
import requests
from json import dumps
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
import json
def showformdata(request):
    if request.method =='POST':
        username = request.POST['username']
        print(username)
        url ='https://competitive-coding-api.herokuapp.com/api/codechef/'+username
        print(url)
        r=requests.get(url)
        data=r.json()
        rating=data['rating']
        highest_rating=data['highest_rating']
        global_rank=data['global_rank']
        country_rank=data['country_rank']
        
        dataJSON=Student.objects.all()
        st=StudentSerializer(dataJSON,many=True)
        for x in st.data:
            if(x['username']==username):
                return render(request, 'error.html',{'data':dumps(st.data)})
        dataJSON=Student.objects.all()
        st=StudentSerializer(dataJSON,many=True)
        ins=Student(username=username,rating=rating,highest_rating=highest_rating,global_rank=global_rank,country_rank=country_rank)
        ins.save()
        return render(request, 'index.html',{'data':dumps(st.data)})
    dataJSON=Student.objects.all()
    st=StudentSerializer(dataJSON,many=True)
    return render(request, 'index.html',{'data':dumps(st.data)})

