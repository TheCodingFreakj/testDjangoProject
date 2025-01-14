import posixpath
from pathlib import Path

from django.utils._os import safe_join
from django.views.static import serve as static_serve


def serve_react(request, path=None, document_root=None):
    if (path is not None):
        path = posixpath.normpath(path).lstrip("/home")
        print(path)
        fullpath = Path(safe_join(document_root, path))
        print(fullpath)
        if fullpath.is_file():
            return static_serve(request, path, document_root)
    else:
        return static_serve(request, "index.html", document_root)
