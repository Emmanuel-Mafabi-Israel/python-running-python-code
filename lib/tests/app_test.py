# GLORY BE TO GOD,
# TESTING FILE
# BY ISRAEL MAFABI EMMANUEL

from os import path
import runpy
import io
import sys
import re

class TestAppPy:
    app_path:str = "lib/app.py"
    def test_app_py_exists(self):
        # app.py exists in the lib directory
        assert(path.exists(self.app_path))
    
    def test_app_py_run(self):
        # app.py runs efficiently and as should
        runpy.run_path(self.app_path)

    def test_app_py_prints_message(self):
        output:str = io.StringIO()
        sys.stdout = output
        runpy.run_path(self.app_path)
        sys.stdout = sys.__stdout__

        # let's match the output
        # assert(output.getvalue() == "Hello World!, greetings from Emmanuel!!!\n")
        assert re.match(r"Hello World!, greetings from .+!!!\n", output.getvalue())