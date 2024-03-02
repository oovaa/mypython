import string
import unittest


def encrypt(msg, by=1):
    abc = string.ascii_letters + string.punctuation + string.digits + " "
    emsg = "".join(abc[(abc.find(x) + by) % len(abc)] for x in msg)

    return emsg


class TestEn(unittest.TestCase):
    def setUp(self):
        self.msg = "banana"
        self.by = -8

    def test_inputExists(self):
        self.assertIsNotNone(self.msg)

    def test_inputType(self):
        self.assertIsInstance(self.msg, str)

    def test_inputNotEmpty(self):
        self.assertNotEqual(self.msg, "")

    def test_ReturnSomething(self):
        self.assertIsNotNone(encrypt(self.msg))

    def test_inputTypeencrypt(self):
        self.assertIsInstance(encrypt(self.msg), str)

    def test_outputNotEmpty(self):
        self.assertEqual(len(encrypt(self.msg)), len(self.msg))

    def test_diffio(self):
        self.assertNotIn(self.msg, encrypt(self.msg))

    def test_outputType(self):
        self.assertIsInstance(encrypt(self.msg), str)

    def test_ShiftedCipher(self):
        abc = string.ascii_letters + string.punctuation + string.digits + " "
        emsg = "".join(abc[(abc.find(x) + self.by) % len(abc)]
                       for x in self.msg)
        print(emsg)

        self.assertEqual(encrypt(self.msg, self.by), emsg)


if __name__ == "__main__":
    unittest.main()
