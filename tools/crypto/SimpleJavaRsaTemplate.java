import java.math.BigInteger;

public class SimpleJavaRsaTemplate {
    /* SIMPLE JAVA RSA TEMPLATE
     *
     * ASSUMES:
     *   * All your values you're working with are in decimal
     *   * You've already factored your p and q
     *   * You are working with just standard RSA (two primes make up N, e, ct)
     */
    public static void main(String[] args) {
        /* TODO:
         *   Replace these with factors you've gotten from FactorDB/etc...
         */
        BigInteger p = new BigInteger("");
        BigInteger q = new BigInteger("");
        /* TODO:
         *   Replace with your e
         */
        BigInteger e = new BigInteger("");
        /* TODO:
         *   Replace with your ct decimal
         */
        BigInteger ct = new BigInteger("");

        BigInteger phi = (p.subtract(new BigInteger("1"))).multiply(q.subtract(new BigInteger("1")));
        BigInteger modulus = p.multiply(q);
        BigInteger privateKey = e.modInverse(phi);

        System.out.println("modulus = "+modulus);
        System.out.println("phi = "+phi);
        System.out.println("d = "+privateKey);

        BigInteger pt = ct.modPow(privateKey, modulus);
        System.out.println("Pt: " + pt);

        /* TODO:
         *   If you want to convert the resultant biginteger decimal value to
         *   ASCII - uncomment this block.
         */
        /*
        String ptHex = pt.toString(16);
        // https://stackoverflow.com/a/4785776/13158274
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < ptHex.length(); i+=2) {
            String str = ptHex.substring(i, i+2);
            output.append((char)Integer.parseInt(str, 16));
        }
        System.out.println(output);
        */
    }
}
