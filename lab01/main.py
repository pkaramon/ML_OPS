import argparse
from dotenv import load_dotenv
from settings import Settings
import yaml
import os


def export_envs(environment: str = "dev") -> None:
    file_name = f"./config/.env.{environment}"
    load_dotenv(file_name)


def load_secrets():
    with open("secrets.yaml", "r") as file:
        secrets = yaml.safe_load(file)
        for key, value in secrets.items():
            os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    load_secrets()
    export_envs(args.environment)

    settings = Settings()

    print("APP_NAME:", settings.APP_NAME)
    print("ENVIRONMENT:", settings.ENVIRONMENT)
    print("API_KEY:", settings.API_KEY)
