import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        BigInteger modulus = new BigInteger("7735208939848985079680614633581782274371148157293352904905313315409418467322726702848189532721490121708517697848255948254656192793679424796954743649810878292688507385952920229483776389922650388739975072587660866986603080986980359219525111589659191172937047869008331982383695605801970189336227832715706317");
        BigInteger e = new BigInteger("65537");
        BigInteger ct = new BigInteger("5300731709583714451062905238531972160518525080858095184581839366680022995297863013911612079520115435945472004626222058696229239285358638047675780769773922795279074074633888720787195549544835291528116093909456225670152733191556650639553906195856979794273349598903501654956482056938935258794217285615471681");
        List<BigInteger> list = new ArrayList<BigInteger>();

        BigInteger prime0 = new BigInteger("2208664111"); list.add(prime0);
        BigInteger prime1 = new BigInteger("2214452749"); list.add(prime1);
        BigInteger prime2 = new BigInteger("2259012491"); list.add(prime2);
        BigInteger prime3 = new BigInteger("2265830453"); list.add(prime3);
        BigInteger prime4 = new BigInteger("2372942981"); list.add(prime4);
        BigInteger prime5 = new BigInteger("2393757139"); list.add(prime5);
        BigInteger prime6 = new BigInteger("2465499073"); list.add(prime6);
        BigInteger prime7 = new BigInteger("2508863309"); list.add(prime7);
        BigInteger prime8 = new BigInteger("2543358889"); list.add(prime8);
        BigInteger prime9 = new BigInteger("2589229021"); list.add(prime9);
        BigInteger prime10 = new BigInteger("2642723827"); list.add(prime10);
        BigInteger prime11 = new BigInteger("2758626487"); list.add(prime11);
        BigInteger prime12 = new BigInteger("2850808189"); list.add(prime12);
        BigInteger prime13 = new BigInteger("2947867051"); list.add(prime13);
        BigInteger prime14 = new BigInteger("2982067987"); list.add(prime14);
        BigInteger prime15 = new BigInteger("3130932919"); list.add(prime15);
        BigInteger prime16 = new BigInteger("3290718047"); list.add(prime16);
        BigInteger prime17 = new BigInteger("3510442297"); list.add(prime17);
        BigInteger prime18 = new BigInteger("3600488797"); list.add(prime18);
        BigInteger prime19 = new BigInteger("3644712913"); list.add(prime19);
        BigInteger prime20 = new BigInteger("3650456981"); list.add(prime20);
        BigInteger prime21 = new BigInteger("3726115171"); list.add(prime21);
        BigInteger prime22 = new BigInteger("3750978137"); list.add(prime22);
        BigInteger prime23 = new BigInteger("3789130951"); list.add(prime23);
        BigInteger prime24 = new BigInteger("3810149963"); list.add(prime24);
        BigInteger prime25 = new BigInteger("3979951739"); list.add(prime25);
        BigInteger prime26 = new BigInteger("4033877203"); list.add(prime26);
        BigInteger prime27 = new BigInteger("4128271747"); list.add(prime27);
        BigInteger prime28 = new BigInteger("4162800959"); list.add(prime28);
        BigInteger prime29 = new BigInteger("4205130337"); list.add(prime29);
        BigInteger prime30 = new BigInteger("4221911101"); list.add(prime30);
        BigInteger prime31 = new BigInteger("4268160257"); list.add(prime31);


        BigInteger phi = new BigInteger("1");
        for (int i=0; i<list.size(); i++){
            phi = phi.multiply((list.get(i).subtract(BigInteger.ONE)));
        }
        System.out.println(phi);

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
