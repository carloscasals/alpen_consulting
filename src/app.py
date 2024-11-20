

import os
import warnings
from dotenv import load_dotenv
from layout import create_layout
# from . import callbacks
import dash_mantine_components as dmc
from dash import Dash, _dash_renderer
_dash_renderer._set_react_version("18.2.0")



warnings.filterwarnings("ignore")
load_dotenv()

app = Dash(
        __name__,
        title="Alpen Consulting",
        suppress_callback_exceptions=True,
        use_pages=True,
        # assets_folder="../assets/",
        # external_stylesheets=["/assets/css/base_layout.css", "/assets/css/default_cards.css"],
        external_stylesheets=dmc.styles.ALL
    )

server = app.server
# No content is displayed before user validation
# This could be replaced by cloud IAM/routing
app.layout = create_layout()

# # ------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port=8080)
