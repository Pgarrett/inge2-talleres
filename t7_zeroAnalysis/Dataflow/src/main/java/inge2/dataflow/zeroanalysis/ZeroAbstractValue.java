package inge2.dataflow.zeroanalysis;

/**
 * This enum represents the possible values of the zero analysis for a variable.
 */
public enum ZeroAbstractValue {

    /**
     * We don't have information about the variable.
     */
    BOTTOM("bottom"),

    /**
     * The variable is not zero.
     */
    NOT_ZERO("not-zero"),

    /**
     * The variable is zero.
     */
    ZERO("zero"),

    /**
     * The variable may be (or not) zero.
     */
    MAYBE_ZERO("maybe-zero");

    /**
     * The name of the ZeroAbstractValue.
     */
    private final String name;

    @Override
    public String toString() {
        return this.name;
    }

    ZeroAbstractValue(String name) {
        this.name = name;
    }

    /**
     * Returns the result of the addition between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the addition.
     */
    public ZeroAbstractValue add(ZeroAbstractValue another) {
        /*
        Transcripcion de la tabla de la primera parte para la suma
         */
        if (this.equals(BOTTOM)) {
            return BOTTOM;
        } else if (this.equals(ZERO)) {
            switch (another) {
                case BOTTOM:
                    return BOTTOM;
                case ZERO:
                    return ZERO;
                case NOT_ZERO:
                    return NOT_ZERO;
                default:
                case MAYBE_ZERO:
                    return MAYBE_ZERO;
            }
        } else if (this.equals(NOT_ZERO)) {
            switch (another) {
                case BOTTOM:
                    return BOTTOM;
                case ZERO:
                case NOT_ZERO:
                    return NOT_ZERO;
                default:
                case MAYBE_ZERO:
                    return MAYBE_ZERO;
            }
        } else {
            switch (another) {
                case BOTTOM:
                    return BOTTOM;
                default:
                case ZERO:
                case NOT_ZERO:
                case MAYBE_ZERO:
                    return MAYBE_ZERO;
            }
        }
    }

    /**
     * Returns the result of the division between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the division.
     */
    public ZeroAbstractValue divideBy(ZeroAbstractValue another) {
        /*
        Transcripcion de la tabla de la primera parte para la division
         */
        if (this.equals(BOTTOM)) {
            return BOTTOM;
        } else if (this.equals(ZERO)) {
            switch (another) {
                case BOTTOM:
                case ZERO:
                    return BOTTOM;
                default:
                case NOT_ZERO:
                case MAYBE_ZERO:
                    return ZERO;
            }
        } else if (this.equals(NOT_ZERO)) {
            switch (another) {
                case BOTTOM:
                case ZERO:
                    return BOTTOM;
                default:
                case NOT_ZERO:
                case MAYBE_ZERO:
                    return NOT_ZERO;
            }
        } else {
            switch (another) {
                case BOTTOM:
                case ZERO:
                    return BOTTOM;
                default:
                case NOT_ZERO:
                case MAYBE_ZERO:
                    return MAYBE_ZERO;
            }
        }
    }

    /**
     * Returns the result of the multiplication between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the multiplication.
     */
    public ZeroAbstractValue multiplyBy(ZeroAbstractValue another) {
        /*
        Transcripcion de la tabla de la primera parte para la multiplicacion
         */
        if (this.equals(BOTTOM)) {
            return BOTTOM;
        } else if (this.equals(ZERO)) {
            switch (another) {
                case BOTTOM:
                    return BOTTOM;
                default:
                case ZERO:
                case NOT_ZERO:
                case MAYBE_ZERO:
                    return ZERO;
            }
        } else if (this.equals(NOT_ZERO)) {
            switch (another) {
                case BOTTOM:
                    return BOTTOM;
                case ZERO:
                    return ZERO;
                case NOT_ZERO:
                    return NOT_ZERO;
                default:
                case MAYBE_ZERO:
                    return MAYBE_ZERO;
            }
        } else {
            switch (another) {
                case BOTTOM:
                    return BOTTOM;
                case ZERO:
                    return ZERO;
                default:
                case NOT_ZERO:
                case MAYBE_ZERO:
                    return MAYBE_ZERO;
            }
        }
    }

    /**
     * Returns the result of the subtraction between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the subtraction.
     */
    public ZeroAbstractValue substract(ZeroAbstractValue another) {
        /*
        Transcripcion de la tabla de la primera parte para la resta
         */
        if (this.equals(BOTTOM)) {
            return BOTTOM;
        } else if (this.equals(ZERO)) {
            switch (another) {
                case BOTTOM:
                    return BOTTOM;
                case ZERO:
                    return ZERO;
                case NOT_ZERO:
                    return NOT_ZERO;
                default:
                case MAYBE_ZERO:
                    return MAYBE_ZERO;
            }
        } else if (this.equals(NOT_ZERO)) {
            switch (another) {
                case BOTTOM:
                    return BOTTOM;
                case ZERO:
                default:
                case NOT_ZERO:
                case MAYBE_ZERO:
                    return MAYBE_ZERO;
            }
        } else {
            switch (another) {
                case BOTTOM:
                    return BOTTOM;
                default:
                case ZERO:
                case NOT_ZERO:
                case MAYBE_ZERO:
                    return MAYBE_ZERO;
            }
        }
    }

    /**
     * Returns the result of the merge between this ZeroAbstractValue and another.
     * @param another the other ZeroAbstractValue.
     * @return the result of the merge.
     */
    public ZeroAbstractValue merge(ZeroAbstractValue another) {
        /*
        El camino hacia arriba en el reticulado
         */
        if (this.equals(BOTTOM)) {
            switch (another) {
                case BOTTOM:
                    return BOTTOM;
                case ZERO:
                    return ZERO;
                case NOT_ZERO:
                    return NOT_ZERO;
                default:
                case MAYBE_ZERO:
                    return MAYBE_ZERO;
            }
        } else if (this.equals(ZERO)) {
            switch (another) {
                case BOTTOM:
                case ZERO:
                    return ZERO;
                default:
                case NOT_ZERO:
                case MAYBE_ZERO:
                    return MAYBE_ZERO;
            }
        } else if (this.equals(NOT_ZERO)) {
            switch (another) {
                case BOTTOM:
                case NOT_ZERO:
                    return NOT_ZERO;
                default:
                case ZERO:
                case MAYBE_ZERO:
                    return MAYBE_ZERO;
            }
        } else {
            switch (another) {
                default:
                case BOTTOM:
                case ZERO:
                case NOT_ZERO:
                case MAYBE_ZERO:
                    return MAYBE_ZERO;
            }
        }
    }

}
