from pprint import pprint
from fastapi import FastAPI

from models.swinir import SWINIR


def startup_SWINIR(app:FastAPI) -> None:
    app.state.SWINIR_config = SWINIR()
    pprint(f"SWINIR:\n{app.state.SWINIR_config.dict()}")
    model = SWINIR.define_model(app.state.SWINIR_config)
    model.eval()
    model = model.to(SWINIR.define_device())
    app.state.SWINIR = model


def startup(app:FastAPI) -> None:
    startup_SWINIR(app)


def shutdown(app:FastAPI) -> None:
    del app.state.ESRGAN
    del app.state.ESRGAN_config
