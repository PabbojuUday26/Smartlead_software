"""Main entry point for Smartlead software."""

from agents import get_default_manager


def main():
    manager = get_default_manager()
    print(manager.summary())


if __name__ == "__main__":
    main()
