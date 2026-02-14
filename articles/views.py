from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Articles
from .models import News


def contacts(request):
    return render(request, 'contacts.html')


class ArticleListView(ListView):
 model = Articles
 template_name = 'index.html'



class ArticleDetailView(DetailView):
  model = Articles
  template_name = 'detail.html' 

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['news_list'] = News.objects.all()[:5]#получаем все данные из таблицы
    return context