import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;
import java.io.*;

class Connected  {
    private ArrayList<Vertex> vertices = new ArrayList<Vertex>();
    private int nedges;
    private int nvertices;
    public static int timer=0;
    private ArrayList<HashSet<Integer>> cycles = new ArrayList<>();
    ArrayList<Integer> stack = new ArrayList<>();

    public Connected(){}


    private void addEdge(Vertex v, int dest) {
        v.adjList.add(dest);
    }


    public ArrayList<HashSet<Integer>> getCycles(){
        for(Vertex v: vertices){
            boolean found = false;
            for(HashSet<Integer> cycl : cycles){
                if(cycl.contains(v.key)) found = true;

            }
            if(!found) {
                HashSet<Integer> c = new HashSet<>();
                c.add(v.key);
                addCycle(c);
            }
        }
        return cycles;
    }

    public int getVertexIndex(int key){
        for ( Vertex v : vertices){
            if (v.key == key)
                return vertices.indexOf(v);
        }
        return -1;
    }


    void get_graph_details(String filename) {
        int num = 0;
        try {
            BufferedReader reader = new BufferedReader(new FileReader(filename));
            String line = reader.readLine();
            while(line != null){
                String[] l = line.split(", ");
                Vertex v = new Vertex(Integer.parseInt(l[0]));
                Vertex w = new Vertex(Integer.parseInt(l[1]));
                if(getVertexIndex(Integer.parseInt(l[0])) == -1){
                    vertices.add(v);
                }
                if(getVertexIndex(Integer.parseInt(l[1])) == -1){
                    vertices.add(w);
                }
                num += 1;
                line = reader.readLine();
            }
        } catch (Exception e){
            System.out.println("Error: " + e);
        }
        nvertices=vertices.size();
        nedges = num;
    }

    void createAdjList(String filename) {
        try {
            BufferedReader reader = new BufferedReader(new FileReader(filename));
            String line = reader.readLine();

            while (line != null) {
                String[] l = line.split(", ");
                int v = Integer.parseInt(l[0]);
                int index = getVertexIndex(v);
                int w = Integer.parseInt(l[1]);
                addEdge(vertices.get(index),w);
                line = reader.readLine();
            }
            sortAdjLists();
        } catch (Exception e) {
            System.out.println(e);
        }
    }


    private void sortAdjLists(){
        for(Vertex v : vertices){
            Collections.sort(v.adjList);
        }
    }

     void DFS(){
        for(Vertex v: vertices){
            if(!v.visited) {
                explore(v);
            }

        }
    }

    void explore(Vertex v){
        v.visited=true;
        previsit(v);
        stack.add(0, v.key);
        ArrayList<Integer> adjs = v.getAdjList();
        for(int key : adjs){
            if(!vertices.get(getVertexIndex(key)).visited){
                explore(vertices.get(getVertexIndex(key)));
            }
            else{
                Vertex w = vertices.get(getVertexIndex(key));
                if((v.pre > w.pre) && ((w.post == 0)) | (w.post < v.post)){
                        //Backedge!
                    getCycle(v.key, key);
                        //Here is where the stack should print the path of the cycle?
                    }
                }
        }
        postvisit(v);
        stack.remove(Integer.valueOf(v.key));
    }

     private void getCycle(int v1, int v2){
        HashSet<Integer> cycle = new HashSet<>();
        boolean in = false;
        for(int v : stack){
            if(v == v1){
                cycle.add(v);
                in = true;
            }
            if((in) && (v != v2)){
                cycle.add(v);
            }
            if((in) && (v== v2)){
                cycle.add(v);
                break;
            }
        }
        addCycle(cycle);
    }

    private void addCycle(HashSet<Integer> cycle){
        //check if this cycle has any same elements in cycles
        for(Integer v : cycle){
            for(int i = 0; i < cycles.size();i++){
                ArrayList<Integer> exisitingCycle = new ArrayList<>(cycles.get(i));
                if(exisitingCycle.contains(v)){
                    cycles.get(i).addAll(cycle);
                    return;
                }
            }
        }

        int cFirst = cycle.iterator().next();
        for(int i = 0; i < cycles.size(); i++){
            HashSet<Integer> c = cycles.get(i);
            ArrayList<Integer> cyc = new ArrayList<>(c);

            int first = c.iterator().next();
            if(cFirst < first){
                cycles.add(i, cycle);
                return;
            }
        }
        cycles.add(cycles.size(), cycle);

    }


    static private void previsit(Vertex v)	{
        v.pre = timer;
        timer++;
    }

    static private void postvisit(Vertex v)	{
        v.post = timer;
        timer++;
    }

    public void printCycles(){
        System.out.println(cycles.size() + " Strongly Connected Component(s):");
        for(HashSet<Integer> c : cycles){
            Iterator<Integer> iterator = c.iterator();
            String SCC = "" + iterator.next();
            while(iterator.hasNext()){
                SCC += ", " + iterator.next();
            }
            System.out.println(SCC);
        }
    }


    class Vertex implements Comparable<Vertex> {
        int key;
        boolean visited = false;
        int pre = 0;
        int post = 0;
        ArrayList<Integer> adjList = new ArrayList<>();

        public Vertex(int tkey){
            key = tkey;
        }
        public int getKey(){ return this.key; }

        public boolean getVisited(){ return this.visited; }

        public int getPre(){ return this.pre; }

        public int getPost(){ return this.post; }

        public ArrayList<Integer> getAdjList() { return this.adjList; }

        @Override
        public int compareTo(Vertex o) {
            if(this.key == o.getKey()) return 0;
            return o.key < this.key ? -1 : 1;
            }

        public boolean equals(Vertex obj){
            return (obj.key == (this.key));
        }

        @Override
        public String toString(){
            return ("key: " + getKey() + "\nvisited: " + getVisited() + "\npre: "
                    + getPre() + "\npost: " + getPost() + "\nadjList: "
                    + getAdjList().toString());
        }

    }

}