import random
import number_theory_functions as ntf


class RSA:
    def __init__(self, public_key, private_key=None):
        self.public_key = public_key
        self.private_key = private_key

    @staticmethod
    def generate(digits=10):
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """

        p = ntf.generate_prime(digits/2)
        q = ntf.generate_prime(digits/2)
        N = p*q
        while p == q or len(str(N)) != digits:
            p = ntf.generate_prime(digits / 2)
            q = ntf.generate_prime(digits / 2)

        k = (p-1)*(q-1)

        def f(n):
            return [j/n for j in range(n*n) if ntf.extended_gcd(j/n, n)[0] == 1]
        u_k = f(k)
        e = random.choice(u_k)
        d = ntf.modular_inverse(e, k)

        public_key = (N, e)
        private_key = (N, d)
        return RSA(public_key=public_key, private_key=private_key)

    def encrypt(self, m):
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        return ntf.modular_exponent(m, self.public_key[1], self.public_key[0])

    def decrypt(self, c):
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
       """
        return ntf.modular_exponent(c, self.private_key[1], self.private_key[0])
