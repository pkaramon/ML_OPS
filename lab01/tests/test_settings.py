from settings import Settings


def test_settings_loaded_from_env_test():
    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "my_app"
    assert settings.API_KEY == "test_api_key"
