public class Driver {
    public static void main(String[] args){
        LCS lcs = new LCS();
        lcs.readFile(args[0]);
        int score = lcs.fillInTable();
        lcs.retrace();
        System.out.println("Score: " + score);
    }
}
