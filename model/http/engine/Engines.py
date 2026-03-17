from model.http.engine.EngineModel import AbstractEngine
from model.http.engine.StandardEngineModel import StandardEngine

standard_engine: AbstractEngine = StandardEngine()

all_engines: dict[str, AbstractEngine] = {
    standard_engine.get_engine_name(): standard_engine
}
