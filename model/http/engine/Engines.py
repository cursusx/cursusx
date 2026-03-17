from model.http.engine.HttpEngineModel import AbstractHttpEngine
from model.http.engine.StandardHttpEngineModel import StandardHttpEngine

standard_engine: AbstractHttpEngine = StandardHttpEngine()

all_engines: dict[str, AbstractHttpEngine] = {
    standard_engine.get_engine_name(): standard_engine
}
