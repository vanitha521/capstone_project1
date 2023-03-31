import logging
logging.basicConfig(filename='hcllog.log',level=logging.DEBUG,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
logging.debug("Hello from debug")
logging.info("hello from info")
logging.warning("hello from warning")
logging.error("hello from error")
logging.critical("hello from critical")