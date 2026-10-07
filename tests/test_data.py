import unittest, csv
from pathlib import Path

class TestData(unittest.TestCase):
    def test_amount_is_hours_times_tariff(self):
        csv_file = Path(__file__).resolve().parent.parent / "data" / "records.csv"
        if not csv_file.exists():
            return
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row or row[0].startswith('#'):
                    continue
                hours, tariff, amount = int(row[4]), int(row[5]), int(row[6])
                self.assertEqual(amount, hours * tariff, f"Row {row[0]} amount error")

if __name__ == '__main__':
    unittest.main()
