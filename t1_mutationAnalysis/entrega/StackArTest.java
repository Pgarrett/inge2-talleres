package org.autotest;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class StackArTest {

    @Test
    public void testExample() {
        StackAr stack = new StackAr();

        assertTrue(true);
        assertFalse(false);
        assertEquals(true, true);
    }

    // ejercicio 1
    @Test
    public void isEmptyWhenNew() {
        StackAr stack = new StackAr();

        assertTrue(stack.isEmpty());
        stack.push(1);
        assertFalse(stack.isEmpty());
    }

    /*
    Ejercicio 2
    Ejecutar PiTest sobre el programa StackAr y el test case escrito.
        ¿Cuantas lıneas cubiertas reporta PiTest? 14 sobre 52
        ¿Cuantos mutantes vivos reporta PiTest? 27 mutantes vivos
        ¿Cual es el mutation score que reporta PiTest? 9/36 es mutation score
     */

    // Ejercicio 3
    @Test
    public void pushAndPopLeavesStackEmpty() {
        StackAr stack = new StackAr();

        stack.push(1);
        assertFalse(stack.isEmpty());
        stack.pop();
        assertTrue(stack.isEmpty());
    }

    @Test
    public void negativeCapacityThrowsException() {
        assertThrows(IllegalArgumentException.class, () -> new StackAr(-1));
    }

    @Test
    public void newStackWithCapacityIsEmpty() {
        StackAr stackAr = new StackAr(0);
        assertEquals(stackAr.size(), 0);
    }

    @Test
    public void pushToFullStackThrowsException() {
        StackAr stackAr = new StackAr(0);
        assertThrows(IllegalStateException.class, () -> stackAr.push(1));
    }

    @Test
    public void popToEmptyStackThrowsException() {
        StackAr stackAr = new StackAr(0);
        assertThrows(IllegalStateException.class, () -> stackAr.pop());
    }

    @Test
    public void topOfEmptyStackThrowsException() {
        StackAr stackAr = new StackAr(0);
        assertThrows(IllegalStateException.class, () -> stackAr.top());
    }

    @Test
    public void popReturnsLastElement() {
        StackAr stackAr = new StackAr(1);
        stackAr.push(1);
        assertEquals(stackAr.pop(), 1);
    }

    @Test
    public void topShowsLastElement() {
        StackAr stackAr = new StackAr(1);
        stackAr.push(1);
        assertEquals(stackAr.top(), 1);
    }

    @Test
    public void hashCodeWithOneElement() {
        StackAr stackAr = new StackAr(1);
        stackAr.push(1);
        assertEquals(stackAr.hashCode(), 1953);
    }

    @Test
    public void hashCodeWithNumberAndNull() {
        StackAr stackAr = new StackAr();
        stackAr.push(1);
        stackAr.push(null);
        assertEquals(stackAr.hashCode(), -1667867678);
    }

    @Test
    public void hashCodeWithSeveralElements() {
        StackAr stackAr = new StackAr();
        stackAr.push(1);
        stackAr.push("abc");
        stackAr.push("def");
        stackAr.push(2134125);
        stackAr.push(2134.4);
        assertEquals(stackAr.hashCode(), 854918908);
    }

    @Test
    public void stacksIsEqualToItself() {
        StackAr stack = new StackAr();

        assertEquals(stack, stack);
    }

    @Test
    public void emptyStacksAreEqual() {
        StackAr stack1 = new StackAr();
        StackAr stack2 = new StackAr();

        assertEquals(stack1, stack2);
    }

    @Test
    public void pushToStackIsDifferentToOtherStack() {
        StackAr stack1 = new StackAr();
        StackAr stack2 = new StackAr();
        stack2.push(1);

        assertNotEquals(stack1, stack2);
    }

    @Test
    public void stackIsNotEqualToNull() {
        StackAr stack = new StackAr();

        assertNotEquals(stack, null);
    }

    @Test
    public void stackIsNotEqualToObject() {
        StackAr stack = new StackAr();

        assertNotEquals(stack, new Object());
    }

    @Test
    public void readIndexIsDifferentWhenOneStackIsEmptyAndTheOtherOneNot() {
        StackAr stack1 = new StackAr();
        StackAr stack2 = new StackAr(0);
        stack1.push(2);
        stack1.push("abc");

        assertNotEquals(stack1, stack2);
    }

    @Test
    public void toStringOfEmptyStackIsEmpty() {
        StackAr stackAr = new StackAr();
        assertEquals(stackAr.toString(), "[]");
    }

    @Test
    public void toStringOfStackWithContentIsNotEmpty() {
        StackAr stackAr = new StackAr();
        stackAr.push(123);
        assertEquals(stackAr.toString(), "[123]");
    }

    @Test
    public void toStringOfStackWithMoreThanOneElementIsNotEmpty() {
        StackAr stackAr = new StackAr();
        stackAr.push(123);
        stackAr.push("abc");
        assertEquals(stackAr.toString(), "[123,abc]");
    }

    /*
    Extender el test suite para obtener el mejor mutation score posible con PiTest.
        ¿Cual es el mejor mutation score que pudo obtener? 94% - 34/36
        ¿Cuantos mutantes equivalentes encontro? ¿Cuales fueron? Encontramos dos mutantes equivalentes.
            - Uno en el hashCode, donde cambia en la linea 65 la multiplicacion por la division, dicho mutante no muere porque siempre divide sobre 1, que da el mismo resultado.
            - El segundo mutante esta en el equals en la linea 82, que nunca se va a ejecutar, ya que el if de la linea 79 contiene al if de la linea 81. Esto porque no podemos acceder al readIndex, entonces si tienen readIndex distinto, si o si salio por el if de la linea 79.
     */
}
