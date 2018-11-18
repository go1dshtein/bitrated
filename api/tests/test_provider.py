import pytest


@pytest.fixture
def provider():
    from bitrate.provider import BitFinexProvider

    return BitFinexProvider()


@pytest.mark.live
@pytest.mark.gen_test
async def test_get_tickers(provider):
    result = await provider.get_tickers()
    assert isinstance(result, list)
    assert len(result) > 100


@pytest.mark.live
@pytest.mark.gen_test
async def test_get_ticker(provider):
    ticker = 'BTCUSD'
    result = await provider.get_ticker(ticker)

    assert isinstance(result, dict)
    keys = [
        'daily_high', 'daily_low', 'daily_volume',
        'price', 'ask', 'bid']
    for key in keys:
        assert key in result
        assert isinstance(result[key], float)


@pytest.mark.live
@pytest.mark.gen_test
async def test_get_candles(provider):
    ticker = 'BTCUSD'
    result = await provider.get_candles(ticker)

    assert isinstance(result, list)
    assert len(result) == 48
    keys = [
        'timestamp', 'open', 'close', 'high', 'low', 'volume',
    ]
    current_timestamp = 0
    for element in result:
        for key in keys:
            assert key in element
        assert current_timestamp < element['timestamp']
        current_timestamp = element['timestamp']
