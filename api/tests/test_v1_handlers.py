import pytest
import json


@pytest.fixture
def provider(data_dir):
    from .common import MockBitFinexProvider
    return MockBitFinexProvider(data_dir)


@pytest.fixture
def app(provider):
    from bitrate.handlers.v1 import make_router
    return make_router(provider=provider)


@pytest.mark.gen_test
async def test_tickers_handler(http_client, base_url):
    response = await http_client.fetch('%s/v1/tickers' % base_url,
                                       raise_error=False)
    assert response.code == 200
    data = json.loads(response.body)['data']
    assert len(data) == 314
    assert data[0] == {'ticker': 'BTCUSD'}


@pytest.mark.gen_test
async def test_ticker_handler(http_client, base_url):
    response = await http_client.fetch('%s/v1/tickers/BTCUSD' % base_url,
                                       raise_error=False)
    assert response.code == 200
    data = json.loads(response.body)['data']
    assert data == {
        'ticker': 'BTCUSD',
        'ask': 5618.4,
        'bid': 5618.3,
        'daily_high': 5668.2,
        'daily_low': 5553.0,
        'daily_volume': 9626.08500577,
        'price': 5618.4,
    }


@pytest.mark.gen_test
async def test_candles_handler(http_client, base_url):
    response = await http_client.fetch(
        '%s/v1/tickers/BTCUSD/candles' % base_url,
        raise_error=False)

    assert response.code == 200
    data = json.loads(response.body)['data']
    assert len(data) == 48
    assert data[0] == {
        'close': 5598.3,
        'high': 5612.2,
        'low': 5596.6,
        'open': 5612.1,
        'timestamp': 1542447000000,
        'volume': 105.9858068,
    }
