import click
import shutil
from pathlib import Path
from utils import find_by_name
from utils import find_by_ext
from utils import find_by_mod
from utils import timestamp_to_string
from utils import get_foders
from datetime import datetime
from utils import get_files_details
from tabulate import tabulate

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
       table_headers = ["Nome", "Criação", "Modificação", "Localização"]
       table_data = get_files_details(files)
       tabulated_data = tabulate(tabulate_data=table_data, headers=table_headers, tablefmt="tsv")
       click.echo(tabulated_data)
       return table_data

@click.command()
@click.argument("path", default="")
@click.option("-k", "--key", required=True, type=click.Choice(["name","ext", "mod"]))
@click.option("-v", "--value", required=True)
@click.option("-r", "recursive", is_flag=True, default=False)
@click.option("-s", "--save", is_flag=True, default=False)
@click.option("-c", "--copy-to")

def finder(path, key, value, recursive, copy_to, save):
    root = Path(path)

    if not root.is_dir():
        raise Exception("O caminho informado não representa um diretorio.")

    click.echo(f"O diretório selecionado foi: {root.absolute()}")

    files = process_search(path=root, key=key, value=value, recursive=recursive)
    report = process_result(files=files, key=key, value=value)

    if save:
        report_file_path = root / f"fider_report_{datetime.now().strftime('%d%m%Y%H%M%S%f')}.txt"
        with open(report_file_path.absolute(), node="w") as report_file:
            report_file.write(report)

    if copy_to:
        copy_path = path(copy_to)

        if not copy_path.is_dir():
            copy_path.mkdir(parents=True)

        for file in files:
            dst_file = copy_path / f"{file.stem}{datetime.now().strftime('%d%m%Y%H%M%S%f')}{file.suffix}"

        shutil.copy(src=file.absolute(), dst=dst_file)
finder()
