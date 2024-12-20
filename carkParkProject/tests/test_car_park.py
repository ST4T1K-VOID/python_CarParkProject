import unittest
from carpark import CarPark

class TestCarPark(unittest.TestCase):
      def setUp(self):
         self.car_park = CarPark("123 Example Street", 100)

      def test_car_park_initialized_with_all_attributes(self):
         self.assertIsInstance(self.car_park, CarPark)
         self.assertEqual(self.car_park.location, "123 Example Street")
         self.assertEqual(self.car_park.capacity, 100)
         self.assertEqual(self.car_park.plates, [])
         self.assertEqual(self.car_park.sensors, [])
         self.assertEqual(self.car_park.displays, [])
         self.assertEqual(self.car_park.available_bays, 100)

      def test_add_car(self):
         self.car_park.add_car("PL8-000001")
         self.assertEqual(self.car_park.plates, ["PL8-000001"])
         self.assertEqual(self.car_park.available_bays, 99)

      def test_remove_car(self):
         self.car_park.add_car("PL8-000001")
         self.car_park.remove_car("PL8-000001")
         self.assertEqual(self.car_park.plates, [])
         self.assertEqual(self.car_park.available_bays, 100)

      def test_overfill_the_car_park(self):
         for i in range(100):
            self.car_park.add_car(f"PL8-000001-{i}")
         self.assertEqual(self.car_park.available_bays, 0)
         self.car_park.add_car("PL8-000001")
         # Overfilling the car park should not change the number of available bays
         self.assertEqual(self.car_park.available_bays, 0)

         # Removing a car from an overfilled car park should not change the number of available bays
         self.car_park.remove_car("PL8-000001")
         self.assertEqual(self.car_park.available_bays, 0)

      def test_removing_a_car_that_does_not_exist(self):
         with self.assertRaises(KeyError):
            self.car_park.remove_car("NO-1")

      def test_register_raises_type_error(self):
         with self.assertRaises(TypeError):
            self.car_park.register("Probably not what you wanted")

if __name__ == "__main__":
   unittest.main()