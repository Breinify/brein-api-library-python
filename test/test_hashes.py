import unittest
import breinify

class TestHashFunctions(unittest.TestCase):
    def test_sign_activity(self):
        toPush = {"unixTimestamp": 1451962516, "activity": {"type": "search"}}
        breinify.Breinify("abcd", "5e9xqoesiygkuzddxjlkaq==")._Breinify__signActivity(toPush)
        self.assertEqual("rsXU0ozhfzieNLA2jQs2h2e4sz2+qHGxbgSYyfWr5EM=", toPush["signature"])

    def test_sign_lookup(self):
        toPush = {"unixTimestamp": 1451962516, "lookup": {
            "dimensions": [
                "firstname",
                "gender",
                "age",
                "agegroup",
                "digitalfootprint",
                "images"
            ]
        }}
        breinify.Breinify("abcd", "5e9xqoesiygkuzddxjlkaq==")._Breinify__signLookup(toPush)
        self.assertEqual("o/LBuRFrlbZDG9OLdZRrYC2ERYqwIxdv4Dloj/GCeLQ=", toPush["signature"])

    def test_sign_temporal(self):
        toPush = {"unixTimestamp": 1451962516}
        breinify.Breinify("abcd", "5e9xqoesiygkuzddxjlkaq==")._Breinify__signTemporal(toPush)
        self.assertEqual("slh36zSa0drIQY6k5MdhhRd/y8nly0jl7gGlVmhVWE8=", toPush["signature"])

if __name__ == '__main__':
    unittest.main()
