from django.shortcuts import get_object_or_404, render, redirect
from .forms import CSVFileForm
import pandas as pd
from .models import CSVFile

def upload_csv(request):
    if request.method == 'POST':
        form = CSVFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Read CSV file using pandas
            csv_data = pd.read_csv(request.FILES['file'])

            # Convert CSV data to JSON
            json_data = csv_data.to_json(orient='records')

            # Save the CSV file and JSON data to the database
            csv_file = form.save(commit=False)
            csv_file.content_json = json_data
            csv_file.save()

            return redirect('upload_success')  # You can change this to your success page
    else:
        form = CSVFileForm()
    return render(request, 'upload_csv.html', {'form': form})

def uploaded_json(request, pk):
     try:
        csv_file = get_object_or_404(CSVFile, pk=pk)
        json_data = csv_file.content_json
        print(f"JSON Data: {json_data}")
        return render(request, 'uploaded_json.html', {'json_data': json_data})
     except Exception as e:
        print(f"Error in uploaded_json view: {e}")
        raise

def upload_success(request):
    return render(request, 'upload_success.html')


