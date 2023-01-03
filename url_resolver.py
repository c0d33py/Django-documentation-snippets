def get_resolved_urls_names(request):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Open the file in write mode
    with open(os.path.join(BASE_DIR, 'urls.txt'), 'w') as f:
        # to get all files in a directory use os.listdir and then get the url_patterns from each file
        for file in os.listdir(BASE_DIR + '/core/urls'):
            if file.endswith('.py') and file != '__init__.py':
                url_dir = importlib.import_module('core' + '.urls.' + file[:-3])
                url_patterns = url_dir.urlpatterns
                url_patterns_resolved = get_resolved_urls(url_patterns)
                for url in url_patterns_resolved:
                    f.write(url + '\n')

    return HttpResponse('urls')


def get_resolved_urls(url_patterns):
    url_patterns_resolved = []
    for url in url_patterns:
        if isinstance(url.pattern, RegexPattern):
            url_patterns_resolved.append(url.pattern._regex)
        elif isinstance(url.pattern, RoutePattern):
            url_patterns_resolved.append(url.pattern._route)
        else:
            url_patterns_resolved.append(url.pattern)
    return url_patterns_resolved
