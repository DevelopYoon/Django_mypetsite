from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

def post_list(request):
    return render(request, 'post_list.html', {}) 
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
