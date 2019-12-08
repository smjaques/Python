import java.util.*;
import java.io.*;

class Cores  {
    private ArrayList<Vertex> vertices = new ArrayList<>();
    private int nedges;
    private int nvertices;
    private ArrayList<ArrayList<Integer>> VertsByDegree = new ArrayList<>();
    private ArrayList<ArrayList<Integer>> coreCycles = new ArrayList<>();

    public Cores(){

    }


    private void addEdge(Vertex v, int dest) {
        if(!v.adjList.contains(dest))
            v.adjList.add(dest);
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


    void degreeVertexList(){
        VertsByDegree = new ArrayList<>();
        for(int i = 0 ; i < nedges; i++) {
            VertsByDegree.add(i, new ArrayList<>());
            for (Vertex v : vertices) {
                if(v.degree==i){
                    VertsByDegree.get(i).add(v.key);
                }
            }
        }
    }

    void getKCore(){
        for(int i = 0; i < VertsByDegree.size(); i++){
            ArrayList<Integer> degs = VertsByDegree.get(i);
            while(!degs.isEmpty()){
                int v = degs.remove(0);
                updateNeighbors(v);
                vertices.remove(getVertex(v));
            }
            degreeVertexList();
            addToCoreCycle(i);
        }
    }

    void addToCoreCycle(int k){
        ArrayList<Integer> kthCore = new ArrayList<>();
        for(Vertex vert : vertices) {
            kthCore.add(vert.key);
        }
        Collections.sort(kthCore);
        coreCycles.add(k,kthCore);
    }

    void updateNeighbors(int v){
        Vertex vert = vertices.get(getVertex(v));
        for(int neighbor : vert.adjList){
            vertices.get((getVertex(neighbor))).degree-=1;
            vertices.get((getVertex(neighbor))).adjList.remove(Integer.valueOf(v));
        }
    }


    private void sortAdjLists(){
        for(Vertex v : vertices){
            Collections.sort(v.adjList);
        }
    }

    void printCores(){
        for(int i = 0; i < coreCycles.size(); i++){
            if(coreCycles.get(i).isEmpty())
                continue;
            System.out.println("Vertices in " + (i+1) + "-cores:");
            String verts = "";
            for(int v : coreCycles.get(i)){
                verts+= v + ", ";
            }
            System.out.println(verts.substring(0,verts.length()-2));
        }
    }

    class Vertex implements Comparable<Vertex> {
        int key;
        int degree = 0;
        ArrayList<Integer> adjList = new ArrayList<>();

        public Vertex(int tkey){
            key = tkey;
        }
        public int getKey(){ return this.key; }

        public ArrayList<Integer> getAdjList() { return this.adjList; }

        @Override
        public int compareTo(Vertex o) {
            if(this.key == o.getKey()) return 0;
            return o.key < this.key ? -1 : 1;
        }

        public boolean equalsTo(Vertex obj){
            return (obj.key == (this.key));
        }

        @Override
        public String toString(){
            return ("key: " + getKey()  + "\ndegree: " + this.degree
                    + "\nadjList: " + getAdjList().toString());
        }

    }

}