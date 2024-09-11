import unittest
from decouple import config
import requests

SERVER = "server_b"
API_KEY = config('SECRET_KEY')

URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

response = requests.get(URL)
available = False
if response.status_code == 200:
    data = response.json()
    print(data)
    available = True
else:
    print(f'Error {response.status_code}: {response.text}')

class AllAssertsTest(unittest.TestCase):
    
    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertTrue(True)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no soy un número")

    def test_assert_in(self):
        self.assertIn(10, [2, 4, 5, 10])
        self.assertNotIn(5, [2, 4, 10])

    def test_assert_dicts(self):
        user = {"name": "jesus", "last_name": "vergara"}
        self.assertDictEqual(
            {"name": "jesus", "last_name": "vergara"},
            user
        )
        self.assertSetEqual(
            {1, 2, 3},
            {1, 2, 3}
        )

    @unittest.skip("Trabajo en progreso, se habilitará nuevamente!")
    def test_skip(self):
        self.assertEqual("hola", "chao")

    @unittest.skipIf(SERVER == "server_b", "Saltado porque no estamos en el servidor a")
    def test_skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100, 150)

    @unittest.skipUnless(available, "La API no está disponible para pruebas")
    def test_api_response(self):
        self.assertTrue(available, "La API debería estar disponible")
        if available:
            print("La API está disponible.")
