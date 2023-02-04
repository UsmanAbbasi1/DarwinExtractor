import logging

import requests
from requests import RequestException, Response

from models import DarwinPurchaseResponse

logger = logging.Logger(__name__)


class DarwinException(BaseException):
    pass


class DarwinClient:
    BASE_URL = 'https://api.darwinex.com/'
    API_VERSION = '2.1'

    def __init__(self, token: str) -> None:
        self.__product_score_url = "darwininfo/{api_version}/products/{product_name}/scores"  # ravelin_client_config.url_without_score()
        self.__token = token
        self.__headers = {"Authorization": f"Bearer {self.__token}"}

    @staticmethod
    def __check_response(response: Response) -> None:
        if not response.ok:
            breakpoint()

            raise RequestException("Darwin request failed", response=response)

    def __get(self, url: str) -> Response:
        try:
            response: Response = requests.get(url, headers=self.__headers)
            self.__check_response(response)
        except RequestException as e:
            raise DarwinException from e

        return response

    def get_darwin_product_score(self, product_name: str):
        url = self.BASE_URL + self.__product_score_url.format(
            api_version=self.API_VERSION,
            product_name=product_name,
        )

        try:
            response: Response = self.__get(url)
        except DarwinException as e:
            # TODO: Can send to Sentry or other montiring tool based on business requirements
            logger.error(f"Failed to get darwin product info: {e}")
            return

        darwin_response = DarwinPurchaseResponse(**response.json())

        return darwin_response
