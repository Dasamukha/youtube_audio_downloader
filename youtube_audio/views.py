from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube 
# Create your views here.

def home(request):
    return render(request, 'youtube_audio/index.html')

def audio(request):

    return render(request,'youtube_audio/audio.html')


def Adownload(request):
    link = str(request.GET.get('Ytlink'))    
    yt = YouTube(link)

    audio = yt.streams.filter(only_audio=True)
    ys = yt.streams.get_by_itag('251')
    ys.download()
    return render(request, 'youtube_audio/Adownload.html')

