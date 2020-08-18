from django.shortcuts import render
from django.http import HttpResponse    # httpresponse
from django.http import Http404         # error 404 response

from .models import CISBenchmark        # import model
from .models import ProwlerOutput

# Create your views here.
def home(request):
    # return HttpResponse('Welcome Home')   # uncomment this line for simple welcome page
    benchmarks = CISBenchmark.objects.all()
    return render(request, 'home.html', {'benchmarks': benchmarks})


def benchmark_detail(request, benchmark_id):
    # return HttpResponse(f'Benchmark ID: {benchmark_id}')   # uncomment this for simple httpresponse check
    try:
        benchmark = CISBenchmark.objects.get(id=benchmark_id)
    except CISBenchmark.DoesNotExist:
        raise Http404('Benchmark not found.!!')
    return render(request, 'benchmark_detail.html', {'benchmark': benchmark})

