# from app.core.container import ApplicationContainer
# from app.application.application import Application
from app.application.cli import run

def main():
    # container = ApplicationContainer()
    # app = Application(container)
    # app.start()
    run()

if __name__ == "__main__":
    main()