#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime

from crew import ProjetoParaProducao

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Configurar a API key diretamente no código
# Substitua 'sua_chave_openai_aqui' pela sua chave real da API da OpenAI
os.environ["OPENAI_API_KEY"] = "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"

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    
    try:
        ProjetoParaProducao().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        ProjetoParaProducao().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ProjetoParaProducao().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        ProjetoParaProducao().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":

    print(f"OPENAI_API_KEY configurada: {'Sim' if os.getenv('OPENAI_API_KEY') else 'Não'}")
    run()
