from darwin_extractor.config import DarwinConfig
from darwin_extractor.darwin_client import DarwinClient
from darwin_extractor.models import DarwinPurchaseResponse


class DarwinService:
    def __init__(self, darwin_config: DarwinConfig):
        self.__config = darwin_config
        self.__client = DarwinClient(token=self.__config.access_token)

    def get_darwin_info(self, darwin_name: str):
        darwin_response: DarwinPurchaseResponse = self.__client.get_darwin_product_score(darwin_name)

        return darwin_response

    @staticmethod
    def format_darwin_info(darwin_response: DarwinPurchaseResponse):
        """
        This function makes the formatting of data totally separate from the fetching of data
        A.K.A. Separation of concern.
        """
        print(f"response from darwin: {darwin_response} ")
