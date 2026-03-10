# OpenGates CC

Commercial repo for OpenGates.

This repo now contains:
- product thesis and planning docs
- the commercial app surface under `cc/`
- internal product iteration work

The OSS runtime now lives separately at:
- [nvsudo/opengates-oss](https://github.com/nvsudo/opengates-oss)

## Run The Commercial Surface
```bash
cd cc
uv sync --extra dev
uv run opengates-cc serve --host 127.0.0.1 --port 8100
```

Open [http://127.0.0.1:8100/demo](http://127.0.0.1:8100/demo).

## Notes
- `cc/` reuses the OSS engine as a dependency during development.
- the commercial UI is intentionally more opinionated than the OSS reference UI.
