import click
import os

from flask import current_app
from flask.cli import cli, with_appcontext
from sqlalchemy.exc import IntegrityError

from app import create_app, db
from app.models import PostTypeModel, PlatformModel, RoleModel, PermissionModel, PlatformConfigModel
from app.constants import app_constants
from app.shared.db_api import execute_change
from app.services import db_service


def register_commands(app):
    app.cli.add_command(clean_pyc)
    app.cli.add_command(configure_db)
    app.cli.add_command(test)

@click.command()
def test():
    """This is for testing"""
    click.echo('TEST COMMAND from click')

@click.command()
def clean_pyc():
    """Recursively remove *.pyc and *.pyo files."""
    exclude = set(['venv', 'git', 'migrations'])
    for dirpath, dirnames, filenames in os.walk('.'):
        dirnames[:] = [d for d in dirnames if d not in exclude]
        for filename in filenames:
            if filename.endswith('.pyc') or filename.endswith('.pyo'):
                filepath = os.path.join(dirpath, filename)
                click.echo(f'Removing {filepath}')
                os.remove(filepath)

@click.command()
@with_appcontext
def configure_db():
    db_service.populate_db()