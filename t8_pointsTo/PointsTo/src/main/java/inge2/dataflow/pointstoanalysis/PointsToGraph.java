package inge2.dataflow.pointstoanalysis;

import soot.Unit;
import soot.jimple.AssignStmt;
import soot.tagkit.LineNumberTag;

import java.util.*;

public class PointsToGraph {

    /**
     * Nodos del grafo.
     *
     * Cada nodo representa todos los objetos creados por cada sentencia "new".
     * Es decir, tenemos un nodo por cada "new" en el programa.
     */
    public Set<String> nodes;

    /**
     * Ejes del grafo.
     *
     * Un eje (n1, f, n2) indica que el los objetos representados por el nodo n1 tienen un campo f que apunta al/los
     * objetos representados por n2.
     */
    public Set<Axis> axis;

    /**
     * Mapping de variables locales a nodos.
     * Representa el conjunto de objetos a los que puede apuntar una variable local.
     */
    public Map<String, Set<String>> mapping;

    public PointsToGraph(){
        nodes = new HashSet<>();
        axis = new HashSet<>();
        mapping = new HashMap<>();
    }

    public void clear() {
        nodes.clear();
        axis.clear();
        mapping.clear();
    }

    /**
     * Devuelve el nombre del nodo correspondiente a la sentencia <code>stmt</code>.
     * @param stmt
     * @return
     */
    public String getNodeName(AssignStmt stmt) {
        LineNumberTag lineNumberTag = (LineNumberTag) stmt.getTag("LineNumberTag");
        return String.valueOf(lineNumberTag.getLineNumber());
    }

    /**
     * Devuelve el conjunto de nodos a los que apunta la variable <code>variableName</code>.
     * @param variableName
     * @return
     */
    public Set<String> getNodesForVariable(String variableName) {
        // Obtenemos los nodos apuntados por la variable pasada por parametro
        return mapping.get(variableName);
    }

    /**
     * Setea el conjunto de nodos a los que apunta la variable <code>variableName</code>.
     * @param variableName
     * @param nodes
     */
    public void setNodesForVariable(String variableName, Set<String> nodes) {
        // Agregamos los nuevos nodos y lo asociamos a la variable pasada por parametro
        this.nodes.addAll(nodes);
        mapping.put(variableName, nodes);
    }

    /**
     * Agrega un eje al grafo.
     * @param leftNode
     * @param fieldName
     * @param rightNode
     */
    public void addEdge(String leftNode, String fieldName, String rightNode) {
        // Agregamos un eje por los nodos pasados por parametro
        axis.add(new Axis(leftNode, fieldName, rightNode));
    }

    /**
     * Devuelve el conjunto de nodos alcanzables desde el nodo <code>node</code> por el campo <code>fieldName</code>.
     * @param node
     * @param fieldName
     * @return
     */
    public Set<String> getReachableNodesByField(String node, String fieldName) {
        // Los nodos a los que se puede llegar son aquellos para los existe un eje, devolvemos ese conjunto
        Set<String> result = new HashSet<>();
        for (Axis a : axis) {
            if (a.leftNode.equals(node) && a.fieldName.equals(fieldName)) {
                result.add(a.rightNode);
            }
        }
        return result;
    }

    /**
     * Copia de un grafo (modifica el this).
     * @param in
     */
    public void copy(PointsToGraph in) {
        this.clear();
        in.putAll(this);
    }

    /**
     * Union de dos grafos (modifica el this).
     * this = this U in
     * @param in el grafo a unir
     */
    public void union(PointsToGraph in) {
        // Agregamos ejes, mappings y nodos sin eliminar los ya existentes
        this.axis.addAll(in.axis);
        for (String variableName : in.mapping.keySet()) {
            Set<String> nodes = this.mapping.get(variableName);
            if (nodes == null) {
                nodes = new HashSet<>();
                this.mapping.put(variableName, nodes);
            }
            nodes.addAll(in.mapping.get(variableName));
        }
        this.nodes.addAll(in.nodes);
    }

    /**
     * Metodo privado para agregar toda la información de este grafo al grafo dst.
     * @param dst el grafo destino.
     */
    private void putAll(PointsToGraph dst) {
        // Reutilizamos union
        dst.union(this);
    }
}
