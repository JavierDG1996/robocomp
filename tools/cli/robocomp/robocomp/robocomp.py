import typer as typer
from rcbuild import rcbuild
from rccd import rccd
from rcconfig import rcconfig
from rcdocker import rcdocker
from rcportchecker import rcportchecker
from rcrun import rcrun
from rcworkspace import main as rcworkspace
from robocompdsl import main as robocompdsl


app = typer.Typer(help="Tool to manage and group all the Robocomp commands.")
app.add_typer(rcbuild.app, name="build")
app.add_typer(rcconfig.app, name="config")
app.add_typer(rcdocker.app, name="docker")
app.add_typer(rcportchecker.app, name="list")
app.add_typer(rcrun.app, name="run")
app.add_typer(rcworkspace.app, name="workspace")
app.command(name="cd", help=typer.style("Change directory to Robocomp components",fg=typer.colors.GREEN))(rccd.cd_exec)
app.command(name="dsl", help=typer.style("Tool to create components and interfaces.", fg=typer.colors.GREEN))(robocompdsl.generate)

help=typer.style("Build documentation of the specified component", fg=typer.colors.GREEN)
if __name__ == "__main__":
    app()
