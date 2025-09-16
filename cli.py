import click
from asp_motor import calcular_variables

@click.command()
@click.option("--etp", type=float, required=True, help="ETp en mm/día")
@click.option("--eficiencia", type=float, required=True, help="Eficiencia (0-1)")
@click.option("--q", type=float, required=True, help="Caudal disponible en L/s")
@click.option("--sup", type=float, required=True, help="Superficie de riego en ha")
def cli(etp, eficiencia, q, sup):
    res = calcular_variables(etp, eficiencia, q, sup)
    click.echo("=== Resultados ===")
    for k, v in res.items():
        click.echo(f"{k}: {v:.3f}")

if __name__ == "__main__":
    cli()
