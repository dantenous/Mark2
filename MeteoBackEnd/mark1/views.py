from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User, auth
from .models import Domacnost
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .serial import Serial

# Create your views here.


def uvod(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("index")
        else:
            return redirect('/')

    else:
        return render(request, 'uvod.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def index(request):
    if not request.user.is_authenticated:
        return redirect('/')
    vsechno = Domacnost.objects.last()
    last_ten = Domacnost.objects.all().order_by('-id')[:10]
    posle10 = reversed(last_ten)

    temp = []
    for tl in last_ten:
        temp.append(int(str(tl.tlak[0:2])))
    print(temp)

    mereni = []
    for i in posle10:
        mereni.append([str(i.cas), str(i.teplota), str(i.tlak), str(i.vlhkost), str(i.teplotav), str(i.teplotazdanliva), str(
            i.rosnybod), str(i.vlhostv), str(i.densrazky), str(i.tlakv), str(i.smervetru), str(i.rychlostvetru), str(i.narazovyvitr), str(i.co2)])
    # print(mereni)

    return render(request, 'index.html', {'vsechno': vsechno, 'mereni': mereni, 'temp': temp})


class SerialView(ListAPIView):
    queryset = Domacnost.objects.all().order_by('-id')[:20]
    serializer_class = Serial


class ChartData(APIView):  # Trida View REST API

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):  # Nacte data z DB
        last_ten = Domacnost.objects.all().order_by('-id')[:20]
        posle10 = reversed(last_ten)
        datum = []
        temp = []
        temp_venku = []
        tlak = []
        vetr = []
        narazovyvitr = []
        co2 = []
        for tl in posle10:
            temp.append(tl.teplota)  # Vlozi data do seznamu
            temp_venku.append(tl.teplotav)  # Vlozi data do seznamu
            datum.append(str(tl.cas)[11:19])
            tlak.append(tl.tlak)
            vetr.append(tl.rychlostvetru)
            narazovyvitr.append(tl.narazovyvitr)
            co2.append(tl.co2)
        data = {
            "labels": datum,  # pripravene data pro vraceni jako odpoved do Ajaxu
            "teplotadoma": temp,
            "teplotavenku": temp_venku,
            "tlak": tlak,
            "vetr": vetr,
            "narazovyvitr": narazovyvitr,
            "co2": co2
        }
        return Response(data)
