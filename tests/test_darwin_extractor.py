from unittest import TestCase
from unittest.mock import Mock, patch

from darwin_extractor.models import DarwinPurchaseResponse
from darwin_extractor.services import DarwinService


class MockResponse:
    @property
    def ok(self):
        return True

    @staticmethod
    def json():
        return {
            "productName": "DAH.5.24", "dc": 5.18, "os": 4.82, "cs": 1.57,
            "mc": 9.89, "rplus": 1.31, "ra": 9.87, "ex": 10.0, "pf": 0.87,
            "score": 48.51, "rminus": 3.21, "rs": 7.16, "sc": 4.54, "la": 7.85,
            "cp": 4.54,
        }


class TestDarwinExtractor(TestCase):
    @patch("darwin_extractor.darwin_client.requests.get")
    def test_get_darwin_product_info(self, mock_darwin_request):
        mock_darwin_request.return_value = MockResponse()

        expected_response = DarwinPurchaseResponse(
            product_name='DAH.5.24', dc='5.18', os='4.82', cs='1.57', mc='9.89',
            rplus='1.31', ra='9.87', ex='10.0', pf='0.87', score='48.51',
            rminus='3.21', rs='7.16', sc='4.54', la='7.85', cp='4.54',
        )

        darwin_name = "DAH"
        darwin_service = DarwinService(Mock())
        response = darwin_service.get_darwin_info(darwin_name)

        assert response == expected_response
