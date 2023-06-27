import click
from pathlib import Path
from utils import find_by_name
from utils import find_by_ext
from utils import find_by_mod

def process_search(path, key, value):
    search_mapping ={
        "name": find_by_name,
        "ext": find_by_ext,
        "mod": find_by_mod,
    }

    files = search_mapping[key](path, value)

    if not files:
        click.echo(f"Nenhum arquivo encontrado com {key} {value} foi encontrda")
    else:
        for f in files:
            click.echo(
                f"Nome: {f.name}\n"
                f"Data Criação: {f.stat().st_mtime}\n"
                f"Localização: {f.parent.absolute()}"
            )
@click.command()
@click.argument("path", default="")
@click.option("-k", "--key", required=True, type=click.Choice(["name","ext", "modified"]))
@click.option("-v", "--value", required=True)
def finder(path, key, value):
    root = Path(path)

    if not root.is_dir():
        raise Exception("O caminho informado não representa um diretorio.")

    click.echo(f"O diretório selecionado foi: {root.absolute()}")

    process_search(path=root, key=key, value=value)

finder()
