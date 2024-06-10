import typer
from rich.console import Console
from rich.table import Table
from sqlmodel import Session, select

from .db import engine
from .models.cliente import Cliente
from .config import settings
from .db import engine, SQLModel

main = typer.Typer(name="clientes CLI", add_completion=False)


@main.command()
def shell():
    """Opens interactive shell"""
    _vars = {
        "settings": settings,
        "engine": engine,
        "select": select,
        "session": Session(engine),
        "Cliente": Cliente,
    }
    typer.echo(f"Auto imports: {list(_vars.keys())}")
    try:
        from IPython import start_ipython

        start_ipython(
            argv=["--ipython-dir=/tmp", "--no-banner"], user_ns=_vars
        )
    except ImportError:
        import code

        code.InteractiveConsole(_vars).interact()


@main.command()
def cliente_list():
    """Lists all users"""
    table = Table(title="lista cliente")
    fields = ["username", "email", "phone"]
    for header in fields:
        table.add_column(header, style="magenta")

    with Session(engine) as session:
        users = session.exec(select(Cliente)).all()
        for user in users:
            table.add_row(*[getattr(user, field) for field in fields])

    Console().print(table)


@main.command()
def cliente_create(
    username: str,
    email: str,
    phone: str
):
    """Criar Cliente"""
    with Session(engine) as session:
        cliente = Cliente(
            username=username,
            email=email,
            phone=phone
        )
        session.add(cliente)
        session.commit()
        session.refresh(cliente)
        typer.echo(f"created {cliente.username} cliente")
        return cliente


@main.command()
def reset_db(
    force: bool = typer.Option(
        False, "--force", "-f", help="Run with no confirmation"
    )
):
    """Resets the database tables"""
    force = force or typer.confirm("Are you sure?")
    if force:
        SQLModel.metadata.drop_all(engine)
