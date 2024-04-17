import logging
import JsonResponse

class save_professionalData(View):
    def post(self, request):
        professionid = request.POST.get('professionid', '')
        form = EmpProfessionalCreateForm(request.POST or None, instance=None if professionid == '' else EmpProfessional.objects.get(id=professionid))
        loggedInUserCompany = request.user.profile.company
        
        if form.is_valid():
            professional = form.save(commit=False)
            professional.user = request.user
            professional.company = loggedInUserCompany
            
            professional.save()

            return JsonResponse({'status': 'save'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Form data is invalid'}) 