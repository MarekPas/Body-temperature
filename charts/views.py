from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # dodaje wymóg logowania do klas
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Chart
# from django.http import JsonResponse


def add_chart(request):
    return render(request, "charts/add_chart.html", {'title': 'Add chart'})


def view_chart(request):
    context = {
        'charts': Chart.objects.all(),
        'title': 'Charts'
    }
    return render(request, 'charts/charts.html', context)

# def create_chart(request):
#     if request.method == 'POST':
#         form = CreateChart(request.POST)
#         context = {
#             'form': form,
#             'user': form.get('username')
#         }
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('user')
#             messages.success(request, f'Chart created for {user}!')
#             return redirect('chart-detail')
#     else:
#         context = {'form': CreateChart}
#     return render(request, 'charts/chart_form.html', context)

class ChartCreateView(LoginRequiredMixin, CreateView):
    model = Chart
    fields = ['cycle','start_date','comment', 'day1']

    def form_valid(self, form):  # integrity error without it (26min Part10 Django Tutorial)
        form.instance.user = self.request.user
        return super().form_valid(form)

class ChartListView(ListView):
    model = Chart
    template_name = 'charts/charts.html'
    context_object_name = 'charts'
    ordering = ['-cycle']
    paginate_by = 12

    # def get_queryset(self):   # function to show list only for username we put in the url
    #     user = get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Chart.objects.filter(user=user).order_by('cycle')


class ChartDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Chart
    fields = '__all__'

    def test_func(self):  # checking if logged user is a user who create
        chart = self.get_object()
        if self.request.user == chart.user:
            return True
        return False

class ChartUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Chart
    fields = '__all__'


    def form_valid(self, form):  # integrity error without it (26min Part10)
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        chart = self.get_object()
        if self.request.user == chart.user:
            return True
        return False

class ChartDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Chart
    success_url = '/charts'

    def test_func(self):
        chart = self.get_object()
        if self.request.user == chart.user:
            return True
        return False

