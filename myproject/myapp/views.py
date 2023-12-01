from django.shortcuts import render, redirect
import pandas as pd
from .models import CSVFile
from .forms import CSVFileForm

def upload_csv(request):
    if request.method == 'POST':
        form = CSVFileForm(request.POST, request.FILES)
        if form.is_valid():
            
            csv_data = pd.read_csv(request.FILES['file'])

           
            json_data = csv_data.to_json(orient='records')

           
            csv_file = form.save(commit=False)
            csv_file.content_json = json_data
            csv_file.save()

            
            return render(request, 'upload_success.html', {'json_data': json_data})
    else:
        form = CSVFileForm()
    return render(request, 'upload_csv.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')


