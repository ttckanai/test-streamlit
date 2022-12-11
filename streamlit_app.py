import pkg_resources
packages = []
for _lib in pkg_resources.working_set:
    # print(_lib.project_name, _lib.version)
    packages.append((_lib.project_name,_lib.version))

packages