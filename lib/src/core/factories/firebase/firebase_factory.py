import json
import os

import pyrebase

from lib.src.core.factories.firebase.constants.firebase_constants import (
    FirebaseConstants,
)


class FirebaseFactory:
    """Factory para inicializar e fornecer uma instância singleton da autenticação Firebase.

    A classe `FirebaseFactory` é responsável por carregar a configuração do Firebase a partir de um arquivo JSON,
    inicializar o aplicativo Firebase e fornecer a instância de autenticação. Utiliza o padrão Singleton para
    garantir que apenas uma instância da autenticação seja criada.
    """

    _instance = None

    @classmethod
    def instance(cls):
        """Retorna a instância singleton da autenticação Firebase.

        Se a instância ainda não foi criada, chama o método privado `_create` para criá-la.

        Returns:
            firebase.auth(): A instância de autenticação do Firebase.

        Raises:
            RuntimeError: Se ocorrer um erro durante a inicialização do Firebase.
        """
        if cls._instance is None:
            cls._instance = cls._create()
        return cls._instance

    @staticmethod
    def _create():
        """Cria a instância de autenticação Firebase usando a configuração carregada.

        Carrega a configuração do Firebase a partir de um arquivo JSON especificado, inicializa o aplicativo Firebase
        e retorna a instância de autenticação.

        Returns:
            firebase.auth(): A instância de autenticação do Firebase.

        Raises:
            RuntimeError: Se ocorrer um erro durante a inicialização do Firebase.
        """
        try:
            firebase_config = FirebaseFactory._load_config()
            firebase = pyrebase.initialize_app(firebase_config)
            auth = firebase.auth()
            return auth
        except Exception as e:
            raise RuntimeError(f"Erro ao inicializar o Firebase: {e}")

    @staticmethod
    def _load_config():
        """Carrega a configuração do Firebase a partir do arquivo JSON especificado.

        Lê o arquivo de configuração JSON localizado no caminho especificado em `FirebaseConstants` e retorna
        o conteúdo como um dicionário.

        Returns:
            dict: O dicionário de configuração do Firebase.

        Raises:
            FileNotFoundError: Se o arquivo de configuração não for encontrado.
            ValueError: Se ocorrer um erro ao decodificar o arquivo de configuração JSON.
        """
        try:
            project_path = os.getcwd()
            firebase_config_path = os.path.join(
                project_path, FirebaseConstants.firebase_config_path
            )
            with open(firebase_config_path) as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Arquivo de configuração não encontrado: {firebase_config_path}"
            )
        except json.JSONDecodeError:
            raise ValueError("Erro ao decodificar o arquivo de configuração JSON")
