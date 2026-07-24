import functools
from datetime import datetime
from pathlib import Path

LOG_FILE = Path('datos/operaciones.log')


def log_operacion(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        msg = f'[{ts}] {func.__name__}'
        try:
            resultado = func(*args, **kwargs)
            linea = f'[{msg}] -> OK'
            print(linea)
            with LOG_FILE.open('a', encoding='utf-8') as f:
                f.write(linea + '\n')
            return resultado
        except Exception as e:
            linea = f'[{msg}] -> ERROR: {e}'
            print(linea)
            with LOG_FILE.open('a', encoding='utf-8') as f:
                f.write(linea + '\n')
            raise
    return wrapper
