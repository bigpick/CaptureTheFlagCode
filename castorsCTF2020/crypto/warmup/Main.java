import java.math.BigInteger;

public class Main {
    /*
     * Method to do sqrt on a BigInteger.
     * Credit: https://stackoverflow.com/a/16804098/13158274
     */
    public static BigInteger sqrt(BigInteger x) {
        BigInteger div = BigInteger.ZERO.setBit(x.bitLength()/2);
        BigInteger div2 = div;
        for(;;) {
            BigInteger y = div.add(x.divide(div)).shiftRight(1);
            if (y.equals(div) || y.equals(div2))
                return y;
            div2 = div;
            div = y;
        }
    }

    public static void main(String[] args) {
        java.math.BigInteger c_squared = new java.math.BigInteger("41027546415588921135190519817388916847442693284567375482282571314638757544938653824671437300971782426302443281077457253827782026089649732942648771306702020");
        java.math.BigInteger A = new java.math.BigInteger("1780602199528179468577178612383888301611753776788787799581979768613992169436352468580888042155360498830144442282937213247708372597613226926855391934953064");
        java.math.BigInteger e = new java.math.BigInteger("65537");
        java.math.BigInteger ct = new java.math.BigInteger("825531027337680366509171870396193970230179478931882005355846498785843598000659828635030935743236266080589740863128695174980645084614454653557872620514117");
        java.math.BigInteger sixteen = new java.math.BigInteger("16");

        // Calculate a, by using a^4−c^2*a^2+4*(A^2) = 0
        java.math.BigInteger  a = sqrt(c_squared.add( sqrt((c_squared.pow(2)).subtract(sixteen.multiply(A.pow(2))))).divide(new BigInteger("2")) );
        System.out.println("a = "+a);

        // Calculate b from a^2 + b^2 = c^2 (since we now know c and a)
        java.math.BigInteger b = sqrt(c_squared.subtract(a.pow(2)));
        System.out.println("b = "+b);

        // Calculate p, since:
        //   a = p + q            (1)
        //   b = p - q            (2)
        //  so
        //   q = a - p            (1 re-arranged, 3)
        //   b = p - (a - p)      (plugging 3 into 2 for q, 4)
        //     b = p - a + p
        //     b = 2p -a
        //     a+b = 2p
        //     (a+b)/2 = p
        java.math.BigInteger p = (b.add(a)).divide(new BigInteger("2"));
        System.out.println("p = "+p);
        // And then calculate q since we know a and p, and a=p+q so q=a-p
        java.math.BigInteger q = (a.subtract(p));
        System.out.println("q = "+q);

        // Sanity check, based on what they gave us in the chall.txt values:
        System.out.println(p.add(q).equals(a));
        System.out.println(p.subtract(q).equals(b));

        // Now just doing normal RSA stuff now that we have all values, first we find phi
        BigInteger phi = (p.subtract(new BigInteger("1"))).multiply(q.subtract(new BigInteger("1")));
        // Then we need to find the modulus (usually referred to as N)
        BigInteger modulus = p.multiply(q);
        // Then we can find the private key (d, usually)
        BigInteger privateKey = e.modInverse(phi);
        // Value dump
        System.out.println("modulus = "+modulus);
        System.out.println("phi = "+phi);
        System.out.println("d = "+privateKey);
        // Now we just find our plaintext since we got the private key:
        System.out.println("plaintext = "+ct.modPow(privateKey, modulus));
        // Convert the decimal number to hex, and then the hex to ascii
        //  --> castorsCTF{n0th1ng_l1k3_pr1m3_numb3r5_t0_w4rm_up_7h3_3ng1n3s}
    }
}
