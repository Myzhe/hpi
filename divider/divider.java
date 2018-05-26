class divider {
    public static void main(String []args) {
        int zaehler = 1;
        int zahl = 5;
        while (zaehler <= 2000000) {
            zahl++;
            int counter = 0;
            inner: for (int aktuell = 1; aktuell <= (int) Math.sqrt(zahl); aktuell++) {
                if (zahl%aktuell == 0) {
                    counter++;
                    if (counter > 2 || Math.sqrt(zahl)%1 == 0) {
                        break inner;
                    }
                }
            }
            if (counter == 2) {
                System.out.println(zaehler + ": " + zahl);
                zaehler++;
            }
        
        }
        System.out.println(zahl);
    }
}