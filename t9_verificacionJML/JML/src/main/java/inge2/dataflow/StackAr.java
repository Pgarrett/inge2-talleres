package inge2.dataflow;

public class StackAr {

    /**
     * Capacidad por defecto de la pila.
     */
    private final static int DEFAULT_CAPACITY = 10;

    /**
     * Arreglo que contiene los elementos de la pila.
     */
    //@ spec_public
    private final int[] elems;

    /**
     * Indice del tope de la pila.
     */
    //@ spec_public
    private int top = -1;

    //@ requires true;
    //@ ensures elems.length == 10;
    public StackAr() {
        this(DEFAULT_CAPACITY);
    }

    //@ requires 0 <= capacity < Integer.MAX_VALUE;
    //@ ensures elems.length == capacity;
    public StackAr(int capacity) {
        elems = new int[capacity];
    }

    //@ requires true;
    //@ ensures \result <==> top == -1;
    public boolean isEmpty() {
        return top == -1;
    }

    //@ requires true;
    //@ ensures \result == (top+1 == elems.length);
    public boolean isFull() {
        return top == elems.length - 1;
    }

    //@ requires top + 1 < Integer.MAX_VALUE;
    //@ ensures top < Integer.MAX_VALUE;
    //@ ensures \result == top + 1;
    public int size() {
        return top+1;
    }

    //@ requires 0 <= top < elems.length - 1;
    //@ ensures \forall int j; 0 <= j < top; elems[j] == \old(elems[j]);
    //@ ensures elems[top] == o;
    public void push(int o) {
        top++;
        elems[top] = o;
    }

    //@ requires -1 < top < elems.length;
    //@ ensures \forall int j; 0 <= j < top; elems[j] == \old(elems[j]);
    //@ ensures top == \old(top) - 1;
    //@ ensures \result == \old(elems[top]);
    public int pop() {
        int res = elems[top];
        top--;
        return res;
    }

    //@ requires -1 < top < elems.length;
    //@ ensures \forall int j; 0 <= j <= top; elems[j] == \old(elems[j]);
    //@ ensures top == \old(top);
    //@ ensures \result == \old(elems[top]);
    public int peek() {
        return elems[top];
    }
}

