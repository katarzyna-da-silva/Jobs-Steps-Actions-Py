import sys
import unittest  # Dodaj tę linię
sys.path.append("..")

from colors import colorize_text, Colors

class TestColorizeText(unittest.TestCase):
    def test_colorize_text_bold_green(self):
        result = colorize_text("Je serai un devOps bientot ou pas!", f"{Colors.BOLD}{Colors.GREEN}")
        expected = f"{Colors.BOLD}{Colors.GREEN}Je serai un devOps bientot ou pas!{Colors.RESET}"
        self.assertEqual(result, expected)

    # Dodaj więcej testów w razie potrzeby

if __name__ == '__main__':
    unittest.main()
