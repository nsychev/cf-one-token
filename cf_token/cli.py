import click
import uvicorn


@click.command()
@click.option("--host", default="0.0.0.0", help="Host to bind to.")
@click.option("--port", default=8000, type=int, help="Port to bind to.")
def main(*, host: str, port: int) -> None:
    """Run the CF Access token web app."""
    uvicorn.run("cf_token.app:app", host=host, port=port)


if __name__ == "__main__":
    main()
