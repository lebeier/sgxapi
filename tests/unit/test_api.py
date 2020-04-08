from unittest.mock import MagicMock
from unittest.mock import patch

from sgxapi.api import get_latest_price

class TestApi:

    class TestGetLatestPrice:

        @patch('requests.get')
        def test_should_call_requests_get(self, mock_requests_get: MagicMock) -> None:
            get_latest_price()
            mock_requests_get.assert_called()
