from core.cipher import ALGORITHMS


class CryptoController:
    def encrypt(self, text: str, algo_id: str) -> str:
        if algo_id not in ALGORITHMS:
            raise ValueError(f"Неизвестный алгоритм: {algo_id}")
        return ALGORITHMS[algo_id](text, decrypt=False)


    def decrypt(self, text: str, algo_id: str) -> str:
        if algo_id not in ALGORITHMS:
            raise ValueError(f"Неизвестный алгоритм: {algo_id}")
        return ALGORITHMS[algo_id](text, decrypt=True)

