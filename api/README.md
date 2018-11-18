## Run server localy

Setup environment


    python3 -mvenv ./env
    . ./env/bin/activate
    pip install --upgrade pip setuptools
    pip install -r requirements.txt


Then run server


    ./bin/bitrated --host 127.0.0.1


And check it


    curl http://127.0.0.1:8080/v1/tickers/BTCUSD; echo
    {"data": {"bid": 5654.4, "ask": 5654.5, "price": 5654.4, "daily_volume": 8167.47328237, "daily_high": 5688.4, "daily_low": 5569.1, "ticker": "BTCUSD"}}


## Running tests

Setup environment


    python3 -mvenv ./env
    . ./env/bin/activate
    pip install --upgrade pip setuptools
    pip install -r requirements.txt


Install development requirements


    pip install -r requirements-dev.txt


Run style checks

  
    flake8 .

And run unittests


    py.test -vv ./tests


To run just offline tests

  
    py.test -vv -m 'not live' ./tests


To produce coverage report

  
    py.test -vv --cov ./bitrate --cov-report=html:coverage-report ./tests
    open ./coverage-report/index.html


## Build and run container


    docker build . -t bitrated:latest
    docker run --rm -p 8080:8080 bitrated:latest
    curl http://127.0.0.1:8080/v1/tickers/BTCUSD; echo
    {"data": {"bid": 5654.4, "ask": 5654.5, "price": 5654.4, "daily_volume": 8167.47328237, "daily_high": 5688.4, "daily_low": 5569.1, "ticker": "BTCUSD"}}
