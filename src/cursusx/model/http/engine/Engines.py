from cursusx.model.http.engine.HttpEngineModel import AbstractHttpEngine
from cursusx.model.http.engine.StandardHttpEngineModel import StandardHttpEngine, STANDARD_ENGINE_NAME

standard_engine: AbstractHttpEngine = StandardHttpEngine()

all_engines: dict[str, AbstractHttpEngine] = {
    STANDARD_ENGINE_NAME: standard_engine
}


def get_engine(engine_name: str = '') -> AbstractHttpEngine:
    if engine_name not in all_engines:
        raise ValueError('The engine name is not supported!')
    return all_engines[engine_name]
