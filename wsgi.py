from app import create_app

application = create_app()


@application.route('/')
def home():
    return "Hello!"