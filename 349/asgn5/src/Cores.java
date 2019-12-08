import java.util.*;
import java.io.*;

class Cores  {
    private ArrayList<Vertex> vertices = new ArrayList<>();
    private int nedges;
    private int nvertices;
    public static int timer=0;
    private ArrayList<HashSet<Integer>> cycles = new ArrayList<>();
    ArrayList<Integer> stack = new ArrayList<>();
    private int core = 1;
    private ArrayList<ArrayList<Integer>> coreCycles = new ArrayList<>();

    public Cores(){
        coreCycles.add(0, new ArrayList<>());
        coreCycles.add(1, new ArrayList<>());
    }


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

    public int getVertex(int key){
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
                int v = Integer.parseInt(l[0]);
                int w = Integer.parseInt(l[1]);
                if(getVertex(v) == -1){
                    Vertex vertex = new Vertex(Integer.parseInt(l[0]));
                    vertex.degree+=1;
                    vertex.adjList.add(w);
                    vertices.add(vertex);

                }
                else{
                    int i = getVertex(v);
                    vertices.get(i).degree+=1;
                    vertices.get(i).adjList.add(w);
                }

                if(getVertex(w) == -1){
                    Vertex vertex = new Vertex(Integer.parseInt(l[1]));
                    vertex.degree+=1;
                    vertex.adjList.add(v);
                    vertices.add(vertex);
                }
                else{
                    int i = getVertex(w);
                    vertices.get(i).degree+=1;
                    vertices.get(i).adjList.add(v);
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
                int index = getVertex(v);
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
            if(!vertices.get(getVertex(key)).visited){
                explore(vertices.get(getVertex(key)));
            }
            else{
                Vertex w = vertices.get(getVertex(key));
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
        //found a cycle
        //get max common degree of all vertices
        //add to list of that core#
        findMinDegree(cycle);
        addCycle(cycle);
    }

    private void findMinDegree(HashSet<Integer> cycle){
        int min = 1000000000;
        //is it a real cycle??
        if(cycle.size() == 2)
            return;
        for(int v : cycle){
            if(vertices.get(getVertex(v)).degree < min)
                min=vertices.get(getVertex(v)).degree;
        }
        addCycletoCores(cycle, min);

    }

    private void addCycletoCores(HashSet<Integer> cycle, int core){
        //does add all add duplicates?
        ArrayList<Integer> curCore;
        if(coreCycles.size() < core+1) {
            coreCycles.add(core, new ArrayList<>());
        }
        curCore = coreCycles.get(core);
        Iterator<Integer> iterator = cycle.iterator();
        int v = iterator.next();
        if(!curCore.contains(v)){
            curCore.add(v);
        }
        while(iterator.hasNext()){
            int w = iterator.next();
            if(!curCore.contains(w)){
                curCore.add(w);
            }
        }
        Collections.sort(curCore);
        coreCycles.set(core, curCore);
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
        String printCore = "";
        coreCycles.set(1, new ArrayList<>(cycles.get(0)));
        for(int i=1; i < coreCycles.size(); i++){
            printCore="";
            ArrayList<Integer> c = coreCycles.get(i);
            for(int j : c){
                 printCore += j + ", ";
            }

            System.out.println("Vertices in " + i + "-cores:");
            System.out.println(printCore.substring(0, printCore.length()-2));

        }
    }


    class Vertex implements Comparable<Vertex> {
        int key;
        boolean visited = false;
        int pre = 0;
        int post = 0;
        int degree = 0;
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
            return ("key: " + getKey() + "\nvisited: " + getVisited() + "\ndegree: " + this.degree + "\npre: "
                    + getPre() + "\npost: " + getPost() + "\nadjList: "
                    + getAdjList().toString());
        }

    }

}