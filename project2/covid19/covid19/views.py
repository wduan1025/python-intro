from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import re
from . import cov19_visualization
from os import path
from . import settings

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def visualize(request):
    if request.method == 'POST':
        date = request.POST.get('date', '')
        print(date)
        # date_pattern = r"\d{2}/\d{2}\/\d{4}"
        date_pattern = r"\d(\d/\d\d/)\d\d(\d\d)"
        match_results = re.findall(date_pattern, date)
        # The date is valid
        if match_results is not None:
            # convert datetime
            date_code = (match_results[0][0] + match_results[0][1]).replace('/', '-')
            print(date_code)
            data_fname = 'time_series_2019-ncov-Confirmed.csv'
            country_name_fname = "country_code.xlsx"
            data_path = settings.BASE_DIR + '/covid19/data/' + data_fname
            country_name_path = settings.BASE_DIR + '/covid19/data/' + country_name_fname
            output_prefix = settings.BASE_DIR + '/templates/'
            print(path.exists(data_path))
            print(path.exists(country_name_path))
            print(path.exists(output_prefix))
            output_fname = cov19_visualization.run(date_code.replace('-', '/'), data_path, country_name_path, output_prefix)
            print(path.exists(output_fname))
            # print(path.exists(target_fname))
            # run visualize script
            return render(request, output_fname)
        return HttpResponse("visualize page")
    return HttpResponse("???")