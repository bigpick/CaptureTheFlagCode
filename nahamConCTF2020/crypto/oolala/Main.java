import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        BigInteger p = new BigInteger("1830213987675567884451892843232991595746198390911664175679946063194531096037459873211879206428207");
        BigInteger q = new BigInteger("1830213987675567884451892843232991595746198390911664175679946063194531096037459873211879206428213");
        BigInteger e = new BigInteger("65537");
        BigInteger ct = new BigInteger("87760575554266991015431110922576261532159376718765701749513766666239189012106797683148334771446801021047078003121816710825033894805743112580942399985961509685534309879621205633997976721084983");

        BigInteger phi = (p.subtract(new BigInteger("1"))).multiply(q.subtract(new BigInteger("1")));
        BigInteger modulus = p.multiply(q);
        BigInteger privateKey = e.modInverse(phi);

        System.out.println("modulus = "+modulus);
        System.out.println("phi = "+phi);
        System.out.println("d = "+privateKey);

        BigInteger pt = ct.modPow(privateKey, modulus);
        System.out.println("Pt: " + pt);

        String ptHex = pt.toString(16);
        // https://stackoverflow.com/a/4785776/13158274
        StringBuilder output = new StringBuilder();
        for (int i = 0; i < ptHex.length(); i+=2) {
            String str = ptHex.substring(i, i+2);
            output.append((char)Integer.parseInt(str, 16));
        }
        System.out.println(output);
    }
}
