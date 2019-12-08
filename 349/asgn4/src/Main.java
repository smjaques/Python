import java.util.ArrayList;
import java.util.HashSet;
import java.io.FileNotFoundException;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        Connected test1 = new Connected();
        test1.get_graph_details(args[0]);
        test1.createAdjList(args[0]);
        test1.DFS();
        test1.getCycles();
        test1.printCycles();
    }
}