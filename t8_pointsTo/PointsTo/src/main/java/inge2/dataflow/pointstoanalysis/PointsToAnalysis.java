package inge2.dataflow.pointstoanalysis;

import soot.Unit;
import soot.toolkits.graph.UnitGraph;
import soot.toolkits.scalar.ForwardFlowAnalysis;

import java.util.HashSet;
import java.util.Set;

public class PointsToAnalysis extends ForwardFlowAnalysis<Unit, PointsToGraph> {

    private PointsToGraph lastPointsToGraph;

    public PointsToAnalysis(UnitGraph graph) {
        super(graph);
        doAnalysis();
    }

    public PointsToGraph getLastPointsToGraph() {
        return lastPointsToGraph;
    }

    /**
     * This method is called for each unit in the control flow graph.
     * @param in the input flow
     * @param unit the current node
     * @param out the returned flow
     */
    @Override
    protected void flowThrough(PointsToGraph in, Unit unit, PointsToGraph out) {
        out.copy(in);

        PointsToVisitor visitor = new PointsToVisitor(out);
        unit.apply(visitor);

        this.lastPointsToGraph = out;
    }

    @Override
    protected PointsToGraph newInitialFlow() {
        return new PointsToGraph();
    }

    /**
     * This method merges the two input flows into a single output flow.
     * @param input1 the first input flow
     * @param input2 the second input flow
     * @param output the returned flow
     */
    @Override
    protected void merge(PointsToGraph input1, PointsToGraph input2, PointsToGraph output) {
        output.copy(input1);
        output.union(input2);
    }

    @Override
    protected void copy(PointsToGraph source, PointsToGraph dest) {
        dest.copy(source);
    }

    /**
     * Este método retorna true si alguno de los objetos apuntados por leftVariableName y rightVariableName coinciden.
     * @param leftVariableName
     * @param rightVariableName
     * @return
     */
    public boolean mayAlias(String leftVariableName, String rightVariableName) {
        // Obtenemos los nodos de ambas variables, con que un lado contenga un nodo del otro, ya hay aliasing
        Set<String> leftNodes = lastPointsToGraph.getNodesForVariable(leftVariableName);
        Set<String> rightNodes = lastPointsToGraph.getNodesForVariable(rightVariableName);
        for (String leftNode : leftNodes) {
            if (rightNodes.contains(leftNode)) {
                return true;
            }
        }
        return false;
    }

    /**
     * Este método retorna true si alguno de los objetos apuntados por leftVariableName.fieldName y rightVariableName coinciden.
     * @param leftVariableName
     * @param fieldName
     * @param rightVariableName
     * @return
     */
    public boolean mayAlias(String leftVariableName, String fieldName, String rightVariableName) {
        // Primero debemos obtener los nodos apuntados por el campo fieldName de la variable leftVariableName, luego pedimos los nodos del lado derecho. Al igual que el caso anterior, con que un lado contenga un nodo del otro, tenemos aliasing
        Set<String> reachableByLeftVariable = new HashSet<>();
        for (String leftNode : lastPointsToGraph.getNodesForVariable(leftVariableName)) {
            reachableByLeftVariable.addAll(lastPointsToGraph.getReachableNodesByField(leftNode, fieldName));
        }
        Set<String> rightNodes = lastPointsToGraph.getNodesForVariable(rightVariableName);
        for (String leftNode : reachableByLeftVariable) {
            if (rightNodes.contains(leftNode)) {
                return true;
            }
        }
        return false;
    }
}
