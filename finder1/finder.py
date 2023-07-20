import click
from pathlib import Path
from utils import find_by_name
from utils import find_by_ext
from utils import find_by_mod
from utils import timestamp_to_string
from utils import get_foders

def process_search(path, key, value, recursive):
    search_mapping ={
        "name": find_by_name,
        "ext": find_by_ext,
        "mod": find_by_mod,
    }

    files = search_mapping[key](path, value)

    if recursive:
        subdirs = get_foders(path)
        for subdirs in subdirs:
            files += process_search(subdirs, key, value, recursive)
    return files

def process_result(files, key, value):
    if not files:
        click.echo(f"Nenhum arquivo encontrado com {key} {value} foi encontrda")
    else:
        for f in files:
            click.echo(
                f"Nome: {f.name}\n"
                f"Data Criação: {timestamp_to_string(f.stat().st_birthtime)}\n"
                f"Data Modificação: {timestamp_to_string(f.stat().st_mtime)}\n"
                f"Localização: {f.parent.absolute()}"
            )

    if not files:
        click.echo(f"Nenhum arquivo encontrado com {key} {value} foi encontrda")
    else:
        for f in files:
            click.echo(
                f"Nome: {f.name}\n"
                f"Data Criação: {timestamp_to_string(f.stat().st_birthtime)}\n"
                f"Data Modificação: {timestamp_to_string(f.stat().st_mtime)}\n"
                f"Localização: {f.parent.absolute()}"
            )
@click.command()
@click.argument("path", default="")
@click.option("-k", "--key", required=True, type=click.Choice(["name","ext", "mod"]))
@click.option("-v", "--value", required=True)
@click.option("-r", "recursive", is_flag=True, default=False)

def finder(path, key, value, recursive):
    root = Path(path)

    if not root.is_dir():
        raise Exception("O caminho informado não representa um diretorio.")

    click.echo(f"O diretório selecionado foi: {root.absolute()}")

    files = process_search(path=root, key=key, value=value, recursive=recursive)
    process_result(files=files, key=key, value=value)

finder()
