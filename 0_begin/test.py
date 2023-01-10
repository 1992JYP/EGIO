import click

@click.command()
@click.option('--count', default = 1 , help = 'Number of greeting')
@click.option('--name', prompt = 'Your name', help = 'The person to greet.')
def hello(count,name):
    for x in range(count):
        click.echo(f"Hello {name}")

@click.group()
def cli():
    pass

# @click.command()
# def initdb():
#     click.echo('Initialized the database')

# @click.command()
# def dropdb():
#     click.echo('Dropped the database')

# cli.add_command(initdb)
# cli.add_command(dropdb)

@cli.command()
def initdb():
    click.echo('init')

@cli.command()
def dropdb():
    click.echo('drop')


if __name__ =='__main__':
    cli()