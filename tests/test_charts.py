import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from medflux.charts import (
    save_horizontal_bar_chart,
    save_pie_chart,
    save_vertical_bar_chart,
)


class ChartImageSavingTests(unittest.TestCase):
    def test_horizontal_bar_chart_creation(self):
        with TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "horizontal_chart.png"
            saved_path = save_horizontal_bar_chart(["A", "B", "C"], [10, 20, 30], output_path)
            self.assertEqual(saved_path, output_path)
            self.assertTrue(output_path.exists())
            self.assertGreater(output_path.stat().st_size, 0)

    def test_vertical_bar_chart_creation(self):
        with TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "vertical_chart.png"
            saved_path = save_vertical_bar_chart(["A", "B", "C"], [5, 15, 25], output_path)
            self.assertEqual(saved_path, output_path)
            self.assertTrue(output_path.exists())
            self.assertGreater(output_path.stat().st_size, 0)

    def test_pie_chart_creation(self):
        with TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "pie_chart.png"
            saved_path = save_pie_chart(["A", "B", "C"], [25, 50, 25], output_path)
            self.assertEqual(saved_path, output_path)
            self.assertTrue(output_path.exists())
            self.assertGreater(output_path.stat().st_size, 0)

    def test_invalid_input_raises_value_error(self):
        with self.assertRaises(ValueError):
            save_horizontal_bar_chart(["A", "B"], [1], "/tmp/invalid.png")


if __name__ == "__main__":
    unittest.main()
