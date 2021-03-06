from invoke import Collection, task

from tasks.common import VENV_PREFIX
from tasks.env import clean as clean_env
from tasks.env import init as _init


@task
def develop(ctx):
    """Install script in pipenv environement in development mode"""
    ctx.run(f"{VENV_PREFIX} python setup.py develop")


@task
def install(ctx):
    """Install script in pipenv environement"""
    ctx.run(f"{VENV_PREFIX} python setup.py install")


@task
def dist(ctx):
    """Build distribution"""
    ctx.run(f"{VENV_PREFIX} python setup.py sdist bdist_wheel")


@task
def clean(ctx):
    """Remove all the tmp files in .gitignore"""
    ctx.run("git clean -Xdf")


@task
def test_cli(ctx, clean=False):
    """Test whether the cli is runnable"""
    if clean:
        clean_env(ctx)
        _init(ctx)
    install(ctx)
    ctx.run(f"{VENV_PREFIX} rg-cli --help")


build_ns = Collection("build")
build_ns.add_task(develop)
build_ns.add_task(install)
build_ns.add_task(dist)
build_ns.add_task(clean)
build_ns.add_task(test_cli)
