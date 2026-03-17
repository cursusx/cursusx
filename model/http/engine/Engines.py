from model.http.engine.EngineModel import AbstractHttpEngine
from model.http.engine.StandardEngineModel import StandardEngine

standard_engine: AbstractHttpEngine = StandardEngine()

all_engines: dict[str, AbstractHttpEngine] = {
    standard_engine.get_engine_name(): standard_engine
}
