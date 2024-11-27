import dash
from dash import html, callback, Output, Input, State, ctx
import dash_mantine_components as dmc


def create_layout():
    return dmc.MantineProvider([
        # Manual header using Group, Text, and Anchor
        # dmc.Container(
        #     size="xl",
        #     children=[
        #         dmc.Group(
        #             justify="space-arounds",  # Spreads items apart
        #             align="center",    # Vertically centers the items
        #             style={"height": "60px"},
        #             children=[
        #                 dmc.Group(
        #                     gap="md",
        #                     children=[
        #                         dmc.Anchor(
        #                             dmc.Image(
        #                             src="assets/icon/alpen_consulting_white.png",
        #                             style={"width": "130px"}
        #                         ), 
        #                         href="/"),
        #                         dmc.Anchor("About us", href="/team", className="anchor-link"),
        #                         dmc.Anchor("Value Proposition", href="/value_proposition", className="anchor-link"),
        #                         dmc.Anchor("Approach", href="/approach", className="anchor-link"),
        #                         dmc.Anchor("Team", href="/team", className="anchor-link"),
        #                         dmc.Anchor("Contact", href="/contact", className="anchor-link"),
        #                     ],
        #                 ),
        #             ],
        #         )
        #     ],
        # ),
        dmc.Container(
            size="xl",
            children=[
                dmc.Group(
                    justify="space-between",  # Aligns logo and toggle button
                    align="center",
                    style={"height": "60px"},
                    children=[
                        # Logo
                        dmc.Anchor(
                            dmc.Image(
                                src="assets/icon/alpen_consulting_white.png",
                                style={"width": "130px"},
                            ),
                            href="/",
                        ),
                        # Burger button for mobile
                        html.Div(
                            dmc.Burger(
                                id="burger-button",
                                opened=False,
                                size="sm",
                                style={"display": "block"},  # Shown by default
                            ),
                            id="burger-container",
                        ),
                    ],
                ),
                # Collapsible menu
                dmc.Collapse(
                    id="collapse-menu",
                    opened=False,  # Closed by default
                    children=[
                        dmc.Stack(
                            gap="sm",
                            children=[
                                dmc.Anchor("About us", href="/team", className="anchor-link"),
                                dmc.Anchor("Value Proposition", href="/value_proposition", className="anchor-link"),
                                dmc.Anchor("Approach", href="/approach", className="anchor-link"),
                                dmc.Anchor("Team", href="/team", className="anchor-link"),
                                dmc.Anchor("Contact", href="/contact", className="anchor-link"),
                            ],
                        ),
                    ],
                ),
                # Desktop links
                html.Div(
                    dmc.Group(
                        gap="md",
                        children=[
                            dmc.Anchor("About us", href="/team", className="anchor-link"),
                            dmc.Anchor("Value Proposition", href="/value_proposition", className="anchor-link"),
                            dmc.Anchor("Approach", href="/approach", className="anchor-link"),
                            dmc.Anchor("Team", href="/team", className="anchor-link"),
                            dmc.Anchor("Contact", href="/contact", className="anchor-link"),
                        ],
                    ),
                    id="desktop-menu",
                ),
            ],
            style={"position": "relative"},
        ),
        dmc.Divider(variant="solid", style={"marginBottom":10}),
        dash.page_container
    ])



# Callbacks
@callback(
    Output("collapse-menu", "opened"),
    [Input("burger-button", "opened")],
)
def toggle_collapse(opened):
    return opened


@callback(
    Output("burger-container", "style"),
    Output("desktop-menu", "style"),
    [Input("burger-button", "n_clicks")],
    [State("burger-button", "opened")],
)
def adjust_nav_visibility(n_clicks, opened):
    if ctx.triggered_id == "burger-button" or n_clicks:
        return {"display": "block"}, {"display": "none"} if not opened else {"display": "flex"}
    # Default: Show desktop menu and hide burger on large screens
    return {"display": "none"}, {"display": "flex"}
