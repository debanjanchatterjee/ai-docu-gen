# views.py

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .github_handler.clone_and_list import clone_and_list_files
from .llm.generator import generate_readme_from_file_list
from django.http import HttpResponse
from pathlib import Path

@csrf_exempt  # TODO: remove this for production
def home(request):
    generated_readme = None

    if request.method == 'POST':
        url = request.POST.get('url')

        # Clone the repo and list files
        files, error = clone_and_list_files(url)

        if error:
            generated_readme = "❌ Failed to clone the repo. Make sure the URL is valid and public."
        else:
            # Generate the README using the LLM handler
            generated_readme = generate_readme_from_file_list(files, url)

    return render(request, 'docugen/home.html', {'generated_readme': generated_readme})


def download_readme(request):
    readme_path = Path("README.md")

    if not readme_path.exists():
        return HttpResponse("README.md not found.", status=404)

    with readme_path.open("rb") as f:
        response = HttpResponse(f.read(), content_type="text/markdown")
        response["Content-Disposition"] = 'attachment; filename="README.md"'
        return response