from logging import Logger, Formatter, DEBUG, StreamHandler


def create_logger(name: str) -> Logger:
    logger = Logger(name, DEBUG)
    handler = StreamHandler()
    handler.setFormatter(Formatter("%(name)s: %(message)s"))
    logger.addHandler(handler)
    return logger
