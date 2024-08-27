from django.shortcuts import render

from .forms import FeedbackForm


def feedback_form(request):
    #print(request.user.is_superuser)
    if request.user.is_superuser:
        if request.method == 'POST':
            form = FeedbackForm(request.POST)

            if form.is_valid():
                form.save()
                return render(request, 'form/thanks.html')
        else:
            form = FeedbackForm()
    else:
        return render(request, 'form/not_admin.html')
    return render(request,'form/feedback_form.html', {'form': form})
