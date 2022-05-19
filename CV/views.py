from django.shortcuts import render
from .models import Legends, WorkExperience, Education, Skills, Works
from django.http import HttpResponse

def CVshow(request, name):
    print(name)
    try:
        all_details = Legends.objects.get(L_codeName=name)
    except:
        return HttpResponse(status=404)

    all_Education = Education.objects.filter(L_id=all_details.L_id)
    all_WorkExperience = WorkExperience.objects.filter(L_id=all_details.L_id)
    all_Skills = Skills.objects.filter(L_id=all_details.L_id)
    all_Works = Works.objects.filter(L_id=all_details.L_id)

    context = {
        'title': name,
        'legend': all_details,
        'E': all_Education,
        'WE': all_WorkExperience,
        'S': all_Skills,
        'W': all_Works
    }

    return render(request, 'CV/CV.html', context=context)
