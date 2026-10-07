from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="Service Status")

table.add_column("Service")
table.add_column("Status")
table.add_row("API", "[green]Healthy[/green]")
table.add_row("Cache", "[red]Degraded[/red]")
console.print(table)