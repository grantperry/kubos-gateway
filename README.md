# Development

First time:

1. Setup a virtualenv
```bash
virtualenv virtualenv -p `which python3`
source virtualenv/bin/activate
pip install -r requirements.txt
```
1. Copy `config.json` to `config.local.json` and edit it.
1. For a server with basic auth endabled, set the websocket URL to something like `wss://username:password@staging.majortom.cloud/cable`

Every time:

```bash
source virtualenv/bin/activate
python run.py
```

Deactivate virtualenv:
```bash
deactivate
```

## Building and distributing

### Locally

See also [this page](http://www.puzzlr.org/install-packages-pip-conda-environment/) and [this page](https://python-packaging.readthedocs.io/en/latest/minimal.html#creating-the-scaffolding).

```bash
cd kubos_gateway
pip install -e .
```

### On PyPI

Read this: https://python-packaging.readthedocs.io/en/latest/minimal.html#publishing-on-pypi
