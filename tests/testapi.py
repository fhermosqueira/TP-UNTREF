import requests
import unittest

class Test_PokeApi(unittest.TestCase):

    def setUp(self) -> None:
        self.pokeurl = 'https://pokeapi.co/api/v2/'
        
    def test_case_one(self):
        pokeget = requests.get(self.pokeurl+'berry/1')
        pokedata = pokeget.json()
        self.assertEqual(pokedata['size'], 20)
        self.assertEqual(pokedata['soil_dryness'], 15)
        self.assertEqual(pokedata['firmness']['name'], 'soft')
        
    def test_case_two(self):
        pokeget = requests.get(self.pokeurl+'berry/2')
        pokedata = pokeget.json()
        self.assertEqual(pokedata['firmness']['name'], 'super-hard')
        get_berry_1 = requests.get(self.pokeurl+'berry/1')
        data_berry_1 = get_berry_1.json()
        self.assertGreater(pokedata['size'], data_berry_1['size'])
        self.assertEqual(pokedata['soil_dryness'], data_berry_1['soil_dryness'])

    def test_case_three(self):
        pokeget = requests.get(self.pokeurl+'pokemon/pikachu/')
        pokedata = pokeget.json()
        self.assertGreater(pokedata['base_experience'], 10)
        self.assertLess(pokedata['base_experience'], 1000)
        poketype = [t['type']['name'] for t in pokedata['types']]
        self.assertIn('electric', poketype)

    