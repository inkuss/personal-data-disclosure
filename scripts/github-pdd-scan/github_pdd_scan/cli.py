import click


@click.group()
@click.version_option()
def cli():
    "Scan GitHub repositories for PERSONAL_DATA_DISCLOSURE documents"


@cli.command(name="command")
@click.argument("example")
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(example, option):
    "Command description goes here"
    click.echo("Here is some output")
