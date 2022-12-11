import pkg_resources
for _lib in pkg_resources.working_set:
    print(_lib.project_name, _lib.version)