from darwin_extractor.config import DarwinConfig
from services import DarwinService


def main():
    darwin_config = DarwinConfig()
    # This will come from Frontend or user input in production code.
    darwin_name = "DAH"
    darwin_service = DarwinService(darwin_config)
    darwin_response = darwin_service.get_darwin_info(darwin_name)
    darwin_service.format_darwin_info(darwin_response)


if __name__ == "__main__":
    main()
