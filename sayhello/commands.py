import click
from sayhello import db, app


@click.command('init_db')
@click.option('--drop', is_flag=True, help='create or drop tables')
def init_db(drop):
    if drop:
        db.drop_all()
        click.confirm('Do you want drop all tables', abort=True)
        click.echo('Drop all table')
    db.create_all()
    click.echo('Init all tables')
    pass


