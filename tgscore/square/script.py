"""
Example file

python Tribler/Main/dispersy.py --script template
"""

from dispersy.script import ScriptBase

class TestScript(ScriptBase):
    def run(self):
        self.caller(self.test)

    def test(self):
        assert True
