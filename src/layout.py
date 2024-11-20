import dash
from dash import html
import dash_mantine_components as dmc


def create_layout():
    return dmc.MantineProvider([
        # Manual header using Group, Text, and Anchor
        dmc.Container(
            size="xl",
            # style={"padding": "0 20px", "backgroundColor": dmc.theme.DEFAULT_COLORS["blue"][6]},
            children=[
                dmc.Group(
                    justify="space-arounds",  # Spreads items apart
                    align="center",    # Vertically centers the items
                    style={"height": "60px"},
                    children=[
                        
                        dmc.Group(
                            gap="md",
                            children=[
                                dmc.Anchor(
                                    dmc.Image(
                                    src="assets/icon/alpen_consulting_white.png",
                                    style={"width": "130px"}
                                ), 
                                href="/"),
                                dmc.Anchor("Why?", href="/about", className="anchor-link"),
                                dmc.Anchor("Contact", href="/contact", className="anchor-link"),
                            ],
                        ),
                    ],
                )
            ],
        ),
        dash.page_container
    ])