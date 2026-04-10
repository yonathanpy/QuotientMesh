import traceback
import logging


class FaultBoundary:
    def __init__(self):
        self._errors = []
        logging.basicConfig(level=logging.INFO)

    def capture(self, context: str, fn, *args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            err = {
                "context": context,
                "error": str(e),
                "trace": traceback.format_exc()
            }
            self._errors.append(err)
            logging.error(f"[fault] {context}: {e}")
            return None

    def history(self):
        return list(self._errors)
