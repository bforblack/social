import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)


class Logger:
    def __init__(self):
        self.logger = logging.getLogger()

    def info_msg(self, message):
        """

        :param message:
        :return: log with the time
        """
        self.logger.info(message)

    def error_msg(self, message):
        """

        :param error message:
        :return: log with the time
        """
        self.logger.error(message)
