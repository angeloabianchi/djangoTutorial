from django.urls import path

from . import views

app_name = 'polls'                                                      # 3.8

urlpatterns = [
    # path('', views.index, name='index'),                              # /polls/  -  updated on 4.2, item 1
    path('', views.IndexView.as_view(), name='index'),                  # 4.2, item 1
    # path('<int:question_id>/', views.detail, name='detail'),          # /polls/5/             adicionado em 3.1       updated at 3.7 as you can see below
    # path('specifics/<int:question_id>/', views.detail, name='detail'),# polls/specifics/1/    3.7  -  updated on 4.2, item 1
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),       # 4.2, item 1
    # path('<int:question_id>/results', views.results, name='results'), # /polls/5/results/     add em 3.1  -  updated on 4.2, item 1
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),     # 4.2, item 1
    path('<int:question_id>/vote/', views.vote, name='vote'),            # /polls/5/vote/        add em 3.1
]