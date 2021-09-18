from youtube_dl import YoutubeDL
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import View, TemplateView


class MainPageView(TemplateView):
    template_name = 'home.html'


class DownloadView(View):
    def post(self, request):
        if request.method == 'POST':
            video_url = request.POST['url'] 
            if video_url:
                download_option = {
                    'outtmp1': '',
                }
                with YoutubeDL(download_option) as ydl:
                    ydl.download([video_url])
                messages.success(request, 'Ваше видео скачалось!')
                return redirect('home')
            else:
                messages.warning(request, 'Введите url вашего видео!')
                return redirect('home')
        return redirect('home')













