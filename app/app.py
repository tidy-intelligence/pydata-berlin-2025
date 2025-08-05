import matplotlib.pyplot as plt
import numpy as np
from shiny import App, render, ui

# Define the UI
app_ui = ui.page_sidebar(
    ui.sidebar(ui.input_slider("n", "N", min=0, max=100, value=20)),
    ui.output_plot("histogram"),
)


# Define the server logic
def server(input, output, session):
    @output
    @render.plot
    def histogram():
        np.random.seed(1234)
        x = 100 + 15 * np.random.randn(437)
        plt.hist(x, bins=input.n(), density=True)


# Create the Shiny app
app = App(app_ui, server)
