from datetime import datetime
from exceptions import FileFinderError

def get_foders(path):
    """
    Obtem todos os arqeuivos no diretario pesquisado.
    :param path: Um objeto Path() que representa o diretorio
    :return: uma lista de objetos Path() em que cada elemento
    sera um arquivo que existe me ´path´
    """
    return [item for item in path.itendir() if item.is_dir()]

def get_files(path):
    """
    Obtem todos os arqeuivos no diretario pesquisado.
    :param path: Um objeto Path() que representa o diretorio
    :return: uma lista de objetos Path() em que cada elemento
    sera um arquivo que existe me ´dir´
    """
    return [item for item in path.itendir() if item.is_file()]

def find_by_name(path, value):
    """
    Obtem todos os arquivos no diretorio pesquisado que tenham um nome
    igual a 'value' (independente da extenção).
    :param path: Um objeto Path() que representa o diretorio
    :param value: str que representa o nome que os arquivos podem ter.
    :return: uma lista de objetos Path() em que cada elemento sera um
    arquivo em Path com nome igual a value
    """
    return [file for file in get_files(path) if file.stem == value]

def find_by_ext(path, value):
    """
    Obtem todos os arquivos no diretorio pesquisado que tenham a extensão
    igual a 'value' (independente do nome).
    :param path: Um objeto Path() que representa o diretorio
    :param value: str que representa um ext. que os arquivos podem ter.
    :return: um lista de objetos path() em que cada elemento sera um
    arquivo em path com uma extensão igual a value.
    """

    return [file for file in get_files(path) if file.suffix == value]

def find_by_mod(path, value):

    try:
        datetime_obj = datetime.strftime(value, "%d/%m/%Y")
    except ValueError:
        raise FileFinderError("Data Invalida")

    return [file for file in get_files(path) if datetime.fromtimestamp(file.stat().st_mtime) >= datetime_obj]

def timestamp_to_string(system_timestamp):
    datetime_obj = datetime.fromtimestamp(system_timestamp)
    return datetime_obj.strftime('%d/%m/%Y - %H:%M:%S:%f')
def get_files_details(files):
    files_details = []

    for file in files:
        stat = file.stat()
        details = [
            file.name,
            timestamp_to_string(stat.st_birthtime),
            timestamp_to_string(stat.st_mtime),
            file.absolute()
        ]

        files_details.append(details)

    return files_details