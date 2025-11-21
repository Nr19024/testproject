from django.urls import path
from . import views


# URLパターンを逆引きできるように名前を付ける
app_name = 'testapp'

# URLパターンを登録する変数
urlpatterns = [
    # photoアプリへのアクセスはviewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),
    path('post/',views.CreateTestView.as_view(),name='post'),
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),
    path('tests/<int:category>',
         views.CategoryView.as_view(),
         name='tests_cat'),
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name='user_list'
         ),
    path('test-detail/<int:pk>',
         views.DetailView.as_view(),
         name='test_detail'
         ),
    path('mypage/',views.MypageView.as_view(),name='mypage'),
    path('testapp/<int:pk>/delete/',
          views.TestDeleteView.as_view(),
          name='test_delete'
          ),
     path('contact/',
          views.ContactView.as_view(),
          name='contact'),
]
