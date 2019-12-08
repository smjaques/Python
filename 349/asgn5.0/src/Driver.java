import java.util.ArrayList;
import java.util.HashSet;
import java.io.FileNotFoundException;

public class Driver {
    public static void main(String[] args) throws FileNotFoundException {
        Cores test1 = new Cores();
        test1.get_graph_details(args[0]);
        test1.createAdjList(args[0]);
        test1.degreeVertexList();
        test1.getKCore();
        test1.printCores();
    }
}