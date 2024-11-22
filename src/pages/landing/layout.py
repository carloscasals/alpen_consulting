import dash
from dash import html, dcc
import dash_mantine_components as dmc
from datetime import datetime, timedelta, date
from dash_iconify import DashIconify


contruction_icon = DashIconify(icon="lucide:construction", style={"marginRight": 5})

def create_layout() -> dmc.MantineProvider:
    return dmc.MantineProvider(
        [
            dmc.Container(
                size='xl',
                style={"height": "100vh"},  # Set full height of the viewport
                children=[
                    dmc.Center(style={"height": "100%", "width": "100%"},
                        children=[
                            dmc.Stack([
                                dmc.Image(
                                    src="assets/icon/alpen_consulting_white.png",
                                    style={"width": "60%"}
                                ),
                                dmc.Text([contruction_icon,"Under Construction"], c="grey")
                            ],align="center",
                            )
                        ],
                    ),
                ]
            )
        ])


dash.register_page(
    __name__,
    path="/",
    layout=create_layout,
)