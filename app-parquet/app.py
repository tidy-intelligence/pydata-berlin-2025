import matplotlib.pyplot as plt

# Import polars to load Parquet
import polars as pl
from shiny import App, render, ui

df = pl.read_parquet("app-parquet/data.parquet")

app_ui = ui.page_sidebar(
    ui.sidebar(ui.input_slider("n", "N", min=0, max=100, value=20)),
    ui.output_plot("histogram"),
    title="Hello, PyData Berlin!",
)


def server(input, output, session):
    @output
    @render.plot
    def histogram():
        # Use data frame instead of generated values
        data = df["values"].to_numpy()
        plt.hist(data, bins=input.n(), density=True)


app = App(app_ui, server)
