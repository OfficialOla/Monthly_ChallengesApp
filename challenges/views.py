from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january": "No soda for the entire month",
    "february": "Workout for at least 20 minutes everyday!",
    "march": "Learn Django for at least 20 minutes every day",
    "april": 'Practice mindful eating by slowing down and savoring each bite',
    "may": "Take a few moments each day to reflect on the positive aspects of your life",
    "june": "Express gratitude to others by writing thank-you notes or showing appreciation in person",
    "july": "Engage in mindful physical activities like yoga, tai chi, or walking meditation",
    "august": "Focus on the sensations in your body and be fully present in the movement",
    "september": "Pay attention to your breath and the way your body moves",
    "october": "Take mindful breaks during the day to pause, breathe, and center yourself",
    "november": "Practice deep breathing exercises to calm the mind and reduce stress",
    "december": None
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href = \"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def my_monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponse("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def my_monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render(request, "challenges/challenge.html", {"text": challenge_text,
                                                                      "month_name": month})
        return HttpResponse(response_data)
    except:
        raise Http404()
        # respond_request = get_object_or_404()
        # return HttpResponse(request, respond_request)
