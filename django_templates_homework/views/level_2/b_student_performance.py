"""
Оживите шаблон.

Исходите из предположения, что в курсе не может быть больше 3-х недель.
"""
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.defaulttags import register

@register.filter
def get_week_by_index(dictionary, index):
    return dictionary.get(f"week{index}_completed")

def students_performance_view(request: HttpRequest) -> HttpResponse:
    performances = [
        {"student_name": "Reed Boles", "week1_completed": False, "week2_completed": False, "week3_completed": False},
        {"student_name": "David Mitchell", "week1_completed": True, "week2_completed": True, "week3_completed": True},
        {"student_name": "Teresa Monger", "week1_completed": False, "week2_completed": False, "week3_completed": True},
        {"student_name": "Doris Dayton", "week1_completed": True, "week2_completed": False, "week3_completed": False},
    ]
    return render(request, 'level_2/students_performance.html', context={"performances": performances})
