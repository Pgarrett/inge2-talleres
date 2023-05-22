package inge2.dataflow.zeroanalysis;

import inge2.dataflow.util.visitor.AbstractValueVisitor;
import inge2.dataflow.util.visitor.ValueVisitor;
import soot.Local;
import soot.jimple.ParameterRef;

/**
 * This class implements a visitor that tries to deduce if the ZeroAbstractValue for a Soot expression.
 */
public class ZeroValueVisitor extends AbstractValueVisitor<ZeroAbstractValue> {
    /**
     * The IN set that affect the expression being analyzed.
     */
    private final ZeroAbstractSet set;

    /**
     * The resolved ZeroAbstractValue for the expression being analyzed.
     */
    private ZeroAbstractValue resolvedValue;

    /**
     * Indicates if there is a possible division by zero in the expression being analyzed.
     */
    private Boolean possibleDivisionByZero;

    public ZeroValueVisitor(ZeroAbstractSet set) {
        this.set = set;
        this.possibleDivisionByZero = false;
    }

    /**
     * This method is called when the expression being analyzed is a parameter.
     * @param parameter the parameter.
     */
    @Override
    protected void visitParameterRef(ParameterRef parameter) {
        resolvedValue = ZeroAbstractValue.MAYBE_ZERO;
    }

    /**
     * This method is called when the expression being analyzed is a local variable.
     * @param variable the local variable.
     */
    @Override
    public void visitLocal(Local variable) {
        String name = variable.getName();
        if (set.hasValue(name)) {
            resolvedValue = set.getValue(name);
        } else {
            resolvedValue = ZeroAbstractValue.ZERO;
        }
    }

    /**
     * This method is called when the expression being analyzed is a division.
     * @param leftOperand the left operand of the division.
     * @param rightOperand the right operand of the division.
     */
    @Override
    public void visitDivExpression(ZeroAbstractValue leftOperand, ZeroAbstractValue rightOperand) {
        /*
         Asignamos el valor despues de la division.
         A su vez, marcamos que dividir por ZERO o MAYBE_ZERO puede resultar en una division por cero.
         */
        resolvedValue = leftOperand.divideBy(rightOperand);
        if (rightOperand == ZeroAbstractValue.ZERO || rightOperand == ZeroAbstractValue.MAYBE_ZERO) {
            possibleDivisionByZero = true;
        }
    }

    /**
     * This method is called when the expression being analyzed is a multiplication.
     * @param leftOperand the left operand of the multiplication.
     * @param rightOperand the right operand of the multiplication.
     */
    @Override
    public void visitMulExpression(ZeroAbstractValue leftOperand, ZeroAbstractValue rightOperand) {
        resolvedValue = leftOperand.multiplyBy(rightOperand);
    }


    /**
     * This method is called when the expression being analyzed is a subtraction.
     * @param leftOperand the left operand of the subtraction.
     * @param rightOperand the right operand of the subtraction.
     */
    @Override
    public void visitSubExpression(ZeroAbstractValue leftOperand, ZeroAbstractValue rightOperand) {
        resolvedValue = leftOperand.substract(rightOperand);
    }

    /**
     * This method is called when the expression being analyzed is an addition.
     * @param leftOperand the left operand of the addition.
     * @param rightOperand the right operand of the addition.
     */
    @Override
    public void visitAddExpression(ZeroAbstractValue leftOperand, ZeroAbstractValue rightOperand) {
        resolvedValue = leftOperand.add(rightOperand);
    }

    /**
     * This method is called when the expression being analyzed is an integer constant.
     * @param value the integer constant.
     */
    @Override
    public void visitIntegerConstant(int value) {
        /*
         Al ser una constante, el valor resuelto es deterministico.
         */
        resolvedValue = value == 0 ? ZeroAbstractValue.ZERO : ZeroAbstractValue.NOT_ZERO;
    }

    /**
     * Method called after this visitor has finished analyzing the expression.
     * @return the ZeroAbstractValue for the expression.
     */
    @Override
    public ZeroAbstractValue done() {
        return resolvedValue;
    }

    @Override
    public ValueVisitor<ZeroAbstractValue> cloneVisitor() {
        return new ZeroValueVisitor(set);
    }

    /**
     * This method returns true if there is a possible division by zero in the expression being analyzed.
     * @return true if there is a possible division by zero in the expression being analyzed.
     */
    public Boolean getPossibleDivisionByZero() {
        return possibleDivisionByZero;
    }
}
