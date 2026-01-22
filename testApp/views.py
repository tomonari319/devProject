from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import ReviewForm


def review_list(request):
    """
    レビュー一覧表示 ＋ 新規投稿
    """
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()

    reviews = Review.objects.all().order_by('-id')

    return render(request, 'review_list.html', {
        'reviews': reviews,
        'form': form,
    })


def review_delete(request, pk):
    """
    レビュー削除
    """
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('review_list')


def review_edit(request, pk):
    """
    レビュー編集
    """
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm(instance=review)

    return render(request, 'review_edit.html', {
        'form': form,
        'review': review,
    })
