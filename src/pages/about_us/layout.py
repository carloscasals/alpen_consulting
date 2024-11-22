import dash
from dash import html, dcc
import dash_mantine_components as dmc
from datetime import datetime, timedelta, date
from dash_iconify import DashIconify


contruction_icon = DashIconify(icon="lucide:construction", style={"marginRight": 5})
linkedin_icon = DashIconify(icon="mdi:linkedin", style={"marginLeft": 5})



def create_layout() -> dmc.MantineProvider:
    return dmc.MantineProvider(
        [
            dmc.Container(
                size='xl',
                style={"height": "100vh"},  # Set full height of the viewport
                children=[
                    dmc.Grid(
                        gutter=12,
                        children=[
                            dmc.GridCol(html.Div([
                                    html.H1("About us",style={"marginBottom":5}),
                                    html.H3("A team of passionate consultants and industry experts",style={"marginTop":5})
                                ])),
                            dmc.GridCol(
                                span=4,
                                children=[
                                    # 1st consultant
                                    dmc.Grid(
                                        gutter=8,
                                        children=[
                                            dmc.GridCol(span=4,children=[
                                                    dmc.Image(src="https://media.licdn.com/dms/image/v2/C5603AQHESZBGoc7QNQ/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1584210187270?e=1737590400&v=beta&t=uxLPxg0DHctF9hK2TQ24l6foWq1Qh154I3DSgzT9MIM",
                                                    h=160,
                                                    alt="Norway",
                                                ),    
                                            ]),
                                            dmc.GridCol(span=8,children=[
                                                    dmc.Text(["César Ferrer", html.A(linkedin_icon,href="https://www.linkedin.com/in/c%C3%A9sar-ferrer/")], fw=500, size="lg", c="blue"),
                                                    dmc.Text("Managing Partner", fw=700),
                                                    dmc.Text("Strategy and management consultant with almost 20 years in operations helping PE, investement funds and family-owned clients at McKinsey & Accenture", size="sm",),  
                                            ])
                                    ]),
                                ]
                            ),
                            dmc.GridCol(
                                span=4,
                                children=[
                                    # 2nd consultant
                                    dmc.Grid(
                                        gutter=8,
                                        children=[
                                            dmc.GridCol(span=4,children=[
                                                    dmc.Image(src="https://media.licdn.com/dms/image/v2/C4E03AQE6dU65Ksm0sg/profile-displayphoto-shrink_400_400/profile-displayphoto-shrink_400_400/0/1522928486611?e=1737590400&v=beta&t=D1UgkwtMumXLaUBz4AEsZW4_a28jGg_ztyIzDDHDr54",
                                                    h=160,
                                                    alt="Norway",
                                                ),    
                                            ]),
                                            dmc.GridCol(span=8,children=[
                                                    dmc.Text(["Marta Serradell", html.A(linkedin_icon,href="https://www.linkedin.com/in/marta-serradell-bustamante/")], fw=500, size="lg", c="blue"),
                                                    dmc.Text("Senior Advisor - Finance", fw=700),
                                                    dmc.Text("Finance executive and consultant with +10 years of experience in the educational sector (schools, universities and language)", size="sm",),  
                                            ])
                                    ]),
                                ]
                            )
                        ]
                    )
                ]
            )
        ])


dash.register_page(
    __name__,
    path="/about_us",
    layout=create_layout,
)

