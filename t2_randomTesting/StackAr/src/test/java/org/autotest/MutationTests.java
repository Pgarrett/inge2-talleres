package org.autotest;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class MutationTests {

    @Test
    public void stacksIsEqualToItself() {
        StackAr stack = new StackAr();

        assertEquals(stack, stack);
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
    public void newStackCompliesWithRep() {
        StackAr stackAr = new StackAr();
        assertTrue(stackAr.repOK());
    }

    @Test
    public void stackWithTwoCompliesWithRep() {
        StackAr stackAr = new StackAr(2);
        stackAr.push("a");
        stackAr.push(1);
        assertTrue(stackAr.repOK());
    }

    @Test
    public void pushAndPopFromStackCompliesWithRep() {
        StackAr stackAr = new StackAr(2);
        stackAr.push("a");
        stackAr.pop();
        assertTrue(stackAr.repOK());
    }

    @Test
    public void pushTwoAndPopOneFromStackCompliesWithRep() {
        StackAr stackAr = new StackAr(2);
        stackAr.push("a");
        stackAr.push(1);
        stackAr.pop();
        assertTrue(stackAr.repOK());
    }

}
