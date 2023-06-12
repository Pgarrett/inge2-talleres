package inge2.dataflow.pointstoanalysis;

import soot.jimple.*;
import soot.jimple.internal.JInstanceFieldRef;
import soot.jimple.internal.JimpleLocal;

import java.util.HashSet;
import java.util.Set;

public class PointsToVisitor extends AbstractStmtSwitch<Void> {

    private final PointsToGraph pointsToGraph;

    public PointsToVisitor(PointsToGraph pointsToGraph) {
        this.pointsToGraph = pointsToGraph;
    }

    @Override
    public void caseAssignStmt(AssignStmt stmt) {
        boolean isLeftLocal = stmt.getLeftOp() instanceof JimpleLocal;
        boolean isRightLocal = stmt.getRightOp() instanceof JimpleLocal;

        boolean isLeftField = stmt.getLeftOp() instanceof JInstanceFieldRef;
        boolean isRightField = stmt.getRightOp() instanceof JInstanceFieldRef;

        boolean isRightNew = stmt.getRightOp() instanceof AnyNewExpr;

        if (isRightNew) { // x = new A()
            processAssignToNewObject(stmt);
        } else if (isLeftLocal && isRightLocal) { // x = y
            processAssignLocalToLocal(stmt);
        } else if (isLeftField && isRightLocal) { // x.f = y
            processAssignFieldToLocal(stmt);
        } else if (isLeftLocal && isRightField) { // x = y.f
            processAssignLocalToField(stmt);
        }
    }

    private void processAssignToNewObject(AssignStmt stmt) {
        String leftVariableName = stmt.getLeftOp().toString();
        String nodeName = pointsToGraph.getNodeName(stmt);

        Set<String> nodes = new HashSet<>();
        nodes.add(nodeName);

        // Solo debemos agregar el nuevo nodo al grafo
        pointsToGraph.setNodesForVariable(leftVariableName, nodes);
    }

    private void processAssignLocalToLocal(AssignStmt stmt) {
        String leftVariableName = stmt.getLeftOp().toString();
        String rightVariableName = stmt.getRightOp().toString();

        // Al ser una asignacion, pisamos los nodos de leftVariableName con los de rightVariableName
        pointsToGraph.setNodesForVariable(leftVariableName, pointsToGraph.getNodesForVariable(rightVariableName));
    }

    private void processAssignFieldToLocal(AssignStmt stmt) {
        JInstanceFieldRef leftFieldRef = (JInstanceFieldRef) stmt.getLeftOp();
        String leftVariableName = leftFieldRef.getBase().toString();
        String fieldName = leftFieldRef.getField().getName();
        String rightVariableName = stmt.getRightOp().toString();

        // A los ejes existentes del grafo, agregamos el producto cartesiano entre los nodos de leftVariableName.fieldName y rightVariableName
        Set<String> leftVariableNodes = pointsToGraph.getNodesForVariable(leftVariableName);
        Set<String> rightVariableNodes = pointsToGraph.getNodesForVariable(rightVariableName);
        for (String lefVariableNode : leftVariableNodes) {
            for (String rightVariableNode : rightVariableNodes) {
                pointsToGraph.addEdge(lefVariableNode, fieldName, rightVariableNode);
            }
        }
    }

    private void processAssignLocalToField(AssignStmt stmt) {
        String leftVariableName = stmt.getLeftOp().toString();
        JInstanceFieldRef rightFieldRef = (JInstanceFieldRef) stmt.getRightOp();
        String rightVariableName = rightFieldRef.getBase().toString();
        String fieldName = rightFieldRef.getField().getName();

        // El conjunto de nodos de leftVariableName es reemplazado por el conjunto de nodos de la variable rightVariableName apuntados por el campo fieldName
        Set<String> rightVariableNodes = pointsToGraph.getNodesForVariable(rightVariableName);
        Set<String> reachableRightVariableNodes = new HashSet<>();
        for (String rightNode : rightVariableNodes) {
            reachableRightVariableNodes.addAll(pointsToGraph.getReachableNodesByField(rightNode, fieldName));
        }
        pointsToGraph.setNodesForVariable(leftVariableName, reachableRightVariableNodes);
    }
}
