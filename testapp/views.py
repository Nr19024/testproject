from django.shortcuts import render
# django.views.genericからTemplateViewをインポート
from django.views.generic import TemplateView,ListView
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import TestPostForm
from .forms import ContactForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import TestPost
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.core.mail import EmailMessage
from django.contrib import messages
from django.views.generic import FormView
class ContactView(FormView):
     template_name='contact.html'
     form_class=ContactForm
     success_url=reverse_lazy('testapp:contact')
     def form_valid(self,form):
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']
        subject='お問い合わせ:{}'.format(title)
        message=('送信者名:{0}\nメールアドレス:{1}\n タイトル:{2}\n メッセージ:\n{3}').format(name,email,title,message)
        from_email=['kmm2559345@stu.o-hara.ac.jp']
        to_list=['kmm2559345@stu.o-hara.ac.jp']
        message=EmailMessage(subject=subject,
                             body=message,
                             from_email=from_email,
                             to=to_list,)
        message.send()
        messages.success(
            self.request,'お問い合わせは正常に送信されました。')
        return super().form_valid(form)

class IndexView(ListView):
    template_name='index.html'
    queryset=TestPost.objects.order_by('-posted_at')
    paginate_by=9

@method_decorator(login_required,name='dispatch')
class CreateTestView(CreateView):
    form_class=TestPostForm
    template_name='post_test.html'
    success_url=reverse_lazy('testapp:post_done')
    def form_valid(self, form):
        postdata=form.save(commit=False)
        postdata.user=self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name='post_success.html'

class CategoryView(ListView):
    template_name='index.html'
    paginate_by=9
    def get_queryset(self):
        category_id=self.kwargs['category']
        categories=TestPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories

class UserView(ListView):
    template_name='index.html'
    paginate_by=9
    def get_queryset(self):
        user_id=self.kwargs['user']
        user_list=TestPost.objects.filter(
            user=user_id).order_by('-posted_at')
        return user_list

class DetailView(DetailView):
    template_name='detail.html'
    model=TestPost

class MypageView(ListView):
    template_name='mypage.html'
    paginate_by=9
    def get_queryset(self):
        queryset=TestPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset

class TestDeleteView(DeleteView):
    model=TestPost
    template_name='test_delete.html'
    success_url=reverse_lazy('testapp:mypage')
    def delete(self,request,*args,**kwargs):
        return super().delete(request,*args,**kwargs)