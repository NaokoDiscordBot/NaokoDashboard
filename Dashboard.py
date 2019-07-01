from quart import Quart, jsonify, request, render_template, send_from_directory

class Dashboard(Quart):

    def __init__(self, *args, **kwargs):

        """
        Initiates class
        """

        super().__init__(*args, **kwargs)

    def __repr__(self):

        """
        Class representation
        """

        return "Naoko Quart Dashboard"

    @property
    def version(self) -> str:

        """
        Returns dashboard version
        """

        return "Dashboard Version 0.0.2"


application = Dashboard(
    __name__,
    template_folder="site",
    static_folder="site/assets",
)

@application.route(
    "/", 
    methods=[
        "GET"
    ]
)
async def index():

    """
    Main route for our website
    """

    return await render_template(
        "index.html"
    )

@application.route(
    "/donate", 
    methods=[
        "GET"
    ]
)
async def donate():

    """
    Donations route for our website
    """

    return await render_template(
        "donate.html"
    )

@application.errorhandler(404)
async def handler_404(error):

    """
    404 error handler for our website
    """

    return await render_template(
        "error.html",
        code=404
    )

@application.errorhandler(500)
async def handler_500(error):

    """
    500 error handler for our website
    """

    return await render_template(
        "error.html",
        code=500
    )

def run_application():

    """
    Run our website
    """

    application.run(
        host="0.0.0.0", 
        port=80, 
        debug=False,
    )

if __name__ == "__main__":
    run_application()