from django.shortcuts import render, redirect
from books.models import Book_Model, Purchase_Model
from django.views.generic import DetailView
from . forms import Comment_Form
from transactions.models import AccountBalance


# Create your views here.


class All_details(DetailView):
    model = Book_Model
    template_name = 'books/details_view.html'
    pk_url_kwarg = 'id'
    
    def post(self, request, *args, **kwargs):
        comment_form = Comment_Form(data= self.request.POST)
        data = self.get_object()
        if comment_form.is_valid():
            comment = comment_form.save(commit= False)
            comment.book = data
            comment.save()
 
        return self.get(request, *args, **kwargs)
        
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.get_object()
        context['data'] = data
        context['comments'] = data.comments.all()
        context['comment_form'] = Comment_Form()
        return context
    
    