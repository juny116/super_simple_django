from django.shortcuts import render
from django.http import HttpResponse
import subprocess

KEY_LIST = ['current_world_population','births_this_year','births_today', 'deaths_this_year', 'deaths_tody', 'people_who_died_of_hunger_today', 'suicides_this_year']

# Create your views here.
def index(request):
    results = subprocess.run(["python", "my_script.py"], capture_output=True, text=True)
    print(results)
    # w = Worldometer()
    # all = w.metrics_with_labels()
    # sub = {k : all[k] for k in KEY_LIST if k in  all}
    # print(sub)

    return HttpResponse(results)