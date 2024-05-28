"""
Main Runner for the Inference Engine (Medical Diagnostic)
"""
from medical_diagnostic import MedicalDiagnostic

if __name__ == "__main__":
    engine = MedicalDiagnostic()
    engine.run_diagnostics()
