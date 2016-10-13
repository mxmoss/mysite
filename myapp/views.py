from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import myRecord
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def index(request):
  return HttpResponse("Hello, world. You're at the myapp index.")
	
def post_list(request):
  if not request.user.is_authenticated():
    return render(request, 'registration/login.html')
  else:
    records = myRecord.objects.filter().order_by('add_dt')
#    records = myRecord.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myapp/post_list.html', {'records': records})

def post_detail(request, pk):
  if not request.user.is_authenticated():
    return render(request, 'registration/login.html')
  else:
    record = get_object_or_404(myRecord, pk=pk)
    return render(request, 'myapp/post_detail.html', {'record': record})
		
def post_new(request):
  if not request.user.is_authenticated():
    return render(request, 'registration/login.html')
  else:
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.added_by = request.user
            post.edited_by = request.user
            post.edit_dt = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'myapp/post_edit.html', {'form': form})
		
def post_edit(request, pk):
  if not request.user.is_authenticated():
    return render(request, 'registration/login.html')
  else:
    record = get_object_or_404(myRecord, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=record)
        if form.is_valid():
            post = form.save(commit=False)
            #post.edited_by = request.user
            post.edit_dt = timezone.now()
            record.save()
            return redirect('post_detail', pk=record.pk)
    else:
        form = PostForm(instance=record)
    return render(request, 'myapp/post_edit.html', {'form': form})