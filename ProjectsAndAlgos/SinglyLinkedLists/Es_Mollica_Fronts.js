class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class SLL {
    constructor() {
        this.head = null;
    }

    //Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.
    addFront(val) {

        let new_node = new Node(val);

        if(!this.head){
            this.head = new_node;
            return this;
        }

        new_node.next = this.head;

        this.head = new_node;
        return this;
    }

    // Write a method to remove the head node and return the new list head node. If the list is empty, return null.
    removeFront() {
        if (!this.head){
            return null;
        }
        var current = this.head;
        this.head = current.next;
        current.next = null;
        return this;
    }

    //Write a method to return the value (not the node) at the head of the list. If the list is empty, return null.
    front() {
        if(this.head === null){
            return null;
        }
        else {
            return this.head.data;
        }
    }
    }


let sll1 = new SLL()
sll1.addFront(18);
console.log(sll1);

sll1.addFront(5);
console.log(sll1);

sll1.addFront(73);
console.log(sll1);

sll1.removeFront();
console.log(sll1);
sll1.removeFront();
console.log(sll1);

sll1.front();
console.log(sll1.front());