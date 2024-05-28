"""
Main Runner for the Inference Engine (Car Mechanic)
"""
from car_engine import CarEngine

if __name__ == "__main__":
    engine = CarEngine()
    engine.run_diagnostics()
