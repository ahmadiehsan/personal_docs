# Personal Docs

Personal docs and notes

## Usage

```shell
git clone <this/repo/url>
cd <cloned_dir>

curl -LsSf https://astral.sh/uv/0.7.9/install.sh | sh

make manage.serve
```

## Developers

```shell
npm install -g opencommit
oco config set OCO_API_URL="<llm/provider/api/url>"
oco config set OCO_API_KEY="<llm_provider_api_key>"
oco config set OCO_MODEL="<desired_llm_name>"

make dependencies.install
make git.init_hooks
make help
```
