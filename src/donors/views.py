from django.shortcuts import render
from django.views.generic import ListView
from .models import DonorList
# from .forms import DonorCreateForm
# Create your views here.

class DonorListView(ListView):
	template_name = "index.html"
	queryset = DonorList.objects.all()
	def get_context_data(self,*args,**kwargs):
		context = super(DonorListView, self).get_context_data(*args,**kwargs)
		# context["another_list"]  = Article.objects.all()
		# context["speciality_list"]  = Speciality.objects.all()
		# context['create_form'] = QuestionModelForm()
		# context['create_url'] = reverse_lazy("question:create")
		return context



# class DonorCreateView(CreateView):
#     form_class = DonorCreateForm
#     template_name = 'index.html'
#     success_url = '/'
#     # success_message = "Your account was created successfully. Please check your email."

#     def dispatch(self, *args, **kwargs):
#         # if self.request.user.is_authenticated():
#         #     return redirect("/logout")
#         return super(DonorCreateView, self).dispatch(*args, **kwargs)