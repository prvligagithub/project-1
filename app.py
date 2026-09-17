import os

# Jenkins automatically injects the ENVIRONMENT parameter into the shell environment
env = os.getenv("ENVIRONMENT", "dev")

print(f"Building the application for the {env} environment...")
