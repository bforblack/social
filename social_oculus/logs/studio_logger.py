import logging
import os
import inspect
import colorlog

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Log_levels = {'CRITICAL': 50, 'ERROR': 40,
              'WARNING': 30, 'INFO': 20, 'DEBUG': 10}


class Logger:

    # def __init__(self, ai_flow_id: str):
    #
    #     self.log = self.get_logger(logger_id=ai_flow_id)
    #     self.ai_flow_id = ai_flow_id
    #     os.environ["logger_id"] = self.ai_flow_id

    @staticmethod
    def location(logging_string):
        frame = inspect.stack()[2]  # Adjust the stack level as needed
        caller_filename = frame[0].f_globals['__file__']
        caller_lineno = frame[0].f_lineno
        filename = os.path.basename(caller_filename)
        log_msg = f"{filename}:{caller_lineno} - {logging_string}"
        return log_msg

    def debug(self, logging_string):
        """
        Provide logs for debug states, ensure debug level is set.
        """
        self.log.debug(self.location(logging_string), exc_info=True)

    def info(self, logging_string):
        """
        Provide logs for Info states, ensure debug level is set.
        """
        self.log.info(self.location(logging_string))

    def warning(self, logging_string):
        """
         Provide logs for warning states, ensure debug level is set.
        """
        self.log.warning(self.location(logging_string), exc_info=True)

    def error(self, logging_string):
        """
            Provide logs for Error states, ensure debug level is set.
        """
        self.log.error(self.location(logging_string), exc_info=True)

        raise Exception(self.location(logging_string))

    def critical(self, logging_string):
        """
            Provide logs for critical states, ensure debug level is set.
        """

        self.log.critical(self.location(logging_string), exc_info=True)

    @staticmethod
    def __log_file(logger_id):
        """
        logger_id: flow_id to create dedicated log file
        """
        return BASE_DIR + '/logs/' + str(logger_id) + ".log"

    def get_logger(self, logger_id):
        logfile_path = self.__log_file(logger_id)

        try:
            for handler in logging.root.handlers[:]:
                logging.root.removeHandler(handler)

            if os.getenv("LOG_LEVEL") and os.getenv("LOG_LEVEL") in Log_levels:
                LEVEL = Log_levels[os.getenv("LOG_LEVEL")]
            else:
                LEVEL = Log_levels['INFO']

            # Configure colorlog handler for console output
            stream_handler = colorlog.StreamHandler()
            stream_handler.setFormatter(colorlog.ColoredFormatter(
                '%(log_color)s%(asctime)s - %(levelname)s - %(message)s%(reset)s',
                # Customize format to colorize the entire log message
                log_colors={
                    'DEBUG': 'cyan',
                    'INFO': 'blue',  # Change INFO log level color to blue
                    'WARNING': 'yellow',
                    'ERROR': 'red',
                    'CRITICAL': 'bold_red,bg_white',
                }
            ))

            # Set the log level and handler for the logger
            logging.basicConfig(level=LEVEL, format='%(asctime)s - %(levelname)s - %(message)s',
                                handlers=[logging.FileHandler(logfile_path), stream_handler]
                                )

            _logger = logging.getLogger(f"{logger_id}_logs")

            return _logger

        except OSError as err:
            print("OS error: {0}".format(err))


def logger():
    return Logger(os.getenv("MODEL_ID"))
