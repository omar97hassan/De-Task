import logging

def log(exception_string: str, tags: list[str]):
    logging.basicConfig(filename="Decorator_Task.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info("exception_string: "+ str(exception_string)+", Tags: "+str(tags))


def internal_exception_logger(tags: list[str]):
    def decorator_orginal_function_wrapper(original_function):
        try:
            original_function()
        except Exception as e:
            log(e, tags)

    return decorator_orginal_function_wrapper


@internal_exception_logger(['tag_1', 'tag_2'])
def test_call():
    raise Exception('This is an exception')
