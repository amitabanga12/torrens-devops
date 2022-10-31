from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

# Create your views here.

@csrf_exempt
def load_file(request):
    df = []
    if request.method == 'POST' and request.FILES and request.FILES['csv-file-input']:
        csvFile = request.FILES['csv-file-input']
        chunk = pd.read_csv(csvFile, chunksize=1000)
        df = pd.concat(chunk)
        list = df.to_dict(orient='records')
        tableHead = df.columns.tolist()
    else:
        list = []
        tableHead = []
    return render(request, 'process_files.html', {'df': list, 'tableHead': tableHead})