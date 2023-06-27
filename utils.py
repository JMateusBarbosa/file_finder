
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
    pass
