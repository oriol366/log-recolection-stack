import logging
import time
import random
import sys
import uuid
from ecs_logging import StdlibFormatter

# Configurar logging
logger = logging.getLogger('example_logger')
logger.setLevel(logging.DEBUG)

# Crear manejador para stdout
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.INFO)

# Crear manejador para stderr
stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setLevel(logging.WARNING)

# Formateador ECS JSON
ecs_formatter = StdlibFormatter()

# Asignar el formateador ECS JSON a los manejadores
stdout_handler.setFormatter(ecs_formatter)
stderr_handler.setFormatter(ecs_formatter)

# Añadir manejadores al logger
logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)

# Mensajes de ejemplo
info_messages = [
    "User logged in successfully.",
    "Data retrieved from the database.",
    "Cache hit for user profile.",
    "User profile updated."
]

warning_messages = [
    "API response time is slower than expected.",
    "Cache miss for user profile.",
    "Disk space is running low.",
    "High memory usage detected."
]

error_messages = [
    "Failed to connect to the database.",
    "Null pointer exception occurred.",
    "Out of memory error.",
    "Service unavailable, retrying..."
]

# Función para generar logs aleatorios
def generate_random_logs():
    while True:
        level = random.choice(['INFO', 'WARNING', 'ERROR'])
        trace_id = str(uuid.uuid4())
        span_id = str(uuid.uuid4())
        extra = {'extra': {'trace_id': trace_id, 'span_id': span_id}}
        
        if level == 'INFO':
            message = random.choice(info_messages)
            logger.info(message, extra=extra)
        elif level == 'WARNING':
            message = random.choice(warning_messages)
            logger.warning(message, extra=extra)
        else:
            message = random.choice(error_messages)
            logger.error(message, extra=extra)
        
        time.sleep(random.uniform(1, 5))

if __name__ == "__main__":
    generate_random_logs()
