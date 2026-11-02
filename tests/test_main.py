import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'src'))
from main import severity
class SecurityTests(unittest.TestCase):
 def test_high(self):self.assertEqual(severity(5,4),('high',20))
 def test_reject(self):
  with self.assertRaises(ValueError):severity(0,5)
