import pytest


@pytest.fixture
def app():
    from bitrate.metrics import make_router
    return make_router()


@pytest.mark.gen_test
async def test_metrics_handler(http_client, base_url):
    response = await http_client.fetch(
        f'{base_url}/metrics', raise_error=False)

    assert response.code == 200
    assert response.headers.get('Content-type', '').startswith('text/plain')
    assert b'python_info' in response.body
    assert b'api_request_processing_seconds' in response.body
