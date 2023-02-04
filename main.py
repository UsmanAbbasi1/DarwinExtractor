from config import DarwinConfig
from darwin_client import DarwinClient
from models import DarwinPurchaseResponse


def main():
    darwin_config = DarwinConfig()

    darwin_name = "DAH"
    get_darwin_info(darwin_name, darwin_config)


def get_darwin_info(darwin_name: str, darwin_config: DarwinConfig):
    client = DarwinClient(token=darwin_config.access_token)
    darwin_response: DarwinPurchaseResponse = client.get_darwin_product_score(darwin_name)

    print(f"response from darwin '{darwin_name}': {darwin_response} ")


if __name__ == "__main__":
    main()
