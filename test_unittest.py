from unittest import TestCase, main

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

class Testes(TestCase):
    def test_some(self):
        self.assertEqual(soma(5, 5), 10)

if __name__ == '__main__':
    main()
